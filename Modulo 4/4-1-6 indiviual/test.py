from main import *


usuarios.append(Administrador('admin1', 'María González', '87654321', 'maria_01@hotmail.com', 15, 'P@ssw0rd!', '+56912345678', nivel=1))
usuarios.append(Administrador('admin2', 'Hugo Sánchez', '13579086', 'hugo_02@hotmail.com', 15, 'MyP@ssword1', '+56945678901', nivel=1))
usuarios.append(Administrador('admin3', 'Ana Vega', '39586472', 'ana_2022@hotmail.com', 18, 'P4ssword!', '+56978901234', nivel=1))
usuarios.append(Superadmin('super1', 'Jorge Hernández', '24681357', 'jorge_2023@hotmail.com', 22,'1qaz@WSX', '+56990123456', nivel=0))
usuarios.append(Superadmin('super2', 'Diego Castro', '12345678', 'diego_23@hotmail.com', 50,'Pwd!4567', '+56911223344', nivel=0))
usuarios.append(Superadmin('super3', 'Carla Rodríguez', '76543219', 'carla_24@hotmail.com', 33,'Pwd$1234', '+56922334455', nivel=0))
usuarios.append(Administrador('admin4', 'Miguel Flores', '21436587', 'miguel_04@hotmail.com', 1,'s3cr3tPwd', '+56933445566', nivel=1))
usuarios.append(Administrador('admin5', 'Renata Díaz', '96387421', 'renata_05@hotmail.com', 99,'P@ssw0rd!', '+56944556677', nivel=1))
usuarios.append(Superadmin('super4', 'Gonzalo Pérez', '15935728', 'gonzalo_27@hotmail.com', 81,'1q2w3e4R', '+56955667788', nivel=0))
usuarios.append(Administrador('admin6', 'Lucas Ramírez', '82734169', 'lucas_06@hotmail.com', 35, 'Pwd$5678', '+56966778899', nivel=1))
usuarios.append(Cuenta_de_usuario('user1', 'Juan González', '12345678', 'juangonzalez_user@hotmail.com', 55,'P4ssword!', '+56912345678', nivel=2))
usuarios.append(Cuenta_de_usuario('user4', 'Sofía Sánchez', '24681357', 'sofia_user_01@hotmail.com', 89,'MyP@ssword1', '+56945678901', nivel=2))
usuarios.append(Cuenta_de_usuario('user7', 'José Vega', '64285739', 'jose_boss2022@hotmail.com', 56,'P4ssword!', '+56978901234', nivel=2))
usuarios.append(Cuenta_de_usuario('user9', 'Camila Hernández', '21436587', 'camila_user2023@hotmail.com', 34,'1qaz@WSX', '+56990123456', nivel=2))
usuarios.append(Cuenta_de_usuario('user11', 'Pedro Castro', '46973216', 'pedro_user_23@hotmail.com', 11, 'Pwd!4567', '+56911223344', nivel=2))
usuarios.append(Cuenta_de_usuario('user12', 'Lucía Rodríguez', '38904127', 'lucia_user_24@hotmail.com', 58,'Pwd$1234', '+56922334455', nivel=2))
usuarios.append(Cuenta_de_usuario('user13', 'Manuel Flores', '76549231', 'manuel_user_25@hotmail.com', 55,'s3cr3tPwd', '+56933445566', nivel=2))
usuarios.append(Cuenta_de_usuario('user14', 'Florencia Díaz', '89462137', 'florencia_user_26@hotmail.com', 34,'P@ssw0rd!', '+56944556677', nivel=2))
usuarios.append(Cuenta_de_usuario('user15', 'Carlos Pérez', '35291764', 'carlos_user_27@hotmail.com', 23,'1q2w3e4R', '+56955667788', nivel=2))
usuarios.append(Cuenta_de_usuario('user16', 'Laura Ramírez', '24978136', 'laura_user_28@hotmail.com', 28,'Pwd$5678', '+56966778899', nivel=2))
#TESTS=================================================

#escribir_a_csv(usuarios) <- ta weno, pero no es lo que pidieron. Quiero usar esto para otras tareas.
escribir_a_csv_sinimport(usuarios)

def leer_a_csv():
    #with open(r'c:\temp\usuarios.csv', 'r') as file:
    with open(r'c:\temp\usuarios2.csv', 'r') as file:
     csv_reader = csv.reader(file, delimiter=';')
     for row in csv_reader:
        #le estoy pasando esto al archivo:
        #cabecera = ["nombre", "username", "id", "edad", "telefono", "password en texto plano"]     
        #apuntar a TELEFONO y EDAD
        #print(row[0])
        print(f"Telefono y edad de usuario {row[1]} son: {row[4]} y {row[3]} respectivamente")
     #notablemente, no pude hacer este print (de acceder a lso items del row de esta forma si no usando la lista entera
     # hasta que puse delimitador semicolon. Sin delimitador asume coma y me tiraba index error.)
     #porque era en efecto asi una lista, pero de 1 columna.

leer_a_csv()
#En un script diferente será posible acceder al archivo y verificar la información de teléfono y edad.
"""
Así mismo se solicita contar con un registro de los usuarios de tu aplicación. Este registro debe contar
con información del nombre, nombre de usuario, un identificador y la contraseña. Este registro debe ser
serializado. Identifiquen la forma de desarrollarlo.
En un script diferente, acceda a los diferentes datos registrados.
Guarde información de 10 colaboradores y 10 usuarios.
"""
#test_user.ticket()
#test_user.logoff()
#test_user.login()
#primer_admin.modificar_usuario()
#print("prueba de funcionalidad de creación de cuentas por parte de invitado")
#primer_superadmin.modificar_usuario()

#new_invitado = Invitado()
#new_invitado.crear_cuenta()