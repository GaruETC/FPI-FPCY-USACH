![logo](./assets/logo_usach.png)

# Costo de Compra

Se requiere calcular el total de una compra de dos productos, para lo que se te pide construir un programa que ayude con ello. El programa debe pedir, en orden, el nombre de un producto, el precio unitario (en euros) y la cantidad. Esto lo hará para dos productos y mostrará el total para cada producto, el total de la compra y el impuesto pagado (19%).

## Entradas

Las entradas son el nombre de cada producto, su precio unitario en euros y su cantidad:
```
<Nombre de producto 1>
<Precio de producto 1>
<Cantidad de producto 1>
<Nombre de producto 2>
<Precio de producto 2>
<Cantidad de producto 2>
```

## Salida

La salida es un mensaje en varias líneas que contenga el precio total por producto redondeado a dos decimales (uno por línea) y una línea con el total y cuánto IVA se pagó (también redondeado a dos decimales):
```
El total para <Nombre de producto 1> es <total del producto 1>.
El total para <Nombre de producto 2> es <total del producto 2>.
El valor total de la compra es <total>, con <impuesto> en impuestos.
```

## Consideraciones
- Los euros consideran hasta centavos (es decir, su unidad más pequeña es 0,01, correspondiente a un centavo de euro).
- El IVA está incluido en el precio de los productos, tu deber es calcular cuánto del precio final corresponde al IVA. En otras palabras, el total es 1,19 veces el valor real y la diferencia con este es el IVA que debes reportar.
- Para redondear, usa la función `round(n, d)`, que redondea `n` a `d` decimales.
- Redondea cada total que calcule, no solo al final. Es decir, el total del producto 1 debe ser calculado redondeado a dos decimales, al igual que el total del producto 2, el total de ambos y los impuestos.

## Ejemplos

### Ejemplo 1
Entrada:
```
Cafetera
49.99
2
Café en grano
9.99
5
```

Salida:
```
El total para Cafetera es 99.98.
El total para Café en grano es 49.95.
El valor total de la compra es 149.93, con 23.94 en impuestos.
```

### Ejemplo 2
Entrada:
```
Polera
12.99
3
Jeans
34.95
2
```

Salida:
```
El total para Polera es 38.97.
El total para Jeans es 69.9.
El valor total de la compra es 108.87, con 17.38 en impuestos.
```
