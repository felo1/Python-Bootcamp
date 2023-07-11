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
import re, os, time
usuarios = []

def email_coincidir(email):
    for usuario in usuarios:
        #if usuario["email"] == email: #recordatorio de que no estoy trabajando con diccionarios si no instancias de clase usuario
        if usuario.email == email:
            return True
    else:
        return False
        
def user_coincidir(nombre): 
    for usuario in usuarios:
        if usuario.username == nombre:
            return usuario #esto me sirve para que además de chequear si existe el usuario, me sirve tb para referenciarlo y manipularlo fuera de este metodo.
    else:
        return False
        
def validar_pass(password = None):
    #acá uso sobrecarga
    #si no recibe un pass de entrada, te atrapa hasta tener un password que pueda devolver
    if password == None:
        while(True):
            errores = []
            password = ""
            password= input("\nAsegúrese de incluír al menos 8 caracteres, con mayúsculas, minúsculas y cifras:")
            if(password==""):
                errores.append("Su contraseña no puede estar vacía")
            if(len(password) < 8):
                errores.append("Su contraseña debe contener al menos 8 caractéres")
            
            #chequeo de upper Y lower, isnumeric, tiene simbolo con regex, usa import RE
            #pattern es frase arbitraria para almacenar el patron de regex
            pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$') #holy shit
            #return bool(pattern.match(password)) sugerencia original, devuelve un bool segun lo que resulte
            if not pattern.match(password): #es decir, en false te anota el error
                errores.append("Su contraseña debe contener al menos un caracter mayúscula, uno minúscula, uno numérico y un caracter especial")
            if len(errores) > 0:
                print("\nSu contraseña no cumple con nuestros criterios, favor revisar lo siguiente:\n")
                for error in errores:
                    print(error)
                input("presiona una tecla para continuar\n")
            else:
                return password
    else:
        #chequeo con contraseña preinserta, ej, para usuario creando cuenta.
        #debe devolver un boolean, true para validada, false para inválida con feedback.
            errores = []
            if(len(password) < 8):
                errores.append("Su contraseña debe contener al menos 8 caractéres")
            #chequeo de upper Y lower, isnumeric, tiene simbolo con regex, usa import RE
            #pattern es frase arbitraria para almacenar el patron de regex
            pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$') #holy shit
            #return bool(pattern.match(password)) sugerencia original, devuelve un bool segun lo que resulte
            if not bool(pattern.match(password)):
                errores.append("Su contraseña debe contener al menos un caracter mayúscula, uno minúscula, uno numérico y un caracter especial")
            if len(errores) > 0:
                print("\nSu contraseña no cumple con nuestros criterios, favor revisar lo siguiente:\n")
                for error in errores:
                    print(error)
                input("Presione una tecla para continuar...\n")
                return False
            else:
                return True

class Cuenta_de_usuario:
    def __init__(self, username, email, contraseña, nivel=3):
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.nivel = nivel #3 = usuario base
        self.inbox = []
        self.estado = "nunca ha surfeado"

    def logoff(self):
        self.estado = "desconectado"

    def login(self, username, password):
        pass

    def enviar_mensaje():
        pass

class Administrador(Cuenta_de_usuario):

    def modificar_usuario(self):
        opciones = [
            "Modificar contraseña\n",
            "Modificar username\n",
            "Suspender Usuario\n"
             ]
        print("Eliga una opción")
        [print(opcion) for opcion in opciones]
        print("Este perfil es un admin básico. Para efectos de este ejercicio no hace nada"
              "más que imprimir, pero contrasta con el de superAdmin que sí tiene funcionalidad")
        
    #se me ocurre que los superadmin podrian sobrecargar el login para loguearse con la identidad de otro usuario para hacer cambios, dar soporte, etc.
    #superadmin debera ser diseñado como heredando de admin para tener 3 nivles de herencia.

