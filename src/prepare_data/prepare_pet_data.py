from data.pet_data_class import PetDataClass
from src.prepare_data.prepare_basic_data import BaseTestData
from src.schemas.pet_request_schema import PetRequestSchema


class PreparePetData(BaseTestData):
    
    def prepare_pet_json(self, info: PetDataClass):
        data = PetRequestSchema(
            id=info.uid,
            category=info.category,
            name=info.name,
            photoUrls=info.photoUrls,
            tags=info.tags,
            status=info.status
        )
        return data.model_dump_json()