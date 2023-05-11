#link al drive
#https://drive.google.com/file/d/1sLf1IH4NsgCmlTKttwDpa-znSJmu_lfV/view
"""
def abrir_archivo(archivo)
try:
	file = open(archivo)
	raise Exception("no es del tipo correcto")
excepto FileNotFoundError as e:
	print("No es un archivo", e)

esto sirve para identificar errores para debugging
"""

"""
def division(dividendo, divisor)
try:
    resultado = dividendo / divisor
	raise Exception("Error en numeros")
excepto FileNotFoundError as err:
	print("No es un archivo", err)
Aqui el raise corre antes del except. En este caso lo identificamos pero no lo manejamos.

"""
class perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def bark():
        print("woof")
#Los atributos son inmutables   . Los estados no lo son
    def metodo(self):
        return 'metodo de instancia llamado', self
        #esto devuelve el texto Y luego te da la ubicacion en memoria(?) del objeto.
    #metodo de instancia regular. acceden libremente a atributos y otros metodos del objeto.
    #pueden modificar estado del objeto. pueden acceder a la misma clase con self.__class__.
    @classmethod
    #A decorator is a design pattern in Python that allows a user to add new functionality to an 
    # existing object without modifying its structure.
    def metodo_de_clase(cls):
        return 'metodo de clase llamado', cls
    #metodo de clase. acceden libremente a atributos y otros metodos de la clase. 
    #no pueden modificar estado de la clase.
    #con ese de

    def metodo_estatico():
        return 'metodo estatico llamado'
    
obj = perro('iriel', 15)
obj.metodo() #llamara al metodo "metodo" desde una instancia de la clase perro.
#Cuando se llama al método, Python reemplaza el argumento self con el objeto de
#instancia, obj.


boby = perro('boby', 10)
duque= perro('duque', 3)
print(boby.nombre)

print("output de perro.metodo(obj): ")
perro.metodo(obj) #llama al metodo de la instancia.  


class Inst:
    def __init__(self, nombre):
        self.nombre = nombre
        
def presentar(self):
    print("Hola, Soy %s, y mi nombre es is %s" % (self, self.name))
    mi_inst = Inst("Instancia de Prueba")
    otra_inst = Inst("Otra Instancia")

mi_inst.presentar()
Otra_inst.presentar()
