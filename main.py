# IMPORTS
import json
import keyboard

# TOOLS
from tools.grammars import print_grammar_info, are_empty_grammars
from tools.dictionaries import dict_to_json, get_functions_dict
from tools.automaton import get_automaton_from_grammar
from tools.menu import arrow_menu
from tools.colors import color

# FILES
from files.reader import file_reader
from files.parser import parse_file

# GLOBALES
main_grammars = []
valid_grammars = {}

# ARCHIVO PRINCIPAL


def set_file():
    # PARSEAR ARCHIVO
    main_file = file_reader(is_dev=True)
    main_dict = parse_file(main_file)

    # GRAMÁTICAS
    global valid_grammars
    valid_grammars = main_dict.get("validGrammars", {})
    invalid_grammars = main_dict.get("invalidGrammars", {})

    # JSON DE SALIDA
    dict_to_json(valid_grammars, './out/grammars.json')
    dict_to_json(invalid_grammars, './out/invalid_grammars.json')

# MOSTRAR INFORMACIÓN


def show_grammars_info():
    # DICCIONARIO DE FUNCIONES
    functions_dict = get_functions_dict(valid_grammars, print_grammar_info)

    # MENSAJE DE ADVERTENCIA
    if not are_empty_grammars(valid_grammars):
        # MENU CON CON GRAMÁTICAS
        arrow_menu("Selecciona una gramática:", list(
            valid_grammars.keys()), functions_dict)


# GENERAR AUTOMATA
def get_automaton():
    # DICCIONARIO DE FUNCIONES
    functions_dict = get_functions_dict(
        valid_grammars, get_automaton_from_grammar)

    # MENSAJE DE ADVERTENCIA
    if not are_empty_grammars(valid_grammars):
        # MENU CON CON GRAMÁTICAS
        arrow_menu("Selecciona una gramática:", list(
            valid_grammars.keys()), functions_dict)


# INICIAR
if __name__ == "__main__":
    # LOOP DE MENU
    arrow_menu("Selecciona una opción:", ["Cargar", "Información", "Autómata", "Recorrido", "Tabla"], {
        "0": set_file,
        "1": show_grammars_info,
        "2": get_automaton
    }, ["Esta opción permite cargar un archivo de entrada\n  con extensión .glc que contiene la información\n  de las gramáticas libres del contexto.", "Esta opción del menú deberá mostrar todos los\n  nombres de gramáticas que se encuentran\n  actualmente en el sistema para elegir una.", "Esta opción permite generar un autómata de pila\n  con respecto de alguna gramática independiente\n  del contexto previamente cargada.", "El usuario podrá elegir uno de los autómatas de\n  pila. Luego solicitará el ingreso de una cadena\n  de entrada para generar un recorrido animado.", "El usuario podrá elegir uno de los autómatas de\n  pila. Luego solicitará el ingreso de una cadena\n  de entrada para generar una tabla de resumen.", "Detiene totalmente la ejecución del programa, y\n  los datos temporales se perderán, a excepción\n  de los archivos de salida ya generados."], horizontal=True)
