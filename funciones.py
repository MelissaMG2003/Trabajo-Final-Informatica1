import mysql.connector  # noqa: F401
    
import datetime

def ingresar_medicamento(cnx):
    """ 
    En esta funcion se piden los datos del medicamento a ingresar, se tiene dos listas donde se almacenan los 
    codigos disponibles los cuales son ingresados o predeterminados con antelacion sobre proveedores y ubicaciones, 
    esto le aparece al usuario para que pueda elegir uno de los disponibles, si elige una opcion no disponible se 
    vuelve a preguntar,esto por la relacion entre tablas.  Finalmente la informacion ingresada se agrega 
    a la tabla de medicamentos en MySQL.
    """

    codigos_proveedor = []
    codigos_ubicacion = []
    cursor = cnx.cursor()

    print("Ingresar nuevo medicamento")
    lote = input("Ingrese el lote del medicamento: ")
    nombre_del_medicamento = input("Ingrese el nombre del medicamento: ")
    distribuidor = input("Ingrese el distribuidor del medicamento: ")
    cantidad_en_bodega = input("Ingrese la cantidad del medicamento: ")

    try:
        fecha_de_llegada = input("Ingrese la fecha (en formato YYYY-MM-DD): ")
        fecha = datetime.datetime.strptime(fecha_de_llegada, "%Y-%m-%d")
        print("Fecha ingresada correctamente:", fecha)
    except ValueError:
        print("Error: El formato de fecha ingresado no es válido.")
       
    precio = input("Ingrese el precio de venta del medicamento: ")
    cursor.execute('SELECT * FROM proveedores')
    proveedores = cursor.fetchall()
    for i in proveedores:
        codigos_proveedor.append(str(i[0]))
    print('Ingrese el codigo correspondiente al proveedor')
    for i in proveedores:
        print(str(i[0])+' - '+str(i[1])+' '+str(i[2]))
    codigo_proveedor = input('Ingrese el codigo del proveedor del medicamento: ')
    if codigo_proveedor in codigos_proveedor:
        pass
    else:
        print('Ingrese un codigo valido')
        

    cursor.execute('SELECT * FROM ubicaciones')
    ubicaciones = cursor.fetchall()
    for i in ubicaciones:
        codigos_ubicacion.append(str(i[0]))
    print('Ingrese el codigo correspondiente al proveedor')
    for i in ubicaciones:
        print(str(i[0])+' - '+str(i[1]))
    codigo_ubicacion = input('Ingrese el codigo de la ubicacion del medicamento: ')
    if codigo_ubicacion in codigos_ubicacion:
        pass
    else:
        print('Ingrese un codigo valido')

    sql = "INSERT INTO medicamentos (lote, nombre_del_medicamento, distribuidor, cantidad_en_bodega, fecha_de_llegada, precio, codigo_proveedor, codigo_ubicacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (lote, nombre_del_medicamento, distribuidor, cantidad_en_bodega, fecha_de_llegada, precio, codigo_proveedor, codigo_ubicacion)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"El medicamento {nombre_del_medicamento} con lote {lote} ha sido ingresado exitosamente.")

def actualizar_medicamento(cnx):
    """ 
    En esta funcion se piden los datos del medicamento a actualizar para luego actualizarse en la base de datos.
    """
    print("Actualizar medicamento")
    lote = input("Ingrese el lote del medicamento a actualizar: ")
    nombre_del_medicamento = input("Ingrese el nuevo nombre del medicamento: ")
    distribuidor = input("Ingrese el nuevo distribuidor del medicamento: ")
    cantidad_en_bodega = input("Ingrese la nueva cantidad del medicamento: ")
    fecha_de_llegada = input("Ingrese la nueva fecha de llegada del medicamento: ")
    precio = input("Ingrese el nuevo precio de venta del medicamento: ")
    codigo_proveedor = input("Ingrese el codigo de proveedor del medicamento: ")
    codigo_ubicacion = input("Ingrese el codigo de ubicacion del medicamento: ")
    cursor = cnx.cursor()
    sql = "UPDATE medicamentos SET nombre_del_medicamento=%s, distribuidor=%s, cantidad_en_bodega=%s, fecha_de_llegada=%s, precio=%s, codigo_proveedor=%s, codigo_ubicacion=%s WHERE lote=%s"
    val = (lote, nombre_del_medicamento, distribuidor, cantidad_en_bodega, fecha_de_llegada, precio, codigo_proveedor, codigo_ubicacion)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"El medicamento con lote {lote} ha sido actualizado exitosamente.")


