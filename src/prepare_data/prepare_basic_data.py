import json


class BaseTestData:
    
    def format_data_as_json(self, data):
        json_data = json.dumps(data)
        return json_data