import json
from functions import get_json_data
from src.prepare_data.prepare_basic_data import BaseTestData


class PreparePetData(BaseTestData):
    
    def prepare_pet_json(self):
        # json_data = get_json_data("pet_data.json")
        # return json.dumps(json_data)

        data = {
            "id": get_id(uid=uid),
            "category": create_category(category_value=category_value),
            "name": get_name(name=name),
            "photoUrls": get_photo_urls(),
            "tags": get_tags(),
            "status": get_status()
        }
        return data
