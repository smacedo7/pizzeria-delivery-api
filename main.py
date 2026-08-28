from fastapi import FastAPI


app = FastAPI()

from auth_routes import auth_route
from order_routes import order_route

app.include_router(auth_route)
app.include_router(order_route)
