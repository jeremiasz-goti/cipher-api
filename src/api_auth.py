import secrets
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic

security = HTTPBasic()

def user_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "dev")
    correct_password = secrets.compare_digest(credentials.password, "dev")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
