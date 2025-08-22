
"""
#primer ejemplo
import keyboard


#Eventos



#Accion
def presionar_h():
    print("Presionaste la tecla H....")

keyboard.add_hotkey('h',presionar_h)
print("Presiona h  para ver mensaje. Ctrl + C para salir")
keyboard.wait()

#Escucha en segundo plano
#Detecta cuando se presiona la tecla o la combinación esperada



# los parametros son la tecla y la acción
keyboard.add_hotkey('h', presionarH)
print("Presiona h  para ver mensaje. Ctrl + C para salir")
keyboard.wait()



"""


"""

#Segundo ejemplo
import time

def revisar_evento():
    print(time.time() % 4)
    return time.time() % 4 < 0.2

def manejador():
    segundos = time.localtime().tm_sec
    print(f"Evento detectado {segundos:02}")
    
while True:
    if revisar_evento():
        manejador()
    time.sleep(0.1) # Evita que el bucle consuma todo el CPU
        
print(revisar_evento())

"""


#ejemplo 3

"""
Mostrar un menú
A Activar el sistema de ventilación
L Enceder luces
S Detener todos los sistemas
Q Salir
"""
import keyboard
def presionar_a():
    print("Activar el sistema de ventilación....")
def presionar_l():
    print("Enceder luces....")
def presionar_s():
    print("Detener todos los sistemas....")    
def presionar_q():
    print("Salir....")    
def menu():
    print("Presione a para Activar el sistema de ventilación")
    print("Presione l para Enceder luces")
    print("Presione s para Detener todos los sistemas")
    print("Presione Ctrl + C para Salir")
        
       
keyboard.add_hotkey('a', presionar_a)
keyboard.add_hotkey('l', presionar_l)
keyboard.add_hotkey('s', presionar_s)
keyboard.add_hotkey('q', presionar_q)
keyboard.add_hotkey('m', menu)
print("Presione m para mostrar menú")
keyboard.wait('q')



#ejemplo 4

"""
Mostrar un mensaje inicial
    iniciando el sistema....add()
    
cada 5 segundos:
    Alerta: Verificando la temperatura del CPU
    
Cada 10 segundos: 
    Revisión completa del sistema
"""