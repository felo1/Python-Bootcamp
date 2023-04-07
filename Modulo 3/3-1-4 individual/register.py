

password = input("Bienvenido.\nPor favor, ingrese su contraseña."
                 "\nAsegúrese de incluír al menos 8 caracteres, con mayúsculas, minúsculas y cifras \n")
errores = []
if(len(password) < 8):
    errores.append("Su contraseña debe contener al menos 8 caractéres")
if not any(caracter.islower() for caracter in password):
    errores.append("Su contraseña debe contener al menos un caractér en minúsculas")
if not any(caracter.isupper() for caracter in password):
    errores.append("Su contraseña debe contener al menos un caractér en mayúscula")
if not any(caracter.isdigit() for caracter in password):
    errores.append("Su contraseña debe contener al menos un caractér numérico")

if len(errores) > 0:
    print("Su contraseña no cumple con nuestros criterios, favor revisar:\n")
    print(errores)
else:
    print("Gracias por crear su cuenta")   

"""

"""