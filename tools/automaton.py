# IMPORTS
import keyboard
import os

# FILES
from files.graphviz import get_automaton_graph
from files.html import grammar_dict_to_HTML, get_automaton_html_route

# TOOLS
from tools.colors import color


# GENERAR AUTOMATA DESDE GRAMÁTICA


def get_automaton_from_grammar(grammar_dict, grammar_name):
    # GENERAR GRAFO
    get_automaton_graph(grammar_dict, grammar_name)

    # GENERAR HTML
    grammar_dict_to_HTML(grammar_dict, f'AP_{grammar_name}')

    # MENSAJE DE OK
    print(f'{color.BOLD}{color.GREEN}  ✔️  Automata generado correctamente.{color.END}')
    keyboard.read_key()


def get_automaton_route_from_grammar(grammar_dict, grammar_name):
    # LIMPIAR
    os.system('clear' if os.name == 'posix' else 'cls')

    # LEER
    print(
        f'\n  {color.BOLD}Escribe una cadena para evaluar el automata: {color.END}')

    # GLOBALES
    word = ''

    while(True):
        word = input('')
        key = keyboard.read_key()

        # SALIR
        if key == 'enter':
            get_automaton_html_route(grammar_dict, grammar_name, word)
            break
