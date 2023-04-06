"""
usuarios = [
    ["Eduardo", "LATAM", 30, 0, "deportes"],
    ["Ignacio", "LATAM", 18, 0, "natación"],
    ["Anthony", "USA", 40, 0, "autos"],
    ["Jeff", "CND", 60, 0, "computacion"],
    ["MACRON", "FR", 50, 0, "nada"]
]
"""
user = ["", "", "", "", ""]

nombre = input(f"ingrese su nombre:\n")
locale = input(f"ingrese su zona, ej: LATAM, USA, CND:\n")
edad = int(input(f"ingrese su edad , ej: 18, 35:\n"))
intereses = input(f"ingrese sus afinidad por los deportes, ej deportes, natación, nada:\n")
contador = user[3] = 0

print(f"Gracias por colabiración, estimad@ {nombre:}\n")   
print("vendiendo sus datos al mejor postor, espere por favor...\n")
# habitos
if locale == "LATAM" and contador < 3:
    print("recibirá el formulario de hábitos alimenticios")
    contador += 1
# empleabilidad
if 18 <= edad <= 29 and contador < 3:
    print("recibirá el formulario de empleabilidad")
    contador += 1
# experiencia
if 30 <= edad <= 59 and locale == "LATAM":
    print("recibirá el formulario de experiencia laboral")
    contador += 1
# recreativas
if edad >= 60 and contador < 3:
    print("recibirá el formulario de actividades recreativas")
    contador += 1
# deportes, menores de 60
if intereses == "deportes" and contador < 3 and edad < 60:
    print("recibirá el formulario de deportes")
    contador += 1
# atletismo: deportistas menores de 60
if intereses == "deportes" and contador < 3 and edad < 60:
    print("recibirá el formulario de atletismo")
    contador += 1
# natación: LATAMs deportistas menores de 60
if intereses == "deportes" and contador < 3 and edad < 60 and locale == "LATAM":
    print("recibirá el formulario de natación")
    contador += 1
# notDeportes
if intereses != "deportes":
    print("vas a recibir un formulario de deportes y te va a gustar")
    contador += 1

print("fin del main")
