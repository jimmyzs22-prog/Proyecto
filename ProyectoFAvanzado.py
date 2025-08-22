#Paso 1
import datetime as dt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import DateEntry
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.toast import ToastNotification

# Datos en memoria
registros = []

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="flatly")
        self.title("Gestión de usuarios")
        self.geometry("1020x720")

        # Frame cambio de temas
        top = ttk.Frame(self, padding=12)
        top.pack(fill=X)
        ttk.Label(top, text="Tema:", bootstyle=SECONDARY).pack(side=LEFT, padx=8)
        self.cbo_theme = ttk.Combobox(top, state="readonly", width=18, values=sorted(self.style.theme_names()))
        self.cbo_theme.set(self.style.theme_use())
        self.cbo_theme.pack(side=LEFT)
        ttk.Button(top, text="Cambiar", bootstyle="outline-primary", command=self._change_theme).pack(side=LEFT, padx=6)

        # Construcción formulario
        cont = ttk.LabelFrame(self, text="Nuevo Usuario", padding=12, bootstyle=PRIMARY)
        cont.pack(fill=BOTH, expand=YES, padx=12, pady=12)

        ttk.Label(cont, text="Nombre Completo").grid(row=0,column=0, sticky=W, pady=4)
        self.ent_nombre = ttk.Entry(cont,width=32)
        self.ent_nombre.grid(row=0,column=1,sticky=EW, pady=4, padx=6)

        ttk.Label(cont, text="Correo").grid(row=1,column=0, sticky=W, pady=4)
        self.ent_email = ttk.Entry(cont,width=32)
        self.ent_email.grid(row=1,column=1,sticky=EW, pady=4, padx=6)

        ttk.Label(cont, text="Rol").grid(row=2,column=0, sticky=W, pady=4)
        self.cbo_rol = ttk.Combobox(cont, state="readonly", width=20, values=["Administrador","Editor","Visitante"])
        self.cbo_rol.set("Visitante")
        self.cbo_rol.grid(row=2,column=1,sticky=EW, pady=4, padx=6)

        ttk.Label(cont, text="Estado").grid(row=3,column=0, sticky=W, pady=4)
        self.var_estado=ttk.StringVar(value="Activo")
        rf = ttk.Frame(cont); rf.grid(row=3,column=1,sticky=W, pady=4)
        ttk.Radiobutton(rf, cursor="hand2", text="Activo", variable=self.var_estado, value="Activo", bootstyle= SUCCESS).pack(side=LEFT, padx=2)
        ttk.Radiobutton(rf, text="Inactivo", variable=self.var_estado, value="Inactivo", bootstyle= WARNING).pack(side=LEFT, padx=2)

        ttk.Label(cont, text="Fecha Registro").grid(row=4,column=0, sticky=W, pady=4)
        self.ent_fecha = DateEntry(cont, dateformat="%Y-%m-%d")
        self.ent_fecha.set_date(dt.date.today())
        self.ent_fecha.grid(row=4, column=1, sticky=W,pady=4)

        btns = ttk.Frame(cont); btns.grid(row=5, columnspan=2, column=0, sticky=W, pady=4)
        ttk.Button(btns, text="Guardar / Actualizar",bootstyle=PRIMARY, command=self._guardar_actualizar).pack(side=LEFT, padx=4)
        ttk.Button(btns, text="Limpiar",bootstyle=SECONDARY, command=self._limpiar).pack(side=LEFT, padx=4)
        ttk.Button(btns, text="Eliminar",bootstyle=SECONDARY, command=self._eliminar).pack(side=LEFT, padx=4)
        
        for i in range(2):
            cont.columnconfigure(i,weight=1)

        # TABLA DE DATOS
        tabla_box = ttk.LabelFrame(self, text="Usuarios", padding=8, bootstyle=INFO)
        tabla_box.pack(fill=BOTH, expand=YES, padx=12,pady=12)

        cols = ("nombre","email","rol","estado","fecha")
        self.tree = ttk.Treeview(tabla_box,columns=cols, show="headings", height=12,bootstyle=PRIMARY)
        self.tree.pack(side=LEFT, fill=BOTH, expand=YES)

        headers = {"nombre":"Nombre","email":"Correo","rol":"Rol","estado":"Estado","fecha":"Fecha Registro"}
        widths = {"nombre":180,"email":240,"rol":120,"estado":100,"fecha":120}
        for columna in cols:
            self.tree.heading(columna,text=headers[columna])
            self.tree.column(columna,width=widths[columna], anchor=W, stretch=True)

        yscroll=ttk.Scrollbar(tabla_box,command=self.tree.yview)
        yscroll.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=yscroll.set)

        # Evento para cargar datos desde tabla
        self.tree.bind("<<TreeviewSelect>>", self._cargar_desde_tabla)

    def _limpiar(self):
        self.ent_nombre.delete(0, END)
        self.ent_email.delete(0, END)
        self.cbo_rol.set("Visitante")
        self.var_estado.set("Activo")
        self.ent_fecha.set_date(dt.date.today())
        self.ent_nombre.focus_set()
        
    def _eliminar(self):
        email = self.ent_email.get().strip()
        if not email:
            Messagebox.show_warning("Advertencia", "Ingrese el correo del usuario a eliminar")
            return

        encontrado = None
        for reg in registros:
            if reg["email"].lower() == email.lower():
                encontrado = reg
                break

        if not encontrado:
            Messagebox.show_warning("Advertencia", f"No se encontró un usuario con el correo {email}")
        else:
            # Eliminar del listado de registros
            registros.remove(encontrado)
            # Eliminar del Treeview
            for item_id in self.tree.get_children():
                item = self.tree.item(item_id)
                if item['values'][2].lower() == email.lower():  # índice 2 = email
                    self.tree.delete(item_id)
                    break
            ToastNotification(
                title="Eliminado",
                message=f"Usuario {encontrado['nombre']} eliminado",
                duration=2000,
                position=(self.winfo_x() + 40, self.winfo_y() + 60)
            ).show_toast()  
                  
            self._refresh_table()
            
            # Limpiar formulario si estaba cargado
            if self.usuario_seleccionado and self.usuario_seleccionado["email"].lower() == email.lower():
                self._limpiar()
                
                
    def _guardar_actualizar(self):
        nombre = self.ent_nombre.get().strip()
        email = self.ent_email.get().strip()

        if not nombre or not email:
            Messagebox.show_error("Error", "Nombre y correo no pueden estar vacíos")
            return
        if "@" not in email:
            Messagebox.show_error("Error", "El correo debe contener un @")
            return

        # Verificar si existe un usuario con ese correo
        encontrado = False
        for reg in registros:
            if reg["email"].lower() == email.lower():
                # Actualizar registro existente
                reg["nombre"] = nombre
                reg["rol"] = self.cbo_rol.get()
                reg["estado"] = self.var_estado.get()
                reg["fecha"] = self.ent_fecha.entry.get()
                encontrado = True
                ToastNotification(title="Actualizado", message=f"Usuario {nombre} actualizado", duration=2000,
                                  position=(self.winfo_x() + 40, self.winfo_y() + 60)).show_toast()
                break

        if not encontrado:
            # Crear nuevo registro
            usuario = {
                "nombre": nombre,
                "email": email,
                "rol": self.cbo_rol.get(),
                "estado": self.var_estado.get(),
                "fecha": self.ent_fecha.entry.get()
            }
            registros.append(usuario)
            ToastNotification(title="Guardado", message=f"Usuario {nombre} creado", duration=2000,
                              position=(self.winfo_x() + 40, self.winfo_y() + 60)).show_toast()

        self._refresh_table()
        self._limpiar()

    def _refresh_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for usuario in registros:
            self.tree.insert("", END, values=(usuario["nombre"], usuario["email"], usuario["rol"], usuario["estado"], usuario["fecha"]))

    def _change_theme(self):
        self.style.theme_use(self.cbo_theme.get())

    def _cargar_desde_tabla(self, event):
        seleccionado = self.tree.selection()
        if seleccionado:
            item = self.tree.item(seleccionado[0])
            valores = item['values']
            self.ent_nombre.delete(0, END)
            self.ent_nombre.insert(0, valores[0])
            self.ent_email.delete(0, END)
            self.ent_email.insert(0, valores[1])
            self.cbo_rol.set(valores[2])
            self.var_estado.set(valores[3])
            self.ent_fecha.set_date(valores[4])

if __name__ == "__main__":
    App().mainloop()