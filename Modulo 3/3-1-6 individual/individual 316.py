"""
En esa ocasión se solicita un programa que:
- Pregunta el nombre de usuario y una contraseña.
- Almacene ambos datos en una variable.
- Que obtenga la edad del usuario a través de la consola. Sólo acepta números enteros.
- Almacene el dato edad a cada usuario.
- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.
El programa debe reiniciarse cada vez que termina. Sin perder la información anterior, debe continuar
preguntando por nombre y contraseña.
Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe
imprimir en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’.
Consideraciones generales
- Se pide enviar el archivo .py con el script correspondiente.
- El tiempo máximo para resolver la evaluación es el periodo correspondiente a una clase regular.
"""
"""
"""
import time
john_doe = {"username":"John Doe", "password":"segurito", "edad":33}
usuarios = [john_doe]

dest = {}
def crear_usuario():
    username = input(f"Por favor ingrese su nombre de usuario:\n")
    password = input(f"Por favor ingrese su contraseña:\n")
    edad = int(input(f"Por favor ingrese su edad:\n"))
    usuario_nuevo = {"username":str(username), "password":str(password), "edad":edad}
    usuarios.append(usuario_nuevo)
    print(f"se agregó a {usuario_nuevo['username']} exitosamente")

    print("Estas son las edades y contraseñas de nuestros usuarios(?)")
    for user in usuarios:
        print(f"Edad: {user['edad']} y contraseña: {user['password']}")
        time.sleep(5)
    print("Se han impreso todos los usuarios. Escriba 'salir' para terminar el proceso.")

    #Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe
    if(input()=='salir'):
        print("Ha salido")
        print("Lleve más datos para el camino:")
        #imprimir en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’.
        print(usuarios)
    else:
        print("Lo siento mucho, le toca otro loop")
        crear_usuario()
crear_usuario()



    #print(f"nuestros usuarios:")
    #for user in usuarios.values(): 
    #    print(user['username'])
    #nada de esto funciona


    #for user in usuarios_temp["username"]:
    #    print(user)

    #username = input(f"Por favor ingrese su nombre de usuario:\n")
    #password = input(f"Por favor ingrese su contraseña:\n")
    #edad = int(input(f"Por favor ingrese su edad:\n"))
    #usuario_nuevo = {"username":str(username), "password":str(password), "edad":int(edad)}