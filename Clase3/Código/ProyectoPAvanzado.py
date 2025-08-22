#
import datetime as dt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import DateEntry
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.toast import ToastNotification


#Datos en memoria
registros= []
_next_id = 1

def generar_id():
    global _next_id
    val= _next_id
    _next_id +=1
    return val


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="flatly")
        self.title("Gestion de usuarios")
        self.geometry("520x420")


        #Construccion
        cont = ttk.LabelFrame(self, text="Nuevo Usuario", padding=12, bootstyle=PRIMARY)
        cont.pack(fill=BOTH,expand=YES, padx=12, pady=12 )

        #Nombre
        ttk.Label(cont, text="Nombre Completo").grid(row=0, column=0, sticky=W, pady=4)
        self.ent_nombre= ttk.Entry(cont, width=32)
        self.ent_nombre.grid(row=0, column=1, sticky=EW, pady=4, padx=6)

        #Correo
        ttk.Label(cont, text="Correo").grid(row=1, column=0, sticky=W, pady=4)
        self.ent_email= ttk.Entry(cont, width=32)
        self.ent_email.grid(row=1, column=1, sticky=EW, pady=4, padx=6)

        #Rol
        ttk.Label(cont, text="Rol").grid(row=2, column=0, sticky=W, pady=4)
        self.cbo_rol= ttk.Combobox(cont, state="readonly", width=20, values=["Administrador","Editor","Visitante"])
        self.cbo_rol.set("Visitante")
        self.cbo_rol.grid(row=2, column=1, sticky=EW, pady=4, padx=6)

        #eSTADO
        ttk.Label(cont, text="Estado").grid(row=3, column=0, sticky=W, pady=4)
        self.var_estado=ttk.StringVar(value="Activo")
        rf = ttk.Frame(cont); rf.grid(row=3, column=1, sticky=W, pady=4)
        ttk.Radiobutton(rf, cursor="hand2" , text="Activo", variable=self.var_estado, value="Activo", bootstyle=SUCCESS).pack(side=LEFT, padx=2)
        ttk.Radiobutton(rf, text="Inactivo", variable=self.var_estado, value="Inactivo", bootstyle=WARNING).pack(side=LEFT, padx=2)


        #Fecha de registro
        ttk.Label(cont, text="Fecha Registro").grid(row=4, column=0, sticky=W, pady=4)
        self.ent_fecha = DateEntry(cont, dateformat="%Y-%m-%d")
        self.ent_fecha.set_date(dt.date.today())
        self.ent_fecha.grid(row=4, column=1, sticky=W, pady=4)

        
        #BOTONES
        btns = ttk.Frame(cont); btns.grid(row=5, columnspan=2 ,column=0, sticky=W, pady=4)
        ttk.Button(btns, text="Guardar", bootstyle=PRIMARY, command=self._guardar).pack(side=LEFT, padx=4)
        ttk.Button(btns, text="Limpiar", bootstyle=SECONDARY).pack(side=LEFT, padx=4)

        for i in  range(2):
            cont.columnconfigure(i, weight=1)

    def _guardar(self):
        usuario={
            "id": generar_id(),
            "nombre": self.ent_nombre.get(),
            "email": self.ent_email.get(),
            "rol":self.cbo_rol.get(),
            "estado":self.var_estado.get(),
            "fecha":self.ent_fecha.entry.get()
        }

        registros.append(usuario)

        print(registros)

        ToastNotification(title="Guardado",
                            message=f"Usuario {usuario['nombre']} creado",
                            duration=2000,
                            position=(self.winfo_x()+40, self.winfo_y()+60)).show_toast()




    
if __name__ == "__main__":
    App().mainloop()