![logo](./assets/logo_usach.png)

# Comparando matrices

Se tienen 10 archivos, en cada uno de los cuales hay una matriz de *n*x*m* con números. Se le solicita crear un archivo llamado `"resultado.txt"` que tenga un deglose de comparación de los archivos, indicando cuántos elementos coinciden con los demás archivos. Cada vez que dos matrices tienen el mismo número en la misma posición de la matriz, se concidera una coincidencia. Por ejemplo

Si la primera matriz es:
```
1 2
3 4
```
Y la segunda matriz es:
```
1 5
4 4
```

Las matrices tienen dos coincidencias (el 1 y el 4).

## Entradas

Los 10 archivos, desde el `"Matriz1.txt"` hasta el `"Matriz10.txt"`. 

## Salida

Debe crear el archivo `"resultado.txt"`, que debe contener la comparación de todos lor archivos, indicando por cada archivo el nombre de la matriz, seguido de 10 líneas indicando cuántas coincidencias tuvo esta matriz con cada una de las otras con el formato:
```
   Matriz <número>: <cantidad_de_coincidencias> elementos coinciden.
```

Note que hay tres espacios antes de este último mensaje. Por lo tanto, el archivo se vería así:
```
Matriz <número>
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
   Matriz <número>: <cant_de_coincidencias> elementos coinciden.
```

## Consideraciones
- Considere para su desarrollo la implementación del bloque principal en una función llamada `comparar` que no tome parámetros, o que todos sus parámetros sean opcionales. Los tests cases ejecutarán dicha función (de nuevo, sin utilizar parámetros) y luego verificarán el archivo generado, no la «salida» de la función.
- Las matrices de los archivos tienen el mismo tamaño, el cual corresponde a números naturales. Si bien las 10 matrices tendrán el mismo tamaño en la ejecución, estos valores varían de ejecución en ejecución al evaluar los test.

## Ejemplo

Entrada:
Para los archivos desde `"Matriz1.txt"` a `"Matriz10.txt"` con el siguiente contenido:
```
5 2 6
3 6 2
6 2 4
3 6 8
```

```
8 1 6
4 6 9
3 3 4
8 2 4
```

```
1 4 3
1 8 8
1 9 2
5 6 6
```

```
2 2 4
7 2 2
6 8 6
9 4 8
```

```
3 1 1
9 2 9
4 3 3
5 1 2
```

```
5 3 4
3 1 5
3 9 9
7 9 4
```

```
4 4 4
9 4 3
1 4 3
6 7 5
```

```
3 4 5
5 2 6
6 1 3
9 6 3
```

```
3 1 5
2 5 2
4 2 4
6 7 2
```

```
2 3 3
1 8 4
2 3 2
8 5 8
```


