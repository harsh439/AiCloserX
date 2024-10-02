from fastapi import APIRouter, HTTPException, Depends
from typing import Optional, List
from datetime import datetime

router = APIRouter()

# Simulated Databases for Personalization (to be replaced by CRM and Order Management Systems)
fake_customer_db = {
    "user123": {
        "preferences": {
            "preferred_language": "English",
            "preferred_category": "electronics",
            "device": "smartphone"
        },
        "recent_orders": [
            {
                "order_id": "12345",
                "product": "Smartphone",
                "price": "$799.99",
                "order_date": "2023-09-20"
            }
        ]
    }
}

# In-memory storage for personalized recommendations and dynamic content
personalization_log = {}


# Endpoint 1: Personalized Recommendations
@router.post("/recommendations", response_model=dict)
async def personalized_recommendations(customer_id: str, context: dict):
    """
    Provides personalized product or service recommendations based on the user's history, preferences, and interactions.
    """
    customer_data = fake_customer_db.get(customer_id)

    if not customer_data:
        raise HTTPException(status_code=404, detail="Customer not found")

    preferences = context.get("preferences", {})
    recent_interactions = context.get("recent_interactions", [])

    # Example recommendation logic (this would typically use a recommendation engine)
    if preferences.get("preferred_category") == "electronics":
        recommendations = [
            {
                "product_id": "987",
                "product_name": "Wireless Earbuds",
                "category": "accessories",
                "price": "$99.99"
            },
            {
                "product_id": "1234",
                "product_name": "Phone Case",
                "category": "accessories",
                "price": "$19.99"
            }
        ]
        response_text = "Since you've bought a smartphone recently, we recommend these accessories."
    else:
        recommendations = []
        response_text = "We couldn't find any recommendations for your preferences."

    return {
        "recommendations": recommendations,
        "response_text": response_text
    }


# Endpoint 2: Fetch or Update Customer Profile
@router.post("/customer-profile", response_model=dict)
async def manage_customer_profile(customer_id: str, update: Optional[bool] = False, profile_update: Optional[dict] = None):
    """
    Fetches or updates the customer's profile.
    If `update` is True, it updates the customer's preferences; otherwise, it fetches the profile.
    """
    customer_data = fake_customer_db.get(customer_id)

    if not customer_data:
        raise HTTPException(status_code=404, detail="Customer not found")

    if update and profile_update:
        # Update profile
        customer_data["preferences"].update(profile_update)
        return {
            "status": "profile_updated",
            "updated_profile": customer_data
        }

    # Fetch profile
    return {
        "customer_id": customer_id,
        "preferences": customer_data["preferences"],
        "recent_orders": customer_data["recent_orders"]
    }


# Endpoint 3: Deliver Personalized Dynamic Content
@router.post("/dynamic-content", response_model=dict)
async def dynamic_content(customer_id: str, interaction_context: dict):
    """
    Delivers personalized dynamic content such as banners, offers, and discounts based on the user's preferences and behavior.
    """
    customer_data = fake_customer_db.get(customer_id)

    if not customer_data:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Simulate personalized dynamic content
    if interaction_context.get("last_clicked_item") == "Smartphone":
        dynamic_content = {
            "banner": "Get 10% off on Smartphone Accessories!",
            "offers": [
                {
                    "product_id": "987",
                    "offer": "10% off Wireless Earbuds"
                },
                {
                    "product_id": "1234",
                    "offer": "Buy 1 Get 1 Free on Phone Cases"
                }
            ]
        }
    else:
        dynamic_content = {
            "banner": "Check out our latest offers!",
            "offers": []
        }

    return {
        "dynamic_content": dynamic_content
    }


# Endpoint 4: Retrieve Order History
@router.get("/order-history", response_model=dict)
async def order_history(customer_id: str):
    """
    Retrieves the customer's order history.
    """
    customer_data = fake_customer_db.get(customer_id)

    if not customer_data:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {
        "customer_id": customer_id,
        "order_history": customer_data["recent_orders"]
    }


# Endpoint 5: Contextual Response Based on User Data
@router.post("/contextual-response", response_model=dict)
async def contextual_response(session_id: str, customer_id: str, input_text: str, context: dict):
    """
    Generates a personalized response during a conversation based on the user’s profile, preferences, and interaction history.
    """
    customer_data = fake_customer_db.get(customer_id)

    if not customer_data:
        raise HTTPException(status_code=404, detail="Customer not found")

    preferences = context.get("preferences", {})
    recent_interactions = context.get("recent_interactions", [])

    # Simulate response generation based on context
    if "smartphone" in input_text.lower():
        suggested_items = [
            {
                "product_id": "987",
                "product_name": "Wireless Earbuds",
                "price": "$99.99"
            },
            {
                "product_id": "1234",
                "product_name": "Phone Case",
                "price": "$19.99"
            }
        ]
        response_text = "Based on your recent smartphone purchase, I recommend checking out wireless earbuds or phone accessories."
    else:
        suggested_items = []
        response_text = "I don't have specific recommendations for that request."

    return {
        "response_text": response_text,
        "suggested_items": suggested_items
    }
