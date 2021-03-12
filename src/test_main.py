"""

Main api tests

"""

import base64
from main import app
from fastapi.testclient import TestClient

# use fastapi test client
client = TestClient(app)

# credentials base64 encode for auth testing
creds = "dev:dev"
creds_bytes = creds.encode("ascii")  
creds64_bytes = base64.b64encode(creds_bytes) 
creds64_string = creds64_bytes.decode("ascii")

# test data
phrase = "(T4stowa Fr&z@]"
shifted = "čY9xytBfĀKwċEěĞ"
shift = 5

headers = {'Authorization': 'Basic ' + creds64_string}


# test encoding endpoint with authorization
def test_Encode(phrase=phrase, shift=shift, headers=headers):
    response = client.get('/encode/msg={}&shift={}'.format(phrase, shift), headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": shifted}

# test decoding endpoint with authorization
def test_Decode(phrase=phrase, shift=shift, headers=headers):
    response = client.get('/decode/msg={}&shift={}'.format(shifted, shift), headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": phrase}

# test encoding endpoint with no authorization
def test_Encode(phrase=phrase, shift=shift):
    response = client.get('/encode/msg={}&shift={}'.format(phrase, shift))
    assert response.status_code == 401

# test decoding endpoint with no authorization
def test_Decode(phrase=phrase, shift=shift):
    response = client.get('/decode/msg={}&shift={}'.format(shifted, shift))
    assert response.status_code == 401
    