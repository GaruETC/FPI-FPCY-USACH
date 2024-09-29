![logo](./assets/logo_usach.png)

# Contar Palabras Extreme

Una de las tareas al estudiar un lenguaje es la frecuencia de las palabras. El ejercicio "Contar Palabras" permitía tener una base de información sobre los textos, pero ahora lo llevaremos un poco más allá.

Se requiere determinar cuál es la frecuencia de las palabras en un archivo de texto plano, para poder obtener las *n* palabras más frecuentes de este. Sin embargo, no sirve cualquier palabra, sino que las más frecuentes que no pertenecen a grupos de palabras extremadamente comunes, como las dadas por el código 1, correspondiente a tipos inválidos de palabras a contar.

```python
INVALID_TYPES = ["Adverb", "Adverb et al.", "Adverb, preposition",
 "Adverb, preposition, et al.", "Adverb, pronoun, et al.",
 "Article", "Coordinator", "Coordinator, adverb, et al.",
 "Determiner", "Determiner, adverb", "Determiner, adverb, noun",
 "Possessive pronoun", "Preposition",
 "Preposition, adverb, coordinator", "Preposition, adverb, et al.",
 "Pronoun", "Pronoun, adverb, et al.", "Pronoun, noun",
 "Subordinator, determiner"]
```
***Código 1:** Lista de tipos inválidos de palabras*

Estos tipos de palabras, como se ve, son demasiado comunes como para contarlos, pues son los principales conectores del lenguaje.

Todos los textos a probar serán en inglés y las palabras más frecuentes de dicho idioma se encuentran tabuladas en el archivo `common_words.csv`, que incluye en la primera columna a la palabra (*Word*), en la segunda su tipo (*Part of Speech*) y en las siguientes, algunas clasificaciones adicionales que no interesan para este problema.

Se te pide construir dos funciones, `get_word_frequency`, para determinar la frecuencia de cada palabra en el archivo, sin contar las que tengan alguno de los tipos a descartar según la lista del código 1, y `get_most_frequent`, para obtener las *n* palabras más frecuentes y su respectiva frecuencia.

## Entradas

Los encabezados de las funciones se dan en el código 2. En el caso de `get_word_frequency`, recibe como entrada el texto de un archivo como string (como la función `readfile` del ejercicio "Contar Palabras") y una "tabla" con las palabras a descartar. Esta "tabla" debe ser equivalente a una lista de listas, donde el primer elemento de cada sublista es la palabra y el segundo, el tipo de palabra.

```python
def get_word_frequency(<texto>, <palabras_a_descartar>):
def get_most_frequent(<palabras>, <frecuencias>, <número de palabras> = 10):
```

Por su parte, la función `get_most_frequent` debe recibir la lista de palabras cuya frecuencia fue obtenida, la lista de frecuencias correlativa para cada palabra (es decir, el *i*-ésimo término de la primera lista tiene la frecuencia dada por el *i*-ésimo término de la segunda) y un número entero opcional, que corresponde a cuántas palabras se requieren y, por defecto, es 10.

## Salidas

En el caso de `get_word_frequency`, su salida son dos listas (es decir, una lista con dos listas) que corresponden la primera a la lista de palabras y la segunda, a la frecuencia de cada palabra en la primera lista (en otras palabrass, la salida de esta función son las entradas de la siguiente).

En el caso de `get_most_frequent`, su salida corresponde también a dos listas, pero con las *n* palabras (con *n* el tercer parámetro) más frecuentes, ordenadas ambas listas de manera correlativa por frecuencia y, si la frecuencia entre dos o más palabras es igual, ordenada de manera alfabética inversa.

## Consideraciones
- La definición de "palabra" de este problema es la misma que la del problema de "Contar Palabras", por lo que puede usar algunas de sus funciones como punto de partida para resolver este.
- Dado que el archivo `common_words.csv` *es* un archivo CSV, puede usar cualquier método que estime conveniente para cargar su contenido (una función propia dedicada, el módulo `csv`, el módulo `pandas`, etc.) y utilizarlo en sus funciones, sin embargo, debe considerar que el método utilizado debe generar algo equivalente a una lista de listas. Es decir, dentro de la función `get_word_frequency`, el segundo parámetro debe poder ser utilizado como si tuviese la forma `[['the', 'Article'], ['be', 'Verb'], ...]`, pues los tests lo entregarán con ese formato a la función.
- Para la salida de la función `get_most_frequent`, considere que si, por ejemplo, encuentra que las palabras "ship", "boat" y "cigar" tienen todas la misma frecuencia, estas deben aparecer en el orden "ship", "cigar", "boat" (a esto nos referimos con orden "alfabético inverso").

## Ejemplo

Suponga que se tiene el archivo `"the_raven.txt"` con la primera estrofa de *El Cuervo*, de Edgar Allan Poe (1809-1849):

```
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
“’Tis some visitor,” I muttered, “tapping at my chamber door—
            Only this and nothing more.”
```

Si este contenido ha sido cargado en la variable `text` y el archivo, en la variable `palabras_comunes`, la llamada de la función `get_word_frequency` sería:
```
get_word_frequency(text, palabras_comunes)
```

Y su salida serían las dos listas siguientes. En primer lugar, para las palabras:
```python
words = ['once', 'upon', 'midnight', 'dreary', 'while', 'i', 'pondered', 'weak', 'weary', 'many', 'quaint', 'curious', 'volume', 'forgotten', 'lore', 'nodded', 'nearly', 'napping', 'suddenly', 'came', 'tapping', 'one', 'gently', 'rapping', 'chamber', 'door', 'tis', 'visitor', 'muttered', 'nothing', 'more']
```
Y para las frecuencias:
```python
frequencies = [1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1]
```

Y si estas son las entradas para `get_most_frequent` y necesitamos las cinco palabras más frecuentes, su llamada se vería, por ejemplo, como sigue:
```python
# Se explicita el valor del parámetro opcional
get_most_frequent(words, frequencies, n=5)
```

Y su salida correspondería a las listas:
```python
['i', 'while', 'tapping', 'rapping', 'door']
[3, 2, 2, 2, 2]
```

Nótese que las palabras están en orden alfabético inverso.
