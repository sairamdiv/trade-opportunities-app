from fastapi import Header, HTTPException

API_KEY = "secret123"

def verify_token(authorization: str = Header(...)):
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")
