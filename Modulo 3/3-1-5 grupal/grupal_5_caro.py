"""
INSTRUCCIONES:
Guarde en una variable la siguiente información:
* Información de clientes: nombre, edad, identificador único.
* Información de productos: nombre, precio, identificador único y color.
* Información de la compra de cada cliente.
Debe crear 10 clientes y 5 productos.

Sin definir funciones, utilice métodos necesarios para:
- Agregar Cliente.
- Agregar Producto
- Mostrar Clientes: Muestra el listado de clientes.
- Mostrar Producto: Muestra el listado de productos.
- Elimine clientes. ¿Qué información requiere para eliminar un cliente al azar?
- Elimine productos. ¿Qué información requiere para eliminar el último producto agregado?
En el caso que la información se esté guardando en un diccionario.
- Imprima todas las claves con un delay de 2 segundos.
- Luego imprima los valores con un delay de 3 segundos.
El código siempre debe estar debidamente comentado. Esto les ayudará a comprenderlo en el futuro y
ayudará a otras personas a comprender su código.
¿Lo lograron?
Imprima en pantalla un listado que contenga los ID de los usuarios.
Modifique todos los ID. Agregue la siguiente cadena de caracteres: “_piloto” al final de cada ID.
Imprima en pantalla los nuevos ID.
Elimine los últimos cuatro ID_clientes en el listado.
"""

#importar librerias
import time
import random

clientes = [
    {"nombre": "Cliente1", "edad": 25, "id": "id1"},
    {"nombre": "Cliente2", "edad": 32, "id": "id2"},
    {"nombre": "Cliente3", "edad": 19, "id": "id3"},
    {"nombre": "Cliente4", "edad": 40, "id": "id4"},
    {"nombre": "Cliente5", "edad": 55, "id": "id5"},
    {"nombre": "Cliente6", "edad": 28, "id": "id6"},
    {"nombre": "Cliente7", "edad": 21, "id": "id7"},
    {"nombre": "Cliente8", "edad": 30, "id": "id8"},
    {"nombre": "Cliente9", "edad": 47, "id": "id9"},
    {"nombre": "Cliente10", "edad": 18, "id": "id10"}
]

productos = [
    {"nombre": "Producto1", "precio": 100, "id": "prod1", "color": "rojo"},
    {"nombre": "Producto2", "precio": 200, "id": "prod2", "color": "verde"},
    {"nombre": "Producto3", "precio": 300, "id": "prod3", "color": "azul"},
    {"nombre": "Producto4", "precio": 400, "id": "prod4", "color": "amarillo"},
    {"nombre": "Producto5", "precio": 500, "id": "prod5", "color": "morado"}
]

#(solo se usa una funcion para llamar el menu, todo lo demas es solo con métodos)
def menu():
    print("--------MENU--------")
    print("Agregar nuevo cliente = 1")
    print("Agregar nuevo producto = 2")
    print("Listar clientes = 3")
    print("Listar productos = 4")
    print("Eliminar cliente al azar = 5")
    print("Imprimir claves y valores por separado = 7")
    print("Imprimir ids de usuarios = 8")
    print("Modificar IDs usuario = 9")
    print("Eliminar los ID de los últimos 4 usuarios = 10")

    
    opcion = int(input("ingrese el número correspondiente a la opcion elegida: "))
    if opcion == 1:
        nuevo_cliente = {}
        nom = input("Ingrese el nombre del cliente: ").lower()
        ed = int(input("Ingrese la edad: "))
        idc = 111   #COTRREGIR ID
        nuevo_cliente = {"nombre": nom, "edad": ed, "id": idc}
        clientes.append(nuevo_cliente)
        print(f"El cliente {nom} ha sido agregado.")
        time.sleep(2)
        menu()

    elif opcion == 2:
        nomp = input("Ingrese el nombre del producto: ").lower()
        pr = int(input("Ingrese el precio: "))
        idp = 222
        co = input("Ingrese el color: ").lower()
        nuevo_producto = {"nombre": nomp, "precio": pr, "id": idp, "color": co} #CORREGIR ID
        productos.append(nuevo_producto)
        print(f"El producto {nomp} ha sido agregado.")
        time.sleep(2)
        menu()

    elif opcion == 3:
        print("Listado de Clientes:")
        for cliente in clientes:
            print("Nombre:", cliente["nombre"])
            print("Edad:", cliente["edad"])
            print("ID:", cliente["id"])
        time.sleep(2) 
        menu() 

    elif opcion == 4:
        print("Listado de Productos:")
        for producto in productos:
            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("ID:", producto["id"])
            print("Color:", producto["color"])
        time.sleep(2)
        menu() 

    elif opcion == 5:
        eliminar_cliente = random.choice(clientes)
        clientes.remove(eliminar_cliente)
        print("Se eliminó el cliente:")
        print("Nombre:", eliminar_cliente["nombre"])
        print("Edad:", eliminar_cliente["edad"])
        print("ID:", eliminar_cliente["id"])
        time.sleep(2)
        menu() 

    elif opcion == 6:
        producto_eliminado = productos.pop()
        print(f"Se ha eliminado el ultimo producto agregado: {producto_eliminado['nombre']}")
        time.sleep(2)
        menu() 
    elif opcion == 7:
        print(f"imprimir claves y valores:\n")
        for cliente in clientes:
            print("------------")
            #misma lógica que arriba en el punto de mostrar clientes.
            for id_cliente in cliente.keys():
                print(f"Id de usuario: {id_cliente}")
                time.sleep(2)
        for producto in productos:
            print("------------")
            for id_producto in producto.keys():
                print(f"Id de producto: {id_producto}")
                time.sleep(2)
                #- Luego imprima los valores con un delay de 3 segundos.
        print("imprimiendo los valores de ambos diccionarios")
        #será mas correcto usar .values para objetivos de la tarea?
        for cliente in clientes:
                print("------------")
                #misma lógica que arriba en el punto de mostrar clientes.
                for k, v in cliente.items():
                    print(f"Valores de cliente {k}: {v}")
                    time.sleep(3)
        for producto in productos:
                print("------------")
                for k, v in producto.items():
                    print(f"Valores de cliente {k}: {v}")
                    time.sleep(3)
        time.sleep(2)
        menu() 
    elif opcion == 8:
        print("Imprimir un listado de los ID de los usuarios:")
        for cliente in clientes:
            print(cliente["id"])
        time.sleep(2)
        menu() 
    elif opcion == 9:
        print("modificando IDs...")
        for cliente in clientes:
            cliente["id"] = cliente["id"] + "_piloto"
        time.sleep(2)
        menu() 
    elif opcion == 10:
        print("eliminando los ID 4 ultimos clientes...")
        slice_clientes = clientes[-4:]
        for cliente in slice_clientes:
            cliente["id"] = "" 
        time.sleep(2)
        menu() 
    else:
        print("Opción inválida")
        time.sleep(2)
        menu() 
menu()
"""
#ELIMINAR LOS 4 ULTIMOS ID DE CLIENTE DEL LISTADO



"""