import json
import allure
from requests import Response


class BaseTestData:
    
    def format_data_as_json(self, data):
        json_data = json.dumps(data)
        return json_data

    @staticmethod
    def attach_request(request):
        request = json.dumps(json.loads(request.json()), indent=4)
        allure.attach(
            name="Request",
            body=request,
            attachment_type=allure.attachment_type.JSON
        )

    @staticmethod
    def attach_response(response: Response):
        response = json.dumps(response.json(), indent=4)
        allure.attach(
            name="Response",
            body=response,
            attachment_type=allure.attachment_type.JSON
        )