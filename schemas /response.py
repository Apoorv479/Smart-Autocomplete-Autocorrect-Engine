from pydantic import BaseModel


class AutoCompleteResponse(BaseModel):
    suggestions: list[str]


class AutoCorrectResponse(BaseModel):
    corrected_word: str
    suggestions: list[str]


class NextWordPredictionResponse(BaseModel):
    predictions: list[str]


class SentenceAutoCompleteResponse(BaseModel):
    sentences: list[str]
