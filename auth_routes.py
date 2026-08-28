from fastapi import APIRouter


auth_route = APIRouter(prefix="/auth", tags=["auth"])


@auth_route.get("/")
def authenticate():
    """
    This is the default order route of our system. All order routes require authentication.
    """
    return {
        "message": "You have accessed the default authentication route.",
        "authenticated": False
    }
