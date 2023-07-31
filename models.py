from database import Base, engine
from sqlalchemy import Column, String, Integer

class Contact(Base):
    __tablename__='contact';
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    message = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)