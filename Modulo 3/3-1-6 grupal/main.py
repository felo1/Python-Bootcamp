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
global contador_solicitud
contador_solicitud = 0
global solicitudes_compra
solicitudes_compra = []
global contador_ventas
contador_ventas = 0
#====================================MENUS================================
#usamos este estilo de menu por lo visualmente práctico para trabajar conjuntamente

def menu_ventas():
    print("--------MENU--------")
    print("Mostrar n° clientes = 1")
    print("Solicitar compra = 2")
    print("Revisar stock producto = 3")
    print("Autorizar compra = 4")
    opcion = int(input("Ingrese el número de la opción deseada: \n"))
#hacemos los prints representativos de las opciones que están almacenadas en un diccionario
    switcher = {
        1: mostrar_n_clientes,
        2: solicitar_compra,
        3: revisar_stock_producto,
        4: autorizar_compra,
    }
    #definimos una variable que toma el nombre de las otras según la selección para poder 
    #simular la función de un switch case de otros lenguajes de programacion
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción no válida")

def menu_bodega():
    print("--------Bienvenido a Telovendo SPA--------")
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
#se muestra el largo de la lista de diccionarios de cliente para reflejar la cantidad de clientes guardados.
def mostrar_n_clientes():
    print(f"N° total de clientes: {len(clientes)}")
    time.sleep(2)
    menu_bodega()

#funcion que responde con booleanos sobre si hay stock, o stock suficiente, del item indicado por ID
def revisar_stock_producto(sol_id_producto = None, sol_cantidad = None):  
    print("Revisando stock...")
    #esta es la funcion que solo puede devolver booleanos segun lo solicitado por la tarea
    #este primer if es la ruta que toma si se entra desde el menu en vez de llamar a la funcion con parametros, no pedirá cantida
    if sol_id_producto == None:
        #si el parámetro que representa el ID del producto que está en proceso de solicitud es nulo, consulta por el.
        sol_id_producto = input(f"Ingrese el id del producto a consultar:\n")
        for producto in productos:
            if producto["id"] == sol_id_producto and producto["stock"] >= 1: #si viene sin parametros solamente se revisa si hay existencias
                print("Se encontraron existencias")
                time.sleep(2)
                return True
        #al salir del for si no tuvo éxito
        print("No se encontraron existencias")
        time.sleep(2)
        return False     
        
    #Desde acá trabajaria si trae argumentos de antemano. No llegará a este punto si la funcion no viene prellenada desde solicitar_compra
    for producto in productos:
        if producto["id"] == sol_id_producto and producto["stock"] >= sol_cantidad: #cumplimos con los dos requisitos de la tarea aplicando las dos condiciones
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
            #hacemos un chequeo de nulo para evitar que se caiga el programa si hacen una lectura a este diccionario estando vacío
            print("No hay solicitudes de compra pendientes de autorización")
            print("Saliendo del programa")
            time.sleep(2)
            menu_bodega()
        print("Los siguientes códigos de solicitudes de compra están pendientes de autorización:")
        for solicitud in solicitudes_compra:
            print(solicitud['id_venta'])
        #muestra las solicitudes registradas, que pueden ser más de una en caso de no terminarse el proceso de autorización
        #consulta por cual quiere autorizar
        autorizar = int(input(f"Ingrese la solicitud a autorizar, ingrese 0 para salir: \n"))
        #evitamos que se caiga el programa por recibir un valor no entero o 0
        if  autorizar == 0:
            print("Volviendo al menú")
        #si la encuentra, simulamos que se hace la gestión de autorización
        for solicitud in solicitudes_compra:
            if solicitud['id_venta'] == autorizar:
                print("Compra aprobada y en camino")
                time.sleep(2)
                menu_bodega()
            #no hacemos el descuento de stock, respetando lo que pidieron para la actividad
        else:
            print("Solicitud de compra rechazada")
            print("Saliendo del programa")
            time.sleep(2)    

