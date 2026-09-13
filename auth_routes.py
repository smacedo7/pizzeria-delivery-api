from fastapi import APIRouter, Depends
from models import User
from dependencies import pick_session
from main import bcrypt_context


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
    password: str,
    name: str,
    session=Depends(pick_session),
):
    user = session.query(User).filter(User.email == email).first()
    if user:
        return {"message": "There is already a user registered with this email."}
    else:
        encrypted_password = bcrypt_context.hash(password)
        new_user = User(name=name, email=email, password=encrypted_password)
        session.add(new_user)
        session.commit()
        return {"message": "User successfully registered."}
