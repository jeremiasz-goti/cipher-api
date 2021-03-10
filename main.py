from fastapi import FastAPI, Depends, status, HTTPException
from cipher import encode, decode
from api_auth import user_auth

app = FastAPI()

@app.get("/encode/msg={to_encode}&shift={shift}")
async def enc(to_encode: str, shift: int,username: str = Depends(user_auth)):
    return {"message": encode(to_encode, shift)}

@app.get("/decode/msg={to_decode}&shift={shift}")
async def dec(to_decode: str, shift: int,username: str = Depends(user_auth)):
    return {"message" : decode(to_decode, shift)}