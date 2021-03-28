# TOOLS
from tools.menu import menu

# FILES
from files.reader import file_reader

# GLOBALES
menu_loop = True
main_file = None

# ARCHIVO PRINCIPAL
def set_file():
    global main_file
    main_file = file_reader(True)

# SALIR
def exit_app():
    global menu_loop
    menu_loop = False

# INICIAR
if __name__ == "__main__":
    # LOOP DE MENU
    while menu_loop:
        menu('(1) Cargar archivo | (2) Salir', {
            1: set_file,
            2: exit_app
        })