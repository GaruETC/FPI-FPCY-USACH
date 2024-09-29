![logo](./assets/logo_usach.png)
# VALIDACIÓN DE ENTRADAS NUMÉRICAS

El código presentado a continuación tiene por objetivo validar que un número recibido sea un entero. Usando como base este código, modifícalo para que valide que el número sea un flotante (positivo o negativo).

Nota que el programa pedirá al usuario ingresar valores hasta que el número ingresado sea válido. Cada vez que el valor ingresado sea incorrecto, el programa imprime: `¡Error de ingreso! `. Cuándo el valor ingresado sea el correcto, el programa imprime: `Se ha obtenido el número: <número>`.


## Entrada

Recibirás una cantidad indeterminada de *strings* hasta recibir una entrada válida.

```
.343.55
-4,423
-45
```

## Salida

```
¡Error de ingreso!
¡Error de ingreso!
Se ha obtenido el número: -45.0
```

## Ejemplos

### Ejemplo 1

Entrada:
```
-4..0
-4..0
-4.0
```
Salida:
```
¡Error de ingreso!
¡Error de ingreso!
Se ha obtenido el número: -4.0
```

### Ejemplo 2

Entrada:
```
-21.9
```
Salida:
```
Se ha obtenido el número: -21.9
```
