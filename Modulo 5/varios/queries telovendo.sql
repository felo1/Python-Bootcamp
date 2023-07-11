-- G. Seleccione los vendedores que tienen un salario superior al promedio.
SELECT * FROM empleados WHERE sueldo > (SELECT AVG(sueldo) AS Promedio_Sueldo FROM empleados);

-- H. Seleccione los productos más caros que el promedio.
SELECT * FROM productos WHERE precio > (SELECT AVG(precio) AS Promedio_Precio FROM productos);

-- I. Seleccione los clientes que han pagado más que el promedio.
SELECT * FROM usuarios WHERE total_comprado > (SELECT AVG(total_comprado) FROM usuarios);

-- J. Indique cuántos vendedores tienen un salario inferior al promedio.
SELECT * FROM empleados WHERE sueldo < (SELECT AVG(sueldo) FROM empleados);

-- K. Indique cuántos productos son más baratos que el promedio.
SELECT * FROM productos WHERE precio < (SELECT AVG(precio) FROM productos);

-- L. Seleccione el nombre y el apellido de los vendedores que tienen un salario superior al promedio.
SELECT nombre, apellido FROM empleados WHERE sueldo > (SELECT AVG(sueldo) FROM empleados);

-- M. Indique cuál es el producto más barato y el producto más caro del inventario.
-- N. Indique cual es el costo de comprar uno de cada producto en el inventario.
-- O. Identifique la comuna que tiene más clientes registrados.
-- P. Identifique los productos que tienen más de 5 unidades en stock.