![logo](./assets/logo_usach.png)

# En Búsqueda de la Felicidad

En teoría de números, un número es feliz cuando, al reemplazarlo por la suma de los cuadrados de sus dígitos, eventualmente se puede llegar a 1. Por otra parte, un número se dice que es triste o infeliz cuando entra en un ciclo infinito.

Por ejemplo, 13 se reemplazaría por `1**2 + 3**2` = 10, y este por `1**2 + 0**2` = 1, por lo que 13 es un número feliz. Por otra parte, 4 se reemplazaría por `4**2` = 16, que se reemplazaría a su vez por `1**2 + 6**2` = 37; y sigue la secuencia con 58, 89, 145, 42, 20 y vuelve a 4 (puedes comprobarlo haciendo los cálculos).

Se te pide construir una función **recursiva** que verifique si un número es feliz o no.

## Entradas

La función tomará como entrada un número natural (es decir, entero mayor o igual a 1) y su encabezado está dado por el código 1.

```python
def is_happy(n)
```

## Salida

La función debe retornar `True`, si el número es feliz, o `False`, en caso contrario.

## Consideraciones
- Construye todas las funciones auxiliares que necesites.
- Los tests evalúan el comportamiento y construcción de la función, por lo que asegúrate de que sea recursiva.

## Ejemplos

### Ejemplo 1
Entrada:
```python
is_happy(13)
```

Salida:
```python
True
```

### Ejemplo 2
Entrada:
```python
is_happy(14)
```

Salida:
```
False
```
