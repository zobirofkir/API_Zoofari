from schemas.schemas import contact
from fastapi import APIRouter
from contact.contact import contact_api 

Router = APIRouter(
    prefix="/contact",
    tags=["Contact"]
)

@Router.post('/')
def creat_contact(user:contact):
    return contact_api(user)
