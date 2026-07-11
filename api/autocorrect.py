from fastapi import APIRouter

from app.autocomplete.autocomplete import AutoCompleteEngine
from app.schemas.request import TextRequest
from app.schemas.response import AutoCorrectResponse


router = APIRouter(
    prefix="/autocorrect",
    tags=["Autocorrect"]
)


engine = AutoCompleteEngine("app/data/corpus.txt")


@router.post(
    "/",
    response_model=AutoCorrectResponse
)
def autocorrect(request: TextRequest):

    corrected, suggestions = engine.suggest(
        request.text.lower()
    )

    if corrected is None:
        corrected = request.text.lower()

    return AutoCorrectResponse(
        corrected_word=corrected,
        suggestions=suggestions
    )
