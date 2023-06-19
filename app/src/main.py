'''
Author: Hassan Mahmood

Version: 0.0.1

Description: FastAPI middleware application used to route traffic 
between CMS Frontend application and supporting backend processes

'''




from fastapi import FastAPI
from fastapi.responses import (
	HTMLResponse
)
from fastapi.middleware.cors import CORSMiddleware
# from src.services import auth as Auth


app = FastAPI(
    title="CMS Middleware Application",
    description="Application used to route/authenticate traffic between frontend and supporting backend resources",
    debug=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:
    pass


@app.on_event("shutdown")
async def shutdown() -> None:
    pass


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1><p>Hello World</p></h1>"



# app.include_router(
#     HTMLDownloader.router, 
#     prefix="/auth"
# )





