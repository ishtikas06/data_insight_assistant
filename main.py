from fastapi import FastAPI
from src.router.api import router

app = FastAPI(title="LLM-powered Data Insight Assistant")

app.include_router(router)

@app.get("/")
def root():
    return {"message":"LLM-powered Data Insight Assistant"}