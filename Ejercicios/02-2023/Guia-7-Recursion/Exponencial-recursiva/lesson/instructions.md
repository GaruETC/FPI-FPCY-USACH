![logo](./assets/logo_usach.png)

# Exponencial Recursiva

La *n*-ésima potencia de un número *x* se puede calcular utilizando la fórmula de recurrencia siguiente:
- Si *n* = 0, el resultado es 1.
- Si *n* es par, el resultado es `x**(n/2)*x**(n/2)`.
- Si *n* es impar, el resultado es `x*x**(n-1)`.

Implementa la exponenciación usando esta relación de recurrencia como una función recursiva que calcule la enésima potencia de un número entero, sin usar ni la función `pow` ni el operador de exponenciación `**`.

## Entradas

La función tomará como entrada dos números enteros, `<base>` y `<exponente>`, donde el segundo solo será un entero no negativo.

```python
def exp(<base>, <exponente>)
```

## Salida

La función retorna el resultado de la operación `<base>**<exponente>`.

## Consideraciones
- Recuerda que no se pueden usar ni la función ni el operador de exponenciación.

## Ejemplos

### Ejemplo 1
Entrada:
```python
exp(2, 10)
```

Salida:
```python
1024
```

### Ejemplo 2
Entrada:
```python
exp(3, 8)
```

Salida:
```
6561
```
