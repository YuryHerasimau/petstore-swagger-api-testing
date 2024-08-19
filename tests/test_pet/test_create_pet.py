import allure
import pytest
import json
from data import get_pet_endpoints
from data.data import PetData
from src.http_methods import MyRequests
from src.assertions import Assertions
from src.validator import Validator
from src.schemas import CreatePetSchemas
from src.prepare_data.prepare_pet_data import PreparePetData
from http import HTTPStatus
from generator.pet_generator import PetGenerator


@allure.epic("Testing create pet")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()
    validator = Validator()
    pet_data = PreparePetData()
    pet_generator = PetGenerator()

    @allure.title("Create pet")
    def test_create_pet_and_get_it(self, get_test_name):
        info = next(self.pet_generator.generate_pet(urls_count=2, tags_count=3))
        data = self.pet_data.prepare_pet_json(info=info)
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(
            response=response,
            expected_status_code=HTTPStatus.OK,
            test_name=get_test_name
        )
        self.validator.validate_response(response=response, model=CreatePetSchemas.create_pet)

        pet_id = response.json()["id"]
        response_get = self.request.get(url=self.url.get_pet_by_id(petId=pet_id))
        self.assertions.assert_status_code(
            response=response_get,
            expected_status_code=HTTPStatus.OK,
            test_name=get_test_name
        )
        self.validator.validate_response(response=response_get, model=CreatePetSchemas.create_pet)

    @allure.title("Create pet with valid status")
    @pytest.mark.parametrize("status", PetData.status)
    def test_create_pet_with_valid_status(self, get_test_name, status):
        info = next(self.pet_generator.generate_pet(status=status))
        data = self.pet_data.prepare_pet_json(info=info)
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(
            response=response,
            expected_status_code=HTTPStatus.OK,
            test_name=get_test_name
        )
        self.validator.validate_response(response=response, model=CreatePetSchemas.create_pet)


    @allure.title("Create pet with invalid status")
    def test_create_pet_with_invalid_status(self, get_test_name):
        info = next(self.pet_generator.generate_pet(status="invalid_status"))
        data = self.pet_data.prepare_pet_json(info=info)
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(
            response=response,
            expected_status_code=HTTPStatus.OK,
            test_name=get_test_name
        )
        self.validator.validate_response(response=response, model=CreatePetSchemas.create_pet)
