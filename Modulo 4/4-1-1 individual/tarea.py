"""
crear clases utilizando sintaxis de Python, para comprender
las ventajas de la programación orientada a objetos.
En base al sistema desarrollado anteriormente en el módulo de Python básico, se solicita actualizar
lo siguiente:
Identifica tres tipos de usuarios de su aplicación.
Identifica tres atributos por tipo de usuario.
Identifica tres acciones que pueden desarrollar cada tipo de usuario. Las acciones se deben ejecutar de
forma interna en nuestra aplicación. Por ejemplo, acceder a datos sensibles, registrar nuevos usuarios,
enviar solicitudes de información adicional.
Piense en nuevos atributos y acciones que pueden realizar los objetos.
Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
gráfica. Desarrollen el ejercicio de forma intuitiva.
"""
usuarios = []
class usuario:
    def __init__(self, nivel, nombre, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc

class admin(usuario):
    respeto = "insuficiente"
    carisma = "ninguno"
    profesionalismo = "al debe"

    def accion1(self):
        print(f"Hola, mis datos son:\n{self.nombre}\n{self.desc}\n")

    def accion2(self, usu, passw):
        print("creando nuevo usuario")
        usuario_nuevo = {"username": usu, "password": passw}
        usuarios.append(usuario_nuevo)
        print(f"he creado el usuario {usu}")
        for usuario in usuarios: print(usuario)
    def accion3():
        pass

class regular(usuario):
    regularidad = "total"
    personalidad = "neutra"
    comportamiento = "imprecedible"

    def accion1(self):
        print(f"Soy de clase {str(self.__class__)}\n")
        
    def accion2(self):
        pass
        
    def accion3(self):
        pass

class invitado(usuario):
    privilegios = "chequeados"
    estadia = "corta"
    fidelidad = "nula"

    def accion1(self):
        print(f"Soy de clase {str(self.__class__)}\n")
        
    def accion2(self):
        pass
        
    def accion3(self):
        pass

#acá hago la "instanciación". Creo instancias de objeto de las subclases admin, basico y invitado
administrador = admin("administrativo", "admin", "cuenta administrativa")       
usuario_basico = regular("regular", "usuario_regular", "cuenta regular")
usuario_invitado = invitado("invitado", "invitado", "cuenta invitado")

administrador.accion1()
usuario_basico.accion2()
administrador.accion2(input("ingrese un usuario: "), input("ingrese una contraseña: "))
usuario_invitado.accion1()

