# IMPORTS
from tkinter import filedialog
from tkinter import *

# TKINTER
TK_SILENCE_DEPRECATION = 1
root = Tk()
root.wm_withdraw()

def file_reader(isDev=False, dev_path='./test.glc'):
    # SELECCIONAR ARCHIVO
    isDev = isDev
    filename = None if isDev else filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo", filetypes=(("GLC", "*.glc"), ("all files", "*.*")))

    # LEER LINEAS
    stream = open(dev_path if isDev else filename, encoding='utf-8')
    lines = stream.read()

    # CERRAR STREAM
    stream.close()
    return lines