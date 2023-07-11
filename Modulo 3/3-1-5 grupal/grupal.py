import random
import time
#Guarde en una variable la siguiente información:

#hay una libreria para crear ids parece
#hay que hacer una valoracion que diga 
#recorrer toda la lista de clientes, ver el ID, verificar si el nuevo randing existe y evitarlo.
#sino, la libreria se llama uid que genera un id unico de forma alfanumerica (asi pierde la utilidad matematica supongo)
#

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
#no sé ustedes pero se me hizo más fácil hacer una lista y que esa contenga diccionarios, para
#hacerle append de diccionarios a la lista (donde cada user es un dict)
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
for cliente in clientes:
        print("------------")
        #id_cliente y datos son referencias inventadas a items del dict clientes.
        #id_cliente pesca el key (el id) y datos pesca bueno los datos
        for id_cliente, datos in cliente.items():
            print(f"Usuario con id: {id_cliente} tiene los siguientes datos {datos}")
            #time.sleep(2)



#- Mostrar Producto: Muestra el listado de productos.



#- Elimine clientes. ¿Qué información requiere para eliminar un cliente al azar?
#cliente concreto
cliente_a_eliminar = input("Ingrese cliente a eliminar: ")
for cliente in clientes:
    if cliente_a_eliminar in cliente:
        clientes.remove(cliente)
    else:
        print("cliente no encontrado")
        break

#cliente random
random_cliente = random.choice(clientes)
clientes.remove(random_cliente)
#- Elimine productos. ¿Qué información requiere para eliminar el último producto agregado?
productos.pop()
#ninguna información, aparentemente pop expresamente solo puede remover el último indice
#y no recibe parámetros

#En el caso que la información se esté guardando en un diccionario.
#- Imprima todas las claves con un delay de 2 segundos.
print("impriminedo las claves de ambos diccionarios")
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
print("imprimiendo los valores de ambos diccionarios")
#será mas correcto usar .values para objetivos de la tarea?
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
#Modifique todos los ID. Agregue la siguiente cadena de caracteres: “_piloto” al final de cada ID.
#Imprima en pantalla los nuevos ID.
#Elimine los últimos cuatro ID_clientes en el listado.