from fastapi import APIRouter
from schemas.schemas import Payment
from repository.payment import make_payment

rout = APIRouter(
    prefix="/payment",
    tags=["PAYMENT"]
)

@rout.post('/')
def post_payment(payment: Payment):
    return make_payment(payment)
    
