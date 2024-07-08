from dataclasses import dataclass


@dataclass
class PetDataClass:
    uid: int
    category: dict
    name: str
    photoUrls: str
    tags: dict
    status: str