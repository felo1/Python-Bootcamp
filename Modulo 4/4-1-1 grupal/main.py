"""
SOLUCIÓN
Dados los antecedentes anteriores, es necesario desarrollar una solución tecnológica que cubra los
procesos de negocio descritos y que proponga una mejora en la gestión, el control, la seguridad, y
disponibilidad de información para el negocio y sus clientes. El sistema debe permitir presentar
productos, tomar pedidos y hacer seguimiento de estos y la gestión de clientes. Además, se requiere
que el sistema genere reportes y estadísticas que ayuden a tomar de decisiones y mejorar el
rendimiento de la empresa, considerando la cantidad de clientes, y la demanda de éstos. Es
imprescindible mantener comunicación con los encargados de entregar los pedidos, y darles la
posibilidad de realizar todas sus actividades teniendo conectividad a través de dispositivos móviles.

DESARROLLO - Continuación del trabajo.
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python
En base al sistema desarrollado anteriormente en el módulo de Python básico, se solicita
Incorporar la creación de las siguientes clases.
● Clase Cliente.
● Clase Producto.
● Clase Vendedor.

La Clase Cliente deberá contar con los siguientes atributos:
a. ID Cliente
b. Nombre
c. Apellido
d. Correo
e. Fecha Registro
f. __Saldo

"""
clientes = []

