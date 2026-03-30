"""from fastapi import FastAPI
from app.service import URLService

app = FastAPI()
service = URLService()

@app.get("/urlinfo/1/{hostname}/{path:path}")
def url_info(hostname: str, path: str):
    full_url = f"{hostname}/{path}"
    is_bad = service.is_malicious(full_url)

    return {
        "url": full_url,
        "malicious": is_bad
    }"""
from fastapi import FastAPI, HTTPException
from app.service import URLService

app = FastAPI()
service = URLService()

@app.get("/urlinfo/1/{hostname}/{path:path}")
def url_info(hostname: str, path: str):
    try:
        full_url = f"{hostname}/{path}"
        is_bad = service.is_malicious(full_url)

        return {
            "url": full_url,
            "malicious": is_bad
        }
    except Exception:
        raise HTTPException(status_code=500, detail="Internal error")