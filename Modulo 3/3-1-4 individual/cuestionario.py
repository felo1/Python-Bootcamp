import random
import time
#es una lista q tiene un key y una tupla, para referenciar a la lista de forms o el contador lo hago con
#usuarios[usuario_elegido][x]
usuarios = {"Felipe": ([], 0), "Juan": ([], 0), "Marcelo": ([], 0), "Angelo": ([], 0), "Patricio": ([], 0), "Patricia": ([], 0), "Panchito": ([], 0)}
#mismos cuestionarios
formus = ["formulario de hábitos alimenticios", "formulario de empleabilidad", "formulario de experiencia laboral", 
         "formulario de actividades recreativas", "formulario de deportes", "formulario de atletismo",
          "formulario de natación"]
full_send= False
usuarios_spammeados = []
while(full_send==False):
    #randomizar usuario y form
    formulario_elegido = random.choice(formus)
    usuario_elegido = random.choice(list(usuarios.keys()))
    contador_usuario = usuarios[usuario_elegido][1]
    #max forms por persona son 5
    #me aseguro de no repetirle el formulario
    if formulario_elegido not in usuarios[usuario_elegido][0] and contador_usuario < 5:
        #guardar le nombre de form que respondera cada persona y cantidad de forms.
        usuarios[usuario_elegido][0].append(formulario_elegido)
        print(f"Se agregó {formulario_elegido} a {usuario_elegido}")
        #por concepto de "formulario enviado", con esta línea se simula que se despachó un correo de acuerdo al criterio determinado
        if usuario_elegido not in usuarios_spammeados:
            #llevar nota de los usuarios que recibieron form al menos una vez
            usuarios_spammeados.append(usuario_elegido)
        contador_usuario += 1
        time.sleep(3) #la funcion considera que por defecto trabaja segundos de esta forma. 3 segundos como buffer
    #7 personas responderan, x random
    if len(usuarios_spammeados)>=7:
        full_send = True
print(f"Espameamos a {usuarios_spammeados}")
print("================================")
#programar un mensaje q indique el n! de cuest a responder p persona y cuales son.
print("Los usuarios recibieron los siguientes formularios")
#me ENCANTAN estas dos líneas pero no las entiendo :v (gracias stackoverflow)
for usuario, (formularios, _) in usuarios.items():
    print(f"{usuario}: recibió {len(formularios)} formularios: {formularios}")
        

