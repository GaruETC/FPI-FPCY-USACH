![logo](./assets/logo_usach.png)

# Cuentapárrafos

El código entregado, actualmente, tiene funciones para contar las líneas en un archivo, sin embargo, se busca contar los párrafos de un archivo de texto. Modifique el código para que logre su cometido.

Al momento de ser utilizado el código, se llamará a la siguiente línea:

```python
count_paragraphs(readfile(<nombre_archivo>))
```

Usando esta invocación, se necesita que la función `count_paragraphs()` entregue un entero, el cual es la cantidad de párrafos en el archivo.

## Entradas

La función `readfile` tomará como entrada un string con el nombre del archivo a leer.

La función `count_paragraphs` tomará como entrada un string con los contenidos del archivo.

## Salida

La función `readfile` entregará un string con los contenidos del archivo.

La función `count_paragraphs` entregará el total de párrafos (número entero) del archivo.

## Consideraciones
- Los párrafos en los archivos estan separados por una línea en blanco.
- Ninguna de las líneas en blanco contienen ningún caracter, salvo por el salto de línea. Es decir, una línea en blanco se representaría como `"\n"`, en ningún caso `"  \n"`, `" "`, etc.

## Ayuda
- Puede usar el hecho de cómo está compuesta la línea en blanco, junto al que cada línea del archivo termina con `"\n"`, para determinar cómo identificar un párrafo y distinguirlo de otro.

## Ejemplo

Entrada:
Si el contenido de los archivos es:
```
Hola soy un lindo texto que se usa de ejemplo.

Ya no se me ocurre qué escribir...
```

Salida

```
2
```