class Superadmin(Administrador):
    #Incorpore un ejemplo práctico de sobreescritura de métodos en su ejercicio individual.
    #lo cual significa que una clase hijo tenga un metodo con mismo nombre y que reemplace la funcionalidad original.
    #superadmin sobre-escribe el metodo modificar_usuario de su clase padre Administrador.
    #superadmin tb es nuestra herencia de tercer nivel.    
    def modificar_usuario(self):
        print(f"Hola, soy un {self.__class__.__name__} y mi clase padre es {self.__class__.__base__.__name__}")
        #version que permite también eliminar
        print("==Menu de modificación de usuarios==")
        opciones = [
            "1) Modificar username",
            "2) Modificar password",
            "3) Suspender Usuario",
            "4) Eliminar usuario",
            "5) imprimir usuarios"
             ]
        print("Eliga una opción")
        [print(opcion) for opcion in opciones]
        opcion = input()
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion == 1:
                #Modificar nombre de usuario
                while True:
                    nombre = input("Ingrese @ de usuario a modificar:\n")
                    if user_coincidir(nombre):  #a pesar de que devuelve el objeto en vez de true, igual es "truthy" y responde a este tipo de validacion
                        print("Usuario encontrado.")
                        while True:
                            nuevo_nombre = input("Ingrese nuevo nombre de usuario:\n")
                            if not user_coincidir(nuevo_nombre):
                                user_coincidir(nombre).username = nuevo_nombre #aca está tomando el rol de un getter
                                print("modificación exitosa")
                                time.sleep(2)
                                self.modificar_usuario()
                            else: print("@ en uso"), time.sleep(2)
                    else: print("Usuario no encontrado, digitar otro?"), time.sleep(2)
            elif opcion == 2:
                while True:
                    nombre = input("Ingrese @ de usuario:\n")
                    if user_coincidir(nombre): 
                        print("Usuario encontrado.")
                        #password_nuevo = validar_pass()
                        #user_coincidir(nombre).contraseña = password_nuevo
                        #esas dos lineas se pueden condensar a
                        user_coincidir(nombre).contraseña = validar_pass()
                        print("modificación exitosa")
                        time.sleep(2)
                        self.modificar_usuario()
                    else: print("Usuario no encontrado, ingrese otro"), time.sleep(2)
            elif opcion == 3:
                usuario = user_coincidir(input("Ingrese el nombre de usuario a suspender:\n")) #funciona, puedo condensar 
                #en una linea almacenar el usuario que me devuelve el check que se llama mediante el input! recuerda la usabilidad de los returns "truthy"
                if usuario: usuario.estado = "suspendido" #aca usando truthy
                else: print("Usuario no encontrado") #asi como esta ahora nunca entraría acá.
            elif opcion == 4:
                usuario_a_eliminar = user_coincidir(input("Ingrese el nombre de usuario a suspender:\n")) 
                if input("Está seguro? Ingrese si o no")=="si":
                   usuario_a_eliminar.estado = "eliminado supuestamente"
                else: print("Usuario no encontrado") 
            elif opcion == 5:
                #"imprimir users"
                print("==================================Listado de usuarios==============================")
                [print(f"|username: {user.username}, pass_no_hasheado: {user.contraseña}, Estado:{user.estado}|") for user in usuarios]
            else:
                print("Opción inválida")
                import os
                os.pause(2)
                self.modificar_usuario()
        self.modificar_usuario()
    def asignar_permiso():
        pass

class Invitado:
    def crear_cuenta(self):
        print("Gracias por elegirnos, por favor ingrese los siguientes datos")
        while True:
            nombre = input("Ingrese su nombre de usuario:\n")
            if not user_coincidir(nombre): break
            else: print("Nombre en uso, favor usar otro"), time.sleep(2)
        while True:
            email = input("Ingrese su correo:\n")
            if not email_coincidir(email): break 
            else: print("Email en uso, favor usar otro"), time.sleep(2)
        while True:
            password = input("Ingrese su contraseña:\n")
            if validar_pass(password): break #en este caso, false significa que no lo validó y necesita otra rep
            else: os.system("cls")
            print(f"Gracias por crear su cuenta, {nombre}")   
            newUser = Usuario(nombre, email, password)
            usuarios.append(newUser)

class Usuario(Cuenta_de_usuario):

    def ticket(self):
        for user in usuarios:
            if type(user) == Administrador or type(user) == Superadmin:
                print(f"Acá hay un admin, te voy a espammear {user.username}")
                user.inbox.append("SPAM")
                for inboxItem in user.inbox:
                    print(inboxItem)
        print("Campaña de spam completa")
            
#TESTS=================================================

test_user = Usuario("test", "test@", "1234asdASD***")
primer_superadmin = Superadmin("mainAdmin", "test", 1234, 0)
primer_admin = Administrador("any", "aany@", 1234, 1)
usuarios.append(primer_admin), usuarios.append(test_user), usuarios.append(primer_superadmin)
test_user.ticket()
test_user.logoff()
#test_user.login()
#primer_admin.modificar_usuario()

#print("prueba de funcionalidad de creación de cuentas por parte de invitado")
primer_superadmin.modificar_usuario()

#new_invitado = Invitado()
#new_invitado.crear_cuenta()
