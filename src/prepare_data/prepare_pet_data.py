from data.pet_data_class import PetDataClass
from src.prepare_data.prepare_basic_data import BaseTestData


class PreparePetData(BaseTestData):
    
    def prepare_pet_json(self, info: PetDataClass, key=None):
        data = {
            "id": info.uid,
            "category": info.category,
            "name": info.name,
            "photoUrls": info.photoUrls,
            "tags": info.tags,
            "status": info.status
        }
        # check what happens if some key is not in the request body
        if key is not None:
            data.pop(key)
        return self.format_data_as_json(data=data)
