
import firebase_admin
from firebase_admin import credentials, auth

#cred = credentials.Certificate("D:/code/debate arena/ai-debate-arena-sj-firebase-adminsdk-fbsvc-0ba3debe2e.json")
#this line is used for deployment
import os
import json
import firebase_admin
from firebase_admin import credentials, auth

if not firebase_admin._apps:
    firebase_json = os.environ.get("FIREBASE_SERVICE_ACCOUNT")

    if not firebase_json:
        raise RuntimeError("Missing FIREBASE_SERVICE_ACCOUNT env variable")

    cred = credentials.Certificate(json.loads(firebase_json))
    firebase_admin.initialize_app(cred)
#from here its common


firebase_admin.initialize_app(cred)

def verify_user(token:str):
    decoded = auth.verify_id_token(token)
    return decoded