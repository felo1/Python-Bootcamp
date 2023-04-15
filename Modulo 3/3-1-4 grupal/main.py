""" 
-desarrollaremos una forma de almacenar nuestro stock de dos productos. 
-El primer producto tendrá 120 unidades y el segundo 150.
-Simularemos cada 3 segundos una compra de “n” (rango 1-10) unidades de cualquiera de los dos productos.
-Cada compra afecta el stock inicial de productos. Es decir, si una compra simulada es
de 3 unidades del producto 1, este se debe descontar del stock.
-Cada 10 compras, el programa debe imprimir en pantalla el número de unidades disponibles por producto.
-Cuando un producto tenga un stock de menos de 100 unidades, los proveedores enviarán 50 unidades más. 
Esto se debe reflejar en el stock de cada producto.
-Lamentablemente, los proveedores solo tienen stock suficiente para enviar 150 unidades en total de productos 1 y 2.
"""

#dict stock nombre:numero
#time wait 3s
#compra_random = random range 1-10 
#descontar compra_random de producto_random
#sumar contador de compras
#cada 10, print
#condicional de c/10 compras, agregar 50 más del item, sumarlo a lo entregado por proveedores (stock limitado)

import random
import time

stock_productos = {"Densimetro nuclear": 120, "Lámparas de sal": 150,}
stock_proveedor = {"Densimetro nuclear": 150, "Lámparas de sal": 150,}
def main():
    contador_compras = 0
    while(True):
        numero_productos =  random.randint(1, 10)
        producto_seleccionado = random.choice(list(stock_productos.keys()))
        print(f"nos entró una compra de {numero_productos} {producto_seleccionado}\n")
        if(stock_productos[producto_seleccionado]) >= numero_productos:
            stock_productos[producto_seleccionado] -=  numero_productos
            for producto in (stock_productos.keys()):
                print(f"quedan {stock_productos[producto]} {producto}")
            #print(f"quedan {stock_productos['Densimetro nuclear']} densimetros")
            #print(f"quedan {stock_productos['Lámparas de sal']} lamparas")
            contador_compras += 1
            if(contador_compras % 10==0):
                print(f"Nos van quedando {stock_productos[producto_seleccionado]} del producto {producto_seleccionado}")
            if stock_productos[producto_seleccionado]<=100 and stock_proveedor[producto_seleccionado] >=50: 
                stock_productos[producto_seleccionado]+=50
                stock_proveedor[producto_seleccionado]-=50
            if stock_productos[producto_seleccionado] == 0:
                print(f"No quedan más unidades del producto {producto_seleccionado}")
                #time.sleep(3)
                continue
            if any(stock_productos) == 0:
                break
            #time.sleep(3)
        else:
            print("No hay suficiente stock para completar esa compra")
            print("final:\n")
            print(f"quedan {stock_productos['Densimetro nuclear']} densimetros")
            print(f"quedan {stock_productos['Lámparas de sal']} lamparas")       
            if all(value == 0 for value in stock_productos.values()):
                break
            continue

main()
#deliberadamente sin break