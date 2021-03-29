# IMPORTS
import os
import keyboard
from .colors import color

# OPCIÓN ACTUAL
current_option_index = 0
is_pressed = False

# HABILITAR MOVIMIENTOS
def press_key(pressed):
    global is_pressed
    is_pressed = pressed

# NAVEGAR EN EL MENU
def navigate(key, len_options, horizontal):
    global is_pressed
    global current_option_index

    if not is_pressed:
        # SUBIR
        if key == ('down' if horizontal else 'up') or key == 'left':
            if current_option_index == 0:
                current_option_index = len_options - 1
            else:
                current_option_index -= 1

        # BAJAR
        elif key == ('up' if horizontal else 'down') or key == 'right':
            if current_option_index == len_options - 1:
                current_option_index = 0
            else:
                current_option_index += 1

    # EVITAR QUE SE PRESIONE
    is_pressed = True

# MENU DE FLECHAS
def arrow_menu(title="Selecciona una opción:", options=[], actions={}, helpers=[],on_exit=None, horizontal=False):
    # GLOBALES
    global current_option_index
    global is_pressed

    # AGREGAR EVENTOS
    keyboard.on_release(lambda _: press_key(False), suppress=True)

    # AGREGAR EVENTO DE SALIDA
    options.append("Salir")

    # SEPARADOR Y CONFIGURACIONES
    break_line = "\n"
    len_options = len(options)
    current_option_index = 0

    # MAPA DE MENU
    def menu_map(enum):
        # GLOBALES
        is_current_option = enum[0] == current_option_index

        # STRING DE SALIDA
        return f'{color.BOLD + color.BLUE if is_current_option else color.END}{color.RED if enum[0] == len_options - 1 and is_current_option else ""}{"" if horizontal else "  "}{"⦿  " if is_current_option else "• "}{enum[1]}{color.END}'

    # LOOP
    while True:
        # LIMPIAR
        os.system('clear' if os.name == 'posix' else 'cls')

        # TEXTOS DE MENU
        header = (" │ " if horizontal else break_line).join(map(menu_map, enumerate(options)))
        hr = "–" * (len(header) - (51 if current_option_index < len_options - 1 else 56))

        # IMPRIMIR
        print(f'\n  ⓘ  {color.BOLD}{color.UNDERLINE}{title}\n{color.END}  Puedes usar las flechas de tu{break_line}  teclado para moverte, despues{break_line}  presiona ENTER para seleccionar.{break_line}{break_line}{f"  ○{hr}○" if horizontal else ""}{break_line if horizontal else ""}{"  │ " if horizontal else ""}{header}{" │" if horizontal else ""}{f"{break_line}  ○{hr}○" if horizontal else ""}{break_line}{break_line}  {helpers[current_option_index] if len(helpers) > current_option_index else ""}{break_line}')

        # ESPERAR ENTRADA
        key = keyboard.read_key(suppress=True)
        navigate(key, len_options, horizontal)

        # SELECCIONAR
        if key == 'enter':
            actions.get(str(current_option_index), lambda: None)()

            # SALIR
            if current_option_index == len_options - 1:
                current_option_index = 0
                break
