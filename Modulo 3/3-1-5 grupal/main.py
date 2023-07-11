"""
PROBLEMA
La empresa “Te lo Vendo” es un emprendimiento de un grupo de jóvenes, quienes necesitan vender sus
productos en línea. Actualmente toman sus pedidos vía telefónica y a través del correo electrónico. Al
no existir un sistema centralizado para los pedidos, es complejo tener control oportuno de las entregas,
lo que genera que en algunos casos no se concreten algunos pedidos.
Una opción propuesta es manejar una planilla de cálculo para el registro de los pedidos y realización de
seguimiento. Si bien es factible su uso, a medida que se agreguen nuevos clientes el archivo irá
creciendo, y será complejo mantener la integridad entre los datos, impidiendo relacionarlos
adecuadamente.

SOLUCIÓN
Dados los antecedentes anteriores, es necesario desarrollar una solución tecnológica que cubra los
procesos de negocio descritos y que proponga una mejora en la gestión, el control, la seguridad, y

disponibilidad de información para el negocio y sus clientes. El sistema debe permitir presentar
productos, tomar pedidos y hacer seguimiento de estos y la gestión de clientes. Además, se requiere
que el sistema genere reportes y estadísticas que ayuden a la toma de decisiones y mejorar el
rendimiento de la empresa, considerando la cantidad de clientes, y la demanda de éstos. Es
imprescindible mantener comunicación con los encargados de entregar los pedidos, y darles la
posibilidad de realizar todas sus actividades teniendo conectividad a través de dispositivos móviles.
"""
"""
DESARROLLO
Guarde en una variable la siguiente información:
* Información de clientes: nombre, edad, identificador único.
* Información de productos: nombre, precio, identificador único y color.
* Información de la compra de cada cliente.
Debe crear 10 clientes y 5 productos.
La forma en que se organiza la información es a criterio del equipo. Es decir, ustedes definen el número
de variables y tipo de datos.
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
#clientes = {["id", ""]:{"nombre":"","edad":""}}
#productos = {["id", ""],{"nombre":"", "precio":"","color":""}}

clientes = {}
cliente1 = {["id", "1"]:{"nombre":"Juan","edad":"55"}}
cliente2 = {["id", "2"]:{"nombre":"Pedro","edad":"16"}}


print("ingrese su nombre")

input(f"nombre:")

producto1 = {["id", "1"],{"nombre":"carbon", "precio":50,"color":"negro"}}
producto2 = {["id", "2"],{"nombre":"zapato", "precio":100,"color":"azul"}}

john_doe = {"username":"John Doe", "password":"segurito", "edad":33}
usuarios = [john_doe]

dest = {}
def crear_usuario():
    username = input(f"Por favor ingrese su nombre de usuario:\n")
    password = input(f"Por favor ingrese su contraseña:\n")
    edad = int(input(f"Por favor ingrese su edad:\n"))
    usuario_nuevo = {"username":str(username), "password":str(password), "edad":edad}
    usuarios.append(usuario_nuevo)
