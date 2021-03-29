# IMPORTS
import os

# MENU
def menu(options, actions):
    # LIMPIAR
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # SEPARADOR
    title = " | ".join(map(lambda enum: f'({enum[0] + 1}) {enum[1]}', enumerate(options)))
    hr = "-" * (len(title) + 4)

    # MENU
    print(f'{hr}\n| {title} |\n{hr}')

    # OPCIONES
    option = input('Escribe una opción: ')

    # LLAMAR OPCIÓN
    func = actions.get(int(option), lambda: menu(options, actions))
    func()