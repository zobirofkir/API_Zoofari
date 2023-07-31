from routers.contact import Router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.payment import rout
from routers.payment2 import rout_2
from routers.payment3 import rout_3
from routers.payment4 import rout_4
from routers.payment5 import rout_5
from routers.payment6 import rout_6

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Router)
app.include_router(rout)
app.include_router(rout_2)
app.include_router(rout_3)
app.include_router(rout_4)
app.include_router(rout_5)
app.include_router(rout_6)