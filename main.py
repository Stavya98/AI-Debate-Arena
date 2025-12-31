from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from bson import ObjectId
from datetime import datetime
from fastapi import Response
from debate_flow import run_debate
from db import users_col, debates_col
from dependencies import get_current_user
from auth import verify_user

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# -------------------------
# HOME (PUBLIC)
# -------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None}
    )


# -------------------------
# START DEBATE (PROTECTED)
# -------------------------
@app.post("/", response_class=HTMLResponse)
def start_debate(
    request: Request,
    topic: str = Form(...),
    user = Depends(get_current_user)
):
    #user = get_current_user(f"Bearer {auth_token}")

    # Ensure user exists
    users_col.update_one(
        {"_id": user["uid"]},
        {
            "$setOnInsert": {
                "email": user.get("email"),
                "name": user.get("name"),
                "created_at": datetime.utcnow(),
            }
        },
        upsert=True,
    )

    # Run debate
    result = run_debate(topic)

    # Save debate
    debates_col.insert_one({
        "user_id": user["uid"],
        "topic": topic,
        "clarified_topic": result["clarified_topic"],
        "for_opening": result["for_opening"],
        "for_rebuttal": result["for_rebuttal"],
        "against_opening": result["against_opening"],
        "against_rebuttal": result["against_rebuttal"],
        "summary": result["final_summary"],
        "created_at": datetime.utcnow(),
    })

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result}
    )


# -------------------------
# HISTORY (PROTECTED)
# -------------------------
@app.get("/history", response_class=HTMLResponse)
def history(
    request: Request,
    user=Depends(get_current_user),
):
    debates = list(
        debates_col.find({"user_id": user["uid"]})
        .sort("created_at", -1)
    )

    return templates.TemplateResponse(
        "history.html",
        {"request": request, "debates": debates}
    )


# -------------------------
# VIEW SINGLE DEBATE (PROTECTED)
# -------------------------
@app.get("/debate/{debate_id}", response_class=HTMLResponse)
def view_debate(
    debate_id: str,
    request: Request,
    user=Depends(get_current_user),
):
    debate = debates_col.find_one({
        "_id": ObjectId(debate_id),
        "user_id": user["uid"],
    })

    if not debate:
        raise HTTPException(status_code=404, detail="Debate not found")

    return templates.TemplateResponse(
        "debate_detail.html",
        {"request": request, "debate": debate}
    )


# -------------------------
# CONTACT (PUBLIC)
# -------------------------
@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(
        "contact.html",
        {"request": request}
    )

from fastapi import Response

from fastapi.responses import RedirectResponse

from fastapi import Response

@app.post("/login")
def login(response: Response, auth_token: str = Form(...)):
    user = verify_user(auth_token)

    response.set_cookie(
        key="auth_token",
        value=auth_token,
        httponly=True,
        samesite="lax"
    )

    return {"status": "ok"}



@app.post("/logout")
def logout(
    response: Response,
):
    response.delete_cookie("auth_token")
    return {"status": "logged out"}