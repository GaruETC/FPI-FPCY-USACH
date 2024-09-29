![logo](./assets/logo_usach.png)

# Mejor Jugador del Equipo

Se busca obtener el mejor jugador de cada equipo. Para esto se tiene la información de cada usuario, la cual cuenta con el identificador del usuario, el equipo al que pertenece y el puntaje de ese jugador. 

## Entradas

Se recibe un único texto con toda la información dónde los datos de un jugador se componen por id de usuario, equipo y puntaje y estan separados por comas `,`. Los jugadores están separados entre si por un pipe `|`. Los datos se solicitan con el mensaje `"Ingrese los datos: "`
```
Ingrese los datos: < datos separados por | >
```

## Salida

Debe mostrar al jugador con mayor puntaje en cada equipo con el siguiente formato "`<Team>: <id de usuario> con <puntaje> pts`". Los equipos deben mostrarse en el mismo orden que aparecen en la entrada.

```
El cociente es <resultado>.
```


## Consideraciones 
- En caso de que varios jugadores del mismo equipo tengan el mejor puntaje, se debe mostrar solo el primero según el orden que según el orden en que se encuentran en la entrada.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese los datos: user6968,Team_1,748324|user9678,Team_13,799168|user2786,Team_12,221963|user4208,Team_4,489688|user8286,Team_2,710959|user1666,Team_8,693580|user3435,Team_0,909200|user7561,Team_0,580286|user3323,Team_2,445777|user6203,Team_4,625216
```

Salida:
```
Team_1: user6968 con 748324 pts
Team_13: user9678 con 799168 pts
Team_12: user2786 con 221963 pts
Team_4: user6203 con 625216 pts
Team_2: user8286 con 710959 pts
Team_8: user1666 con 693580 pts
Team_0: user3435 con 909200 pts
```

### Ejemplo 2
Entrada:
```
Ingrese los datos: user6541,Team_10,613464|user0772,Team_0,683899|user0642,Team_13,354542|user1153,Team_12,778717|user9769,Team_12,280196|user5079,Team_1,16656|user8966,Team_0,800727|user1366,Team_6,219821|user1525,Team_12,433908|user5444,Team_7,823551
```

Salida:
```
Team_10: user6541 con 613464 pts
Team_0: user8966 con 800727 pts
Team_13: user0642 con 354542 pts
Team_12: user1153 con 778717 pts
Team_1: user5079 con 16656 pts
Team_6: user1366 con 219821 pts
Team_7: user5444 con 823551 pts
```
