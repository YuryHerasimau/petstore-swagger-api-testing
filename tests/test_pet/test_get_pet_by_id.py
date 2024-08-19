import allure
import pytest
from data import get_pet_endpoints
from data.data import PetData
from src.http_methods import MyRequests
from src.assertions import Assertions
from http import HTTPStatus
from src.validator import Validator
from src.schemas import CreatePetSchemas


@allure.epic("Testing get pet by id")
class TestGetPetById:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()
    validator = Validator()

    @allure.title("Get pet with existing id")
    def test_get_pet_by_existing_id(self, get_test_name):
        response = self.request.get(url=self.url.get_pet_by_id(petId=1))
        self.assertions.assert_status_code(
            response=response,
            expected_status_code=HTTPStatus.OK,
            test_name=get_test_name
        )
        self.validator.validate_response(response=response, model=CreatePetSchemas.create_pet)
        
    @allure.title("Get pet with invalid id")
    @pytest.mark.parametrize("invalid_id", PetData.invalid_integer_values)
    def test_get_pet_by_invalid_id(self, get_test_name, invalid_id):
        response = self.request.get(url=self.url.get_pet_by_id(petId=invalid_id))
        self.assertions.assert_status_code(
            response=response,
            expected_status_code=HTTPStatus.NOT_FOUND,
            test_name=get_test_name
        )