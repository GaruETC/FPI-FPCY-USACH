![logo](./assets/logo_usach.png)

# LA OLA

En el ánimo de los juegos panamericanos, hasta los strings quieren hacer *la ola*. Para que ellos lo hagan, se te pide construir un programa en Python que recibe como entrada un `string` y que muestre en cada línea el paso de la ola, caracter a caracter. 

## Entrada

Recibirás un único string de varios caracteres, donde todos los caracteres alfabéticos estarán en minúscula. Por ejemplo:
```
la usachita
```

## Salida

Deberás generar *la ola*, es decir, imprimir en cada línea una copia del string con un solo caracter en mayúsculas, partiendo del primero hasta el último. Por ejemplo:

```
La usachita
lA usachita
la usachita
la Usachita
la uSachita
la usAchita
la usaChita
la usacHita
la usachIta
la usachiTa
la usacHitA
```

## Consideraciones
- En los caracteres en donde no existe una versión del caracter en mayúsculas, igual se imprime una copia del string (como en la tercera línea para el caracter espacio).

## Ejemplos

#### Ejemplo 1

Entrada 1:
```
la usachita
```

Salida 1:
```
La usachita
lA usachita
la usachita
la Usachita
la uSachita
la usAchita
la usaChita
la usacHita
la usachIta
la usachiTa
la usachitA
```

#### Ejemplo 2

Entrada 1:
```
juegos panamericanos santiago 2023
```

Entrada 2:
```
Juegos panamericanos santiago 2023
jUegos panamericanos santiago 2023
juEgos panamericanos santiago 2023
jueGos panamericanos santiago 2023
juegOs panamericanos santiago 2023
juegoS panamericanos santiago 2023
juegos panamericanos santiago 2023
juegos Panamericanos santiago 2023
juegos pAnamericanos santiago 2023
juegos paNamericanos santiago 2023
juegos panAmericanos santiago 2023
juegos panaMericanos santiago 2023
juegos panamEricanos santiago 2023
juegos panameRicanos santiago 2023
juegos panamerIcanos santiago 2023
juegos panameriCanos santiago 2023
juegos panamericAnos santiago 2023
juegos panamericaNos santiago 2023
juegos panamericanOs santiago 2023
juegos panamericanoS santiago 2023
juegos panamericanos santiago 2023
juegos panamericanos Santiago 2023
juegos panamericanos sAntiago 2023
juegos panamericanos saNtiago 2023
juegos panamericanos sanTiago 2023
juegos panamericanos santIago 2023
juegos panamericanos santiAgo 2023
juegos panamericanos santiaGo 2023
juegos panamericanos santiagO 2023
juegos panamericanos santiago 2023
juegos panamericanos santiago 2023
juegos panamericanos santiago 2023
juegos panamericanos santiago 2023
juegos panamericanos santiago 2023
```