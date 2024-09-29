![logo](./assets/logo_usach.png)

# Power Sets

Se conoce como **conjunto potencia** al conjunto de subconjuntos de un conjunto particular. Toma este nombre de que su cardinalidad es la enésima potencia de dos (`2**n`), donde *n* corresponde a la cantidad de elementos del conjunto.

Adicionalmente, se conoce como **orden lexicográfico** a la generalización del «orden alfabético» al que estamos habituados a los elementos de un conjunto totalmente ordenado. Se crea comparando todos los subelementos de cada elemento a ordenar y ordenando según cuál subelemento venga primero (como en  un diccionario). Por ejemplo, la palabra "pato" viene después de "orégano", porque la "p" (primer subelemento de la primera palabra) viene después de la "o" (primer subelemento de la segunda palabra). Por otra parte, "pata" viene antes de "pato", pues los primeros tres subelementos son iguales, pero el cuarto los distingue: "a" viene antes de "o". En este tipo de orden, "ala", por ejemplo, viene antes de "alas", pues "ala" no tiene un cuarto subelemento, mientras que "alas", sí, así que se considera que esta carencia de cuarto elemento tiene prioridad. De este modo, un string vacío  (`""`) vendría antes que cualquier otro string.

Con estos antecedentes, crea una función que tome un conjunto de caracteres como string y entregue como salidad el conjunto potencia de este ordenado lexicográficamente.

Por ejemplo, si la entrada es el conjunto `"abc"`, la salida es:
```python
['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
```

Nota que los elementos siguen el orden descrito más arriba.

## Entradas

La función tomará como entrada un string de largo arbitrario. Su encabezado es el siguiente:

```python
def power_set(s)
```

## Salida

La función debe retornar una lista de strings con las combinaciones encontradas y ordenadas según lo pedido.

## Consideraciones
- Nota que el string vacío (representando la ausencia de elementos) **es** un subconjunto de todo conjunto, por lo que debe estar en todas las respuestas entregadas.
- Dado que la entrada son conjuntos, no tendrán elementos repetidos.

## Ayudas
- Considera dejar fijo un caracter y generar recursivamente todas las combinaciones a partir de ese caracter.
- Podría ser necesario mezclar ciclos con recursión para resolver este problema.

## Ejemplos

### Ejemplo 1
Entrada:
```python
power_set('1+a')
```

Salida:
```python
['', '+', '+1', '+1a', '+a', '1', '1a', 'a']
```

### Ejemplo 2
Entrada:
```python
power_set('bajo')
```

Salida:
```
['', 'a', 'ab', 'abj', 'abjo', 'abo', 'aj', 'ajo', 'ao', 'b', 'bj', 'bjo', 'bo', 'j', 'jo', 'o']
```
