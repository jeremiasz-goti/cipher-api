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

To deploy cypher-api in a Docker container use:

```sh
cd cipher-api
docker build -t cipher-api:1.0 .
```

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8000 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d --name test -p 8000:8000 cipher-api:1.0
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000/docs
```

## To do

- implement more complex cryptographic solution
- more tests
- better documentation
- optimize optimize optimize
