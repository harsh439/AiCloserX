from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
import time
import jwt

JWT_SECRET = "your-secret-key"  # You should load this from environment or secret management service

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth = HTTPBearer()
        credentials = await auth(request)
        token = credentials.credentials
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            request.state.user = payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

        return await call_next(request)

class RateLimitMiddleware(BaseHTTPMiddleware):
    # Simple rate-limiting using an in-memory store
    RATE_LIMIT = 100  # 100 requests per minute
    request_counts = {}

    async def dispatch(self, request: Request, call_next):
        user_ip = request.client.host
        current_time = int(time.time())

        if user_ip not in self.request_counts:
            self.request_counts[user_ip] = [current_time]

        request_times = self.request_counts[user_ip]
        # Remove requests older than a minute
        request_times = [t for t in request_times if current_time - t < 60]

        if len(request_times) >= self.RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        request_times.append(current_time)
        self.request_counts[user_ip] = request_times

        return await call_next(request)

# CORS Middleware
def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
