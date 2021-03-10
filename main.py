import secrets
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from cipher import encode, decode


app = FastAPI()
security = HTTPBasic()

def user_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "development")
    correct_password = secrets.compare_digest(credentials.password, "development")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/encode/msg={to_encode}&shift={shift}")
async def enc(to_encode: str, shift: int,username: str = Depends(user_auth)):
    return {"message": encode(to_encode, shift)}

@app.get("/decode/msg={to_decode}&shift={shift}")
async def dec(to_decode: str, shift: int,username: str = Depends(user_auth)):
    return {"message" : decode(to_decode, shift)}