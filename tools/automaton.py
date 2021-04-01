# IMPORTS
import keyboard

# FILES
from files.graphviz import get_automaton_graph
from files.html import grammar_dict_to_HTML

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
    print(grammar_dict)
