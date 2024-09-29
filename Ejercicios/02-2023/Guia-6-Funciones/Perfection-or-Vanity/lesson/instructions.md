![logo](./assets/logo_usach.png)

# Perfection or Vanity

En teoría de números, se dice que un número es perfecto cuando este es igual a la suma de sus divisores propios (es decir, los divisores que no son 1 y el mismo número) y 1. Por ejemplo, 6, el primer número perfecto, es 1+2+3, que es la suma de sus divisores propios (2 y 3) y 1.

Construye dos funciones: una que obtenga los divisores de un número en una listas (código 1) y otra que verifique si un número dado es perfecto (código 2).

```python
def obtener_divisores(n):
```
***Código 1:** Encabezado de la función para obtener los divisores de un número n.*

```python
def es_perfecto(n):
```
***Código 2:** Encabezado de la función para verificar si un número n es perfecto.*

## Entradas

La entrada a ambas funciones es un número entero positivo.

## Salida

Para la función `obtener_divisores`, la salida es una lista de números con los divisores de su entrada. Esto significa que incluye entre los divisores a 1 y al número mismo.

Para la función `es_perfecto`, la salida es si el número es perfecto (`True`) o no (`False`).

## Ejemplos

### Ejemplo 1
Entrada:
```
6
```

Salida:
- Divisores:
```python
[1, 2, 3, 6]
```
- Es perfecto:
```python
True
```

### Ejemplo 2
Entrada:
```
20
```

Salida:
- Divisores:
```python
[1, 2, 4, 5, 10, 20]
```
- Es perfecto:
```python
False
```
