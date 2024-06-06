#integrantes
#Melissa Meneses- 1001228485
#Nickolas Hache- 1004549966

import mysql.connector
from tkinter import *  # noqa: F403
from tkinter import messagebox
from tkinter.ttk import * # para llamar todas las funciones de una vez  # noqa: F403
from funciones import *  # noqa: F403

# Conexión a la base de datos
cnx = mysql.connector.connect(
    host = 'localhost',
    user = 'informatica1',
    password = 'bio123',
    database = 'informatica1'
)

cursor = cnx.cursor() #para inicializar la funcion cursor
cursor.execute("CREATE DATABASE IF NOT EXISTS informatica1")
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(usuario VARCHAR(255), contraseña VARCHAR(255))')
cursor.execute('CREATE TABLE IF NOT EXISTS proveedores(codigo VARCHAR(255) PRIMARY KEY, nombre VARCHAR(255), apellido VARCHAR(255), numero_de_ID VARCHAR(255), entidad VARCHAR(255))')
cursor.execute('CREATE TABLE IF NOT EXISTS ubicaciones(codigo VARCHAR(255) PRIMARY KEY, nombre_de_la_ubicacion VARCHAR(255), telefono VARCHAR(255))')
cursor.execute('CREATE TABLE IF NOT EXISTS medicamentos(lote VARCHAR(255), nombre_del_medicamento VARCHAR(255), distribuidor VARCHAR(255), cantidad_en_bodega VARCHAR(255), fecha_de_llegada VARCHAR(255), precio VARCHAR(255), codigo_proveedor VARCHAR(255), codigo_ubicacion VARCHAR(255), FOREIGN KEY (codigo_proveedor) REFERENCES proveedores(codigo), FOREIGN KEY (codigo_ubicacion) REFERENCES ubicaciones(codigo))')
cursor.execute('SELECT COUNT(*) FROM usuarios')
if cursor.fetchone()[0] == 0: 
    cursor.execute('INSERT INTO usuarios(usuario, contraseña) VALUES ("informatica1", "bio123")')
cursor.execute('SELECT COUNT(*) FROM proveedores')
if cursor.fetchone()[0] == 0: 
    cursor.execute('INSERT INTO proveedores(codigo, nombre, apellido, numero_de_ID, entidad) VALUES ("101023", "Fabio",  "Orejuela", "1234567890", "DELTA")')
cursor.execute('SELECT COUNT(*) FROM ubicaciones')
if cursor.fetchone()[0] == 0: 
    cursor.execute('INSERT INTO ubicaciones(codigo, nombre_de_la_ubicacion, telefono) VALUES ("343434", "Hopital Pablo Tobon", "3223655205")')
cursor.execute('SELECT COUNT(*) FROM medicamentos') #lee la longitud de la tabla y la guarda en la variable count
if cursor.fetchone()[0] == 0: # fetchone saca el ultimo valor 
    cursor.execute('INSERT INTO medicamentos(lote, nombre_del_medicamento, distribuidor, cantidad_en_bodega, fecha_de_llegada, precio, codigo_proveedor, codigo_ubicacion) VALUES ("1234", "isotretinoina", "DELTA", "100", "12/02/2024", "150000", "101023", "343434")') # si se cumple se ejecuta la funcion
cursor.fetchall() # comando  de sql guarda todas las lineas de codigo sql
cnx.commit()# comando de sql  envia a mysql

# Función para mostrar el menú principal
def mostrar_menu_principal(cnx):  # se pone el parametro cnx para evitar volver a cargar el cursor 
    """ 
    Muestra el menu principal.
    """
    print("Menú Principal")
    print("1. Gestionar medicamentos")
    print("2. Gestionar proveedores")
    print("3. Gestionar ubicaciones")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_menu_medicamentos(cnx)
    elif opcion == "2":
        mostrar_menu_proveedores(cnx)
    elif opcion == "3":
        mostrar_menu_ubicaciones(cnx)
    elif opcion == "4":
        print("Saliendo del sistema")
        cursor.close() #cada vez que se abre el cursor se debe cerrar
        cnx.close()
        exit() #como no se trabaja con ciclos no se puede usar un break, entonces se usa exit
    else:
        print("Opción inválida. Intente nuevamente.")
        mostrar_menu_principal(cnx)

