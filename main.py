from fastapi import FastAPI

from app.api.autocomplete import router as autocomplete_router
from app.api.autocorrect import router as autocorrect_router
from app.api.prediction import router as prediction_router


app = FastAPI(
    title="Smart Autocomplete and Autocorrect Engine",
    description="FastAPI backend for autocomplete, autocorrect, next-word prediction, and sentence autocomplete.",
    version="1.0.0"
)


app.include_router(autocomplete_router)
app.include_router(autocorrect_router)
app.include_router(prediction_router)


@app.get("/")
def home():
    return {
        "message": "Smart Autocomplete and Autocorrect Engine API",
        "docs": "/docs"
    }
