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



stock = {"Densimetro nuclear": 120, "Lámparas de sal": 150,}
while(true):


#deliberadamente sin break