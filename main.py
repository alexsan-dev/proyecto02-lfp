# IMPORTS
import json
import keyboard

# TOOLS
from tools.automaton import get_automaton_from_grammar, get_automaton_input_from_grammar
from tools.grammars import print_grammar_info, are_empty_grammars
from tools.dictionaries import dict_to_json, get_functions_dict
from tools.menu import arrow_menu
from tools.colors import color

# FILES
from files.reader import file_reader
from files.parser import parse_file

# GLOBALES
automatons = []
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
    # COMBINAR FUNCIONES
    def handle_automaton(grammar_dict, grammar_name):
        get_automaton_from_grammar(grammar_dict, grammar_name)
        if not grammar_name in automatons:
            automatons.append(grammar_name)

    # DICCIONARIO DE FUNCIONES
    functions_dict = get_functions_dict(
        valid_grammars, handle_automaton)

    # MENSAJE DE ADVERTENCIA
    if not are_empty_grammars(valid_grammars):
        # MENU CON CON GRAMÁTICAS
        arrow_menu("Selecciona una gramática:", list(
            valid_grammars.keys()), functions_dict)

# GENERAR RECORRIDO


def get_automaton_file(template):
    # COMBINAR FUNCIONES
    def handle_automaton_route(grammar_name):
        get_automaton_input_from_grammar(template,
                                         valid_grammars[grammar_name], grammar_name)

        # DICCIONARIO DE FUNCIONES
    functions_dict = get_functions_dict(
        automatons, handle_automaton_route, is_list=True)

    # MENSAJE DE ADVERTENCIA
    if not are_empty_grammars(automatons, is_list=True, custom_warn='No se ha cargado ningún automata.'):
        # MENU CON CON GRAMÁTICAS
        arrow_menu("Selecciona un automata:",
                   automatons.copy(), functions_dict)


def get_automaton_route():
    # GENERAR AUTOMATA
    get_automaton_file('route')


def get_automaton_table():
    # GENERAR AUTOMATA
    get_automaton_file('table')


# INICIAR
if __name__ == "__main__":
    # LOOP DE MENU
    arrow_menu("Selecciona una opción:", ["Cargar", "Información", "Autómata", "Recorrido", "Tabla"], {
        "0": set_file,
        "1": show_grammars_info,
        "2": get_automaton,
        "3": get_automaton_route,
        "4": get_automaton_table
    }, ["Esta opción permite cargar un archivo de entrada\n  con extensión .glc que contiene la información\n  de las gramáticas libres del contexto.", "Esta opción del menú deberá mostrar todos los\n  nombres de gramáticas que se encuentran\n  actualmente en el sistema para elegir una.", "Esta opción permite generar un autómata de pila\n  con respecto de alguna gramática independiente\n  del contexto previamente cargada.", "El usuario podrá elegir uno de los autómatas de\n  pila. Luego solicitará el ingreso de una cadena\n  de entrada para generar un recorrido animado.", "El usuario podrá elegir uno de los autómatas de\n  pila. Luego solicitará el ingreso de una cadena\n  de entrada para generar una tabla de resumen.", "Detiene totalmente la ejecución del programa, y\n  los datos temporales se perderán, a excepción\n  de los archivos de salida ya generados."], horizontal=True)
