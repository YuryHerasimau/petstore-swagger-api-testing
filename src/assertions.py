from requests import Response
from src.logger import get_logger


class Assertions:

    @staticmethod
    def assert_status_code(response: Response, actual_status_code: int, test_name: str):
        expected_status_code = response.status_code
        assert actual_status_code == expected_status_code, (
            get_logger(test_name).error(f"Expected {expected_status_code} but got {actual_status_code} instead")
        )