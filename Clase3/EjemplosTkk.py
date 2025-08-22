from tkinter.ttk import Frame
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#Ventana con temas
ventana = ttk.Window(themename="flatly")# flatly darkly cosmo...
ventana.geometry("500x300")
ventana.title("Ejemplo con bootstrap")

#Marcp Principal
frame = ttk.Frame(ventana, padding=20)
frame.pack(fill=BOTH, expand=True)

#Etiqueta
ttk.label(frame, text="Nombre", font=("Arial",12)).pack(anchor=W, pady=5)

#Campo de entrada
nombre_entry = ttk.Entry(frame, width=30)
nombre_entry.pack(anchor=w, pady=5)

#Botones
ttk.Button(frame, text="Guardar",bootstyle=SUCCESS, width=15).pack(side=LEFT, padx=5, pady=20)
ttk.Button(frame, text="Cancelar",bootstyle=DANGER, width=15).pack(side=LEFT,padx=5, pady=20)

def mostrarNombre():
    print(f"Hola,{nombre_entry.get}")
    
ttk.Button(frame, text="Saludar",bootstyle=PRIMARY, command=mostrarNombre).pack(side=LEFT,padx=5, pady=20)

ventana.main.loop()
