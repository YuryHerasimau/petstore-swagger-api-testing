from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class PetRequestSchema(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tag]
    status: str