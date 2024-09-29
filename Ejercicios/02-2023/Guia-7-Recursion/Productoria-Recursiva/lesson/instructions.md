![logo](./assets/logo_usach.png)

# Productoria recursiva

El código entregado, mostrado en el código 1, consta de una función, llamada `sumatoria`, la cual recibe como entrada un número entero positivo y retorna un número entero positivo que representa la sumatoria desde 0 al número ingresado.

```python
"""Productoria recursiva
"""
# Modifique este código
def sumatoria(numero):
    '''
    Entrada: Número entero positivo
    Salida: Número entero positivo
    Proceso: Suma de los n primeros números enteros positivos
    '''
    if numero == 0:
        return 0
    return numero + sumatoria(numero - 1)


if __name__ == "__main__":
    # Estas líneas, correspondientes al bloque principal del programa, no se
    # ejecutarán si este módulo es importado. ¿Por qué?
    # Entrada
    n = int(input("Ingrese un número entero positivo: "))

    # Procesamiento
    res = sumatoria(n)

    # Salida
    print("La productoria de los", n, "primeros números es:", res)
```
***Código 1:**Código base con una sumatoria*

Usando como base este código, escribe una función llamada `productoria` que, recibiendo el mismo tipo de entrada, retorne un número que represente la productoria del número 1 al número ingresado.

## Entrada

La entrada a la función, siempre será un número entero positivo.

## Salida

La salida debe ser la productoria del número ingresado.

## Pista

* 

## Consideraciones 
* Para este caso pueden generar un bloque principal para ayudarse en el desarrollo de la función solicitada, pero este no será considerado en los test de la plataforma, ósea se evaluará sólo la función solicitada por medio de los test. Para el correcto funcionamiento de esto debe procurar no cambiar el nombre de las funciones solicitadas.

## Ejemplos 

### Ejemplo 1

Entrada a la función:
```
2
```
Lo que debe retornar:
```
2
```

### Ejemplo 2

Entrada a la función:
```
15
```
Lo que debe retornar:
```
1307674368000
```