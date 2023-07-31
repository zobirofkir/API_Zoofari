from pydantic import BaseModel

class contact(BaseModel):
    name :str
    email :str
    subject :str
    message :str


class Payment(BaseModel):
    card_number: str
    expiration_month: str
    expiration_year: str
    cvc: str
    amount: float
    currency: str