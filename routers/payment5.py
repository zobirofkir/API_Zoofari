from fastapi import APIRouter
from schemas.schemas import Payment
from repository.payment import make_payment

rout_5 = APIRouter(
    prefix="/payment/5",
    tags=["PAYMENT_5"]
)

@rout_5.post('/')
def post_payment(payment: Payment):
    return make_payment(payment)
    
