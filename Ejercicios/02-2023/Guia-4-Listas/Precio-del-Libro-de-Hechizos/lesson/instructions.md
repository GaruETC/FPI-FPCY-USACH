![logo](./assets/logo_usach.png)

# Precio del Libro de Hechizos

El libro de hechizos de un mago es una de sus herramientas más importantes, pues debe estudiar sus conjuros diarios desde él. En su libro anota los hechizos que ha aprendido e investigado, además, para poder acceder a ellos más adelante. Sin embargo, no necesita ser su propio libro, puede estudiar desde los libros de otros, o comprar libros pre-llenados, los que tienen un precio que depende de cuántos hechizos contiene y de qué rango son estos.

Los hechizos tienen rangos de 0 a 9 y el precio del libro aumenta por cada uno según la tabla 1.

*Tabla 1: Precio en piezas de oro por cada hechizo en un libro*
| Rango | Precio |
|-------|--------|
| 0     | 5      |
| 1     | 10     |
| 2     | 40     |
| 3     | 90     |
| 4     | 160    |
| 5     | 250    |
| 6     | 360    |
| 7     | 490    |
| 8     | 640    |
| 9     | 810    |


Estos valores se han dado en una lista. Sabiendo que el precio base de un libro de hechizos es 15 piezas de oro (po), escriba un programa que calcule cuál es el valor de un libro de hechizos según la cantidad de hechizos que tenga de cada rango.

## Entradas

La entrada será una secuencia de números enteros separados por coma o coma y espacio. Cada valor en la secuencia será la cantidad de hechizos de ese rango, partiendo por 0:
```
<hechizos de rango 0>, <hechizos de rango 1>, <hechizos de rango 2>,..., <hechizos de rango n>
```

El usuario ingresará la secuencia en una única entrada y solo hasta el rango máximo de hechizos disponibles en el libro. Por ejemplo, para la entrada:
```
5,8,1,0,3
```
hay cinco hechizos de rango 0, ocho de rango 1, uno de rango 2, ninguno de rango 3 y tres de rango 4, el más alto disponible en este libro. Por otro lado, para la entrada
```
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
```
hay un hechizo de cada rango, de 0 a 9.

## Salida

La salida corresponde al precio total del libro, entregado a través de un mensaje:
```
El libro tiene un costo de <valor> po.
```

## Consideraciones
- Note que la entrada no requiere especificar que hay cero hechizo de rango más alto que el más alto disponible. En otras palabras, si hay *n* elementos en la entrada, el rango más alto de hechizos será *n*-1.
- La cantidad mínima de elementos de la secuencia de entrada siempre será 1 y la máxima, 10.
- Al transformar un *string* a número, los espacios en blanco son irrelevantes para Python. Es decir, al transformar el string `" 1 "` a entero, el resultado será el mismo que para `"   1"`, `"1  "`, `"1"`, etc.

## Ejemplos

### Ejemplo 1
Entrada:
```
5,8,1,0,3
```

Salida:
```
El libro tiene un costo de 640 po.
```

### Ejemplo 2
Entrada:
```
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
```

Salida:
```
El libro tiene un costo de 2870 po.
```