Salida:
El contenido del archivo `"resultado.txt"` debiese ser:
```
Matriz 1
   Matriz 1: 12 elementos coinciden.
   Matriz 2: 3 elementos coinciden.
   Matriz 3: 1 elementos coinciden.
   Matriz 4: 4 elementos coinciden.
   Matriz 5: 0 elementos coinciden.
   Matriz 6: 2 elementos coinciden.
   Matriz 7: 0 elementos coinciden.
   Matriz 8: 2 elementos coinciden.
   Matriz 9: 3 elementos coinciden.
   Matriz 10: 1 elementos coinciden.
Matriz 2
   Matriz 1: 3 elementos coinciden.
   Matriz 2: 12 elementos coinciden.
   Matriz 3: 0 elementos coinciden.
   Matriz 4: 0 elementos coinciden.
   Matriz 5: 3 elementos coinciden.
   Matriz 6: 2 elementos coinciden.
   Matriz 7: 0 elementos coinciden.
   Matriz 8: 0 elementos coinciden.
   Matriz 9: 2 elementos coinciden.
   Matriz 10: 2 elementos coinciden.
Matriz 3
   Matriz 1: 1 elementos coinciden.
   Matriz 2: 0 elementos coinciden.
   Matriz 3: 12 elementos coinciden.
   Matriz 4: 0 elementos coinciden.
   Matriz 5: 1 elementos coinciden.
   Matriz 6: 1 elementos coinciden.
   Matriz 7: 2 elementos coinciden.
   Matriz 8: 2 elementos coinciden.
   Matriz 9: 0 elementos coinciden.
   Matriz 10: 4 elementos coinciden.
Matriz 4
   Matriz 1: 4 elementos coinciden.
   Matriz 2: 0 elementos coinciden.
   Matriz 3: 0 elementos coinciden.
   Matriz 4: 12 elementos coinciden.
   Matriz 5: 1 elementos coinciden.
   Matriz 6: 1 elementos coinciden.
   Matriz 7: 1 elementos coinciden.
   Matriz 8: 3 elementos coinciden.
   Matriz 9: 1 elementos coinciden.
   Matriz 10: 2 elementos coinciden.
Matriz 5
   Matriz 1: 0 elementos coinciden.
   Matriz 2: 3 elementos coinciden.
   Matriz 3: 1 elementos coinciden.
   Matriz 4: 1 elementos coinciden.
   Matriz 5: 12 elementos coinciden.
   Matriz 6: 0 elementos coinciden.
   Matriz 7: 2 elementos coinciden.
   Matriz 8: 3 elementos coinciden.
   Matriz 9: 4 elementos coinciden.
   Matriz 10: 1 elementos coinciden.
Matriz 6
   Matriz 1: 2 elementos coinciden.
   Matriz 2: 2 elementos coinciden.
   Matriz 3: 1 elementos coinciden.
   Matriz 4: 1 elementos coinciden.
   Matriz 5: 0 elementos coinciden.
   Matriz 6: 12 elementos coinciden.
   Matriz 7: 1 elementos coinciden.
   Matriz 8: 0 elementos coinciden.
   Matriz 9: 0 elementos coinciden.
   Matriz 10: 1 elementos coinciden.
Matriz 7
   Matriz 1: 0 elementos coinciden.
   Matriz 2: 0 elementos coinciden.
   Matriz 3: 2 elementos coinciden.
   Matriz 4: 1 elementos coinciden.
   Matriz 5: 2 elementos coinciden.
   Matriz 6: 1 elementos coinciden.
   Matriz 7: 12 elementos coinciden.
   Matriz 8: 2 elementos coinciden.
   Matriz 9: 2 elementos coinciden.
   Matriz 10: 0 elementos coinciden.
Matriz 8
   Matriz 1: 2 elementos coinciden.
   Matriz 2: 0 elementos coinciden.
   Matriz 3: 2 elementos coinciden.
   Matriz 4: 3 elementos coinciden.
   Matriz 5: 3 elementos coinciden.
   Matriz 6: 0 elementos coinciden.
   Matriz 7: 2 elementos coinciden.
   Matriz 8: 12 elementos coinciden.
   Matriz 9: 2 elementos coinciden.
   Matriz 10: 0 elementos coinciden.
Matriz 9
   Matriz 1: 3 elementos coinciden.
   Matriz 2: 2 elementos coinciden.
   Matriz 3: 0 elementos coinciden.
   Matriz 4: 1 elementos coinciden.
   Matriz 5: 4 elementos coinciden.
   Matriz 6: 0 elementos coinciden.
   Matriz 7: 2 elementos coinciden.
   Matriz 8: 2 elementos coinciden.
   Matriz 9: 12 elementos coinciden.
   Matriz 10: 0 elementos coinciden.
Matriz 10
   Matriz 1: 1 elementos coinciden.
   Matriz 2: 2 elementos coinciden.
   Matriz 3: 4 elementos coinciden.
   Matriz 4: 2 elementos coinciden.
   Matriz 5: 1 elementos coinciden.
   Matriz 6: 1 elementos coinciden.
   Matriz 7: 0 elementos coinciden.
   Matriz 8: 0 elementos coinciden.
   Matriz 9: 0 elementos coinciden.
   Matriz 10: 12 elementos coinciden.
```
