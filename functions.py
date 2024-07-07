import os


def get_current_path(file_name: str):
    current_path = os.path.dirname(os.path.abspath(__file__))
    print("current_path is ", current_path)
    print("join the current_path and file_name is ", os.path.join(current_path, file_name))
    return os.path.join(current_path, file_name)
