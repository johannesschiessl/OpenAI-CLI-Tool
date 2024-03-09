import os
import json
import config


def create_config_file_if_not_exist():
    """
    Creates a config file if it does not exist.
    """
    if not os.path.exists(find_path_to_data_directory()):
        os.makedirs(find_path_to_data_directory())

    config_data: dict = {
        "version": config.VERSION,
        "model": config.DEFAULT_GPT_MODEL
    }

    with open(find_path_to_data_file("config.json"), 'w') as file:
        json.dump(config_data, file)

def find_path_to_data_directory():
    """
    Function to find the path to the data directory.

    Returns:
        str: The file path to the data directory.
    """
    current_script_path: str = os.path.abspath(__file__)
    ai_assistant_dir: str = os.path.abspath(os.path.join(current_script_path, '..', '..', '..'))
    file_path: str = os.path.join(ai_assistant_dir, 'data')
    return file_path

def find_path_to_data_file(file):
    """
    A function to find the path to a data file.

    Parameters:
    file (str): The name of the data file.

    Returns:
    str: The absolute file path.
    """
    current_script_path: str = os.path.abspath(__file__)
    ai_assistant_dir: str = os.path.abspath(os.path.join(current_script_path, '..', '..', '..'))
    file_path: str = os.path.join(ai_assistant_dir, 'data', file)
    return file_path


def write_output_to_file(output):
    """
    Write the output to a file.

    Args:
        output (str): The output to be written to the file.

    Returns:
        None
    """
    file_path: str = find_path_to_data_file("transcription.txt")
    with open(file_path, 'w') as file:
        file.write(output)
