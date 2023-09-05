# ATTENDENCE TRACKER - razonamiento detrás de las decisiones

Contenido:
1. Análisis del problema
2. Proceso
3. Pruebas
4. Estructura del código

Análisis del problema
---------------------
1.1. Objetivo: Esta aplicación tiene como objetivo detectar a los estudiantes que más asisten a clases.

1.2. Entradas: Como ENTRADA, se le carga un archivo .txt introduciendo su nombre en un argumento el ejecutar la aplicación principal así:
python attendance_tracker.py input.txt

1.3. Salidas: Como SALIDA, el programa muestr en consola una lista de estudiantes con el total de minutos asistidos y los días de la semana que asistió.

Proceso:
----------------------
2.1. Preparación de los datos

2.1.a. Diccionario (tabla hash) de estudiantes: para crear, actualizar y acceder a los estudiantes en tiempo lineal "O(1)" se elige una tabla de hash que tiene como llaves los nombres de los estudiantes (que para fines de este problema, cada nombre pertenece solo a un estudiante), y como valor la instancia correspondinte del a clase estudiante  

2.1.b. Clase estudiantes: Se modela a los estudiantes en una clase Estudiante (ver el módulo models.py), que tiene como propiedades el nombre del estudiante, el total de minutos asistidos, y el conjunto de los días de la semana que ha asistido. Para instanciar la clase, el constructor toma el nombre del estudiante, inicializa el contador de minutos en cero, y asigna, a la propiedad días, un conjunto vacío.

2.1.c. Las instrucciones: El archivo de instruciones se separa (por saltos de línea) en lineas de commandos (Student o Presence). Se recorre la lista de comandos, y cada comando se clasifica, en tiempo de ejecición, según el tipo de instrcucción (Student o Presence). Al recibir el comando Student, el programa agregrega al diccionario de estudiantes una llave correspondiente al nombre del estudiante y como valor le asigna una instancia de la clase Estudiantes. Este objeto resultante contiene las propiedades: nombre, minutos, y días. (Para el cálculo de los minutos se importa la función add_time de utilities.py)

2.1.d. Orden y filtro: Del diccionario resultante, se crea una lista ordenada por el estudiante con mayor asistencia (mayor a menor), se sacan los resultados por conasola, siendo previamante filtrados para mostrar solo los estudiantes con asistencias mayores a 5 minutos.

Pruebas:
--------------------
Para el desarrollo de las utilidades (utilities.py) se planteó TDD. Haciendo pruebas unitarias con pytest. para ello se creó el módulo test_.py


Estructura del código:
-----------------------
El código, que es de pequeño tamaño (acorde al tamaño del problema) sigue las indicaciones de mostrar distintas facetas de la programación, está estructurado por módulos, y tiene una combinación de programación funcional y progrmación orientada a objetos:

Aunque como se mencionó antes, el problema a la mano es reducido, con el fin de facilitar el crecimiento de la aplicación, ésta se divide en módulos. Consta de los módulos models.py, test_.py, utilities.py, y la aplicación principal está en attendance_tracker.py. También, hay módulos necesarios para las pruebas en env\Lib. En el módulo models, se pueden modelar posibles clases, como la clase Student. En el módullo test_.py se encuentra la posibilidad de hacer pruebas unitarias. En el módulo utilities.py se pueden ubicar funciones auxiliares, como en este caso, add_time(). Adicionalmente, los módulos pertienecientes a las dependencias se ubican en su adecuado espacio dentro del entorno virtual. 

La aplicación consta de unas pocas funciones. Se encapsula la función add_time() dentro del módulo utilidadades.py. Esta función recibe dos entradas de cadenas de texto y devuelve un entero igual al total de minutos de permanencia del estudiante en el aula. Las otras funciones (aparte de las funciones incluidas en Python), se incluyen en la función main().

Por el mencionado tamaño de la aplicación se decidió utilizar solo una clase. La clase Student, contenida en el módulo models.py. Ésta consta de un constructor, que recibe el parametro name y 3 propiedades necesarias para dar con la solución del problema. Al registrar un estuiante nuevo, se crea un objeto de calse Student con el nombre del estudiante como argumento, el numero de minutos en cero y un conjunto vacío de días de la samana (de presencia en clase).

Así, a pesar de que se trata de un problema pequeño, se usa una variedad de formas de programar para demostrar su uso.

IMPORTANTE
------------
Prerequisito: para poder correr las pruebas unitarias, se debe instalar pytest en el entorno virtual del proyecto. Ver el archivo requirements.txt.