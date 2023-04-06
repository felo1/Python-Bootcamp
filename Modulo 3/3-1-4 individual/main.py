def audit_contraseña(password):
    def largo(password):
        return len(password) >= 8
        
    def es_mayuscula(password):
        return any(caracter.isupper() for caracter in password)
    
    def es_minuscula(password):
        return any(caracter.islower() for caracter in password)
        
    def tiene_digito(password):
        return any(caracter.isdigit() for caracter in password)
    
    criterios = [largo, es_mayuscula, tiene_digito, es_minuscula]

    errores = []
    for criterio in criterios:
        if not criterio(password):
            errores.append(criterio.__name__)
            return False
    return True

password = input("Bienvenido.\nPor favor, ingrese su contraseña."
                 "\nAsegúrese de incluír al menos 8 caracteres, con mayúsculas, minúsculas y cifras \n")
resultado = audit_contraseña(password)
if resultado:
    print("Gracias por crear su cuenta")
else:
    print("Contraseña no cumple con los requisitos:\n")
    print("The following criteria were not met: ", ", ".join(resultado))
