import os
import json


def get_current_path(file_name: str):
    current_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_path, file_name)


def get_json_data(json_data):
    config_file = get_current_path(json_data)
    with open(config_file) as f:
        config_data = json.load(f)
    return config_data