# IMPORTS
import json

def dict_to_json(file_dict, pathname):
    # JSON DE SALIDA
    with open(pathname, 'w') as out:
        json.dump(file_dict, out)