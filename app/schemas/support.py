from pydantic import BaseModel

class SupportQuery(BaseModel):
    query: str

class SupportResponse(BaseModel):
    intent: str
    confidence: float
