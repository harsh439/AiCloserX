from fastapi import APIRouter, HTTPException
from typing import Optional, List
import redis
import json

# Set up Redis client (for local testing)
cache_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

router = APIRouter()

# Endpoint 1: Store Data in Cache
@router.post("/store", response_model=dict)
async def store_cache(key: str, value: str, ttl: Optional[int] = None):
    """
    Stores data or responses in the cache with an optional TTL (Time-to-Live).
    """
    try:
        cache_client.set(key, value)
        if ttl:
            cache_client.expire(key, ttl)
        return {
            "status": "cache_stored",
            "key": key,
            "ttl": ttl
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cache storage failed: {str(e)}")

# Endpoint 2: Retrieve Data from Cache
@router.get("/retrieve", response_model=dict)
async def retrieve_cache(key: str):
    """
    Retrieves data from the cache using a specific key.
    """
    try:
        value = cache_client.get(key)
        if value:
            return {
                "key": key,
                "value": value
            }
        else:
            raise HTTPException(status_code=404, detail="Cache entry not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cache retrieval failed: {str(e)}")

# Endpoint 3: Invalidate Cache Entry
@router.post("/invalidate", response_model=dict)
async def invalidate_cache(key: str):
    """
    Invalidates or removes a specific cache entry.
    """
    try:
        result = cache_client.delete(key)
        if result:
            return {
                "status": "cache_invalidated",
                "key": key
            }
        else:
            raise HTTPException(status_code=404, detail="Cache entry not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cache invalidation failed: {str(e)}")

# Endpoint 4: Refresh Cache Entry
@router.post("/refresh", response_model=dict)
async def refresh_cache(key: str, new_value: str, ttl: Optional[int] = None):
    """
    Refreshes a cache entry with updated data and an optional TTL.
    """
    try:
        cache_client.set(key, new_value)
        if ttl:
            cache_client.expire(key, ttl)
        return {
            "status": "cache_refreshed",
            "key": key,
            "ttl": ttl
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cache refresh failed: {str(e)}")

# Endpoint 5: Get Cache Status
@router.get("/status", response_model=dict)
async def cache_status(key: str):
    """
    Retrieves the current status of a cached item, including TTL and value.
    """
    try:
        value = cache_client.get(key)
        ttl = cache_client.ttl(key)
        if value is not None:
            return {
                "key": key,
                "value": value,
                "ttl": ttl
            }
        else:
            raise HTTPException(status_code=404, detail="Cache entry not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cache status retrieval failed: {str(e)}")

# Endpoint 6: Retrieve All Cached Keys
@router.get("/all-keys", response_model=dict)
async def get_all_keys():
    """
    Retrieves a list of all keys currently stored in the cache.
    """
    try:
        keys = cache_client.keys("*")
        return {
            "cached_keys": keys
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve cached keys: {str(e)}")
