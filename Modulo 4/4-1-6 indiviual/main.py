"""

DESARROLLO - Continuación del trabajo.
En vista a nuestro sistema desarrollado anteriormente se solicita lo siguiente:
Incorporar un archivo CSV el cual se encargará de almacenar información de los colaboradores de tu
aplicación en un archivo externo.
En un script diferente será posible acceder al archivo y verificar la información de teléfono y edad.

Así mismo se solicita contar con un registro de los usuarios de tu aplicación. Este registro debe contar
con información del nombre, nombre de usuario, un identificador y la contraseña. Este registro debe ser
serializado. Identifiquen la forma de desarrollarlo.



En un script diferente, acceda a los diferentes datos registrados.
Guarde información de 10 colaboradores y 10 usuarios.

"""


"""
ejemplkos del anibal:
archivo = open ("nombres.txt", "r")
print(archivo.read(3))

archivo.readlines() me entrega una lista de strings. 
para hacerlo más legible 

archivo = open("nombres.txt", "w")
archivo.writelines("Damian", "Hernan", "Hugo,\nRamiro, Sofíoa, Yamila")
archivo.close()
eso sería una lista 
para eliminar un archivo.
archivo.remove() (requiere import os)
"""
import re, os, time, csv, json
usuarios = []

#def escribir_a_csv_sinimport(usuarios):
#    archivo = open("c:/temp/usuarios2.csv", "w")
###    cabecera = ["nombre", "username", "id", "edad", "telefono", "password en texto plano"]
#    archivo.writelines(cabecera)
##    for user in usuarios:
#            args = (user.name, user.username, user.id, user.edad, user.telefono, user.contraseña)
#            archivo.writelines(args)

def escribir_a_csv_sinimport(usuarios):
    archivo = open("c:/temp/usuarios2.csv", "w")
    cabecera = ["nombre", "username", "id", "edad", "telefono", "password en texto plano"]
    archivo.writelines(';'.join(cabecera) + '\n')
    for user in usuarios:
        args = [user.name, user.username, str(user.id), str(user.edad), user.telefono, user.contraseña]
        archivo.writelines(';'.join(args) + '\n')
    archivo.close()

def escribir_a_csv(usuarios):
    #eso del mode y newline aun no lo leo
    with open('c:/temp/usuarios.csv', mode='w', newline='') as file:
         #mode w = escribir 
        #hay que hacer el error catching
        #de file, y de type
         writer = csv.writer(file, delimiter=';')
         cabecera = ["nombre", "username", "id", "edad", "telefono", "password en texto plano"]        
         writer.writerow(cabecera)
         
    with open('c:/temp/usuarios.csv', mode='a', newline='') as file:
        #modo a = append
        writer = csv.writer(file, delimiter=';')
        for user in usuarios:
            args = (user.name, user.username, user.id, user.edad, user.telefono, user.contraseña)
            writer.writerow(args)

    #siempre debo cerrar el archivo 
    file.close()

def escribir_a_json(usuarios):
    with open('c:/temp/usuarios.json', 'w', encoding='utf-8') as file:
        usuarios_json = {'usuarios': []}
        for user in usuarios:
            usuarios_json['usuarios'].append({
                'nombre': user.name,
                'username': user.username,
                'id': user.id,
                'edad': user.edad,
                'telefono': user.telefono,
                'contraseña': user.contraseña
            })
        json.dump(usuarios_json, file, indent=4, ensure_ascii=False) #el ensure_ascii me permite que el json respete las ñ.

    # Close the file
    file.close()
    

def email_coincidir(email):
    #email se espera que sea un string y lo usa para comparar la propiedad email de los usuarios. 

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

def pass_coincidir(self, password):
    if self.contraseña == password:
        return True
    else:
        return False        
        
def validar_pass(password = None):
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
    def __init__(self, username, name, id, email, edad, contraseña, telefono, nivel=3):
        self.username = username
        self.email = email
        self.name = name
        self.edad = edad
        self.id = id
        self.email = email
        self.contraseña = contraseña
        self.nivel = nivel #3 = usuario base
        self.inbox = []
        self.estado = "nunca ha surfeado"
        self.telefono = telefono

    def logoff(self):
        self.estado = "desconectado"

    def login(self, username, password):
        try:
            if not type(password) == str or not type(username) == str:
                raise TypeError("Error en la interpretación de las credenciales")
        except Exception as err:
            print(f"Ocurrió un error inesperado. Puede informar a su administrador que su inicio de sesión provocó un error de tipo {type(err).__name__} {err}")
        finally:
            if user_coincidir(username) and pass_coincidir(self, password):
                self.estado = "logueado"
                print("Has iniciado sesión en Myspace")
            else:
                print("Credenciales incorrectas")
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
            #usuarios.append(newUser)
            escribir_a_csv(newUser)

class Usuario(Cuenta_de_usuario):

    def ticket(self):
        for user in usuarios:
            if type(user) == Administrador or type(user) == Superadmin:
                print(f"Acá hay un admin, te voy a espammear {user.username}")
                

                #AttributeError
                try: 
                    user.inbox.append("SPAM")
                    for inboxItem in user.inbox:
                        print(inboxItem)
                except:
                    print("Atributo no apto para el tipo de variable")
                
        print("Campaña de spam completa")
            
#EOP
