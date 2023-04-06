#asignar mensaje a una variable
#el mensaje debe incluir al nombre de todos los integrantes de equipo

nom_1 = input("inserte un nombre: ").upper()
nom_2 = input("inserte otro nombre: ").upper()
nom_3 = input("inserte el último nombre: ").upper()

def funcion(x, y, z):
    return f"Hola somos {x} {y} y {z} queremos que sea viernes"



#elaborar una lista con cada plabra del string
mensaje = funcion(nom_1, nom_2, nom_3).upper()

lista = mensaje.split(" ")


#reconocer en que indice de la lista esta cada nombre


indice_r=(lista.index(nom_1))
indice_f=(lista.index(nom_2))
indice_c=(lista.index(nom_3))
print(f"{nom_1} está en el índice {indice_r}")
print(f"{nom_2} está en el índice {indice_f}")
print(f"{nom_3} está en el índice {indice_c}")



#indicar cuantas letras tiene el string
print(f"{nom_1} tiene {len(nom_1)} letras")
print(f"{nom_2} tiene {len(nom_2)} letras")
print(f"{nom_3} tiene {len(nom_3)} letras")


#imprimir una tupla con todas las letras del string
tupla= (nom_1[0],nom_1[1],nom_1[2],nom_1[3],nom_1[4],nom_1[5],nom_1[6])
print(tupla)

#obtener el mesaje por teclado
mensaje_2 = (input(f"Porfavor ingrese un mensaje: "))
print(mensaje_2)
























