![logo](./assets/logo_usach.png)

# Diferencia Asimétrica

Cree un programa que determine la diferencia asimétrica de dos conjuntos de números.

La diferencia asimétrica de dos conjuntos son los elementos que pertenecen al primer conjunto más los elementos que pertenecen al segundo conjunto, pero sin los que estén en ambos conjuntos

Por ejemplo:
- Conjunto 1: 4 5 6 7 8
- Conjunto 2: 3 4 5 6 7 9
- Diferencia asimétrica: 3 8 9

## Entradas

Se reciben dos entradas, ambas son los números de los respectivos conjuntos. Se entregan como una serie de números separados por espacios. Al momento de solicitar las entradas se debe utilizar los mensajes `"Ingrese los valores 1: "` y `"Ingrese los valores 2: "`, respectivamente. Note que los mensajes tienen un espacio luego de los dos puntos:

```
Ingrese los valores 1:  <números separados por espacios>
Ingrese los valores 2:  <números separados por espacios>
```

## Salida

Debe entregar los números correspondiente a la diferencia asimetrica entre ambos conjuntos separados por espacios en una misma línea. Si bien normalmente en los conjuntos se trabaja sin elementos repetidos, en este ejercicio se esperan todos los elementos repetidos, tanto en las entradas como en el resultado. La salida debe estar ordenada de menor a mayor.
```
<números separados por espacios>
```

## Consideraciones
- Los elementos repetidos deben incluirse.
- La salida debe estar ordenada de menor a mayor.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese los valores 1: 4 5 6 7 8
Ingrese los valores 2: 3 4 5 6 7 9
```

Salida:
```
3 8 9
```

### Ejemplo 2
Entrada:
```
Ingrese los valores 1: 1 2 3 4 5 6 7 8 9
Ingrese los valores 2: 9 8 7 6 5 4 3 2 1 0
```

Salida:
```
0
```

### Ejemplo 3
Entrada:
```
Ingrese los valores 1: 7 3 5 4 6
Ingrese los valores 2: 1 3 2 7 8 9 9 8
```

Salida:
```
1 2 4 5 6 8 8 9 9
```
