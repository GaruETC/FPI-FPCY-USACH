![logo](./assets/logo_usach.png)

# De suma a multiplicación

En este problema, se te presenta un código que realiza la suma de dos valores. Cámbialo para que, en lugar de eso, calcule la multiplicación de los dos valores.

## Entradas

Corresponden a dos números entregados por consola, uno a la vez:
```
Primer valor: <valor_1>
Segundo valor: <valor_2>
```

## Salida

Un mensaje con el resultado:
```
El resultado es <resultado>
```

## Consideraciones

El objetivo de este problema es que te familiarices con otras opciones de *testcases* que usaremos a lo largo del curso. En este caso, serán tests de entrada y salida, por lo que en la pestaña de "Tests", se presentarán cuatro pares de entradas y se verificará que el programa entregue el *mensaje* esperado con el resultado.

Antes de comenzar, ejecuta con el botón "Run" el programa un par de veces y ve qué produce como resultado y qué mensajes muestra. El código original que debes modificar es el siguiente:
```python
# Entrada
entrada_1 = input("Primer valor: ")
entrada_2 = input()

# Procesamiento
x_1 = int(entrada_1)
x_2 = int(entrada_2)

resultado = x_1 + x_2

# Salida
print("El resultado es", resultado)
```

Para efectos de los *testcases*, **todos los mensajes** son considerados salida, y las llamadas a `input` *son* mensajes mostrados al usuario.

Cambia la operación de suma por una multiplicación y corre los tests: vas a notar que todos fallan, a pesar de tener el resultado esperado, porque uno de los mensajes falta. Arréglalo y corre de nuevo los tests. Si el mensaje es el pedido, ¡ahora sí los pasará!

## Ejemplos
### Ejemplo 1
Entradas:
```
Primer valor: 2
Segundo valor: 8
```
Salida:
```
El resultado es 16
```

### Ejemplo 2
Entradas:
```
Primer valor: 5
Segundo valor: 5
```

Salida
```
El resultado es 25
```
