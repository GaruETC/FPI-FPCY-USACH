![logo](./assets/logo_usach.png)

# La Primera Capital

Escribe una función que busque recursivamente la primera mayúscula de un *string* dado como parámetro y entregue tanto la letra como su posición.

Por ejemplo, para el *string* `"-¿Olvida usted algo?"`, la primera mayúscula es `"O"`, en la posición 2 del string.

## Entradas

La función tomará como entrada un string y un parámetro opcional, que corresponde a un índice, cuyo valor por defecto debe ser 0.

```python
def first_capital(text, index=0)
```

## Salida

La función debe retornar una lista con dos elementos, la letra mayúscula y la posición (`[<letra>, <posición>]`). En caso de no encontrar mayúsculas, debe retornar la lista `["", -1]`

## Consideraciones
- No debe usar ciclos para resolver este problema.

## Ejemplos

### Ejemplo 1
Entrada:
```python
first_capital("la huerfanita Anita")
```

Salida:
```python
['A', 14]
```

### Ejemplo 2
Entrada:
```python
first_capital("Anita la huerfanita", 1)
```

Salida (nótese que está contando desde la segunda posición):
```
['', -1]
```
