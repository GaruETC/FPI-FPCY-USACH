![logo](./assets/logo_usach.png)

# Operaciones sobre Matrices

Para dos matrices entregadas por el usuario a partir de una serie de valores, calcule la suma de estas, su multiplicación y el determinante de cada una de ellas.

Los componentes de cada matriz se deben pedir uno a uno, mostrándose las matrices resultantes en mensajes que tengan el siguiente formato:
```
<a_11> <a_12>
<a_21> <a_22>
```

Además, para los determinantes, debe presentar el mensaje:
```
Los determinantes de las matrices son <determinante 1> y <determinante 2>
```

## Entrada

Se deben recibir los cuatro componentes de cada matriz seguidos, uno por línea. Los elementos de la matriz serán números reales. Si el componente `ij` de la matriz a es `a_ij`, la entrada se vería como sigue:

```
Matriz 1:
<a_11>
<a_12>
<a_21>
<a_22>
Matriz 2:
<b_11>
<b_12>
<b_21>
<b_22>
```

## Salida

Siendo `c` la matriz con la suma y `d` la matriz de la multiplicación, la salida del programa debe seguir el siguiente esquema:
  
```
La suma de las matrices es
<c_11> <c_12>
<c_21> <c_22>
La multiplicación de las matrices es
<d_11> <d_12>
<d_21> <d_22>
Los determinantes de las matrices son <determinante 1> y <determinante 2>
```

**Nota**: Los determinantes corresponden a los de las matrices de entrada, no a las matrices con la suma y la multiplicación.

## Ayuda

Considere que cada componente de cada matriz es una variable diferente. Más adelante en el curso se revisarán estructuras como listas, que simplificarán este y otros problemas.

Considere que si las matrices son A:
```
<a_11> <a_12>
<a_21> <a_22>
```
y B: 

```
<b_11> <b_12>
<b_21> <b_22>
```

La suma se calcula componente a componente, por ejemplo: 
`c_11` es `a_11 + b_11`.

La multiplicación se calcula combinando para cada casilla la fila de la primera matriz y con la columna de la segunda, por ejemplo:
`c_11` es `a_11 * b_11 + a_21 * b_12`.

Mientras que el determinante para matrices de 2x2 (2 filas y 2 columnas) se calcula como el resultado de la resta entre la multiplicación de dos diagonales, para el caso de la matriz A:
`a_11 * a_22 - a_21 * a_12` .

## Consideraciones
- Redondee los valores de las matrices resultantes y los determinantes a dos decimales.
- Para redondear, usa la función `round(n, d)`, que redondea `n` a `d` decimales.

## Ejemplos
**Lista de ejemplos con datos de prueba y salida *exacta* esperada**
### Ejemplo 1
Entrada:
```
Matriz 1:
1
2
34
4
Matriz 2:
0
-1
2
3
```

Salida:
```
La suma de las matrices es
1.0 1.0
36.0 7.0
La multiplicación de las matrices es
4.0 5.0
8.0 -22.0
Los determinantes de las matrices son -64.0 y 2.0
```

### Ejemplo 2
Entradas:
```
Matriz 1:
1.2
3.56
7.12
7
Matriz 2:
0.1
-9.8
2.5
-1.06
```

Salida:
```
La suma de las matrices es
1.3 -6.24
9.62 5.94
La multiplicación de las matrices es
9.02 -15.53
18.21 -77.2
Los determinantes de las matrices son -16.95 y 24.39
```
