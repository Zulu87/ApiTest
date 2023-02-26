import json


#  оголошуємо фунцію config_json що вміст json файлу представлятиме у вигляді dict
def config_json(file_to_open):
    with open(file_to_open ) as config_file:
        parsed_json = json.load(config_file)

    return parsed_json