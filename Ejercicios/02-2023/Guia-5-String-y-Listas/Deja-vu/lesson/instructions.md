![logo](./assets/logo_usach.png)

# Reflejando Matrices 2

Se necesita realizar operaciones sobre una matriz de números. En particular, se busca reflejar una matriz de **nxm** de forma vertical y horizontal.

## Entradas

Reciba dos números enteros positivos que representa la cantidad de filas y columnas de la matriz a ingresar con los mensajes "`Ingrese la cantidad de filas: `" e "`Ingrese la cantidad de columnas: `". A continuación, con el mensaje "`Ingrese los datos: `" pida los datos de la matriz, los cuales se entregan en una única entrada con los números separados por comas, los cuales deben guardarse en una lista de listas (matriz), ubicándolos dentro de la matriz en el mismo orden que se ingresan, llenando cada fila desde la primera a la última y, en cada fila, debe llenarse esta de forma ordenada desde la primera posición hasta la última. 

```
Ingrese la cantidad de filas: <número>
Ingrese la cantidad de columnas: <número>
Ingrese los datos:  <números separados por comas>
```

## Salida

Debe mostrar 3 matrices, la matriz original ingresada, la matriz con sus datos reflejados de forma vertical y la matriz con sus datos reflejados de forma horizontal. Al momento de mostrar las matrices en la línea anterior, debe mostrar los mensajes: "`Matriz Original:`", "`Matriz Reflejada Verticalmente:`" y "`Matriz Reflejada Horizontalmente:`" respectivamente.
```
Matriz Original:
<Matriz>
Matriz Reflejada Horizontalmente:
<Matriz>
Matriz Reflejada Verticalmente:
<Matriz>
```

## Consideraciones o Restricciones
- Al momento de mostrar una matriz, esta debe estar en formato de lista de lista de números.
- Cuando la cantidad de filas o columnas es par, el reflejo se hace intercambiando todas las filas o columnas, según si es el reflejo horizontal o vertical, respectivamente.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese la cantidad de filas: 3
Ingrese la cantidad de columnas: 3
Ingrese los datos: 54,49,495,946,4,94,6,94,26
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

**Explicación**
La lista representa a la matriz, las sublistas representan las filas de la matriz y los elementos de las subfilas son las columnas de esa fila.
```
Matriz Original:
54 49 495
946 4 94 
6 94 26

Matriz Reflejada Verticalmente:
6 94 26
946 4 94
54 49 495

Matriz Reflejada Horizontalmente:
495 49 54
94 4 946
26 94 6

```

### Ejemplo 2
Entrada:
```
Ingrese la cantidad de filas: 4
Ingrese la cantidad de columnas: 2
Ingrese los datos: 1,2,3,4,5,6,7,8
```

Salida:
```
Matriz Original:
[[1, 2], [3, 4], [5, 6], [7, 8]]
Matriz Reflejada Verticalmente:
[[7, 8], [5, 6], [3, 4], [1, 2]]
Matriz Reflejada Horizontalmente:
[[2, 1], [4, 3], [6, 5], [8, 7]]
```
