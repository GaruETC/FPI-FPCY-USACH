![logo](./assets/logo_usach.png)

# Conteo de Vocales

El código 1 define una función sencilla para contar palabras en un string (bajo la definición ingenua de que estas son separadas entre sí por un espacio).

```python
# Definición de funciones
def contar_palabras(txt):
    return txt.split(' ')


# Entrada
text = input("Ingrese texto: ")

# Procesamiento
palabras = contar_palabras(text)

# Salida
print(palabras)
```
*Código 1: Programa sencillo para contar palabras*

Usando este código como base, construya una función que cuente las vocales del español en un texto. El encabezado esperado de la función se muestra en el código 2.

```python
def contar_vocales(text):
```
*Código 2: Encabezado de la función pedida*

## Entradas

La entrada corresponde a un string, llamado `text`.

## Salida

La salida es un número entero con el total de vocales identificadas en el texto.

## Consideraciones o Restricciones
- El texto puede tener cualquier tipo y cantidad de caracteres, además de cualquier capitalización.
- Las vocales usadas en el castellano son cinco, pero como caracteres, son once: a, e, i, o, u, á, é, í, ó, ú, ü.
- El uso de bloque principal interferirá con la evaluación, pues se utilizan **test unitarios** para evaluar la función en sí. Comente (sensato) o borre (no recomendado) el bloque principal para evaluar la función.
- El error lanzado por la plataforma con elmensaje `RuntimeError: input() lost sys.stdin` señala que el programa esperaba una entrada que no se va a proveer (generalmente ocurre por el uso de `input` de más).

## Ejemplos

### Ejemplo 1
Entrada:
```
A la víbora de la mar, por aquí puede pasar
```

Salida:
```
17
```

### Ejemplo 2
Entrada:
```
Perdí el juego
```

Salida:
```
6
```
