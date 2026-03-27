## Setup

pip install -r requirements.txt

## Run

uvicorn app.main:app --reload

## Test

pytest

## Example

GET http://localhost:8000/urlinfo/1/bad.com/malware