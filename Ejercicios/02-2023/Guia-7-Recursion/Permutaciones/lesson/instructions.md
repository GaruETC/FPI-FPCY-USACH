![logo](./assets/logo_usach.png)

# Permutaciones

Construye una función que, recursivamente y sin usar herramientas externas, encuentre todas las permutaciones de los elementos de un string.

## Entradas

La función tomará como entrada un string.

```python
def permutations(<string>)
```

## Salida

La función debe retornar una lista cuyos elementos son los strings con las diferentes permutaciones encontradas, ordenadas lexicográficamente.

## Consideraciones
- Puedes definir más entradas para la función, sin embargo, estas no pueden ser obligatorias. Por ejemplo, tu prototipo podría ser `find_min_missing(array, a=0, b=0, c="")`, pero no `find_min_missing(array, a, b=0, c="")`, pues eso implica un segundo parámetro obligatorio.

## Ayuda
- La función `sorted` ordena una lista de modo que sus elementos queden ordenados lexicográficamente.

## Ejemplos

### Ejemplo 1
Entrada:
```python
permutations("xy")
```

Salida:
```python
['xy', 'yx']
```

### Ejemplo 2
Entrada:
```python
permutations("ABC")
```

Salida:
```
['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
```
