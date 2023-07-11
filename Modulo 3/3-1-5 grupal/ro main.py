#importar librerias
import random
import time
#Guarde en una variable la siguiente información:

#Debe crear 10 clientes y 5 productos.
#* Información de clientes: nombre, edad, identificador único.
clientes = [{"id00001" : {"nombre": "Hugo", "edad" :25}},
            {"id00002" : {"nombre": "Paco", "edad" :35}},
            {"id00003" : {"nombre": "Luis", "edad" :45}},
            {"id00004" : {"nombre": "Pedro", "edad" :55}},
            {"id00005" : {"nombre": "Juan", "edad" :65}},
            {"id00006" : {"nombre": "Juana", "edad" :25}},
            {"id00007" : {"nombre": "María", "edad" :35}},
            {"id00008" : {"nombre": "Daniela", "edad" :45}},
            {"id00009" : {"nombre": "Margarita", "edad" :55}},
            {"id00010" : {"nombre": "Ana", "edad" :65}}
            ]

#* Información de productos: nombre, precio, identificador único y color.
productos =[ {"prod001": {"nombre" :"producto_1", "precio": 100, "color" : "rojo" }}, 
            {"prod002": {"nombre" :"producto_2", "precio": 200, "color" : "verde" }},
            {"prod003": {"nombre" :"producto_3", "precio": 300, "color" : "amarillo" }},
            {"prod004": {"nombre" :"producto_4", "precio": 400, "color" : "azul" }},
            {"prod005": {"nombre" :"producto_5", "precio": 500, "color" : "gris" }} ]


#variable autoincremental:


#Agregar Producto
#productos["prod006"] = {"nombre" :"producto_6", "precio": 600, "color" : "violeta" }

#* Información de la compra de cada cliente.


#- Agregar Cliente.
def agregar_cliente():
    contador_último_usuario = 10
    id_nuevo_cliente = "id000" + str(contador_último_usuario + 1)
    contador_último_usuario += 1
    nombre_nuevo_cliente = input("Ingrese nombre de nuevo cliente: ")
    edad_nuevo_cliente = int(input("ingrese la edad: "))
    clientes.append({id_nuevo_cliente: {"nombre": nombre_nuevo_cliente, "edad": edad_nuevo_cliente}})

#para poder hacer algo así
#nombre_nuevo_cliente = input("Ingrese nombre de nuevo cliente")
#edad_cliente = int(input("ingrese su edad"))
#usuario_nuevo = {"id":(contador+1), "nombre":nombre_nuevo_cliente, "edad":edad_cliente}
    #👍 puse el id como el key del diccionario, no era necesario usar otro valor

#clientes.append(usuario_nuevo)👍
#así pude hacer la tarea 6 individual👍.



#- Mostrar Clientes: Muestra el listado de clientes.
def mostrar_clientes():
    for cliente in clientes:
        print("------------")
        for id in cliente:
            print("Número único: ", id)
            for dato in cliente[id]:           
                print(dato, ": ", cliente[id][dato])
                #time.sleep(2)

#- Mostrar Producto: Muestra el listado de productos.

"""
PENDIENTE
"""

#- Elimine clientes. ¿Qué información requiere para eliminar un cliente al azar?
#ninguna realmente, solo evitar que se ejecute esto en un rango vacio
#cliente random
def eliminar_random_cliente():
    random_cliente = random.choice(clientes)
    if random_cliente != "":
        clientes.remove(random_cliente)

#imprimir lista de opciones para ingresar al input
#eliminar cliente concreto
#imprime opciones para eliminar un cliente:
def eliminar_cliente_concreto():
    print("\n=======================\n", "Menú de eliminación de clientes", "\n=======================\n")
    for cliente in clientes:
        print("----------------\n")
        for id in cliente:
            print("Número único: ", id)
            for dato in cliente[id]:           
                print(dato, ": ", cliente[id][dato])
        print(f"Para eliminar este cliente ingrese: {id}\n")

    #pregunta cliente a eliminar, según menu anterior
    while True:
        global cliente_a_eliminar
        print(clientes)
        
        cliente_a_eliminar = input('Ingrese cliente a eliminar. Para no eliminar nada, escriba "NO" y presione ENTER: ').strip().lower()
        print(f"el cliente a eliminar es {cliente_a_eliminar}")
        for cliente in clientes:
            for key, value in cliente.items():
                print(f"la key es {key}")
                print(f"clientes es {clientes}")

                if cliente_a_eliminar == key:
                    clientes.remove(cliente)
            # print("Se ha eliminado el cliente")
            # break
        if cliente_a_eliminar == "no":
            break
        
    print("imprimir para revisar")


#- Elimine productos. ¿Qué información requiere para eliminar el último producto agregado?
def eliminar_ultimo_producto():
    productos.pop()
#ninguna información, aparentemente pop expresamente solo puede remover el último indice
#y no recibe parámetros
#En el caso que la información se esté guardando en un diccionario.
#- Imprima todas las claves con un delay de 2 segundos.
def imprimir_claves():
    print("imprimiendo las claves de ambos diccionarios")
    for cliente in clientes:
            print("------------")
            #misma lógica que arriba en el punto de mostrar clientes.
            for id_cliente in cliente.keys():
                print(f"Id de usuario: {id_cliente}")
                #time.sleep(2)
                
    for producto in productos:
            print("------------")
            for id_producto in producto.keys():
                print(f"Id de producto: {id_producto}")
                #time.sleep(2)
#- Luego imprima los valores con un delay de 3 segundos.
def imprimir_valores():
    print("imprimiendo los valores de ambos diccionarios")
    #será mas correcto usar .values() para objetivos de la tarea?
    #sería for valores in cliente.values() / print(f"valores:{})
    for cliente in clientes:
            print("------------")
            #misma lógica que arriba en el punto de mostrar clientes.
            for k, v in cliente.items():
                print(f"Valores de cliente {k}: {v}")
                #time.sleep(3)
                
    for producto in productos:
            print("------------")
            for k, v in producto.items():
                print(f"Valores de cliente {k}: {v}")
                #time.sleep(3)
#El código siempre debe estar debidamente comentado. Esto les ayudará a comprenderlo en el futuro y
#ayudará a otras personas a comprender su código.
#¿Lo lograron?
#Imprima en pantalla un listado que contenga los ID de los usuarios.
def imprimir_id():
    for cliente in clientes:
        print(cliente[id])
        cliente[id] = cliente[id] + "_piloto"
        print(cliente[id])

#Modifique todos los ID. Agregue la siguiente cadena de caracteres: “_piloto” al final de cada ID.
"""
PENDIENTE
"""
#Imprima en pantalla los nuevos ID.
"""
PENDIENTE
"""
#Elimine los últimos cuatro ID_clientes en el listado.
"""
PENDIENTE
"""