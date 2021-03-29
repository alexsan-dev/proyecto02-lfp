# IMPORTS
import json

# TOOLS
from tools.menu import menu
from tools.dictionaries import dict_to_json

# FILES
from files.reader import file_reader
from files.parser import parse_file

# GLOBALES
menu_loop = True
main_grammars = []

# ARCHIVO PRINCIPAL
def set_file():
    main_file = file_reader(is_dev=True)
    main_dict = parse_file(main_file)

    # JSON DE SALIDA
    dict_to_json(main_dict.get("validGrammars"), './out/grammars.json')
    dict_to_json(main_dict.get("invalidGrammars"), './out/invalid_grammars.json')

# SALIR
def exit_app():
    global menu_loop
    menu_loop = False

# INICIAR
if __name__ == "__main__":
    # LOOP DE MENU
    while menu_loop:
        menu(['Cargar archivo', 'Salir'], {
            1: set_file,
            2: exit_app
        })