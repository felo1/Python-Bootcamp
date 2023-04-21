"""
Una opción propuesta es manejar una planilla de cálculo para el registro de los pedidos y realización de
seguimiento. Si bien es factible su uso, a medida que se agreguen nuevos clientes el archivo irá
creciendo, y será complejo mantener la integridad entre los datos, impidiendo relacionarlos
adecuadamente.

SOLUCIÓN
desarrollar una solución tecnológica que cubra los procesos de negocio descritos y que proponga 
una mejora en la gestión, el control, la seguridad, y disponibilidad de información para el negocio 
y sus clientes. 
-El sistema debe permitir presentar productos, tomar pedidos y hacer seguimiento de estos 
y la gestión de clientes. 
-se requiere que el sistema genere reportes y estadísticas que ayuden 
a tomar de decisiones y mejorar el rendimiento de la empresa, considerando la cantidad de clientes, y la demanda de éstos. 
Es imprescindible mantener comunicación con los encargados de entregar los pedidos, y darles la
posibilidad de realizar todas sus actividades teniendo conectividad a través de dispositivos móviles.
DESARROLLO
● Como se mencionó anteriormente, es necesario mejorar el rendimiento de la empresa. Nuestro
socio se percató que hay mucho código que se repite una y otra vez, lo que dificulta el mantenimiento
de los programas.

Control de Bodega
Nuestro programa deberá tener las siguientes funciones:
- Crear una bodega virtual con los productos iniciales. ok
- Almacenar nuevos productos. ok
- Actualizar el stock de productos en la bodega virtual.
- Mostrar y retornar las unidades disponibles por producto.
- Mostrar y retornar las unidades disponibles de un producto en particular.
- Mostrar y retornar todos los productos de la tienda.
- Mostrar y retornar los productos que tienen más de un número de unidades (el usuario puede
escoger el número de unidades).

Control de Ventas
Nuestro programa deberá tener las siguientes funciones:
- mostrar y retornar el número de clientes registrados en la tienda.
- Funcionalidad para solicitar compra. Se ingresa el id del cliente, id del producto a comprar y las
unidades a comprar.
- respecto a la funcionalidad anterior, por defecto se comprará una unidad.
- Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.
- Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega
virtual.
- Imprimir y retornar un mensaje “Compra aprobada y en camino” en caso que exista el stock
necesario.
- Imprimir y retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.
● Recuerden comentar debidamente su código.
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

def revisar_stock_producto():
    busqueda = input(f"Ingrese el id del producto a consultar:\n")
    for producto in productos:
        if producto["id"] == busqueda:
            print("Se encontró existencias")
            return True
    print("Búsqueda arrojó que no hay un producto con ese ID")
    return False

def autorizar_compra():
    pass
    
def solicitar_compra(cliente, codigo, cantidad):
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
def listar_productos_sobre_cantidad(cantidad):
    valor_filtro = int(input(f"Indique el n° de stock sobre la cual desea filtrar items:\n"))
    print(f"Items con stock sobre {valor_filtro}:")
    for producto in productos:
        if producto["stock"]>valor_filtro:
            print(f"Producto id: {producto['id']} | stock: {producto['stock']}")
    menu_bodega()

menu_bodega()

"""
Control de Ventas
Nuestro programa deberá tener las siguientes funciones:
- mostrar y retornar el número de clientes registrados en la tienda.
- Funcionalidad para solicitar compra. Se ingresa el id del cliente, id del producto a comprar y las
unidades a comprar.
- respecto a la funcionalidad anterior, por defecto se comprará una unidad.
- Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.
- Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega
virtual.
- Imprimir y retornar un mensaje “Compra aprobada y en camino” en caso que exista el stock
necesario.
- Imprimir y retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.
● Recuerden comentar debidamente su código.
"""

    