![logo](./assets/logo_usach.png)

# Reflejando Matrices

Se necesita realizar operaciones sobre una matriz de números. En particular, se busca reflejar una matriz de **3x3** de forma vertical y horizontal.

## Entradas

Reciba 9 números enteros, los cuales deben guardarse en una lista de listas (matriz) ubicándolos dentro de la matriz en el mismo orden que se ingresan, llenando cada fila desde la primera a la última, y en cada fila debe llenarse esta de forma ordenada, desde la primera posición hasta la última. Es decir, el primer valor es la primera fila, primera columna, el segundo es la primera fila, segunda columna; el tercero es la primera fila, tercera columna; el cuarto es la segunda fila, primera columna, etc.

Las solicitides de números se deben hacer con el mensaje "`Ingrese un número: `" (notar el espacio).

```
Ingrese un número: <número>
Ingrese un número: <número>
Ingrese un número: <número>
Ingrese un número: <número>
Ingrese un número: <número>
Ingrese un número: <número>
Ingrese un número: <número>
Ingrese un número: <número>
Ingrese un número: <número>
```

## Salida

Debe mostrar 3 matrices: la matriz original ingresada, la matriz con sus datos reflejados de forma vertical y la matriz con sus datos reflejados de forma horizontal. Al momento de mostrar las matrices en la línea anterior debe mostrar los mensajes: "`Matriz Original:`", "`Matriz Reflejada Verticalmente:`" y "`Matriz Reflejada Horizontalmente:`" respectivamente.
```
Matriz Original:
<Matriz>
Matriz Reflejada Horizontalmente:
<Matriz>
Matriz Reflejada Verticalmente:
<Matriz>
```

## Consideraciones o Restricciones
- Al momento de mostrar una matriz esta debe estar en formato de lista de lista de números.
- Reflejar la matriz horizontalmente quiere decir intercambiar las filas con respecto a la fila del medio (en otras palabras, intercambiar la primera fila con la última, la segunda con la penúltima, etc.).
- Reflejar la matriz verticalmente es equivalente a horizontalmente, pero con respecto a la *columna* del medio.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese un número: 1
Ingrese un número: 2
Ingrese un número: 3
Ingrese un número: 4
Ingrese un número: 5
Ingrese un número: 6
Ingrese un número: 7
Ingrese un número: 8
Ingrese un número: 9
```

Salida:
```
Matriz Original:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Matriz Reflejada Horizontalmente:
[[7, 8, 9], [4, 5, 6], [1, 2, 3]]
Matriz Reflejada Verticalmente:
[[3, 2, 1], [6, 5, 4], [9, 8, 7]]
```

**Explicación**
La lista representa a la matriz, las sublistas representan las filas de la matriz y los elementos de las subfilas son las columnas de esa fila.
```
Matriz Original:
1 2 3
4 5 6
7 8 9

Matriz Reflejada Verticalmente:
7 8 9
4 5 6
1 2 3

Matriz Reflejada Horizontalmente:
3 2 1
6 5 4
9 8 7

```

### Ejemplo 2
Entrada:
```
Ingrese un número: 54
Ingrese un número: 49
Ingrese un número: 495
Ingrese un número: 946
Ingrese un número: 4
Ingrese un número: 94
Ingrese un número: 6
Ingrese un número: 94
Ingrese un número: 26
```

Salida:
```
Matriz Original:
[[54, 49, 495], [946, 4, 94], [6, 94, 26]]
Matriz Reflejada Verticalmente:
[[6, 94, 26], [946, 4, 94], [54, 49, 495]]
Matriz Reflejada Horizontalmente:
[[495, 49, 54], [94, 4, 946], [26, 94, 6]]
```