def existe_cliente(id_cliente):
    #puede que aqui tengamos algunas redundancias por trabajar por separado en pocas tareas.
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
        #hasta que el usuario ingrese un id de cliente válido existnete, consulta por datos
        sol_cliente = input("ingrese id de cliente que solicita: ").strip().lower()
        if existe_cliente(sol_cliente) == True:
            break
        else:
            print("cliente no existe, por favor ingrese nuevamente")
            time.sleep(2)
        #hasta que el usuario ingrese un id de producto válido existente, consulta por datos
    while True:    
        sol_id_producto = input("ingrese id de producto solicitado: ").strip().lower()
        if existe_producto(sol_id_producto) == True:
            break
        else:
            print("El producto no existe. Ingrese otro producto.")
    while True:
        #hasta que el usuario ingrese una cantidad positiva de n° entero, consulta por input
        sol_cantidad = input("Ingrese cantidad solicitada. Para salir ingrese '0' : ")
        if sol_cantidad.isdigit() and sol_cantidad > 0:
            sol_cantidad = int(sol_cantidad)
        else:
            print("El valor ingresado no es un número entero positivo")
            time.sleep(2)
            continue
        if sol_cantidad == 0:
            print("Volviendo al menú...")
            break
        #llegado a este punto, llama a otra funcion para chequear si el stock puede suplir esta solicitud.
        elif revisar_stock_producto(sol_id_producto, sol_cantidad) == True: 
            #componemos un diccionario para subirlo a la lista con un append. 
            #tiene por contenido un id de venta basado en un contador global que partirá en 0 con el programa
            #y con los datos ingresados por el usuario como segundo valor.
            solicitudes_compra.append({'id_venta':contador_solicitud+1,"datos":[sol_cliente, sol_id_producto, sol_cantidad]})
            print("Su solicitud ha sido ingresada y está a la espera de autorización")
            #simulamos la interoperatividad de funciones de venta llamando directamente a autorizar compra con estos parámetros
            #aunque podría no hacerse, el metodo autorizar_compra puede funcionar sin parametros.
            autorizar_compra(solicitudes_compra)
        else:
            print("No existen suficientes unidades del producto. Ingrese otra cantidad o escriba 'salir'")
      
    time.sleep(2)
    menu_bodega()       

    #------exigencias tarea parte 2----
    #usando id cliente, id producto, unidades a comprar (por defecto 1)
    #verificar si hay stock necesario devolviendo bools.
    #funcionalidad que autoriza compra, no es necesario actualizar stock de la bodega virtual
    #para "autorizar" estimo que para hacer esto una funcion llamaría a otra
    #para simular la interacción de dos plataformas distintas, cliente/vendedor
    #y que una vez autorizada la venta se complete la funcion de compra
    #printear “Compra aprobada y en camino” en caso que exista el stock necesario.
    #retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.
    pass
def agregar_cliente(**kwarlitogs):
    nuevo_cliente = {}
    #solicitamos los datos del cliente, nombre (en lowercase) y edad (sanitizado)
    nom = input("Ingrese el nombre del cliente: ").lower()
    while True:
        ed = input("Ingrese la edad: ")
        if ed.isnumeric() == True:
            int(ed)
            break
        else: print("Debe ingresar un número entero")
    #nos basamos en el largo de la lista de clientes para definir el id de próximos usuarios agregados.
    #TODO: #usar alguna libreria que resuelva los IDs vacios si se eliminan usuarios
    ultimo_id = clientes[-1]["id"]  
    #le quitamos las partes que no son numericas a "numeros", que pasa a tener el valor del ultimo ID de cliente, que tiene formato idxx 
    numeros = int(ultimo_id[2:])
    nuevo_numero = numeros + 1
    idc = "id" + str(nuevo_numero)
    #rearmamos el formato de ID luego de incrementarlo.
    #luego lo asignamos a una variable diccionario 
    nuevo_cliente = {"nombre": nom, "edad": ed, "id": idc}
    #y lo inyectamos
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
    valor_filtro = input(f"Indique el n° de stock sobre la cual desea filtrar items:\n")ww
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







"""
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

    