![logo](./assets/logo_usach.png)

# Paridad de un Número

Escriba un programa que reciba un número (perteneciente a los reales) y determine si es par, impar o no puede ser evaluado. Considere que la paridad de un número solo se define para los números naturales.

## Entradas

La entrada será un número real:
```
<número>
```

## Salida

Corresponde a uno de tres mensajes posibles:
- Si es par: `par`.
- Si es impar: `impar`.
- Si no es entero: `El número no es entero.`.

## Consideraciones
- Un número es par cuando es múltiplo de 2 (es decir, se puede escribir como 2*k*, para *k* entero).
- Un número es múltiplo de otro cuando el resto de la división entera del primero por el segundo es 0, es decir, la división es exacta.
- El número cero (0) es múltiplo de 2, por lo tanto, es par. Si no lo fuera, no existiría un *k* tal que 2*k* fuera 0, pero 2*k* = 0 para *k* = 0, por lo tanto, 0 es par.

## Ejemplos

### Ejemplo 1
Entrada:
```
14
```

Salida:
```
par
```

### Ejemplo 2
Entrada:
```
0.5
```

Salida:
```
El número no es entero.
```
