from fastapi import FastAPI, Path , Depends
from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from addressdatabase import Base , engine , SessionLocal
from sqlalchemy import create_engine , Column , String , Integer, Boolean , Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import sqlite3





app = FastAPI()
 
address = {
    1: {
        "name": "john",
        "longitude": 20.59,
        "latitude": 78.93,
        "streetname": "parkstreet"}
}

#model
class addressentry(BaseModel):
    id: int
    name: str
    longitude: float
    latitude: float
    streetname: str

class updatentry(BaseModel):
    id:int
    name: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    streetname: Optional[str] = None


class User(Base):
  __tablename__="users"
  id:int
  name = Column(String, primary_key=True, index=True)
  longitude = Column(Float)
  latitude = Column(Float)
  streetname = Column(String)
  
#schema 
    
class User(Base): 
    __tablename__="users"
    id:int
    name: str
    longitude: float
    latitude: float
    streetname: str
    

   
class UserSchema(BaseModel):
     id:int
     name: str
     longitude: float
     latitude: float
     streetname: str
     
     class Config:
         orm_mode=True
     
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
        
  

Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"name": "first entry"}


@app.get("/get-address/{id}")
def get_address(id: int = Path(None, description="the id is ", gt=0)):
    return address[id]


@app.get("/get-by-longitude")
def get_address(*, longitude: float, test: int):
    for id in address:
        if address[id]["longitude"] == longitude:
            return address[id]
    return {"Data": "not registered"}


@app.get("/get-by-latitude")
def get_address(latitude: float):
    for id in address:
        if address[id]["latitude"] == latitude:
            return address[id]
    return {"Data": "not registered"}


@app.get("/get-by-name")
def get_address(name: str):
    for id in address:
        if address[id]["name"] == name:
            return address[id]
    return {"Data": "not registered"}


@app.get("/get-by-street")
def get_address(streetname: str):
    for id in address:
        if address[id]["streetname"] == streetname:
            return address[id]
    return {"Data": "not registered"}




@app.post("/enter details/{id}")
def create_details(id: int, details: addressentry):
    if id in address:
        return {"Error": "data already exists"}
    address[id] = details
    return address[id]




@app.post("/users",response_model=UserSchema)
def index(user:UserSchema,db:Session=Depends(get_db)):
    u= User(streetname=user.streetname,longitude=user.longitude,
              latitude=user.latitude,name=user.name)
    db.add(u)
    db.commit()
    return u
    

@app.put("/update-entry/{id}")
def update_details(id: int, details: updatentry):
    if id not in address:
        return {"Error": "not registered"}
    if details.name != None:
        address[id].name=details.name
    if details.longitude != None:
        address[id].longitude=details.longitude
    if details.latitude != None:
         address[id].latitude=details.latitude  
    if details.streetname!= None:
        address[id].streetname=details.streetname
    
  
    return address[id]
    
@app.delete("/delete-entry/{id}")    
def delete_details(id:int):
    if id not in address:
        return {"Error": "data not registered"}
    del address[id]
    return {"Massage": " the entry is removed"}

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
