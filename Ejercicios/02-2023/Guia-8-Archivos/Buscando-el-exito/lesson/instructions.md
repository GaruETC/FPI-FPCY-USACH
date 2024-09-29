![logo](./assets/logo_usach.png)

# Buscando el 7.0

Se le ha puesto en un desafio de encontrar un 7.0 para un ejercicio de la nota de guías. Para esto se han dispuesto n archivos de texto plano. Cada archivo tiene un nombre que va desde el `"1.txt"` hasta el `"<n>.txt"`. En cada archivo solo hay escrito una línea que es un 1.0, pero hay uno de los n archivos que contiene un 7.0. Su misión es crear la función `buscar(numero)` que recibe la cantidad de archivos existentes y entrega como retorno el nombre del archivo que contiene la nota que desea obtener (en este caso el 7.0). 

## Entradas

Un número natural que representa la cantidad de archivos a manejar. 
```
buscar(<numero de archivos a trabajar>)
```

## Salida

Un string que indique el nombre del archivo que contiene el 7.0.
```
<nombre del archivo con el 7.0>
```

## Consideraciones o Restricciones
- Los nombres de los archivos siempre parten del `"1.txt"` y termina con el `"<n>.txt"` siendo `<n>` el número de archivos a trabajar.
  - Ejemplo:
    Si el número de archivos es 4, los nombres de los archivos serían: `"1.txt"`, `"2.txt"`, `"3.txt"` y `"4.txt"`.
- En los archivos solo hay una línea y esta es `"1.0"` o `"7.0"`.
- Solo hay un 7.0, todos los demás archivos son 1.0

## Ejemplo

Si el contenido de los archivos fuese el siguiente:

- Archivo `"1.txt"`: `1.0`
- Archivo `"2.txt"`: `1.0`
- Archivo `"3.txt"`: `7.0`
- Archivo `"4.txt"`: `1.0`

Entrada:
```
buscar(4)
```

Salida:
```
3.txt
```
