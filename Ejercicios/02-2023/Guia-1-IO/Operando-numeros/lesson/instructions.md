![logo](./assets/logo_usach.png)

# Operando números

En este proyecto, se te presenta un programa que toma dos números y los suma. Actualmente, su interfaz es la siguiente, por ejemplo, si queremos sumar los números 10 y 4:
```
10
4
El resultado es 14
```

Modifica el código para que permita operar la división entre dos números reales y muestre el resultado por pantalla.

## Entradas

La entrada corresponde a dos números, que se recibirán con la siguiente interfaz:
```
Ingrese el dividendo: <dividendo>
Ingrese el divisor: <divisor>
```

Note los espacios entre los mensajes y los valores esperados.

## Salida

La salida corresponde al siguiente mensaje:
```
El cociente es <resultado>.
```

Note que debe incluir un punto al final de las oraciones.

## Consideraciones
- Recuerde que, al especificar la interfaz, los elementos marcados como `<elemento>` deben ser reemplazados por el dato real, *incluyendo* los símbolos `<` y `>`.
- Considere que, si quiere cambiar el separador entre elementos mostrados por `print`, puede usar el parámetro opcional `sep`.
- Los números reales no pueden ser representados de manera exacta, por lo que decida cuál es el tipo de dato que mejor representa los valores a utilizar.
- No haga verificaciones, si el usuario ingresa 0 como divisor, el resultado será un error, sin embargo, todas las entradas para probar serán válidas.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese el dividendo: 10
Ingrese el divisor: 5
```

Salida:
```
El cociente es 2.0.
```

### Ejemplo 2
Entrada:
```
Ingrese el dividendo: 5
Ingrese el divisor: 0.2
```

Salida:
```
El cociente es 25.0.
```
