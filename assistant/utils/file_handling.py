import os

def find_path_to_data_file(file):

    current_script_path = os.path.abspath(__file__)
    ai_assistant_dir = os.path.abspath(os.path.join(current_script_path, '..', '..', '..', '..'))
    file_path = os.path.join(ai_assistant_dir, 'data', file)

    return file_path


def write_output_to_file(output, file_path):
    with open(file_path, 'w') as file:
        file.write(output)
