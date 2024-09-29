![logo](./assets/logo_usach.png)

# Cálculo de Promedio Semestral 2

Se desea poder saber la situación de cátedra de un estudiante dadas sus notas durante el semestre. Las notas comprenden el promedio de actividades en clases, el promedio de las guías semanales y las notas de la tarea 1, tarea 2 y tarea 3. Las ponderaciones de cada uno de estos items son las siguientes:

* 15% Promedios de Actividades en clases
* 25% Promedio de Guías
* 10% Tarea 1
* 20% Tarea 2
* 30% Tarea 3

En caso de obtener promedio 3.95 o superior, se aprueba la cátedra. En caso de no aprobar existe un examen, el examen (EAO) puede ser rendido por los estudiantes que tengan promedio igual o superior a 2.95 y no tengan faltas al código de honor. En caso de rendir el examen, la nota se calcula ponderando con 60% el promedio durante el semestre y con 40% nota del examen.

Se le solicita crear un código que reciba el promedio de actividades en clases, el promedio de las guías, nota tarea 1, nota tarea 2, nota de tarea 3 y si ha cometido faltas al código de honor, y entregue como respuesta la situación del estudiante.

## Entradas

Las entradas corresponden a cada una de las notas con un decimal, además de la respuesta a si ha faltado al código de honor representada como las palabras `YES` o `NO`, según corresponda:
```
Ingrese el promedio de actividades en clases: <Nota con 1 decimal>
Ingrese el promedio de guías: <Nota con 1 decimal>
Ingrese la nota de la tarea 1: <Nota con 1 decimal>
Ingrese la nota de la tarea 2: <Nota con 1 decimal>
Ingrese la nota de la tarea 3: <Nota con 1 decimal>
Tienes falta al código de honor (YES/NO): <Texto "YES" o "NO">
```
(Note que cada mensaje tiene un espacio luego del dos puntos)

## Salida

La salida corresponde a indicar la situación del estudiante, la cual puede ser:
- `Aprobado/a <promedio>`
- `Reprobado/a <promedio>`
- `Debe rendir examen y necesita al menos un <Nota que necesita en el examen>`

```
`Debe rendir examen y necesita al menos un 5.6`
```

Los datos de promedio y la nota que necesita son números con un decimal de precisión.

## Consideraciones
- Al momento de realizar el cálculo de qué nota se necesita en el examen, realicelos usando como objetivo terminar con promedio 3.95, para así calcular cuál es la menor nota necesaria.
- Tenga en cuenta que, si está calculando la nota necesaria en el examen para obtener promedio final 3.95 y su cálculo obtiene valores con centésimas, milésimas, etc., debe aproximar inmediatamente a la siguiente décima. Ejemplo: si su cálculo obtiene que el alumno necesita en el examen un 3.2036512, eso significa que va a necesitar un 3.3, ya que con un 3.2 no le es suficiente.

## Ayuda
- Recuerde que puede usar la función `round(n, d)` para redondear el número `n` a `d` decimales.
- La función `round` de Python redondea decimales terminados en 5 siguiendo la lógica de acercarse al par más cercano, por lo que, si va a probar los cálculos "a mano", se sugiere usar la misma consola de Python (la que accede con la pestaña llamada `>_ Console`).

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese el promedio de actividades en clases: 3.0
Ingrese el promedio de guías: 3.0
Ingrese la nota de la tarea 1: 3.0
Ingrese la nota de la tarea 2: 3.0
Ingrese la nota de la tarea 3: 3.0
Tienes falta al código de honor (YES/NO): NO
```

Salida:
```
Debe rendir examen y necesita al menos un 5.4
```

### Ejemplo 2
Entrada:
```
Ingrese el promedio de actividades en clases: 3.9
Ingrese el promedio de guías: 3.9
Ingrese la nota de la tarea 1: 3.9
Ingrese la nota de la tarea 2: 3.9
Ingrese la nota de la tarea 3: 3.9
Tienes falta al código de honor (YES/NO): YES
```

Salida:
```
Reprobado/a 3.9
```
### Ejemplo 3
Entrada:
```
Ingrese el promedio de actividades en clases: 4.2
Ingrese el promedio de guías: 4.4
Ingrese la nota de la tarea 1: 1.0
Ingrese la nota de la tarea 2: 4.8
Ingrese la nota de la tarea 3: 5.3
Tienes falta al código de honor (YES/NO): YES
```

Salida:
```
Aprobado/a 4.4
```
