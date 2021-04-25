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

    # LISTA DE LLAVES
    keys = []
    for key in main_dict if is_list else main_dict.keys():
        keys.append(key)

    # FUNCIONES
    for index in range(len(keys)):
        functions_dict[str(index)] = lambda opt: function(
            keys[opt]) if is_list else function(main_dict[keys[opt]], keys[opt])

    # SALIDA
    return functions_dict
