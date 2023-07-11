#- importar copy para hacer deepcopy
import copy

#- Definir el stock de un producto en una variable.
stock = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100, 9: 100, 10: 100}


#- Definir una forma de solicitar el stock disponible del producto por consola.

def consulta_stock(codigo_stock):
    print(f"El producto {codigo_stock} tiene un stock de {stock[codigo_stock]} unidades")
   #ABPro - Proyecto Grupal 3

#- Definir una forma de solicitar unidades del producto por consola. Este número de productos se
#almacenarán en una nueva variable llamada ‘Productos seleccionados’.
productos_seleccionados_plantilla = dict()
productos_seleccionados = copy.deepcopy(productos_seleccionados_plantilla)

def pedir(codigo, cantidad):
    global productos_seleccionados #para usar el scope global de la variable
    if cantidad > 20: # si pide más de 20
        print(f"No se pueden pedir más de 20 unidades. Usted pidió {cantidad}")
    elif (cantidad +1) <= stock[codigo] and cantidad >= 12: #si pide 12 o más, va uno de yapa
        productos_seleccionados.update({codigo: (cantidad + 1)}) #se agrega con yapa
        stock[codigo] -= cantidad+1
        print(f"Producto {codigo} : Se agregaron {cantidad} más 1 unidad, de yapa al pedido, {cantidad + 1} en total.")
    elif cantidad <= stock[codigo]: #si son menos de 12
        productos_seleccionados[codigo] = cantidad 
        stock[codigo] -= cantidad
        print(f"Producto {codigo}: Se agregaron {cantidad} unidades al pedido")
    else: #si no queda stock  
        print(f"No quedan suficientes unidades del Item {codigo}") 



#- Los productos reubicados serán descontados del stock inicial.
""""
#- Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen
# más de 12 unidades. Verificar que el stock posibilite entregar una unidad extra. Sino se entregan las
# unidades justas. Cada una de las posibles acciones debe imprimir un mensaje explicando lo realizado.
# - No se pueden solicitar más de 20 unidades en un mismo pedido.
# - Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no
#es posible realizar esta acción debido a que no hay stock suficiente.
"""