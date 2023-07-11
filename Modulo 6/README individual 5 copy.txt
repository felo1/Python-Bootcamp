Aplicación básica de testeo de funcionalidades de django base:
En vista login, podemos utilizar funcionalidad de autenticacion, y subsecuentemente
ser redirigidos a una página de bienvenida si la autenticación es exitosa, de lo contrario
seremos devueltos al login advirtiendo el error.
En vista forms, podemos registrar por fuera de la adminsitración a usuarios nuevos
En vista users, podemos listar los usuarios registrados en la base de datos.

Restricciones
-Se incluyeron dos restricciones, según lo solicitado:
-La interfaz de las vistas logout, welcome, no son accesibles pero aparecerán 
a usuarios normales logueados
-Los botones de registro y listar usuarios son solo accesibles por Administradores
(requiere que exista en la Base de datos un grupo con ese nombre exacto y que el
usuario logueado pertenezca a él)