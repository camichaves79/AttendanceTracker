# ATTENDENCE TRACKER - razonamiento detrás de las decisiones

Contenido:
1. Análisis del problema
2. Proceso
3. Pruebas
4. Estructura del código

Análisis del problema

1.1. Objetivo: Esta aplicación tiene como objetivo detectar a los estudiantes que más asisten a clases.

1.2. Entradas: Como ENTRADA, se le carga un archivo .txt introduciendo su nombre en un argumento el ejecutar la aplicación principal así:
python attendance_tracker.py input.txt

1.3. Salidas: Como SALIDA, el programa muestr en consola una lista de estudiantes con el total de minutos asistidos y los días de la semana que asistió.

Proceso:

2.1. Preparación de los datos

2.1.a. Diccionario (tabla hash) de estudiantes: para crear, actualizar y acceder a los estudiantes en tiempo lineal "O(1)" se elige una tabla de hash que tiene como llaves los nombres de los estudiantes (que para fines de este problema, cada nombre pertenece solo a un estudiante), y como valor la instancia correspondinte del a clase estudiante  

2.1.b. Clase estudiantes: Se modela a los estudiantes en una clase Estudiante (ver el módulo models.py), que tiene como propiedades el nombre del estudiante, el total de minutos asistidos, y el conjunto de los días de la semana que ha asistido. Para instanciar la clase, el constructor toma el nombre del estudiante, inicializa el contador de minutos en cero, y asigna, a la propiedad días, un conjunto vacío.

2.1.c. Las instrucciones: El archivo de instruciones se separa (por saltos de línea) en lineas de commandos (Student o Presence). Se recorre la lista de comandos, y cada comando se clasifica, en tiempo de ejecición, según el tipo de instrcucción (Student o Presence). Al recibir el comando Student, el programa agregrega al diccionario de estudiantes una llave correspondiente al nombre del estudiante y como valor le asigna una instancia de la clase Estudiantes. Este objeto resultante contiene las propiedades: nombre, minutos, y días. (Para el cálculo de los minutos se importa la función add_time de utilities.py)

2.1.d. Orden y filtro: Del diccionario resultante, se crea una lista ordenada por el estudiante con mayor asistencia (mayor a menor), se sacan los resultados por conasola, siendo previamante filtrados para mostrar solo los estudiantes con asistencias mayores a 5 minutos.

Pruebas:
Para el desarrollo de las utilidades (utilities.py) se planteó TDD. Haciendo pruebas unitarias con pytest. para ello se creó el módulo test_.py





IMPORTANTE
Prerequisito: para poder correr las pruebas unitarias, se instala pytest en el entorno virtual del proyecto. Ver el archivo requirements.txt.