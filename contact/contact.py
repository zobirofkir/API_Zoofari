from database import Base, SessionLocal
from fastapi import HTTPException, status
from schemas.schemas import contact
from models import Contact

def contact_api(user:contact):
    db = SessionLocal()
    existing_email = db.query(Contact).filter(Contact.email==user.email).first()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This email has been already existing !!!")
    else:
        new_cont = Contact(
            name = user.name,
            email = user.email,
            subject = user.subject,
            message = user.message
        )
        db.add(new_cont)
        db.commit()
        db.refresh(new_cont)
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Ok")
    