from fastapi import APIRouter
from schemas.schemas import Payment
from repository.payment import make_payment

rout_2 = APIRouter(
    prefix="/payment/2",
    tags=["PAYMENT_2"]
)

@rout_2.post('/')
def post_payment(payment: Payment):
    return make_payment(payment)
    
