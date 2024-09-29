![logo](./assets/logo_usach.png)

# NEGAFIBONACCI

La secuencia de Fibonacci se define tradicionalmente en números enteros positivos. Comienza con los números 0 y 1, y luego cada número subsiguiente en la secuencia es la suma de los dos números anteriores. En otras palabras:
    
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) para n ≥ 2

Sin embargo, esta secuencia puede ser extendida lógicamente hacia los negativos despejando en la ecuación:

- F(n-2) = F(n) - F(n-1)

O, de otra forma:

- F(n) = F(n+2) - F(n+1)

De esta forma, puede extenderse como:

- F(-1) = F(1) - F(0) = 1 - 0 = 1
- F(-2) = F(0) - F(-1) = 0 - 1 = -1
- F(-3) = F(-1) - F(-2) =1 -(-1) = 2
- F(-4) = F(-2) - F(-3) = -1 - 2 = -3

A esta secuencia se le conoce como *la extensión de Fibonacci para todo el conjunto de números reales*, pero de cariño le diremos *NegaFibonacci*. Construya un programa en Python que, a partir de F(0) y F(1) conocidos, calcule el *NegaFibonacci* de cualquier número entero negativo.  

## Entrada

La entrada será siempre un número entero negativo, es decir, menor que 0.

```
-4
```

## Salida

  
```
-3
```
En este caso, se imprime -3, dado que el *NegaFibonacci* de F(-4) = F(-2) - F(-3) = -1 - 2 = -3.

## Restricciones

* Considere que la entrada siempre será un número entero negativo.

### Ejemplo 1
Entrada:
```
-1
```


Salida:
```
1
```

### Ejemplo 2
Entrada:
```
-7
```

Salida:
```
13
```
