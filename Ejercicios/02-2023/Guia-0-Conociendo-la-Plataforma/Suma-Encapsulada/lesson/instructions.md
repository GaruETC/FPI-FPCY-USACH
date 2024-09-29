![logo](./assets/logo_usach.png)

# Suma Encapsulada

## Contexto

Más adelante en el curso, particularmente desde la Unidad 2, comenzaremos a trabajar en funciones, una característica de los lenguajes para encapsular código y reutilizarlo. Por ahora no te preocupes de cómo es la sintaxis, nos enfocaremos en ver los tests que aparecerán cuando lleguemos a ese momento.

## El problema

En este problema, se le pide generar una función que tome como parámetros dos números y entregue como resultado la suma de este.

### Entradas

Dos números de cualquier tipo, con el siguiente encabezado:
```python
def sumar(<número_1>, <número_2>):
```

### Salidas

La función debe retornar la suma de los dos valores

### Ejemplos
#### Ejemplo 1
Para la llamada:
```python
sumar(2, 2)
```
Debe retornar 4.

#### Ejemplo 2
Para la llamada:
```python
sumar(3, 5)
```
Debe retornar 8.

## Para resolverlo

Un código que no resuelve el problema es el siguiente:
```python
valor_1 = int(input())
valor_2 = int(input())

resultado = valor_1 + valor_2

print(resultado)
```

Prueba a pegar ese código en el archivo `main.py` y verifica que funciona. Al ejecutar los tests, podrás ver el resultado de estos en la pestaña ">_ Console". Notarás que fallan todos, mostrando una excepción que indica el error. En este caso, dicen que "sumar" no está definido, pues no está definida la función `sumar`, que es lo pedido en este programa (ya veremos en el curso el detalle de cómo se define).

Otro código que no resuelve el problema, pero sí define la función es este:

```python
def sumar(a, b):
  return a - b
```

Copia el código. Al ejecutarlo, verás que no imprime nada. Este comportamiento es lo que esperamos de este código, así que está bien, pero si ejecutas los tests, verás que lanzan un mensaje de error como este:
```
Traceback (most recent call last):
  File "/home/runner/Suma-Encapsulada/_test_runnertest_suite.py", line 9, in test_1
    self.assertEqual(sumar(1, 1), 2)
AssertionError: 0 != 2
```

Este error significa que la función debería dar como resultado 2, pero está dando como resultado 0, es decir, ¡el código no resuelve el problema! Esto es lo que esperábamos, también, pues dijimos que el código no resolvería el problema.

Los **tests unitarios** son un tipo especial de tests que verifica que un bloque de código (una función) entregue un resultado esperado. Difieren de los de entrada y salida, pues estos no evalúan las entradas del programa y las salidas, sino que las entradas y salidas de un *fragmento* de este, que son las funciones. Es como que comprobáramos que la instrucción `int("42")` entregara como resultado el número 42. Esto es muy importante para verificar que hemos escrito bien las funciones y es lo que usaremos para evaluar varios de los problemas más adelante.

Este código sí funciona:

````python
def sumar(valor_1, valor_2):
    resultado = valor_1 + valor_2
    return resultado
```

Nota que la consola pone un ticket verde al lado de cada test y finaliza con el mensaje "All tests have passed", ¡esto significa que efectivamente funciona!
