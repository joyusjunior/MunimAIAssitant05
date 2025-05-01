from fastapi import FastAPI, HTTPException
import firebase_admin
from firebase_admin import auth, credentials

# 🔥 Initialize Firebase
cred = credentials.Certificate("firebase-key.json")  # Path to your .json file
firebase_admin.initialize_app(cred)

app = FastAPI()

@app.post("/ask")
def ask(user_token: str, query: str):
    try:
        # 🔐 Verify Google Login
        user = auth.verify_id_token(user_token)
        user_id = user["uid"]  # Unique user ID
        
        # ✅ Now only this user can use the chatbot!
        return {"response": f"Hello user {user_id}! You asked: {query}"}
    except:
        return {"error": "Login failed!"}
