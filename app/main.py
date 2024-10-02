from fastapi import FastAPI
from app.api.v1.endpoints import customer, auth, support, channels, orchestration, personalization, model_management, active_learning, cache, monitoring, security_compliance, tts  # Added security and compliance
from app.db import connect_to_mongo, close_mongo_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Customer Care API",
    version="1.0",
)

# MongoDB connection lifecycle events
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# API Routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(customer.router, prefix="/api/v1/customer", tags=["Customer"])
app.include_router(support.router, prefix="/api/v1/support", tags=["Support"])
app.include_router(channels.router, prefix="/api/v1/channels", tags=["Channels"])  # New multi-channel router
app.include_router(orchestration.router, prefix="/api/v1/orchestration", tags=["Orchestration"])  # New orchestration router
app.include_router(personalization.router, prefix="/api/v1/personalization", tags=["Personalization"])  # New personalization router
app.include_router(model_management.router, prefix="/api/v1/model", tags=["Model Management"])  # New model management router
app.include_router(active_learning.router, prefix="/api/v1/active-learning", tags=["Active Learning"])  # New active learning router
app.include_router(cache.router, prefix="/api/v1/cache", tags=["Cache Mechanism"])  # New cache router
app.include_router(monitoring.router, prefix="/api/v1/monitoring", tags=["Monitoring and Error Reporting"])  # New monitoring router
app.include_router(security_compliance.router, prefix="/api/v1/security", tags=["Compliance and Security Enhancements"])  # New security router
app.include_router(tts.router, prefix="/api/v1", tags=["TTS"])

# Root endpoint for health check
@app.get("/")
async def root():
    return {"message": "API is running"}