def buscar_medicamento(cnx):
    """ 
    Esta funcion pide el lote del medicamento para buscarlo, posteriormente se guarda la informacion encontrada.
    """
    print("Buscar medicamento")
    lote = input("Ingrese el lote del medicamento a buscar: ")

    cursor = cnx.cursor()
    sql = "SELECT * FROM medicamentos WHERE lote=%s"
    val = (lote,)
    cursor.execute(sql, val)
    resultado = cursor.fetchone()

    if resultado:
        print(f"Lote: {resultado[0]}")
        print(f"Nombre: {resultado[1]}")
        print(f"Distribuidor: {resultado[2]}")
        print(f"Cantidad: {resultado[3]}")
        print(f"Fecha de llegada: {resultado[4]}")
        print(f"Precio de venta: {resultado[5]}")
        print(f"Codigo de proveedor: {resultado[6]}")
        print(f"Codigo de ubicacion: {resultado[7]}")
    else:
        print("No se encontró el medicamento.")


def ver_medicamentos(cnx):
    """ 
    Esta funcion  imprime la informacion encontrada en la base de datos de medicamentos.
    """
    print("Ver todos los medicamentos")

    cursor = cnx.cursor()
    sql = "SELECT * FROM medicamentos"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    for medicamento in resultado:
        print(f"Lote: {medicamento[0]}")
        print(f"Nombre: {medicamento[1]}")
        print(f"Distribuidor: {medicamento[2]}")
        print(f"Cantidad: {medicamento[3]}")
        print(f"Fecha de llegada: {medicamento[4]}")
        print(f"Precio de venta: {medicamento[5]}")
        print(f"Codigo de proveedor: {medicamento[6]}")
        print(f"Codigo de ubicacion: {medicamento[7]}")
        print()


def eliminar_medicamento(cnx):
    """ 
    Esta funcion pide el lote del medicamento para eliminarlo, posteriormente se elimina el medicamento.
    """
    print("Eliminar medicamento")
    lote = input("Ingrese el lote del medicamento a eliminar: ")

    cursor = cnx.cursor()
    sql = "DELETE FROM medicamentos WHERE lote=%s"
    val = (lote,)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"El medicamento con lote {lote} ha sido eliminado exitosamente.")
    

def ingresar_proveedor(cnx):
    """ 
    En esta funcion se piden los datos del proveedor a ingresar, posteriormente agrega la informacion en
    la base de datos de proveedores.
    """
    print("Ingresar nuevo proveedor")
    codigo = input("Ingrese el código del proveedor: ")
    nombre = input("Ingrese el nombre del proveedor: ")
    apellido = input("Ingrese el apellido del proveedor: ")
    numero_de_ID = input("Ingrese el número del documento de identidad del proveedor: ")
    entidad = input("Ingrese la entidad del proveedor: ")

    cursor = cnx.cursor()
    sql = "INSERT INTO proveedores (codigo, nombre, apellido, numero_de_ID, entidad) VALUES (%s, %s, %s, %s, %s)"
    val = (codigo, nombre, apellido, numero_de_ID, entidad)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"El proveedor {nombre} {apellido} ha sido ingresado exitosamente.")

def actualizar_proveedor(cnx):
    """ 
    En esta funcion se piden los datos del proveedor a actualizar, posteriormente actualiza la informacion en
    la base de datos de proveedores.  
    """
    print("Actualizar proveedor")
    codigo = input("Ingrese el código del proveedor a actualizar: ")
    nombre = input("Ingrese el nuevo nombre del proveedor: ")
    apellido = input("Ingrese el nuevo apellido del proveedor: ")
    numero_de_ID = input("Ingrese el nuevo número del documento de identidad del proveedor: ")
    entidad = input("Ingrese la nueva entidad del proveedor: ")

    cursor = cnx.cursor()
    sql = "UPDATE proveedores SET nombre=%s, apellido=%s, numero_de_ID=%s, entidad=%s WHERE codigo=%s"
    val = (nombre, apellido, numero_de_ID, entidad, codigo)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"El proveedor {nombre} {apellido} ha sido actualizado exitosamente.")

def buscar_proveedor(cnx):
    """ 
    En esta funcion se pide el codigo del proveedor a buscar, posteriormente se guarda la informacion especificada por 
    el codigo que hay en la base de datos de proveedores. 
    """
    print("Buscar proveedor")
    codigo = input("Ingrese el código del proveedor a buscar: ")

    cursor = cnx.cursor()
    sql = "SELECT * FROM proveedores WHERE codigo=%s"
    val = (codigo,)
    cursor.execute(sql, val)
    resultado = cursor.fetchone()

    if resultado:
        print(f"Código: {resultado[0]}")
        print(f"Nombre: {resultado[1]}")
        print(f"Apellido: {resultado[2]}")
        print(f"Documento de identidad: {resultado[3]}")
        print(f"Entidad: {resultado[4]}")
    else:
        print("No se encontró el proveedor.")

