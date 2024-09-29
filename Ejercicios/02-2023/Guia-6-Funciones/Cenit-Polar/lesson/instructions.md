![logo](./assets/logo_usach.png)

# Cenit-Polar

Una forma habitual de cifrar mensajes en entornos no informáticos es a través de combinaciones de palabras como *cenit polar*. Lo que se busca es intercambiar las letras de la primera por las correspondientes de la segunda, formando una tabla como la mostrada en el cuadro 1.

|   |   |   |   |   |
|---|---|---|---|---|
| C | E | N | I | T |
| P | O | L | A | R |

***Cuadro 1:** Conversión usando el código CENIT/POLAR*

La lógica detrás de esta tabla es que la letra de una fila es reemplazada por la letra en la columna correspondiente de la *otra* fila. Por ejemplo, si el mensaje contiene una «t» (primera fila), esta se reemplaza por «r», su letra correspondiente en la segunda fila. Por otro lado, si el mensaje tiene una «a» (segunda fila), se reemplaza por una «i», su letra correspondiente en la primera fila. Así, el mensaje «*the game*» se transforma en «*rho gimo*».

Nótese que este cifrado es «bidireccional», pues la misma clave, al aplicarla sobre el mensaje cifrado, entrega el mensaje original.

Un cifrado como este no se logra solo con la combinación CENIT/POLAR, sino que con cualquiera que cumpla tres requisitos:
1) Deben ser dos palabras.
2) Ambas deben tener la misma cantidad de letras.
3) No pueden repetirse las letras, ni en una misma palabra ni entre ellas.

Así, otra combinación posible es *huevo/frito* o el alfabeto al revés (*abcdef...uvwxyz/zyxwvu...fedcba*). Construye una función con el encabezado dado por el código 1 que permita cifrar un texto utilizando la clave solicitada. La función debe verificar que se pueda cifrar con la clave pedida.

```python
def cypher_text(text, key):
```
***Código 1:** Encabezado de la función para cifrar texto*.

## Entradas

Las entradas corresponde al mensaje a cifrar (`text`), como string, y la clave a utilizar (`key`), como lista de dos strings.

## Salida

La salida corresponde al mensaje cifrado, en caso de que la clave sea válida, o el número entero -1, en caso de que las claves sean inválidas.

## Consideraciones
- Lo único que se cifra con este tipo de claves son letras. Números, caracteres especiales, etc., quedan sin modificar.
- Las entradas no llevarán caracteres con tildes y, si lo hicieran, pueden ser tratados como caracteres especiales.
- Debe preservar las mayúsculas, pero las claves deben ser entregadas en minúsculas.

## Ejemplos

### Ejemplo 1
Entrada:
```python
cypher_text(text="Este mensaje debe ser escondido", key=["cenit", "polar"])
```

Salida:
```python
"Osro molsijo dobo sot ospeldade"
```

### Ejemplo 2
Entrada:
```python
cypher_text(text="Este mensaje debe ser escondido", ["clave", "mala"])
```

Salida:
```
-1
```
