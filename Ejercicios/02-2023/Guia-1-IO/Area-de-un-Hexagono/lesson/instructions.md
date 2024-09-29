![logo](./assets/logo_usach.png)

# Área de un Hexágono

Se puede calcular el área de un hexágono regular a partir de su lado *l* utilizando la fórmula
```
        3*sqrt(3)
A = l^2 ---------
            2
```
donde `a^b` significa "a elevado a b" y `sqrt(x)` es la raíz cuadrada de `x`.

Escriba un programa que calcule el área de un hexágono regular a partir de su lado, redondeado a dos decimales.

## Entradas

La entrada corresponde al lado del hexágono regular:
```
<lado>
```

## Salida

La salida corresponde a un mensaje que entregue el área calculada:
```
El área es <área>
```

## Consideraciones
- Recuerda que la raíz cuadrada corresponde a elevar a 1/2.
- Para redondear, utiliza la función `round(n, d)`, que redondea el número `n` a `d` decimales.
- Ten en cuenta que la medida del lado de un hexágono es un número real positivo.

## Ejemplos

### Ejemplo 1
Entrada:
```
1
```

Salida:
```
El área es 2.6
```

### Ejemplo 2
Entrada:
```
5
```

Salida:
```
El área es 64.95
```
