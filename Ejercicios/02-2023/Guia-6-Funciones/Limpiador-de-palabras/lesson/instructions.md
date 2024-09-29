![logo](./assets/logo_usach.png)

# Limpiador de Palabras

Una palabra, en escritura, es una unidad que se separa de las demás unidades de un texto mediante «blancos» en la escritura, es decir, espacios en blanco en el texto. Se te pide crear una función que, a partir de un texto, obtenga las palabras en este. El encabezado de la función se muestra en el código 1.

```python
def limpiar_palabras(texto):
```
*Código 1: Encabezado de la función* `limpiar_palabras`.

## Entradas

La entrada corresponde a un string, llamado `texto`.

## Salida

La salida es una lista con las palabras del texto, en el orden de aparición (incluyendo repeticiones).

## Consideraciones o Restricciones
- Los signos de puntuación no son parte de las palabras.
- Considere que los signos de puntuación son los habituales del castellano: coma, punto, punto y coma, signos de exclamación e interrogación (tanto apertura como de cierre), comillas simples y dobles. Las comillas latinas se ignorarán para este problema.

## Ejemplos

### Ejemplo 1
Entrada:
```
A la víbora de la mar, por aquí puede pasar
```

Salida:
```
['A', 'la', 'víbora', 'de', 'la', 'mar', 'por', 'aquí', 'puede', 'pasar']
```

### Ejemplo 2
Entrada:
```
Perdí el juego
```

Salida:
```
['Perdí', 'el', 'juego']
```