class Usuario:
    def __init__(self, nivel, nombre, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc

#Se solicita que los atributos __Saldo (Cliente), __Impuesto (Producto) y __Comision (Vendedor) se
#encuentren encapsulados. (hecho ok)
class Cliente(Usuario):
    def __init__(self, ID_Cliente, Nombre, Apellido, Correo, Fecha_Registro, __Saldo):
        #tomo saldo como parametro porque en la tarea no le dan un valor por defecto
        self.ID_Cliente = ID_Cliente
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Correo = Correo
        self.Fecha_Registro = Fecha_Registro
        self.__Saldo = __Saldo #la encapsulacion la hago asi, con __ antes de la definicion del atributo de clase

    def agregar_saldo(self, saldo, ID_Cliente):
        if ID_Cliente == self.ID_Cliente:
            print("El saldo inicial es de: ", self.__Saldo)
            self.__Saldo += saldo
            print("Se agrego el saldo de: ", saldo)
            print("El saldo nuevo es de: ", self.__Saldo)
        else:
            print("No se encuentra el cliente indicado")
    def mostrar_saldo(self):
        print(f"Saldo de cliente es {self.__Saldo}")
#  Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
#Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar
#correctamente los métodos de las clases en las opciones del menú desarrollado.

class Vendedor(Usuario):
    def __init__(self, RUN, Nombre, Apellido, Seccion):
        self.RUN = RUN
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Seccion = Seccion
        self.__Comision = 0

class Producto():
    def __init__(self, SKU, Nombre, Categoria, Proveedor, Stock, Valor_Neto):
        self.SKU = SKU
        self.Nombre = Nombre
        self.Categoria = Categoria
        self.Proveedor = Proveedor
        self.Stock = Stock
        self.Valor_Neto = Valor_Neto
        self.__Impuesto = 1.19 

"""





Desarrollar 5 instancias de cada clase creada en los puntos anteriores.
Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
gráfica. Desarrollen el ejercicio de forma intuitiva.
"""

import time
#====================================DICCIONARIOS HARD================================
clientes = [
    {"nombre": "Cliente1", "edad": 25, "id": "id1"},
    {"nombre": "Cliente2", "edad": 32, "id": "id2"},
    {"nombre": "Cliente3", "edad": 19, "id": "id3"},
    {"nombre": "Cliente4", "edad": 40, "id": "id4"},
]
#productos hardcodeados según lo solicitado
productos = [
    {"nombre": "Zapatillas", "stock": 20, "precio": 100, "id": "prod1", "color": "rojo"},
    {"nombre": "POLERAS", "stock": 10, "precio": 100, "id": "prod2", "color": ["rojo", "azul", "amarillo","avengers"]},
    {"nombre": "ZAPATOS", "stock": 15, "precio": 100, "id": "prod3", "color": "negro" },
    {"nombre": "POLERÓN", "stock": 3, "precio": 100, "id": "prod4", "color": "rosa" },
    {"nombre": "CHAQUETA", "stock": 5, "precio": 100, "id": "prod5", "color": "azul" },
]
global contador_solicitud
contador_solicitud = 0
global solicitudes_compra
solicitudes_compra = []
global contador_ventas
contador_ventas = 0
#====================================MENUS================================

def menu_ventas():
    print("--------MENU--------")
    print("Mostrar n° clientes = 1")
    print("Solicitar compra = 2")
    print("Revisar stock producto = 3")
    print("Autorizar compra = 4")
    opcion = int(input("Ingrese el número de la opción deseada: \n"))
    switcher = {
        1: mostrar_n_clientes,
        2: solicitar_compra,
        3: revisar_stock_producto,
        4: autorizar_compra,
    }
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción no válida")

def menu_bodega():
    print("--------MENU--------")
    print("Agregar nuevo cliente = 1")
    print("Agregar nuevo producto = 2")
    print("Actualizar stock = 3")
    print("Listar productos = 4")
    print("Mostrar y retornar las unidades disponibles = 5")
    print("Mostrar y retornar las unidades disponibles de producto en particular = 6")
    print("Mostrar y retornar los productos que tienen > x numero de unidades = 7")
    print("Acceder a menu ventas = 8")

    opcion = int(input("Ingrese el número de la opción deseada: \n"))

    
    switcher = {
        1: agregar_cliente,
        2: agregar_producto,
        3: actualizar_stock,
        4: listar_productos,
        5: listar_stock,
        6: listar_stock_item,
        7: listar_productos_sobre_cantidad,
        8: menu_ventas,
    }
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción no válida")
#====================================FUNCIONALIDADES================================
def mostrar_n_clientes():
    print(f"N° total de clientes: {len(clientes)}")
    
    time.sleep(2)
    menu_bodega()

def revisar_stock_producto(sol_id_producto = None, sol_cantidad = None):  
    print("Revisando stock...")
    #esta es la funcion que solo puede devolver booleanos segun lo solicitado por la tarea
    #este primer if es la ruta que toma si se entra desde el menu en vez de llamar a la funcion con parametros, no pedirá cantidad
    if sol_id_producto == None:
        sol_id_producto = input(f"Ingrese el id del producto a consultar:\n")
        for producto in productos:
            if producto["id"] == sol_id_producto and producto["stock"] >= 1:
                print("Se encontraron existencias")
                time.sleep(2)
                return True
        #al salir del for si no tuvo éxito
        print("No se encontraron existencias")
        time.sleep(2)
        return False     
        
    #Desde acá trabajaria si trae argumentos de antemano. No llegará a este punto si la funcion no viene prellenada desde solicitar_compra
    for producto in productos:
        if producto["id"] == sol_id_producto and producto["stock"] >= sol_cantidad:
            print(f"Hay stock suficiente igual o mayor a {sol_cantidad}")
            time.sleep(2)
            return True
        else:
            print("No se encontraron existencias")
            time.sleep(2)
            return False

def autorizar_compra(solicitudes_compra = None):
    while True:
        if solicitudes_compra == None:
            print("No hay solicitudes de compra pendientes de autorización")
            print("Saliendo del programa")
            time.sleep(2)
            menu_bodega()
        print("Los siguientes códigos de solicitudes de compra están pendientes de autorización:")
        for solicitud in solicitudes_compra:
            print(solicitud['id_venta'])
        autorizar = int(input(f"Ingrese la solicitud a autorizar, ingrese 0 para salir: \n"))
        if  autorizar == 0:
            print("Volviendo al menú")
        for solicitud in solicitudes_compra:
            if solicitud['id_venta'] == autorizar:
                print("Compra aprobada y en camino")
                time.sleep(2)
                menu_bodega()
        else:
            print("Solicitud de compra rechazada")
            print("Saliendo del programa")
            time.sleep(2)    

def existe_cliente(id_cliente):
    """Devuelve 'True' si el cliente indicado existe"""
    resultado = ""
    for cliente in clientes:
        if (cliente["id"] == id_cliente):
            resultado = True
    if resultado == True:
        return True

def existe_producto(id_producto):
    """Devuelve 'True' si el producto indicado existe"""
    resultado = ""
    for producto in productos:
        if (producto["id"] == id_producto):
            resultado = True
    if resultado == True:
        return True

def solicitar_compra():
    """ Pide datos al usuario para generar solicitud de compra, luego verifica stock y finalmente DEVUELVE orden de compra"""
    #serie de inputs que llenarán la variable solicitudes_compra, con los controles correspondientes a las entradas
    while True:
        sol_cliente = input("ingrese id de cliente que solicita: ").strip().lower()
        if existe_cliente(sol_cliente) == True:
            break
        else:
            print("cliente no existe, por favor ingrese nuevamente")
            time.sleep(2)
    
    while True:    
        sol_id_producto = input("ingrese id de producto solicitado: ").strip().lower()
        if existe_producto(sol_id_producto) == True:
            break
        else:
            print("El producto no existe. Ingrese otro producto.")
    while True:
        sol_cantidad = input("Ingrese cantidad solicitada. Para salir ingrese '0' : ")
        if sol_cantidad.isdigit():
            sol_cantidad = int(sol_cantidad)
        else:
            print("El valor ingresado no es un número entero")
            time.sleep(2)
        if sol_cantidad == 0:
            print("Volviendo al menú...")
            break
        elif revisar_stock_producto(sol_id_producto, sol_cantidad) == True: 
            #solicitudes_compra = {sol_cliente: {sol_id_producto: sol_cantidad}}
            solicitudes_compra.append({'id_venta':contador_solicitud+1,"datos":[sol_cliente, sol_id_producto, sol_cantidad]})
            print(solicitudes_compra)
            print("Su solicitud ha sido ingresada y está a la espera de autorización")
            #return(solicitudes_compra)
            autorizar_compra(solicitudes_compra)
        else:
            print("No existen suficientes unidades del producto. Ingrese otra cantidad o escriba 'salir'")
      
    time.sleep(2)
    menu_bodega()       
    #usando id cliente, id producto, unidades a comprar (por defecto 1)
    #verificar si hay stock necesario devolviendo bools.
    #funcionalidad que autoriza compra, no es necesario actualizar stock de la bodega virtual
    #para "autorizar" estimo que para hacer esto una funcion llamaría a otra
    #para simular la interacción de dos plataformas distintas, cliente/vendedor
    #y que una vez autorizada la venta se complete la funcion de compra
    #printear “Compra aprobada y en camino” en caso que exista el stock necesario.
    #retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.
    pass
def agregar_cliente():
    nuevo_cliente = {}
    nom = input("Ingrese el nombre del cliente: ").lower()
    ed = int(input("Ingrese la edad: "))
    #idc = 
    #debe haber alguna mejor manera de llevar los ID que 
    #evite que eliminar IDs deje hoyos en el contador.
    ultimo_id = clientes[-1]["id"]  
    #lo paso de alfanumerico a solo numero
    numeros = int(ultimo_id[2:]) 
    nuevo_numero = numeros + 1
    idc = "id" + str(nuevo_numero)
    nuevo_cliente = {"nombre": nom, "edad": ed, "id": idc}
    clientes.append(nuevo_cliente)
    print(f"El cliente {nom} ha sido agregado.")
    time.sleep(2)
    menu_bodega()
def agregar_producto(nombre, cantidad):
    if nombre in productos:
        productos[nombre] += cantidad #si ya existe el producto, solo aumenta la cantidad
    else:
        productos[nombre] = cantidad #si no existe el producto , agrega nombre y producto
    time.sleep(2)
    menu_bodega()

def actualizar_stock(nombre, cantidad):
    if nombre in productos:
        productos[nombre] = cantidad # si ya existe el producto, reemplaza la cantidad
    else:
        print(f"El producto {nombre} no existe")# si no existe entrega mensaje de error

def listar_productos():
    print("Listado de Productos:")
    for producto in productos:
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("ID:", producto["id"])
        print("Color:", producto["color"])
    time.sleep(2)
    menu_bodega() 

def listar_stock():
    print("Listado de Productos:")
    for producto in productos:
        print(f"Id: {producto['id']}:, stock: {producto['stock']}")
    time.sleep(2)
    menu_bodega() 

def listar_stock_item():
    busqueda = input(f"Ingrese el id del producto a consultar:\n")
    for producto in productos:
        if producto["id"] == busqueda:
            print(f"El stock del producto consultado es {producto['stock']}")
            break
    print("Búsqueda arrojó que no hay un producto con ese ID")
    menu_bodega()
def listar_productos_sobre_cantidad():
    valor_filtro = input(f"Indique el n° de stock sobre la cual desea filtrar items:\n")
    if valor_filtro.isdigit():
        valor_filtro = int(valor_filtro)
    else:
        print("El valor ingresado no es un número entero")
        time.sleep(2)
        menu_bodega()
    print(f"Items con stock sobre {valor_filtro}:")
    for producto in productos:
        if producto["stock"]>valor_filtro:
            print(f"Producto id: {producto['id']} | stock: {producto['stock']}")
    menu_bodega()

menu_bodega()

#Control de Ventas

#mostrar y retornar el número de clientes registrados en la tienda.

def listar_clientes():
    print(f"{len(clientes)} Clientes registrados:\n")

    for key, value in clientes:
        print(f"{key}: {value}")