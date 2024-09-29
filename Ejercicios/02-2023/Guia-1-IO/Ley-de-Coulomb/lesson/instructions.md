![logo](./assets/logo_usach.png)

# Ley de Coulomb

El módulo de la fuerza entre dos cargas eléctricas estacionarias (fuerza electrostática) se puede calcular a partir de la ley de Coulomb:

```
      q_1 * q_2
F = k ---------
         r^2
```

donde `q_1` y `q_2` son las cargas en la interacción y `r` es la distancia entre ellas. Por su parte, `k` es la constante de Coulomb y equivale en el Sistema Internacional a 8.987*10^9 [N m^2/C^2].

Escribe un programa que, a partir de las cargas y la distancia entre ellas, calcule la fuerza electrostática entre ellas.

## Entradas

Las entradas corresponden a tres números reales que son, en orden, las dos cargas y la distancia:
```
<carga 1>
<carga 2>
<distancia>
```

## Salida

La salida es la fuerza electrostática calculada entre ambas cargas, redondeada a dos decimales:
```
<Fuerza electrostática>
```

## Consideraciones o Restricciones
- Las unidades de carga y distancia serán dadas en el sistema internacional.
- Para redondear, utilice la función `round(n, d)`, que redondea el número `n` a `d` decimales.

## Ejemplos

### Ejemplo 1
Entrada:
```
4.6e-6
1e-5
1
```

Salida:
```
0.41
```

### Ejemplo 2
Entrada:
```
8e-6
4e-6
0.15
```

Salida:
```
12.78
```
