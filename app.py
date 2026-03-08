from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from langs.langs import programming_languages

app = FastAPI(title="Programming Languages API", version="1.0.0")


@app.middleware("http")
async def rapidapi_host_check(request: Request, call_next):
    host = request.headers.get("x-rapidapi-host", "")
    # RapidAPI gateway always sets the API's host
    if "rapidapi" not in host.lower():
        return JSONResponse(
            status_code=403, content={"detail": "Direct access forbidden"}
        )
    return await call_next(request)


@app.get("/programming-languages")
def get_programming_languages():
    return {"count": len(programming_languages), "languages": programming_languages}


@app.get("/programming-languages/{name}")
def get_language(name: str):
    for lang in programming_languages:
        if lang["name"].lower() == name.lower():
            return lang
    return JSONResponse(status_code=404, content={"detail": "Language not found"})
