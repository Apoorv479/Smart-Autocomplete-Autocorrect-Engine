from fastapi import APIRouter

from app.autocomplete.autocomplete import AutoCompleteEngine
from app.schemas.request import TextRequest
from app.schemas.response import AutoCompleteResponse


router = APIRouter(
    prefix="/autocomplete",
    tags=["Autocomplete"]
)


engine = AutoCompleteEngine("app/data/corpus.txt")


@router.post(
    "/",
    response_model=AutoCompleteResponse
)
def autocomplete(request: TextRequest):

    corrected, suggestions = engine.suggest(
        request.text.lower()
    )

    return AutoCompleteResponse(
        suggestions=suggestions
    )
