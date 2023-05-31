# HULE: Un Lenguaje Estadistico

Este es un lenguaje estadistico escrito en Python usando PLY.
<br>
En `hule_lexer.py` se encuentran los tokens y las palabras reservadas usadas en el lenguaje.
<br>
En `hule_parser.py` se encuentran las reglas gramaticales así como las acciones semanticas.
<br>
Se genera el directorio de funciones con su tabla de variables correspondiente, ademas de la tabla de constantes.
<br>
Se generan cuadruplos de operaciones aritmeticas y booleanas, condiciones y ciclos.
<br>
Tambien se generan los cuadruplos correspondientes a las funciones y el retorno.
<br>
Se genera el mapa de memoria virtual con los alcances correspondientes.
<br>
La maquina virtual ejecuta los cuadruplos y modifica la memoria necesaria.
<br>
<br>
Se requiere installar plotext con `pip install plotext`
Para ejecutarlo solo se debe correr `python3 hule_parser.py`