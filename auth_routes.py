from fastapi import APIRouter
from models import User


auth_route = APIRouter(prefix="/auth", tags=["auth"])


@auth_route.get("/")
async def home():
    """
    This is the default order route of our system. All order routes require authentication.
    """
    return {
        "message": "You have accessed the default authentication route.",
        "authenticated": False
    }

@auth_route.post('/create_account')
async def create_account(
    email: str,
    password: str
):
    user = ...
