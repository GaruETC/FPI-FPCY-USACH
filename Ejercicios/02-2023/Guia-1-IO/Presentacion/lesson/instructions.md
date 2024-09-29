![logo](./assets/logo_usach.png)

# Presentación

Escriba un programa que, a partir del nombre, apellido y año de nacimiento de una persona, muestre un mensaje en que presente su edad.

## Entradas

El programa recibe dos entradas, una con el nombre y apellido de la persona y otra, con el año de nacimiento:
```
Nombre: <nombre y apellido>
Año de nacimiento: <año>
```

## Salida

Debe mostrar el siguiente mensaje por pantalla:
```
Hola, <nombre>. Tienes <edad> años.
```

Donde `<nombre>` debe ser solo el nombre de la persona y no incluir el apellido.

## Consideraciones
- Poner atención a la ortografía.
- El nombre del usuario siempre será una combinación `nombre apellido` (por ejemplo, `Juanito Pérez`), con una palabra en cada parte. La separación siempre será un único espacio.
- Para el cálculo de la edad, no consideres la fecha exacta de nacimiento, solo la diferencia entre los años y este año (2023).

## Ayuda
- Puedes separar los elementos de un string con el método `split`, que se verá con más detalle cuando veamos la unidad de listas. Por ejemplo,
```python
l = s.split(" ")
print(l[0])
```
separa el string `s` por espacios en la primera línea y en la segunda, muestra el primer elemento de esta separación.

## Ejemplos

### Ejemplo 1
Entrada:
```
Nombre: Juanito Pérez
Año de nacimiento: 1980
```

Salida:
```
Hola, Juanito. Tienes 43 años.
```

### Ejemplo 2
Entrada:
```
Nombre: Felipe Hidalgo
Año de nacimiento: 2001
```

Salida:
```
Hola, Felipe. Tienes 22 años.
```
