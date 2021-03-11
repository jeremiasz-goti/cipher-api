from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from cipher import encode, decode
from api_auth import user_auth

app = FastAPI()

@app.get("/")
async def home(username: str = Depends(user_auth)):
    return RedirectResponse(url="/docs/")

@app.get("/encode/msg={phrase}&shift={shift}")
async def Encode(phrase: str, shift: int,username: str = Depends(user_auth)):
    return {"message": encode(phrase, abs(shift))}

@app.get("/decode/msg={phrase}&shift={shift}")
async def Decode(phrase: str, shift: int,username: str = Depends(user_auth)):
    return {"message" : decode(phrase, -abs(shift))}


