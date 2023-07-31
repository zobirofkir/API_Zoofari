from fastapi import HTTPException, status
import stripe
from schemas.schemas import Payment


stripe.api_key = "sk_test_51Na0skEY0P9b2cBmc3gPOfkgEzX8vLMG0VcVVOfW2Aw6mCz0upg2uIjPRV6EA0ZwMDTEo2ed2GUIiEgwWMy8iikP000S00lQGt"
def make_payment(payment: Payment):
    try:
        stripe.Charge.create(
            amount=int(payment.amount * 100),  
            currency=payment.currency,
            source={
                "object": "card",
                "number": payment.card_number,
                "exp_month": payment.expiration_month,
                "exp_year": payment.expiration_year,
                "cvc": payment.cvc,
            },
        )
        return {"message": "Payment successful"}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))