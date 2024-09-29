![logo](./assets/logo_usach.png)

# EL CAMPEÓN DE HALTEROFILIA

Según las reglas del levantamiento de pesas, o halterofilia, el ganador es el competidor que levante más peso entre las dos pruebas, el *snatch*, o arrancada, y el *clean and jerk*, o dos tiempos. En el *snatch*, el competidor debe levantar la barra en un único movimiento, donde normalmente levanta menos peso y luego, en el *clean and jerk*, primero levanta la barra hasta los hombros y luego sobre la cabeza.

Para cada caso, los competidores tienen 3 intentos, y su puntaje se calcula como la suma de su mejor *snatch* y su mejor *clean and jerk*.

A partir de esta información, se debe construir un programa que reciba como entrada los datos de competidores de halterofilia y entregue como resultado el campeón y su marca.

Para ello, primero se entregará un `N` indicando la cantidad de competidores, para luego entregar para cada uno los resultados de sus 3 intentos de *snatch* y sus 3 intentos de *clean and jerk*. Con ello, el programa deberá indicar cuál es el número del competidor que ganó y con qué puntaje. El formato de salida debe ser un string de la forma: `El competidor <número> ha ganado con <mejor_snatch + mejor_clean_and_jerk> kg.`, donde se asume que el primer competidor es el 1, el segundo es el 2 y así sucesivamente.

# Entrada

Las entradas serán, primero, un `N` indicando la cantidad de competidores y luego, los 3 puntajes de *snatch* y los 3 de *clean and jerk* de cada uno. Por ejemplo:

```
2
60
61
65
140
0
143
60
0
62
145
147
150
```

En este caso, se reciben dos competidores. Para el primero, sus intentos de *snatch* fueron 60, 61 y 65 y sus intentos de *clean and jerk* fueron 140, 0 (porque falló este intento) y 143. Para el segundo, sus intentos de *snatch* fueron 60, 0 y 62, mientras que sus *clean and jerk* fueron de 145, 147 y 150.

## Salida

```
El competidor 2 ha ganado con 212 kg.
```

En este caso, el ganador sería el jugador 2, pues su puntaje de mejor *snatch* + mejor *clean and jerk* es de 212 (62 + 150), mientras que el del jugador 1 es de 208 (65 + 143).

## Restricciones

* Un intento anulado se ingresará con valor 0.
* El número de competidores siempre será un entero positivo mayor o igual a 1.
* Todos los competidores hacen 3 intentos para cada prueba, si un competidor se retiró, se ingresarán solo 0.
* Pese a que en la prueba olímpica los valores de peso en cada prueba solo pueden ir subiendo, considere para este ejercicio que un intento podría tener menos peso que uno anterior.
* Considere que en caso de empate el competidor que primero levantó el peso máximo gana.

### Ejemplo 1
Entrada:
```
2
60
61
65
140
0
143
60
0
62
145
147
150
```


Salida:
```
El competidor 2 ha ganado con 212 kg.
```

### Ejemplo 2
Entrada:
```
1
90
92
95
200
205
210
```

Salida:
```
El competidor 1 ha ganado con 305 kg.
```
