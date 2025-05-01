from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import firebase_admin
from firebase_admin import auth, credentials

# Initialize Firebase
cred = credentials.Certificate("path/to/your-firebase-key.json")  
firebase_admin.initialize_app(cred)

app = FastAPI()

@app.post("/ask")
async def ask(user_token: str = Depends(oauth2_scheme), query: str):
    try:
        # Verify Google login token
        user = auth.verify_id_token(user_token)
        user_id = user["uid"]  # Unique ID for each user
        
        # Now, only this user can access their data!
        response = openai.ChatCompletion.create(...)
        return {"response": response.choices[0].message.content}
    except:
        return {"error": "Not logged in!"}
