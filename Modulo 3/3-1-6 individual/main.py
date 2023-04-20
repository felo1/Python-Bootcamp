import time
john_doe = {"username":"John Doe", "password":"segurito", "edad":33}
usuarios = [john_doe]

dest = {}
def crear_usuario():
    while True:
        username = input(f"Por favor ingrese su nombre de usuario:\n").strip()
        if username in usuarios:
            print("El nombre de usuario ingresado está en uso")
            continue
        break
    password = input(f"Por favor ingrese su contraseña:\n").strip()
    edad = abs(int(input(f"Por favor ingrese su edad:\n")))
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