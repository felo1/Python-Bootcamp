""" Diseñe 7 diccionarios, donde el nombre de cada diccionario es el nombre de un usuario de su
aplicación.
En cada diccionario, integre características como: edad, género y otras características particulares de
su aplicación.
Por ejemplo, si la aplicación se enfoca en Juntas de Vecinos integrar dirección y número telefónico.
Integre al menos cinco características.
Guarde estos diccionarios en una lista. En el caso de ejemplo, podría ser nombrada “JJVV”.
A continuación, recorra su lista e imprima toda la información que posee la estructura de datos sobre
cada usuario (en el caso de ejemplo: de cada junta de vecinos).
¿Qué problemas encontró con esta forma de almacenar la información?
Vuelva al inicio del problema y diseñe una estructura de datos unificada que permita almacenar todas
las juntas de vecinos.
Agregue para cada usuario los campos nombre_usuario, id_unico, antigüedad, fecha de incorporación.
Imprima en pantalla la fecha de incorporación de todos los usuarios. """

Ignacio = {"nombre": "Ignacio", "edad":5,"género":"masculino", "dirección": "Agua Santa SN", "teléfono": 1234, "correo": "ignacio@ejemplo.tk", "ocupación": "estudiante", "nombre_usuario": "ignacio01", "id_unico": 1, "antiguedad": 2, "fecha_de_incorporacion": "2022-01-15"}
Alberta = {"nombre":"Alberta", "edad":17,"género":"femenino", "dirección": "Calle 12 #45", "teléfono": 5678, "correo": "alberta@ejemplo.tk", "ocupación": "estudiante", "nombre_usuario": "alberta02", "id_unico": 2, "antiguedad": 1, "fecha_de_incorporacion": "2021-12-01"}
Jeanne = {"nombre":"Jeanne", "edad":30,"género":"no menciona", "dirección": "Avenida del Sol #123", "teléfono": 9012, "correo": "jeanne@ejemplo.tk", "ocupación": "profesora", "nombre_usuario": "jeanne03", "id_unico": 3, "antiguedad": 3, "fecha_de_incorporacion": "2020-09-15"}
Panchito = {"nombre":"Panchito","edad": 12, "género": "masculino", "dirección": "Calle 9 #67", "teléfono": 3456, "correo": "panchito@ejemplo.tk", "ocupación": "estudiante", "nombre_usuario": "panchito04", "id_unico": 4, "antiguedad": 1, "fecha_de_incorporacion": "2021-12-01"}
Panchita = {"nombre":"Panchita","edad": 25, "género": "femenino", "dirección": "Calle 20 #56", "teléfono": 7890, "correo": "panchita@ejemplo.tk", "ocupación": "enfermera", "nombre_usuario": "panchita05", "id_unico": 5, "antiguedad": 2, "fecha_de_incorporacion": "2022-06-30"}
Antonio = {"nombre":"Antonio","edad": 42, "género": "masculino", "dirección": "Avenida Principal #789", "teléfono": 2345, "correo": "antonio@ejemplo.tk", "ocupación": "abogado", "nombre_usuario": "antonio06", "id_unico": 6, "antiguedad": 4, "fecha_de_incorporacion": "2019-03-01"}
Benja = {"nombre":"Benja","edad": 50, "género": "no menciona", "dirección": "Calle Norte #234", "teléfono": 6789, "correo": "benja@ejemplo.tk", "ocupación": "jubilado", "nombre_usuario": "benja07", "id_unico": 7, "antiguedad": 5, "fecha_de_incorporacion": "2019-03-01"}


JJVV_vina = [Ignacio, Alberta, Jeanne, Panchito, Panchita, Antonio, Benja]
JJVV_stgo = [Ignacio, Alberta, Jeanne, Panchito, Panchita, Antonio, Benja]
JJVV_ata = [Ignacio, Alberta, Jeanne, Panchito, Panchita, Antonio, Benja]
JJVV_puren = [Ignacio, Alberta, Jeanne, Panchito, Panchita, Antonio, Benja]
juntas_de_vecinos = [JJVV_vina, JJVV_stgo, JJVV_ata, JJVV_puren]

#for usuario in JJVV:
#    print(f"Los datos del usuario {usuario['nombre']} son: {usuario['edad']}, {usuario['género']}, \
#{usuario['dirección']}, {usuario['teléfono']}, {usuario['correo']}, {usuario['ocupación']}, \
#{usuario['nombre_usuario']}, {usuario['id_unico']}, {usuario['antiguedad']}, {usuario['fecha_de_incorporacion']} ")

#A continuación, recorra su lista e imprima toda la información que posee la estructura de datos sobre
for junta in juntas_de_vecinos:
    for usuario in junta:
        print(f"Imprimiendo datos sensibles de {usuario['nombre']}: {usuario}")
        print("\n")
print("\n fin del infodump...")
#Imprima en pantalla la fecha de incorporación de todos los usuarios. """
print("Listando fechas de incorporación de usuarios, por junta")
for junta in juntas_de_vecinos:
    for usuario in junta:
        print(usuario["fecha_de_incorporacion"])
    print("\n")


#nos mostraron list comprehension
#ej: dict = {"newkey": "new value" for item in new_dict } para insertar valores en diccionario iterativamente.

#ej list_comprehension = [x for x in lista]
#ej dicci = {cliente:random.randint(1,100) for cliente in clientes} usó por ej acá una lista clientes = ["juan","pepo","pepe"]
#    print(dicci) -> y con eso le inserta a los clientes valores random entre 1 y 100. Quedó con {"juan":100, "pepo":50, etcetc}

#cuidado con dejar whitespace en prints seccionados como este, porque te lo imprime      
#me sugieren hacerlo con este estilo por dinamismo
   # print(f"user {usuario['nombre']}': {', '.join([f'{k}={v}'  for k,v in usuario.items() if k!='nombre'     ])}")
#como imprimir valores de un dict pero con rango especifico, en este caso de el key 1 hasta el final, smort.
#values_to_print = list(my_dict.values())[1:]
#for user in JJVV:
#    data = ", ".join(user.values())
#    print(f"Los datos del usuario son: {data}")
    
    #print(f"{usuario}: recibió {len(formularios)} formularios: {formularios}")

