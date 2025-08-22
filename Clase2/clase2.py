#Ejemplo de ventanas
import tkinter as tk
from tkinter import messagebox


"""



#función que se va a ejecutar cuando se da clic

def saludar():
    messagebox.showinfo("Saludar","Hola Jimmy, gracias por utilizar el sistema...")


#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Tk en Python")
ventana.geometry("300x200")

#Etiqueta
#                   parametros de los parentesis donde lo voy a colocar y que contenido va a tener
etiqueta = tk.Label(ventana,text="Hola esta es mi primer ventana")
etiqueta.pack(pady=20)

#Botón que genera el evento
#                 donde lo coloco, mensaje y funcionalidad a que evento llamo
boton = tk.Button(ventana,text="Haz clic aquí", command=saludar)
boton.pack()


#Inicar un ciclo de eventos
ventana.mainloop()


""" # Fin de la explicación

#Función que llama el botón la hacer clic

def enviarInfo():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    motivo = variable_motivo.get()
    mensaje = texto_mensaje.get("1.0",tk.END).strip()
    if not nombre or not correo or not mensaje:
        messagebox.showerror("Faltan datos...")
    else:                             
        messagebox.showinfo("Mensaje enviado",f"Gracias {nombre}, por enviarnos tu {motivo}: {mensaje}, bajo el apartado")
        #Limpiar campos
        entry_nombre.delete(0,tk.END) 
        #Elimina todo el campo de texto. 0 es la posición inicial del contenido, end el final
        entry_correo.delete(0,tk.END)
        texto_mensaje.delete("1.0",tk.END) 
        


ventana = tk.Tk()
ventana.title("Formulario de contacto")
ventana.geometry("500x500")
ventana.config(bg="#B8E6FE")

#Etiqueta t campo del nombre
tk.Label(ventana,text="Nomre: ",bg= "#f0f0f0",font=("Arial",10)).pack(pady=10)
entry_nombre = tk.Entry(ventana,width=40)
entry_nombre.pack(pady=5)

#Correo
tk.Label(ventana, text="Correo: ",bg="#f0f0f0",font=("Arial",10)).pack(pady=10)
entry_correo = tk.Entry(ventana,width=40)
entry_correo.pack(pady=5)

#Motivo del contacto
tk.Label(ventana, text="Motivo: ",bg="#f0f0f0",font=("Arial",10)).pack(pady=10)

#Menú de opciones
motivos = ["Consulta","Sugerencia","Reclamos","Otros"]
variable_motivo = tk.StringVar(ventana)
variable_motivo.set(motivos[0]) #Valor inicial
menu_motivo = tk.OptionMenu(ventana,variable_motivo,*motivos)
menu_motivo.pack(pady=10)

#Área de texto
tk.Label(ventana, text="Mensaje: ",bg="#f0f0f0",font=("Arial",10)).pack(pady=10)
texto_mensaje = tk.Text(ventana,height=10,width=40)
texto_mensaje.pack(pady=5)

#Botón
boton_enviar = tk.Button(ventana,text="Enviar",command=enviarInfo, background="#05df72", fg="#f0f0f0",font=("Arial",10, "bold"))
boton_enviar.pack(pady=10)

#Ejecutar
ventana.mainloop()