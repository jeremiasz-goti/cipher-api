# Cipher Api

Cypher API its an app for encoding and decoding data using Caesar Cipher. Build with FastApi

## Features

- Encoding and decoding data using Caesar Cipher (whitespaces and punctuation suported)

## Tech

Cipher Api is using:

- [Python 3.6.9](https://www.python.org/)
- [FastApi](https://fastapi.tiangolo.com/)


## Installation

Clone repository

```sh
git clone https://github.com/jeremiasz-goti/cipher-api.git
```

Install dependencies and run

```sh
cd cipher-api
pip install -r requirements.txt
cd src
uvicorn main:app --reload
```

## Docker

Still in development :)


## Swagger Docs
```sh
127.0.0.1:8000/docs
```

## To do

- implement more complex cryptographic solution
- docker file
- more tests
- better documentation
- optimize optimize optimize
