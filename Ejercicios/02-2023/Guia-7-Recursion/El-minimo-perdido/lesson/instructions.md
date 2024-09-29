![logo](./assets/logo_usach.png)

# El mínimo perdido

Escribe una función recursiva que reciba una lista ordenada de números no negativos y entregue el menor valor que no esté en la secuencia. Por ejemplo, para la secuencia `0, 1, 2, 6, 8, 9`, el menor valor perdido es 3.

El menor valor perdido puede ser el próximo en la secuencia. Por ejemplo, si la secuencia es `0, 1, 2, 3`, el menor valor perdido en ella es el 4.

## Entradas

El parámetro obligatorio de la función es una lista ordenada de números no negativos.

```python
def find_min_missing(<lista>)
```

## Salida

La función debe retornar el primer número (entero) perdido, o el próximo en la secuencia (que corresponde, en este caso, al mínimo perdido).

## Consideraciones
- Puedes definir más entradas para la función, sin embargo, estas no pueden ser obligatorias. Por ejemplo, tu prototipo podría ser `find_min_missing(array, a=0, b=0, c="")`, pero no `find_min_missing(array, a, b=0, c="")`, pues eso implica un segundo parámetro obligatorio.

## Ejemplos

### Ejemplo 1
Entrada:
```python
find_min_missing([0, 1, 2, 3])
```

Salida:
```python
4
```

### Ejemplo 2
Entrada:
```python
find_min_missing([0, 1, 2, 4, 6])
```

Salida:
```
3
```
