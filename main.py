from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.responses import Response
from starlette.requests import Request
from pydantic import BaseModel
from typing import List

app = FastApi();

class ListModal(BaseModel):
    identifier: str
    brand: str 
    model: str
    characteristics: Characteristic

class Characteristic(BaseModel):
    ram_memory: number
    rom_memory: number

info_store: List[ListModal] = []

def serialized_stored_events():
    return [info.model_dump() for info in info_store]

@app.get("/health")
async def getHealth ():
    return Response(content="Ok", status_code=200, media_type="text/plain")

@app.post("/phones")
async def postPhones (event_payload: List[ListModal]): 
    info_store.extend(event_payload) 
    return JSONResponse(
        content=serialized_stored_events(),
        status_code=201,
        media_type="application/json",
    )

@app.get("/phones")
async def getPhones () -> Response:
    return JSONResponse(content=serialized_stored_events(), status_code="200") 


@app.get("/phones/{id}")
async def getPhoneId ()

