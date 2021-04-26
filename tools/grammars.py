# IMPORTS
import os
import keyboard

# COLORES
from .colors import color

# IMPRIMIR INFORMACIÓN DE GRAMÁTICA


def print_grammar_info(grammar, grammar_name):
    """Imprime en pantalla información sobre una gramática

    Args:
        grammar (dict): diccionario de gramática
        grammar_name (str): nombre de gramática

    Returns:
        void
    """
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

# MENSAJE DE ADVERTENCIA


def are_empty_grammars(valid_grammars, is_list=False, custom_warn='No se ha cargado ninguna gramática valida.'):
    """Alerta de gramáticas no cargadas

    Args:
        valid_grammars (dict): diccionario de gramáticas
        is_list (bool, optional): validar si es lista. Defaults to False.
        custom_warn (str, optional): alerta personalizada. Defaults to 'No se ha cargado ninguna gramática valida.'.

    Returns:
        [type]: [description]
    """
    empty_len = len(valid_grammars if is_list else valid_grammars.keys()) == 0

    # MENSAJE DE ADVERTENCIA
    if empty_len:
        print(
            f"\n{color.BOLD}{color.YELLOW}  ⚠️  {custom_warn}{color.END}")
        keyboard.read_key()

    return empty_len
