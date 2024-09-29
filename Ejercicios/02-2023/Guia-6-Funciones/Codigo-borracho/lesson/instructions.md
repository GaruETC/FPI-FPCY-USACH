![logo](./assets/logo_usach.png)

# Código Borracho

Debido a que las serpientes [no pueden tolerar bien el alcohol](https://everythingreptilion.com/can-snakes-drink-alcohol-the-truth-about-snakes-and-alcohol-consumption/), Python ha estado actuando raro y no está ejecutando adecuadamente las funciones `str` e `int`, por lo que la conversión entre estos dos tipos no está produciendo los resultados deseados.

Construye dos funciones, cuyos encabezados se presentan en los códigos 1 y 2, que realicen la transformación desde un string a un entero y desde un entero a un string, respectivamente.

```python
def str_to_int(value):
```
***Código 1:** Encabezado de la función para convertir de string a entero*.

```python
def int_to_str(value):
```
***Código 2:** Encabezado de la función para convertir de entero a string*.

## Entradas

La entrada de la función `str_to_int` será un string que **posiblemente** represente un entero.

La entrada de la función `int_to_str` será un número entero.

## Salida

La función `str_to_int` retornará su argumento convertido a entero **si este es un entero**, o reportará un error, en caso contrario. Si descubre que el string no puede ser transformado a entero, escriba el contenido del código 3 en el punto que lo detecte, para que quien llama a la función pueda ver el error.

```python
raise ValueError(f"No se puede convertir {source}")
```
***Código 3:** Reporte de error cuando la conversión es imposible.*

La función `int_to_str` retornará su argumento convertido en string.


## Consideraciones
- Los parámetros de la función `int_to_str` siempre serán números enteros válidos, por lo que no hay que preocuparse de errores de ese tipo.
- Cuando un string no pueda ser convertido a número entero, el programa se caerá por el reporte de error: este es el comportamiento esperado y lo que se evaluará en los tests.
- Si bien podría ser que las funciones `str` e `int` funcionen al momento de escribir tu código, no estarán disponibles cuando se ejecuten los tests.
- La conversión de string a número debe ser válida: se permiten números negativos (antecedidos con el caracter `"-"`), espacio alrededor del número, pero no puntos (que señalarían decimales), letras, símbolos especiales diferentes del guión, etc.

## Ejemplos

### Ejemplo 1
Entrada:
```python
str_to_int(" -123 ")
```

Salida:
```python
-123
```

### Ejemplo 2
Entrada:
```python
int_to_str(-123)
```

Salida:
```python
"-123"
```

### Ejemplo 3
Entrada (esta es incorrecta):
```python
str_to_int("-12 3")
```

Salida (reporta el error):
```
Traceback (most recent call last):
  File "/home/runner/Codigo-borracho/main.py", line 47, in <module>
    print(str_to_int("-12 3"))
  File "/home/runner/Codigo-borracho/main.py", line 19, in str_to_int
    raise ValueError(f"No se puede convertir {source}")
ValueError: No se puede convertir 12 3
```
