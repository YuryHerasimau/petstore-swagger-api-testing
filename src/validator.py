from pydantic import ValidationError
from requests import Response
from src.logger import get_logger
# from src.schemas.create_pet_schema import CreatePetSchema


class Validator:
    logger = get_logger(__name__)

    @staticmethod
    def validate_response(response: Response, model):
        try:
            validation = model.model_validate_json(response.text)
            if validation.model_dump():
                return model(**response.json())
        except ValidationError as ex:
            Validator.logger.error(ex)
            raise ex