from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="TCS Financial Forecast Agent")

@app.get("/")
def root():
    return {"status": "TCS Financial Forecast Agent is running"}

app.include_router(router)
