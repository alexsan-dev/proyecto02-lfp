# IMPORTS
import json

# DICCIONARIO A JSON


def dict_to_json(file_dict, pathname):
    # JSON DE SALIDA
    with open(pathname, 'w') as out:
        json.dump(file_dict, out)

# ARREGLO DESDE DICCIONARIO


def get_functions_dict(main_dict, function):
    functions_dict = {}

    # ENUMERAR
    for index, key in enumerate(main_dict.keys()):
        functions_dict[str(index)] = lambda: function(main_dict[key], key)

    # SALIDA
    return functions_dict
