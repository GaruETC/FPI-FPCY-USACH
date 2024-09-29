![logo](./assets/logo_usach.png)

# WOOSH

Un antiguo hechicero dejó en su tratado de magia "*Quæ est in vita magicis*" la teoría de que el poder de los hechizos reside en cómo se utilizan las vocales para construirlo. Según su teoría:

* Un hechizo es *pulentus* si todas las vocales que se utilizaron en su construcción aparecen en orden alfabético.
* Un hechizo es *bacanus* si las vocales que utiliza aparecen en orden alfabético inverso.
* Un hechizo es *cumast*, si las vocales que utiliza no tienen en orden alguno.

Por ejemplo:
* **occidis simia**, es *bacanus* pues las vocales que tiene están en orden alfabético invertido.
* **modicum cattus**, es *cumast*, pues las vocales no tienen orden alfabético alguno.
* **sedivid oud**, es *pulentus*, pues las vocales aparecen en orden alfabético

Construya un programa en Python que reciba un string y clasifique el hechizo según su tipo.

# Entrada

La entrada será un string, donde todas las letras serán minúsculas y las vocales no tendrán tildes.

```
modicum cattus
```

## Salida

Corresponderá al tipo de hechizo que es, únicamente indicando si es *pulentus*, *bacanus* o *cumast*
  
```
cumast
```

En este caso como las vocales son `'o'`, `'i'`, `'u'`, `'a'` y `'u'`, estas no están en orden alfabético, por lo que el hechizo sería *cumast*.

## Restricciones

* Considere que la entrada siempre contendrá sólo letras en minúscula sin tildes.
* Considere que, si el hechizo tiene una sola letra, por ejemplo, *vini, vidi, vici*, este debería clasificarse como *pulentus*.

### Ejemplo 1
Entrada:
```
occidis simia
```

Salida:
```
bacanus
```

### Ejemplo 2
Entrada:
```
ad infinitum
```

Salida:
```
pulentus
```
