usuarios = [    ["Felipe", "1234"],
    ["Antonio", "2"],
    ["Giogio", "2"],
    ["Test", "2"],
    ["NSA", "2"],
    ["user", "2"],
    ["backdoor", "2"]
]

print("Nuestros usuarios")
for user in usuarios:
    print(f"Hola {user[0]}:") #dificil recordar ese formato para f string
    #si le pongo simplemente user como parametro, me imprime todos los datos del usuario incluido la pass, atenti.

print("================")


"""
¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente su nombre? ¿Cómo solucionarías este problema? 
- Se podría encontrar con problemas de mayus vs minusculas, o escribiendo mal su propio nombre. Lo resolvería internamente reduciendo los nombres a minusculas, eliminando espacios y carácteres especiales (a menos que 
estemos hablando de nombres de usuario, en cuyo caso eliminaría caracteres especiales salvo los necesarios)  
● Imprimer en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes
utilizar para realizar esto?
- Lo hice con un for loop iterando por mi lista y saludando a todos con un f string.
"""