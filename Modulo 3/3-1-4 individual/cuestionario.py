import random

#es una lista q tiene un key y una tupla, para referenciar a la lista de forms o el contador lo hago con
#usuarios[usuario_elegido][x]
usuarios = {"Felipe": ([], 0), "Juan": ([], 0), "Marcelo": ([], 0), "Angelo": ([], 0), "Patricio": ([], 0), "Patricia": ([], 0), "Panchito": ([], 0)}
formus = ["formulario de hábitos alimenticios", "formulario de empleabilidad", "formulario de experiencia laboral", 
         "formulario de actividades recreativas", "formulario de deportes", "formulario de atletismo",
          "formulario de natación"]
#me funcionaba sin la idea de la tupla dentro de la lista, veré alternativas mñn.
full_send= False
while(full_send==False):
    def enviar():
        formulario_elegido = random.choice(formus)
        contador_usuario = usuarios[usuario_elegido][1]
        usuario_elegido = random.choice(list(usuarios.keys()))
        if formulario_elegido not in usuarios[usuario_elegido][0] and contador_usuario < 5:
            usuarios[usuario_elegido][0].append(formulario_elegido)
            print(f"Se agregó {formulario_elegido} a {usuario_elegido}")
    break
enviar()
#7 personas responderan, x random
#mismos cuestionarios
#requisitos:
#random, uno tras otro con desfase de 3 segundos
#max forms por persona son 5
#guardar le nombre de form que respondera cada persona
#programar un mensaje q indique el n! de cuest a responder p persona y cuales son.
""" 
7 iteraciones (7 personas)
check para que nadie reciba mas de 5
asi q hace iteraciones hasta que se webee a 7 personas, pero q nunca se le manden mas de 5
guardar por persona cuales son los forms que respondera
y ese dato almacenado servira para imprimir cuantos forms tiene y cuales StopIteration

hasta que 7 personas
        if not ya recibio 5
            enviar formulario random de (lista de forms)
            tomar nota de ese despacho para esa persona en particualr, en un arreglo?
            esperar 3 segundos
            seguir webiando """