# Función para mostrar el menú de medicamentos
def mostrar_menu_medicamentos(cnx):
    """ 
    Menu medicamentos.
    """
    print("Menú de Medicamentos")
    print("1. Ingresar nuevo medicamento")
    print("2. Actualizar medicamento")
    print("3. Buscar medicamento")
    print("4. Ver todos los medicamentos")
    print("5. Eliminar medicamento")
    print("6. Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_medicamento(cnx)  # noqa: F405
    elif opcion == "2":
        actualizar_medicamento(cnx)  # noqa: F405
    elif opcion == "3":
        buscar_medicamento(cnx)  # noqa: F405
    elif opcion == "4":
        ver_medicamentos(cnx)  # noqa: F405
    elif opcion == "5":
        eliminar_medicamento(cnx)  # noqa: F405
    elif opcion == "6":
        mostrar_menu_principal(cnx)
    else:
        print("Opción inválida. Intente nuevamente.")
        mostrar_menu_medicamentos(cnx)

# Función para mostrar el menú de proveedores
def mostrar_menu_proveedores(cnx):
    """ 
    Menu proveedores.
    """
    print("Menú de Proveedores")
    print("1. Ingresar nuevo proveedor")
    print("2. Actualizar proveedor")
    print("3. Buscar proveedor")
    print("4. Ver todos los proveedores")
    print("5. Eliminar proveedor")
    print("6. Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_proveedor(cnx)  # si se cumple se ejecuta la funcion  # noqa: F405
    elif opcion == "2":
        actualizar_proveedor(cnx)  # noqa: F405
    elif opcion == "3":
        buscar_proveedor(cnx)  # noqa: F405
    elif opcion == "4":
        ver_proveedores(cnx)  # noqa: F405
    elif opcion == "5":
        eliminar_proveedor(cnx)  # noqa: F405
    elif opcion == "6":
        mostrar_menu_principal(cnx)
    else:
        print("Opción inválida. Intente nuevamente.")
        mostrar_menu_proveedores(cnx)

# Función para mostrar el menú de ubicaciones
def mostrar_menu_ubicaciones(cnx):
    """ 
    Menu ubicaciones.
    """
    print("Menú de Ubicaciones")
    print("1. Ingresar nueva ubicación")
    print("2. Actualizar ubicación")
    print("3. Buscar ubicación")
    print("4. Ver todas las ubicaciones")
    print("5. Eliminar ubicación")
    print("6. Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_ubicacion(cnx)  # si se cumple se ejecuta la funcion  # noqa: F405
    elif opcion == "2":
        actualizar_ubicacion(cnx)  # noqa: F405
    elif opcion == "3":
        buscar_ubicacion(cnx)  # noqa: F405
    elif opcion == "4":
        ver_ubicaciones(cnx)  # noqa: F405
    elif opcion == "5":
        eliminar_ubicacion(cnx)  # noqa: F405
    elif opcion == "6":
        mostrar_menu_principal(cnx)
    else:
        print("Opción inválida. Intente nuevamente.")
        mostrar_menu_ubicaciones(cnx)


ventana=Tk() #inicializar la nueva ventana  # noqa: F405
ventana.title("BASE DE DATOS") #nombre, funcion crudo, ese sera el titulo
ventana.geometry('500x200') #eje x 500pix y eje y 200pix

usuario = StringVar() #inializar variables como str  # noqa: F405
contraseña = StringVar()  # noqa: F405

label_user=Label(ventana,text="Ingrese el usuario") #etiqueta  # noqa: F405
label_user.pack(pady=(10, 10)) #para que se agregue etiqueta a la ventana y se hace con pack, en el parentesis va la separacion(separacion de lo que esta arriba y abajo, se uso en el eje y
user=Entry(ventana,width=50) #lo que se escribe en el cuadro de texto se guarda en ese user, se debe inicializar, esto es un cuadro de texto, 50 es el ancho del texto  # noqa: F405
user.pack(pady=(0, 10))#hacia arriba no hay separacion
label_password=Label(ventana,text="Ingrese la contraseña")  # noqa: F405
label_password.pack(pady=(10, 10))
password=Entry(ventana,width=50,show='*')  # noqa: F405
password.pack(pady=(0, 10))
print(user.get())
print(password.get())

Usuarios = []
Contraseñas = []

#extrae el usuario y contraseña que esta en la base de datos 
cursor.execute('SELECT * FROM usuarios')
ListaUsuarios = cursor.fetchall() #se extrae toda la informacion de la tabla de ususarios y se guarda en esa variable
for i in ListaUsuarios:
    Usuarios.append(str(i[0]))#rrecorre la lista de tuplas y se le asigna la posicion que corresponda a usuarios 
    Contraseñas.append(str(i[1]))


#se pone el punto get para poder obtenerlo, ya que sin el punto get obtiene un entry que no corresponde al string

def clicked(): #va decir si el usuario si el usuario está en la base de datos
    """ 
     La funcion extrae el usuario y contraseña de la base de datos para verificar que este y darle entrada. 
    """
    if user.get() in Usuarios and password.get() in Contraseñas:
        verificar = True
        messagebox.showinfo('Base de datos', 'Bienvenido')
        while verificar:
            mostrar_menu_principal(cnx)
    else:
        verificar = False
        messagebox.showinfo('Error', 'El usuario o la contraseña son incorrectos')
    return verificar

btn = Button(ventana, text="Entrar", command=clicked) #command nombre de la funcion que se activa cundo se apreta el boton  # noqa: F405
btn.pack(pady=(10, 10))

ventana.mainloop() #hace que la ventana siempre permanezca abierta y funcionando, se crea un bucle

#falta relacionarlo con la base de datos