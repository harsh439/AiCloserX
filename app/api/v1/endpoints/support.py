from fastapi import APIRouter
from app.services.nlp_service import analyze_intent
from app.schemas.support import SupportQuery, SupportResponse

router = APIRouter()

@router.post("/query", response_model=SupportResponse)
async def query_support(query: SupportQuery):
    intent, confidence = analyze_intent(query.query)
    return {"intent": intent, "confidence": confidence}
