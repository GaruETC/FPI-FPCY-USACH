![logo](./assets/logo_usach.png)
# 2. El Reality

El director de un canal de TV ~~medio trucho~~ muy prestigioso te ha pedido que implementes el sistema de votación para eliminar participantes de un Reality Show.

En su diseño de Reality Show, las y los participantes votan por una persona a eliminar y quien tenga más votos al final de la ronda de votación es quien deja la Casa Estudio, es decir, el reality.

Para implementar tu programa se te entregarán los nombres de las y los participantes (separados por comas) y luego el voto de cada uno de ellos. Una vez que recibas los votos, debes imprimir el mensaje `Con <numero> votos, la/el participante <nombre> deja la casa estudio!`

## Entrada

Recibirás primero los nombres de los participantes separados por comas en una única línea y luego los votos de cada uno en formato `<Participante X> vota por <Participante Y>`

```
Gandalf,Aragorn,Legolas,Gimli,Boromir,Frodo,Sam,Merry,Pippin
Gandalf vota por Pippin
Aragorn vota por Boromir
Legolas vota por Gimli
Gimli vota por Legolas
Boromir vota por Aragorn
Frodo vota por Boromir
Sam vota por Boromir
Merry vota por Pippin
Pippin vota por Merry
```

## Salida

Una vez que calcules los votos, deberás imprimir: `Con <numero> votos, la/el participante <nombre> deja la casa estudio!`

```
Con 3 votos, la/el participante Boromir deja la casa estudio!
```

En este caso, si contamos los votos:
* Pippin tiene 2 (de Gandalf y Merry)
* Boromir tiene 3 (de Aragorn, Frodo y Sam)
* Gimli tiene 1 (de Legolas)
* Legolas tiene 1 (de Gimli)
* Merry tiene 1 (de Pippin)
Por lo que el perdedor es Boromir con 3 votos.

## Consideraciones

* En caso de que exista empate, el primero que apareció en el listado original es el eliminado.
* Un participante puede votar por sí mismo.
* Siempre se te entregará a lo menos un participante.
* Todos los participantes emitirán un voto válido, es decir, votarán por alguien del listado.
* No debes preocuparte por el sexo de la o el participante, por eso imprimirás `'la/el'`.

## Ejemplos

### Ejemplo 1

Entrada:
```
Alice,Bob,Charlie,David,Eve
Alice vota por Bob
Bob vota por Alice
Charlie vota por David
David vota por Alice
Eve vota por Charlie
```
Salida:
```
Con 2 votos, la/el participante Alice deja la casa estudio!
```

### Ejemplo 2

Entrada:
```
Gandalf,Aragorn,Legolas,Gimli,Boromir,Frodo,Sam,Merry,Pippin
Gandalf vota por Pippin
Aragorn vota por Boromir
Legolas vota por Gimli
Gimli vota por Legolas
Boromir vota por Aragorn
Frodo vota por Boromir
Sam vota por Boromir
Merry vota por Pippin
Pippin vota por Merry
```
Salida:
```
Con 3 votos, la/el participante Boromir deja la casa estudio!
```