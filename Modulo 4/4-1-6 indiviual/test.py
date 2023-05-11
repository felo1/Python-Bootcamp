from main import *
#TESTS=================================================

test_user = Usuario("test", "test@", "1234asdASD***")
primer_superadmin = Superadmin("mainAdmin", "test", 1234, 0)
primer_admin = Administrador("any", "aany@", 1234, 1)
usuarios.append(primer_admin), usuarios.append(test_user), usuarios.append(primer_superadmin)
escribir_a_csv([primer_admin, test_user, primer_superadmin])
#test_user.ticket()
#test_user.logoff()
#test_user.login()
#primer_admin.modificar_usuario()
#print("prueba de funcionalidad de creación de cuentas por parte de invitado")
#primer_superadmin.modificar_usuario()

#new_invitado = Invitado()
#new_invitado.crear_cuenta()

