![logo](./assets/logo_usach.png)

# Distancia de Números

Se busca determinar si los números cumplen con una distancia entre ellos. Se considera la distancia entre dos números como el valor absoluto de la resta entre ambos. 

El programa debe indicar cuántos pares de números dentro de un conjunto cumplen con una cierta distancia.

## Entradas

Se deben recibir dos entradas, la primera es una serie de números separados por espacios. La segunda entrada es un número entero positivo que representa la distancia buscada. Se deben pedir las entradas con los mensajes: `"Ingrese los números separados por espacios: "` e `"Ingrese la distancia: "`, respectivamente.
```
Ingrese los números separados por espacios: <serie de números>
Ingrese la distancia: <número>
```

## Salida

Debe indicar solamente un número que es la cantidad de pares de números cumplen con la distancia buscada.
```
<resultado>
```

## Consideraciones
- Cada *par* de números debe ser contado solo una vez, pero cada número individual puede ser parte de varios pares dentro de la serie. Por ejemplo, si tiene los valores 1, 2 y 3, los pares son (1, 2), (1, 3) y (2, 3).
- Como pueden estar repetidos los números, debe contar cada par de elementos que cumpla la distancia, incluso si el par ha sido considerado previamente. Por ejemplo, si tiene los valores 1, 1 y 2, los pares posibles son (1, 1), (1, 2) ---con el primer 1--- y (1, 2) ---con el segundo 1.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese los números separados por espacios: 2 4 0 16 14 25 60 84 23 27 90
Ingrese la distancia: 2
```

Salida:
```
5
```
**Explicación:** Hay 5 pares de números que cumplen con tener distancia 2: 
- 4 y 2
- 2 y 0
- 16 y 14
- 25 y 23
- 27 y 25



### Ejemplo 2
Entrada:
```
Ingrese los números separados por espacios: 2 4 6 8 12 6 5 5 4 3
Ingrese la distancia: 3
```

Salida:
```
6
```
**Explicación:** Hay 6 pares de números que cumplen con tener distancia 3: 
- 2 y 5
- 2 y 5
- 6 y 3
- 8 y 5
- 8 y 5
- 6 y 3
