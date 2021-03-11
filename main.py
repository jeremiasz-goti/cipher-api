from fastapi import FastAPI, Depends, status, HTTPException
from cipher import encode, decode
from api_auth import user_auth

app = FastAPI()

@app.get("/encode/msg={phrase}&shift={shift}")
async def enc(phrase: str, shift: int,username: str = Depends(user_auth)):
    return {"message": encode(phrase, abs(shift))}

@app.get("/decode/msg={phrase}&shift={shift}")
async def dec(phrase: str, shift: int,username: str = Depends(user_auth)):
    return {"message" : decode(phrase, -abs(shift))}