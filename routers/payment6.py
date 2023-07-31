from fastapi import APIRouter
from schemas.schemas import Payment
from repository.payment import make_payment

rout_6 = APIRouter(
    prefix="/payment/6",
    tags=["PAYMENT_6"]
)

@rout_6.post('/')
def post_payment(payment: Payment):
    return make_payment(payment)
    
