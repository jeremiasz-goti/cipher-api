from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from cipher import encode, decode
from api_auth import user_auth

"""

Main app file that contains routings and main methods

"""

app = FastAPI(
    title = "Cipher Api",
    description = "Caesar cipher api",
    version = "1.0.0"
)

tags_metadata = [
    {
        "name": "Encode",
        "description": "Method for encoding data",
    },
    {
        "name": "Decode",
        "description": "Method for decoding data",
    },
]

# Encode endpoint - takes str(phrase) and int(shift) and runs it through encode method
@app.get("/encode/msg={phrase}&shift={shift}", tags=["Encode"])
async def Encode(phrase: str, shift: int,username: str = Depends(user_auth)):
    return {"message": encode(phrase, abs(shift))}

# Decode endpoint - takes str(phrase) and int(shift) and runs it through decode method
@app.get("/decode/msg={phrase}&shift={shift}", tags=['Decode'])
async def Decode(phrase: str, shift: int,username: str = Depends(user_auth)):
    return {"message" : decode(phrase, -abs(shift))}


