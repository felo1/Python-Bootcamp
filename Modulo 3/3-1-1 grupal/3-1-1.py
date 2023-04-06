productos = [    ["producto_1", "", 1000],
    ["producto_2", "", 2000],
    ["producto_3", "", 3000],
    ["producto_4", "", 4000],
    ["producto_5", "", 5000]
]

for i in range(len(productos)):
    cantidad =  int(input(f"Ingrese la cantidad de {productos[i][0]}: "))
    productos[i][1] = cantidad

suma = 0
total = 0
for producto in productos:
    suma = producto[1]*producto[2]
    total += suma

print(f"El valor total de los productos es: {total}")