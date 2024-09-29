![logo](./assets/logo_usach.png)

# Allí ves Sevilla

Un palíndromo (del griego, πάλιν δρóμος, «volver a ir atrás») es una palabra o frase que puede leerse igual de izquierda a derecha y viceversa. Construye una función que verifique si un texto dado como parámetro es palíndromo o no. El código 1 muestra el encabezado pedido.

```python
def is_palindrome(text):
```
*Código 1: Encabezado de la función para detectar un palíndromo*.

## Entradas

La entrada corresponde a un string, llamado `text`.

## Salida

La salida es la comprobación de que el texto es palíndromo (`True`) o no (`False`).

## Consideraciones
- Los espacios, signos de puntuación, etc. no son considerados a la hora de determinar si una frase u oración es un palíndromo. Así, «Roma ni se conoce sin oro, ni se conoce sin amor» es un palíndromo, a pesar de que la coma no queda en la misma posición leyendo al revés, ni las palabras son las mismas.
- Asímismo, los caracteres con tilde (sin incluir la ñ) no se consideran. En español, los caracteres con tilde son á, é, í, ó, ú y ü.
- Claramente, tampoco son consideradas mayúsculas y minúsculas en esta comprobación.

## Ejemplos

### Ejemplo 1
Entrada:
```python
"¿Son mulas o cívicos alumnos?"
```

Salida:
```python
True
```

### Ejemplo 2
Entrada:
```python
"Esto totalmente no es un palíndromo."
```

Salida:
```python
False
```
