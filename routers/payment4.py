from fastapi import APIRouter
from schemas.schemas import Payment
from repository.payment import make_payment

rout_4 = APIRouter(
    prefix="/payment/4",
    tags=["PAYMENT_4"]
)

@rout_4.post('/')
def post_payment(payment: Payment):
    return make_payment(payment)
    
