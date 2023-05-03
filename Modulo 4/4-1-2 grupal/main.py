"""
Una opción propuesta es manejar una planilla de cálculo para el registro de los pedidos y realización de
seguimiento. Si bien es factible su uso, a medida que se agreguen nuevos clientes el archivo irá
creciendo, y será complejo mantener la integridad entre los datos, impidiendo relacionarlos
adecuadamente.

SOLUCIÓN
Dados los antecedentes anteriores, es necesario desarrollar una solución tecnológica que cubra los
procesos de negocio descritos y que proponga una mejora en la gestión, el control, la seguridad, y
disponibilidad de información para el negocio y sus clientes. El sistema debe permitir presentar
productos, tomar pedidos y hacer seguimiento de estos y la gestión de clientes. Además, se requiere
que el sistema genere reportes y estadísticas que ayuden a tomar de decisiones y mejorar el
rendimiento de la empresa, considerando la cantidad de clientes, y la demanda de éstos. Es
imprescindible mantener comunicación con los encargados de entregar los pedidos, y darles la
posibilidad de realizar todas sus actividades teniendo conectividad a través de dispositivos móviles.
DESARROLLO - Continuación del trabajo.
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender
las ventajas de la programación orientada a objetos.
En vista a nuestro sistema desarrollado anteriormente se solicita lo siguiente:
Agregar una clase Proveedor con los siguientes atributos:

● RUT
● Nombre Legal
● Razón Social
● País
● Una distinción entre persona jurídica o persona natural
A las clases creadas en la actividad anterior, incorpore un atributo opcional a cada una.
Al momento de instanciar un objeto de la clase Producto, deberá existir una Composición con la clase
Proveedor.

Se deberá crear un método vender de la clase Vendedor y esta deberá descontar el valor del atributo
stock de la clase Producto y calcular un 0.5% de comisión referente al valor_neto del producto y luego
sumarlo al atributo comisión de la clase Vendedor. Luego el método deberá calcular el valor final del
producto y descontarlo del atributo saldo de la clase Cliente.
Se solicita que existan condicionales para realizar validaciones correspondientes, como por ejemplo si
no existe saldo suficiente en la clase Cliente, este deberá mostrar un mensaje indicando que no es
posible adquirir el producto por saldo insuficiente, de la misma forma para el stock de productos.
Desarrolle cuatro métodos más para dinamizar la interacción entre diferentes clases e instancias. Al
menos uno de estos métodos debe aplicar los contenidos de ‘sobrecarga de métodos’.
"""