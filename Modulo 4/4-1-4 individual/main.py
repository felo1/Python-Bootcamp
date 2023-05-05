"""
DESARROLLO - Continuación del trabajo.
En base al diagrama de clases desarrollado en el ejercicio anterior, integra una estructura de herencia de
tres niveles. Agregue un método por cada clase creada en su proyecto.
Realice ejercicios para comprobar la herencia de métodos y atributos.
Incorpore un ejemplo práctico de sobreescritura de métodos en su ejercicio individual.
Como pista, una forma de identificar niveles dentro de su aplicación, se puede encontrar en base a
diferentes tipos de usuarios con perfiles diferentes. Genere una clase principal, para luego desarrollar
perfiles más particulares.
"""

class Cuenta_de_usuario:
    def __init__(self, username, email, contraseña, nivel):
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.nivel = nivel
        self.inbox = []

    def logoff():
        pass

    def login():
        pass

    def enviar_mensaje():
        pass

class Administrador(Cuenta_de_usuario):
    def toggle_suspender():
        pass
    def modificar_usuario():
        pass
    def login():
    #se me ocurre que los superadmin podrian sobrecargar el login para loguearse con la identidad de otro usuario para hacer cambios, dar soporte, etc.
        pass
#superadmin debera ser diseñado como heredando de admin para tener 3 nivles de herencia.

class Superadmin(Administrador):
    def eliminar_usuario():
        pass
    #Incorpore un ejemplo práctico de sobreescritura de métodos en su ejercicio individual.
    #lo cual significa que una clase hijo tenga un metodo con mismo nombre y que reemplace la funcionalidad original.
    #se me ocurre que los superadmin podrian sobrecargar el login para loguearse con la identidad de otro usuario para hacer cambios, dar soporte, etc.
    def login():
        pass
    def asignar_permiso():
        pass

class Invitado:
    def crear_cuenta():
        pass

class Usuario(Invitado):
    def ticket():
        pass