# IMPORTS
import json

# DICCIONARIO A JSON


def dict_to_json(file_dict, pathname):
    # JSON DE SALIDA
    with open(pathname, 'w') as out:
        json.dump(file_dict, out)

# ARREGLO DESDE DICCIONARIO


def get_functions_dict(main_dict, function, is_list=False):
    functions_dict = {}

    # ENUMERAR
    for index, key in enumerate(main_dict if is_list else main_dict.keys()):
        functions_dict[str(index)] = lambda: function(
            key) if is_list else function(main_dict[key], key)

    # SALIDA
    return functions_dict
