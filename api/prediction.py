from fastapi import APIRouter

from app.autocomplete.autocomplete import AutoCompleteEngine
from app.schemas.request import TextRequest
from app.schemas.response import (
    NextWordPredictionResponse,
    SentenceAutoCompleteResponse
)


router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


engine = AutoCompleteEngine("app/data/corpus.txt")


@router.post(
    "/predict-next",
    response_model=NextWordPredictionResponse
)
def predict_next(request: TextRequest):

    words = request.text.lower().split()

    if not words:
        return NextWordPredictionResponse(
            predictions=[]
        )

    predictions = engine.predict_next_word(
        words[-1]
    )

    return NextWordPredictionResponse(
        predictions=predictions
    )


@router.post(
    "/sentence-autocomplete",
    response_model=SentenceAutoCompleteResponse
)
def sentence_autocomplete(request: TextRequest):

    sentences = engine.suggest_sentence(
        request.text
    )

    return SentenceAutoCompleteResponse(
        sentences=sentences
    )
