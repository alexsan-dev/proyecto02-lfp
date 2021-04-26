# IMPORTS
from tkinter import filedialog
from tkinter import *

# TKINTER
TK_SILENCE_DEPRECATION = 1
root = Tk()
root.wm_withdraw()


def file_reader(is_dev=False, dev_path='./test.glc'):
    """Lee un archivo .glc

    Args:
        is_dev (bool, optional): Modo desarrollo, deshabilita Tkinter. Defaults to False.
        dev_path (str, optional): Ruta de desarrollo. Defaults to './test.glc'.

    Returns:
        str: Archivo como texto
    """
    # SELECCIONAR ARCHIVO
    filename = None if is_dev else filedialog.askopenfilename(
        initialdir="/", title="Seleccionar archivo", filetypes=(("GLC", "*.glc"), ("all files", "*.*")))

    # LEER LINEAS
    stream = open(dev_path if is_dev else filename, encoding='utf-8')
    lines = stream.read()

    # CERRAR STREAM
    stream.close()
    return lines
