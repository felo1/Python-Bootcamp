""""

#Para inicializar una instalacion de virtual environment primero necesito instalar virtualenv, que esa libreria pip (?)
#con pip install virtualenv 
#luego puedo 
virtualenv -p python3.11 venv3.11 

Donde la opción -p se utiliza para especificar la versión de Python que será la
base de nuestro ambiente virtual. Por otro lado venv3.11 es un nombre
arbitrario que asignamos al directorio que contendrá todos los archivos que

sean parte de éste ambiente virtual.
luego, sin salirme de mi carpeta de proyecto python puedo 
.nombre\Scripts\activate 
o bien entrar en la carpeta venv que hice y luego 
.\scripts\activate

INDENTACION:
es con ctrl+ ?¿
"""

usuario = "felipe"
fname = ""
def restart(fname):
    print(fname)
datos =  input(f"Ingrese los datos, {usuario}: ")
restart(datos)


