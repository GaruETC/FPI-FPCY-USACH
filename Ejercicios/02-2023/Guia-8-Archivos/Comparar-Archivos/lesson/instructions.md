![logo](./assets/logo_usach.png)

# Comparando matrices

Se tienen dos archivos, en cada uno hay una matriz de nxm con números. Se le solicita crear la función `comparar()` que crea un archivo llamado `"resultado.txt"` que debe tener una matriz del mismo tamaño que las matrices de los archivos de entrada. Esta matriz debe tener únicamente letras `"O"` y `"X"`. Debe tener una `"O"`, si en esa posición en ambas matrices está el mismo número, y una `"X"`, si en esa posición las matrices tienen números distintos.

Por ejemplo:
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
La matriz resultado debe ser:
```
O X
X O
```

## Entradas

Los archivos `"Matriz1.txt"` y `"Matriz2.txt"`.

## Salida

Debe crear el archivo `"resultado.txt"`, que debe contener la matriz resultado.

## Consideraciones
- Considere para su desarrollo la implementación del bloque principal en una función llamada `comparar` que no tome parámetros, o que todos sus parámetros sean opcionales. Los tests cases ejecutarán dicha función (de nuevo, sin utilizar parámetros) y luego verificarán el archivo generado, no la «salida» de la función.
- Las matrices de los archivos `"Matriz1.txt"` y `"Matriz2.txt"` tienen el mismo tamaño, el cual corresponde a números naturales.

## Ejemplo

Entrada:
Si el contenido de los archivos `"Matriz1.txt"` y `"Matriz2.txt" fuese el siguiente:
```
1 5 3 5 6 7 2 8 9
1 3 8 4 7 7 6 2 9
4 5 8 3 3 1 8 8 1
4 8 3 2 9 3 4 2 6
8 5 2 1 6 2 2 9 5
9 5 9 2 6 7 6 9 9
5 2 6 8 6 3 8 1 2
1 2 4 6 5 2 2 6 1
3 4 9 4 9 4 7 6 7
```
```
4 2 2 7 1 8 3 8 4
3 7 1 5 8 9 4 2 6
1 6 1 5 9 2 6 2 1
9 8 3 9 5 1 1 5 8
5 6 5 3 3 4 6 6 8
1 6 7 8 6 5 7 4 3
3 5 3 8 3 8 1 3 6
1 5 2 1 1 4 1 3 2
5 9 1 4 1 1 8 6 7
```

Salida:
El contenido del archivo `"resultado.txt"` debiese ser:
```
X X X X X X X O X
X X X X X X X O X
X X X X X X X X O
X O O X X X X X X
X X X X X X X X X
X X X X O X X X X
X X X O X X X X X
O X X X X X X X X
X X X O X X X O O
```
