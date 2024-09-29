![logo](./assets/logo_usach.png)
# NOT THE BEES, NOT THE BEES!!!

[Nic Cage es un actor conocido por su odio a las abejas](https://www.youtube.com/watch?v=EVCrmXW6-Pk). Sin embargo, a través de los años, ha podido superar diversos enfrentamientos con ellas, usando fuego para espantarlas y desarrollando tolerancia a ellas.

En este ejercicio, se te solicita implementar el *Bee Attack Simulator 9000*, que simulará un escenario en el que Nic Cage será atacado con abejas.

Tu programa recibirá un *string* representando el escenario y deberá indicar cuántas abejas conseguirán atacar a Nic Cage. Para ello, recibirás un único string donde:
* El caracter `N`, representará al único e inigualable Nic Cage.
* Los caracteres `b`, representarán a las abejas, las villanas de esta historia.
* Los caracteres asterisco (`*`), representarán hogueras, las cuales nuestro héroe encendió para mantener a las abejas a raya.

Para determinar si el gran Nic Cage sobrevive, consideraremos que las abejas podrán atacarlo si no hay hogueras entre él y las abejas, mientras que, si existe una hoguera entre las abejas y Nic Cage, este se encontrará a salvo de ese grupo de abejas. Por otro lado, en el año 2023 después de Cristo, nuestro héroe tiene la capacidad de sobrevivir cualquier ataque de 5 abejas o menos. En caso contrario, no sobrevivirá.

En caso de que nuestro héroe sobreviva, el programa deberá imprimir el mensaje `Nic Cage ha sobrevivido al ataque de <X> abejas`, donde `X` es la cantidad de abejas que efectivamente consiguen atacarlo, mientras que, si no sobrevive, se deberá imprimir el mensaje `Nic Cage no lo consiguió, <X> abejas pudieron superarlo`.

## Entrada

La entrada será un *string* que representará el escenario a simular, por ejemplo:

```
bbbb*Nbb***bbbbb*bbb
```

## Salida

```
Nic Cage ha sobrevivido al ataque de 2 abejas
```

En este caso, como hay una hoguera entre las primeras 4 abejas y Nic Cage, estas no pueden atacarlo. Lo mismo ocurre para el grupo de 5 abejas y de 3 abejas. En todos los casos, estas no pueden alcanzar a Nic Cage, por lo que este solo debe enfrentarse a dos abejas. Con lo cual consigue sobrevivir.

## Restricciones

* Siempre habrá un único caracter `N` en el string.

## Ejemplos

### Ejemplo 1
Entrada:
```
bbbb*Nbb***bbbbb*bbb
```
Salida:
```
Nic Cage ha sobrevivido al ataque de 2 abejas
```
### Ejemplo 2

Entrada:
```
bbbbbb*bb*bbbbNbbbbb
```
Salida:
```
Nic Cage no lo consiguió, 9 abejas pudieron superarlo
```
