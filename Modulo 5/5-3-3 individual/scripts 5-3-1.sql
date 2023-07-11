-- Inserte 3 cursos nuevos.
INSERT INTO 512individual.capacitacion (codigo_curso, nombre, horario, costo_realizacion, fecha_realizacion)
VALUES
(11, 'Curso de Programación', 'Lunes a Viernes 9:00 AM - 12:00 PM', 150.00, '2023-06-10'),
(12, 'Taller de Diseño Gráfico', 'Martes y Jueves 6:00 PM - 8:00 PM', 75.00, '2023-06-15'),
(13, 'Seminario de Marketing Digital', 'Sábado 10:00 AM - 4:00 PM', 100.00, '2023-06-22');

-- Inserte 3 profesores nuevos
INSERT INTO 512individual.operadores
(RUN, nombre, apellido, direccion, correo_electronico, fecha_creacion)
VALUES
('86523947-0', 'Juan', 'González', 'Calle 123', 'juangonzalez@hotmail.com', '2023-05-23'),
('95187642-8', 'María', 'López', 'Avenida 456', 'marialopez@b.com', '2023-05-23'),
('73859460-2', 'Carlos', 'Martínez', 'Carrera 789', 'carlosmartinez@c.com', '2023-05-23');

-- ¿Cuál es el curso más costoso? Selecciónelo.
select max(capacitacion.costo_realizacion) from capacitacion;
-- ¿Cuál es el profesor menos con menor salario? Selecciónelo.
select min(sueldo) from `operadores`;
-- ¿Cuál es el curso más costoso? Selecciónelo.
select max(costo_realizacion) from `capacitacion`;
-- Seleccione los cursos más costosos que el promedio.
SELECT costo_realizacion from capacitacion
where costo_realizacion > (
select avg(costo_realizacion) as promedio from capacitacion
) order by costo_realizacion desc;
-- Cree una tabla con los cursos menos costosos que el promedio. La tabla debe tener por nombre Cursos económicos.
SELECT costo_realizacion, nombre 
from capacitacion as `Cursos Económicos`
where costo_realizacion < (
select avg(costo_realizacion) as promedio from capacitacion
)order by costo_realizacion asc;
-- O se refieren a literalmente crear una tabla? En cuyo caso:

create table `cursos economicos` (
costo_realizacion decimal(10,2),
nombre varchar(50));
insert into `cursos economicos` (costo_realizacion, nombre)
SELECT costo_realizacion, nombre 
from capacitacion as `Cursos Económicos`
where costo_realizacion < (
select avg(costo_realizacion) as promedio from capacitacion
)order by costo_realizacion asc;
-- al parecer, el backquote (`) es una exigencia en mi instalación para el "AS" en ese lugar, quizá por el espacio
/* A la tabla Cursos económicos, agrégale dos campos. ‘Cantidad mínima estudiantes’ y ‘Aportes
públicos’. La cantidad mínima de estudiantes se refiere al número mínimo de estudiantes
necesarios para su realización. Los aportes públicos refieren a los aportes entregados por
instituciones públicas para la realización del curso (tiene que ser un valor menor al costo total del
curso).*/

alter table `cursos economicos`
add column `cantidad mínima estudiantes` int,
add column `aportes públicos` int;

/*floor para dejarlo entero, rand*30 para ampliar el rango de rand de 0 a 30 y 0 a 70, para
quedar cerca de los precios de costo efectivo minimo*/
UPDATE `cursos economicos`
SET `cantidad mínima estudiantes` = FLOOR(RAND() * 30),
    `aportes públicos` = FLOOR(RAND() * 70)
LIMIT 8;

-- Renombre la columna “Costo realización” en la tabla Cursos económicos. El nombre nuevo debe
-- ser: Costo efectivo. En dicha columna, a cada valor se le debe restar el valor de ‘Aportes públicos’.

alter table `cursos economicos`
rename column `costo_realizacion` to `Costo efectivo`;

update `cursos economicos`
set `Costo efectivo` = (`Costo efectivo` - `aportes públicos`)
where `Costo efectivo`>=`aportes públicos`
limit 8; -- en mi caso 8 era el numero de cursos que se migraron
-- favor comentar en el feedback una mejor manera de usar una clausula where acá que
-- no exija desactivar el safe mode

-- Por último, actualice 5 cursos y 3 profesores.
update capacitacion
set fecha_realizacion = CURRENT_DATE
where codigo_curso > 1
limit 5;

update operadores
set fecha_creacion = '2020-01-01'
where nombre is not null
limit 3;
