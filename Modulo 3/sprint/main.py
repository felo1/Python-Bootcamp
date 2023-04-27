"""
SPRINT DE ENTREGA:
Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos
durante el Módulo 1 de Python básico. Por tanto, se debe poner foco en lo siguiente:
● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
● Por cada cuenta debe pedir un número telefónico para contactarse.

● El programa no terminará de preguntar por los números hasta que todas las organizaciones
tengan un número de contacto asignado.
● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
● Se debe guardar como un string.
A modo de entrega, se debe disponer un documento Word o PDF en el que se indique:
- Ruta del repositorio en GitHub

Consideraciones adicionales
- El código debe estar debidamente indentado
- El formato del documento Word queda a criterio del equipo.
"""
import random
silabario = ['ba', 'be', 'bi', 'bo', 'bu', 'da', 'de', 'di', 'do', 'du', 'ga', 'ge', 'gi', 'go', 'gu',
             'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu',
             'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu', 'ra', 're', 'ri', 'ro', 'ru',
             'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu',
             'za', 'ze', 'zi', 'zo', 'zu']
simbolos = "!#$%&/()=?" #puros iconos accesibles con el teclado LATAM pasando el dedo + shift ljsjs

usuarios = []
#Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
def crear_usuario():
    #exigencias:
    #crear 10 usuarios iterativamente
    #asignar contraseñas
    #cada cuenta en una nueva -variable- (diccionario nuevo?), con su contraseña
    #por cada cuenta, al momento de crear, pedir un teléfono (input tb en la iteracion)
    #justamente piden que el programa no cierre hasta q se indiquen los 10 fonos
    #cada input debe verificarse de tener 8 digitos y solo digitos
    #se guarda como string
    #la contraseña debe generarse y tener los criterios de mayus, mius y numeros random

    for  i in range(10):
        #generador de nombres rudimentario que randomiza SILABAS preinstruidas (definidas más arriba abajo de los import)
        #con una cantidad entre 3 y 6
        n_silabas = random.randint(3, 6)
        nombre_usuario = ''.join(random.sample(silabario, n_silabas)).capitalize()
        
        #La contraseña debe ser creada con random y 
        # debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
        #password compuesto por una concatenacion de 3 cositas:
        password_1_3 = str(nombre_usuario)[0:3] #las 3 primeras letras, la primera siempre capitalizada y otras dos minus
        password_4_7 = str(random.randint(1000,9999)) #para minimo 5 dígitos
        simbolo_random = random.randint(0, len(simbolos) - 1)
        password_8 = simbolos[simbolo_random] #un simbolo random al final
        password = str(password_1_3 + password_4_7 + password_8) #concatena
        #por cada cuenta, al momento de crear, pedir un teléfono (input tb en la iteracion)
        
        #cada input debe verificarse de tener 8 digitos y solo digitos
        #12346578
        while True: #loop chequeo telefono, recordar que while true es un loop infinito por diseño, necesita un break
            telefono = str(input(f"Ingrese el teléfono para el usuario {nombre_usuario}: \n"))
            if telefono.isdigit() == True and len(telefono) >= 8:  #verifica tener solo digitos y largo minimo
                #repite si alguna de las dos condiciones falla.
                break
            else:
                print("teléfono inválido, de 8 carácteres mínimo:\n")
                continue
        telefono = "+569" + telefono #agrega el prefijo de pais, +569
        usuario_nuevo = {"nombre_usuario":nombre_usuario, "password":password, "telefono":telefono}
        usuarios.append(usuario_nuevo)
        print("Usuario creado exitosamente")
    print("Creación de usuarios terminada")

#12345678
crear_usuario()
#Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
#aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
#este print cumple con la función de recorrer la lista
for user in usuarios: print(user)

