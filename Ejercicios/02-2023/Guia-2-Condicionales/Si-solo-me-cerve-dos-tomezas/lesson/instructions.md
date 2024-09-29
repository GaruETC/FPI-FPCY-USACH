![logo](./assets/logo_usach.png)

# Si solo me cervé dos tomezas

La universidad está preocupada por el bienestar de sus estudiantes luego de las fiestas patrias, por lo que busca corroborar que se puedan ir correctamente a sus hogares (sobre todo los viernes). Para esto, ha implementado un alcotest, el cual arroja los gramos de alcohol por litro de sangre del estudiante. Lamentablemente los funcionarios encargados de aplicar los test no saben interpretar el resultado, por lo que se le solicita que cree un programa que, dados los gramos de alcohol en la sangre del estudiante, muestre un mensaje representativo de la condición de este.

Para esto se le hace entrega de la siguiente tabla con rangos de valores y el mensaje que debe entregar en cada caso:

| Rango      | Mensaje                            |
|------------|------------------------------------|
|[0.0 - 0.1[ | `"BIEN"`                           |
|[0.1 - 0.2[ | `"HAPPY"`                          |
|[0.2 - 0.3[ | `"AL LÍMITE"`                      |
|[0.3 - 0.5[ | `"BAJO LA INFLUENCIA DEL ALCOHOL"` |
|[0.5 - 0.8[ | `"LLAMANDO AL EX"`                 |
|[0.8 - 1.0[ | `"ESTADO DE EBRIEDAD"`             |
|[1.0 - 3.0[ | `"DANDO JUGO"`                     |
|[3.0 - 4.0[ | `"ESCUCHO BORROSO"`                |
|[4.0 - ∞+ [ | `"¿HAY UN MÉDICO EN LA SALA?"`     |

En caso de ingresar un valor fuera de los rangos esperados, se debe mostrar el mensaje `"MEDICIÓN ERRONEA"`.

## Entradas

El usuario le entrega un número representa la cantidad de alcohol por litro de sangre. Se debe pedir con el mensaje: `"Ingrese los gramos por litro de sangre: "` (Note qu hay un espacio luego del dos puntos):
```
Ingrese los gramos por litro de sangre: <gramos x litros>
```

## Salida

La salida solo debe ser el mensaje correspondiente según la tabla antes presentada. Recuerde que debe respetar el uso de espacios, mayúsculas, símbolos, etc.
```
<Mensaje>
```

## Consideraciones
- El problema presentado es una caricatura y solo tiene el fin de usarse como ejercicio para practicar programación y en ningún caso debe utlizarse para evaluar el estado real de una persona.
- Recuerde que el rango [*a*, *b*[ significa desde *a* hasta *b*, sin incluir *b*.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese los gramos por litro de sangre: 3.7
```

Salida:
```
ESCUCHO BORROSO
```

### Ejemplo 2
Entrada:
```
Ingrese los gramos por litro de sangre: 1.1
```

Salida:
```
HAPPY
```
