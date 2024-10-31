from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional 
     
class Usuario(BaseModel):
    id: str = Field(..., example='p1')
    nombre: str= Field(..., example='Juan')
    email: str = Field(..., example='juan.judas@example.com')
    edad: int = Field(..., example='2024-10-23T19:00:00Z')

class Proyecto(BaseModel):
    id: str 
    nombre: str 
    desripcion:str
    idusuario: str 