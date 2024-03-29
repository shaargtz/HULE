# HULE: Un Lenguaje Estadistico

Este es un lenguaje estadistico escrito en Python usando PLY. El lenguaje tiene componentes básicos como variables, aritmética, ciclos, condicionales, arreglos de una, dos o tres dimensiones, funciones y recursión. Cuenta con funciones especiales para operaciones matemáticas y estadísticas, como lo son la media, la moda, la mediana, generación de números aleatorios, graficación, entre otras.

## ¿Por qué?
Hoy en día existen recursos practicamente ilimitados para aprender programación, y aunque cada vez son más accesibles, el núcleo de todos los lenguajes utilizados sigue siendo el inglés. Claro, no es *necesario* saber inglés, mientras uno pueda hacer la relación meramente lógica entre escribir la palabra *while* y lo que sucederá con el código que le sigue. No obstante, esto pone en una posición de privilegio a las personas que saben inglés, ya sea nativamente o por acceso a distintos niveles educativos. HULE propone, entonces, una manera de combatir el colonialismo que conlleva la confección de código.

## Instalacion
Con clonar el repositorio es suficiente, ya que viene la libreria de PLY integrada.
<br> Se requiere instalar plotext con `pip install plotext`

## Ejecucion
Se debe guardar el codigo `.hule` en este mismo folder. <br>
Para ejecutarlo solo se debe correr `python3 hule.py` y seguir las instrucciones.

## Ejemplos de codigo
Dentro de la carpeta de `/pruebas` se encuentran varios ejemplos que estan listos para ejecutarse.

## Referencia rapida

### Tipos
- ent
- flot
- car
- cadena
- bool

### Declaracion
`var ent a ;`<br>
`var ent B[3] ;`<br>
`var cadena c ;`

### Asignacion
`a = 5 ;`<br>
`B[1] = 8 ;`

### Condiciones
`si ( a < 3 ) { a = a + 1 } ;` <br>
`si ( a < 3 ) { a = a + 2 } sino { a = a - 3 } ;`

### Ciclos
`mientras ( a > 3 ) { a = a - 1 } ;` <br>
`por ( i en B  ) { B[i] = B[i] - i } ;`

### Lectura
`c = lee() ;`

### Escritura
`imprime(c) ;`

### Aritmetica
`B[0] = abs(B[0]) ;`<br>
`B[1] = poder(B[1], 3) ;`

### Estadistica
`a = moda(B) ;`<br>
`imprime(mediana(B)) ;`
