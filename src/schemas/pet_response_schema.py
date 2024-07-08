from pydantic import BaseModel, field_validator
from data.data import PetData


class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class CreatePetSchema(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: list[str] = []
    tags: list[Tag] = []
    status: str

    @field_validator("status")
    def check_status(cls, v: str) -> str:
        if v not in PetData.status:
            raise ValueError(f"Invalid status: {v}. Status must be one of {PetData.status}")
        return v