# IMPORTS
import os
import keyboard

# COLORES
from .colors import color

# IMPRIMIR INFORMACIÓN DE GRAMÁTICA


def print_grammar_info(grammar, grammar_name):
    # LIMPIAR
    os.system('clear' if os.name == 'posix' else 'cls')

    # PRODUCCIONES A DICCIONARIO
    productions_dict = {}
    for production in grammar["productions"]:
        # AGREGAR TRANSICION
        transition = productions_dict.get(production["entry"], [])
        transition.append("".join(production["transitions"]))

        # AGREGAR A DICCIONARIO
        productions_dict[production["entry"]] = transition

    # MAPA DE PRODUCCIONES
    def productions_map(production_key):
        return f'    {production_key} ⮕  {" | ".join(productions_dict[production_key])}'

    # IMPRIMIR GRAMÁTICA
    break_line = "\n"
    brackets = ["{", "}"]
    print(
        f'\n{color.BOLD}  Nombre de la gramática tipo 2 :{color.END} {grammar_name}\n{color.BOLD}  No terminales ={color.END} {brackets[0]} {",".join(grammar["noTerminals"])} {brackets[1]}\n{color.BOLD}  Terminales ={color.END} {brackets[0]} {",".join(grammar["terminals"])} {brackets[1]}\n{color.BOLD}  No terminal inicial ={color.END} {grammar["initialNoTerminal"]}\n{color.BOLD}  Producciones :{color.END}\n\n{break_line.join(map(productions_map, productions_dict.keys()))}\n\n{color.BOLD}{color.RED}  ⦿  Salir {color.END}')

    # SALIR
    key = keyboard.read_key()
    if key == "enter":
        return True

# MENSAJE DE ADVERTENCIA


def are_empty_grammars(valid_grammars):
    empty_len = len(valid_grammars.keys()) == 0

    # MENSAJE DE ADVERTENCIA
    if empty_len:
        print(
            f"\n{color.BOLD}{color.YELLOW}  ⚠️  No se ha cargado ninguna gramática valida.{color.END}")
        keyboard.read_key()

    return empty_len
