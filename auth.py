
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("D:/code/debate arena/ai-debate-arena-sj-firebase-adminsdk-fbsvc-0ba3debe2e.json")
firebase_admin.initialize_app(cred)

def verify_user(token:str):
    decoded = auth.verify_id_token(token)
    return decoded