
import time
import os

password_completo = []
print("Bienvenido.\nPor favor, ingrese su contraseña")


while(True):
    errores = []
    print("\nAsegúrese de incluír al menos 8 caracteres, con mayúsculas, minúsculas y cifras"
    "\nIngrese su contraseña un carácter a la vez, carácteres en exceso se descartarán:")
    password = ""
    password = input(f"ingrese un caracter: {''.join(password_completo)}")
    if(password!=""):
        password_completo.append(password[0])
    if(len(password_completo) < 8):
        errores.append("Su contraseña debe contener al menos 8 caractéres")
    if not any(caracter.islower() for caracter in password_completo):
        errores.append("Su contraseña debe contener al menos un caractér en minúsculas")
    if not any(caracter.isupper() for caracter in password_completo):
        errores.append("Su contraseña debe contener al menos un caractér en mayúscula")
    if not any(caracter.isdigit() for caracter in password_completo):
        errores.append("Su contraseña debe contener al menos un caractér numérico")

    if len(errores) > 0:
        print("\nSu contraseña no cumple con nuestros criterios, favor revisar lo siguiente:\n")
        for error in errores:
            print(error)
        input("presiona una tecla para continuar\n")
        os.system("cls")
    else:
        print("Gracias por crear su cuenta")   
        break


"""
ingresen la contraseña de a 1 caracter, no usar splits y eso. rodrigo recomendo no sobre-complicarse con esto

mientras el input no llegue a 8


"""

