![logo](./assets/logo_usach.png)

# Tarjeta Adulto Mayor

Se le presenta el siguiente código en este repositorio, que calcula si una persona puede o no beber alcohol, según su edad:
```python
# Constantes
LEGAL_AGE = 18

# Bloque principal
# Entrada
age = int(input("Ingrese edad: "))

# Procesamiento y Salida
if age < LEGAL_AGE:
    print("No está autorizado para beber alcohol.")
else:
    print("Está autorizado para beber alcohol.")
```

Usando este código como base y sabiendo que el Metro de Santiago [entrega la Tarjeta Adulto Mayor](https://www.chileatiende.gob.cl/fichas/7812-tarjeta-adulto-mayor-de-metro-de-santiago) a mujeres de 60 años o más y a hombres de 65 años o más, escriba un programa que determine si una persona califica para obtener esta tarjeta.

## Entradas

Las entradas son el género de la persona y su edad:
```
Ingrese su género: <género>
Ingrese su edad: <edad>
```

El género será solo alguna de las dos opciones validadas por el gobierno, es decir, `mujer` y `hombre`.

## Salida

Un mensaje que indique si califica o no para la tarjeta, que puede ser una de dos opciones. En caso de que califique:
```
Ud. califica para la tarjeta de tercera edad.
```
Y en caso de que no:
```
Ud. no califica para la tarjeta de tercera edad.
```

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese su género: mujer
Ingrese su edad: 35
```

Salida:
```
Ud. no califica para la tarjeta de tercera edad.
```

### Ejemplo 2
Entrada:
```
Ingrese su género: hombre
Ingrese su edad: 76
```

Salida:
```
Ud. califica para la tarjeta de tercera edad.
```
