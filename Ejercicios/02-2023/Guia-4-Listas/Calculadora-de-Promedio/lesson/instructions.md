![logo](./assets/logo_usach.png)

# Calculadora de Promedio

El siguiente código:
```python
# Entrada
numbers = [10, 20, 30, 40, 50]

# Procesamiento
total = 0

for number in numbers:
    total += number

mean = total / len(numbers)

# Salida
print("El promedio es " + str(mean) + ".")
```

Permite calcular el promedio de una lista de números y presentarlo por pantalla. Si bien este código funciona, se requiere que lo haga para *cualquier* lista de números y no solo la entregada. Modifique el programa para que reciba una lista como una única entrada de usuario con los valores separados por punto y coma ("`;`") y entregue la media geométrica de estos valores, redondeada a dos decimales.

Recuerde que la media geométrica se calcula como la raíz enésima del producto de los valores a promediar. Por otra parte, la raíz enésima de un número puede ser obtenida elevando al inverso multiplicativo de *n*, es decir, 1/*n*.

## Entradas

La entrada será una secuencia de valores separados por punto y coma:
```
<valor1>;<valor2>;<valor3>;...
```
los que serán ingresados en una única vez en una sola línea.

## Salida

Un mensaje que señale cuál es la media geométrica:
```
La media geometrica es <media>.
```

## Consideraciones
- La secuencia de valores nunca estará vacía.
- Cada valor de la secuencia siempre será un número válido a transformar.
- Los valores ingresados pueden ser enteros o reales.
- Recuerde que puede redondear el número `n` a `d` decimales con la función `round(n, d)`.

## Restricciones
- No use módulos externos para determinar la raíz, use solo operadores básicos de Python.

## Ejemplos

### Ejemplo 1
Entrada:
```
8;2;4
```

Salida:
```
La media geometrica es 4.0.
```

### Ejemplo 2
Entrada:
```
3;9;27;3
```

Salida:
```
La media geometrica es 6.84.
```
