from pydantic import BaseModel
from typing import Optional

class TextInput(BaseModel):
    text: str

class PredictResponse(BaseModel):
    status: str
    data: Optional[dict] = None
    message: Optional[str] = None

class TrainingResponse(BaseModel):
    status: str
    data: Optional[dict] = None
    message: Optional[str] = None