#Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
usuarios = "Felipe, Antonio, Giogio, THENSA, User, Mamá, Test"
#Convierte tu string en una lista, en la cual cada elemento es un usuario.
lista = usuarios.lower().split(", ")

print("Tenemos " + str(len(lista)) + " usuarios")
print("Los usuarios son:\n")
for user in lista:
    print(user)

print("================")
user = input("Su nombre de usuario:\n").lower()
if user in lista:
    print("login exitoso")
else:
    print("No te encontré")
"""
¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente su nombre? ¿Cómo solucionarías este problema? 

● Imprimer en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes
utilizar para realizar esto?
- Lo hice con un for loop iterando por mi lista con un for/in, y luego con un mensaje referenciando al iterador.
● Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
● Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce
● Ahora piensa en tres de ellos. Buscalos en la lista con el método adecuado.
● ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa
manualmente su nombre? ¿Cómo solucionarías este problema?
- Se podría encontrar con problemas de mayus vs minusculas, o escribiendo mal su propio nombre. Lo resolvería internamente reduciendo los nombres a minusculas, eliminando espacios y carácteres especiales (a menos que 
estemos hablando de nombres de usuario, en cuyo caso eliminaría caracteres especiales salvo los necesarios)  
● Imprime en pantalla la cantidad usuarios que tiene tu aplicación.
● Imprimer en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes utilizar para realizar esto?
"""