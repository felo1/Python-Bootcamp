usuarios = []
#Agregar una nueva clase pertinente a la aplicación que están desarrollando e 
class Superadmin():
    def __init__(self, nivel, nombre, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc
        #identificar en ella al menos cuatro atributos (uno de ellos debe ser opcional). 
        self.permisos = ["crear_usuarios", "crear_grupo", "crear_rol", "crear_permiso"]
    def asignar_permisos():
         pass
    
    def cambiar_nivel():
         pass
    
    def eliminar_usuario():
         pass

class Admin():
    def __init__(self, nivel, nombre, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc

    def mostrar_datos(self):
        print(f"Hola, mis datos son:\n{self.nombre}\n{self.desc}\n")

    def crear_usuario(self, usu, passw):
        print("creando nuevo usuario")
        usuario_nuevo = {"username": usu, "password": passw}
        usuarios.append(usuario_nuevo)
        print(f"he creado el usuario {usu}")
        for usuario in usuarios: print(usuario)

    def suspender_usuario():
        pass

class Regular():
    def __init__(self, nivel, nombre, username, password, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc
        self.username = username
        self.password = password
        self.estado = "creado"

    def login(self, username, password):
        for user in usuarios:
            if user["username"] == username:
                if user["password"] == password:
                    self.estado = "logueado"
                    print(f"Bienvenido {user['username']}")
                    return
        print("Usuario o password incorrectos")
        
    def accion2(self):
                print("Esta es mi acción 2")

        
    def accion3(self):
                print("Esta es mi acción 3")

class Invitado():
    def __init__(self, nivel, nombre, desc):
        self.nivel = "usuario invitado"
        self.nombre = nombre
        self.desc = "Cuenta de usuario invitado"
        
    def accion1(self):
        print(f"Soy de clase {str(self.__class__)}\n")
        
    def accion2(self):
        print("Esta es mi acción 2")
        
    def accion3(self):
        print("Esta es mi acción 3")


administrador = Admin("administrativo", "admin", "cuenta administrativa")       
usuario_basico = Regular("regular", "usuario_regular1", "username1", "1234", "cuenta regular")
usuario_invitado = Invitado("invitado", "invitado", "cuenta invitado")

#administrador.crear_usuario("username1", "1234")
administrador.crear_usuario(input("ingrese un usuario: "), input("ingrese una contraseña: "))

usuario_basico.login("username1", "1234")

"""
DESARROLLO - Continuación del trabajo.

-Agréguela al diagrama intuitivo que realizó en la actividad anterior.
- Se deberá crear métodos para cada uno de los usuarios. Piensen en diferentes acciones particulares
que pueda ejecutar cada una de sus clases. Desarrolle cuatro métodos por cada clase. Dos deben
incluir acciones que afecten números y dos que afecten strings. 
-Al menos uno de estos métodos debe aplicar los contenidos de ‘sobrecarga de métodos’.
-También se solicita que existan condiciones para realizar las validaciones correspondientes.

El entregable es un script .PY
- El tiempo máximo para resolver la evaluación es el periodo correspondiente a una clase regular.

"""