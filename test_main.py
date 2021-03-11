import base64
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

creds = "dev:dev"
creds_bytes = creds.encode("ascii")  
creds64_bytes = base64.b64encode(creds_bytes) 
creds64_string = creds64_bytes.decode("ascii")

phrase = "(T4stowa Fr&z@]"
shifted = "čY9xytBfĀKwċEěĞ"
shift = 5

headers = {'Authorization': 'Basic ' + creds64_string}


def test_Encode(phrase=phrase, shift=shift, headers=headers):
    response = client.get('/encode/msg={}&shift={}'.format(phrase, shift), headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": shifted}

def test_Decode(phrase=phrase, shift=shift, headers=headers):
    response = client.get('/decode/msg={}&shift={}'.format(shifted, shift), headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": phrase}

def test_Encode(phrase=phrase, shift=shift):
    response = client.get('/encode/msg={}&shift={}'.format(phrase, shift))
    assert response.status_code == 401

def test_Decode(phrase=phrase, shift=shift):
    response = client.get('/decode/msg={}&shift={}'.format(shifted, shift))
    assert response.status_code == 401




    