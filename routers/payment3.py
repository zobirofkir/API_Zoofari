from fastapi import APIRouter
from schemas.schemas import Payment
from repository.payment import make_payment

rout_3 = APIRouter(
    prefix="/payment/3",
    tags=["PAYMENT_3"]
)

@rout_3.post('/')
def post_payment(payment: Payment):
    return make_payment(payment)
    