def ver_proveedores(cnx):
    """ 
    En esta funcion  imprime la informacion general que se encuentra en la base de datos de proveedores. 
    """
    print("Ver todos los proveedores")

    cursor = cnx.cursor()
    sql = "SELECT * FROM proveedores"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    for proveedor in resultado:
        print(f"Código: {proveedor[0]}")
        print(f"Nombre: {proveedor[1]}")
        print(f"Apellido: {proveedor[2]}")
        print(f"Documento de identidad: {proveedor[3]}")
        print(f"Entidad: {proveedor[4]}")
        print()

def eliminar_proveedor(cnx):
    """ 
    En esta funcion se pide el codigo d a eliminar, posteriormente elimine la informacion especificada por 
    el codigo que hay en la base de datos de  ubiciones. 
    """
    print("Eliminar proveedor")
    codigo = input("Ingrese el código del proveedor a eliminar: ")

    cursor = cnx.cursor()
    sql = "DELETE FROM proveedores WHERE codigo=%s"
    val = (codigo,)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"El proveedor con código {codigo} ha sido eliminado exitosamente.")


def ingresar_ubicacion(cnx):
    """ 
    En esta funcion se piden los datos de la ubicacion a ingresar, posteriormente agrega la informacion en
    la base de datos de ubicaciones.
    """
    print("Ingresar nueva ubicación")
    codigo = input("Ingrese el código de la ubicación: ")
    nombre_de_la_ubicacion = input("Ingrese el nombre de la ubicación: ")
    telefono = input("Ingrese el teléfono de la ubicación: ")

    cursor = cnx.cursor()
    sql = "INSERT INTO ubicaciones (codigo, nombre_de_la_ubicacion, telefono) VALUES (%s, %s, %s)"
    val = (codigo, nombre_de_la_ubicacion, telefono)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"La ubicación {nombre_de_la_ubicacion} ha sido ingresada exitosamente.")

def actualizar_ubicacion(cnx):
    """ 
    En esta funcion se piden los datos de la  ubicacion a actualizar, posteriormente actualiza la informacion en
    la base de datos de ubicaciones. 
    """
    print("Actualizar ubicación")
    codigo = input("Ingrese el código de la ubicación a actualizar: ")
    nombre_de_la_ubicacion = input("Ingrese el nuevo nombre de la ubicación: ")
    telefono = input("Ingrese el nuevo teléfono de la ubicación: ")

    cursor = cnx.cursor()
    sql = "UPDATE ubicaciones SET nombre_de_la_ubicacion=%s, telefono=%s WHERE codigo=%s"
    val = (nombre_de_la_ubicacion, telefono, codigo)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"La ubicación {nombre_de_la_ubicacion} ha sido actualizada exitosamente.")

def buscar_ubicacion(cnx):
    """ 
    En esta funcion se pide el codigo de la ubicacion a buscar, posteriormente se guarda la informacion especificada por 
    el codigo que hay en la base de datos de  ubiciones. 
    """
    print("Buscar ubicación")
    codigo = input("Ingrese el código de la ubicación a buscar: ")

    cursor = cnx.cursor()
    sql = "SELECT * FROM ubicaciones WHERE codigo=%s"
    val = (codigo,)
    cursor.execute(sql, val)
    resultado = cursor.fetchone()

    if resultado:
        print(f"Código: {resultado[0]}")
        print(f"Nombre: {resultado[1]}")
        print(f"Teléfono: {resultado[2]}")
    else:
        print("No se encontró la ubicación.")

def ver_ubicaciones(cnx):
    """ 
    En esta funcion  imprime la informacion general que se encuentra en la base de datos de ubicaciones. 
    """
    print("Ver todas las ubicaciones")

    cursor = cnx.cursor()
    sql = "SELECT * FROM ubicaciones"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    for ubicacion in resultado:
        print(f"Código: {ubicacion[0]}")
        print(f"Nombre: {ubicacion[1]}")
        print(f"Teléfono: {ubicacion[2]}")
        print()

def eliminar_ubicacion(cnx):
    """ 
    En esta funcion se pide el codigo de la ubicacion a eliminar, posteriormente elimine la informacion especificada por 
    el codigo que hay en la base de datos de  ubiciones. 
    """
    print("Eliminar ubicación")
    codigo = input("Ingrese el código de la ubicación a eliminar: ")

    cursor = cnx.cursor()
    sql = "DELETE FROM ubicaciones WHERE codigo=%s"
    val = (codigo,)
    cursor.execute(sql, val)
    cnx.commit()
    print(f"La ubicación con código {codigo} ha sido eliminada exitosamente.")
