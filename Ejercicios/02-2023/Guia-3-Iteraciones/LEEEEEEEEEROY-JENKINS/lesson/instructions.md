![logo](./assets/logo_usach.png)
# LEEEEEEEEEROY JENKINS!

Estás jugando un MMORPG, y junto a tu *party*, se encuentran preparándose para el momento de iniciar un ataque. Mientras esperas vas cargando segundo a segundo tu poder, con el objetivo de tener éxito en el ataque. Sin embargo, para poder realizar el ataque de forma coordinada, con el equipo se pusieron de acuerdo en una señal universal de ataque (`LEEEEEEEEEROY JENKINS!`, como buenas personas de cultura), lo que implica que cuando alguien dice exactamente la señal en el chat, es momento de atacar.

En este caso, deberás construir un programa en Python, que como entrada los mensajes del chat del *party*. Cada vez que la entrada no sea la señal de ataque, duplicarás tu poder, el cuál siempre partirá en 1. Una vez que alguien dice la señal, deberás imprimir: `'AL ATAQUE!!!, CON PODER DE: <PODER>'`, indicando que es momento de atacar e informando a tu *party* el poder que conseguiste preparándote.

## Entrada

Recibirás una cantidad indeterminada de *strings* hasta recibir la señal de ataque `LEEEEEEEEEROY JENKINS!`.

```
Oe, cacharon que pusieron domos?
Si, no caxe cuando llegaron
Alguien seco pa progra?
como modelo de lenguaje natural no puedo responder esa pregunta.
LEEEEEEEEEROY JENKINS!
```

## Salida

```
AL ATAQUE!!!, CON PODER DE: 16
```

En este caso, alcanzas a cargar 4 veces el poder, debido a que:
* En el mensaje: `'Oe, cacharon que pusieron domos?'`, tu poder queda en 2.
* En el mensaje: `'Si, no caxe cuando llegaron'`, tu poder se duplica quedando en 4.
* En el mensaje: `'Alguien seco pa progra?'`, tu poder se duplica quedando en 8.
* En el mensaje: `'como modelo de lenguaje natural no puedo responder esa pregunta.'`, tu poder se duplica quedando en 16.
* Al recibir la señal de ataque, no puedes seguir cargando, por lo que debes imprimir el mensaje y el poder alcanzado.

## Consideraciones

* En todos los casos, existirá un string `'LEEEEEEEEEROY JENKINS!'` al final del proceso.
* Si alguien envía la señal en minúsculas, con un número distinto de `'E'` o cualquier otra variación, dicho mensaje, no se considera la señal de ataque.

## Ejemplos

### Ejemplo 1

Entrada:
```
Preparando snacks para la misión
Estoy listo para atacar, ¿y ustedes?
LEEEEROY JENKINS!
LEEEEEEEEEROY JENKINS!
```
Salida:
```
AL ATAQUE!!!, CON PODER DE: 8
```

### Ejemplo 2

Entrada:
```
Cargando poder
Cargando poder
Cargando poder
Cargando poder
Cargando poder
LEEEEEEEEEROY JENKINS!
```
Salida:
```
AL ATAQUE!!!, CON PODER DE: 32
```
