![logo](./assets/logo_usach.png)

# Password Generator 8000

La seguridad informática es muy importante, pues nuestros datos son los que están expuestos, si no somos cuidadosos y los protegemos detrás de contraseñas seguras.

Una forma de generar contraseñas es a través de procesos aleatorios o pseudoaleatorios. Utilizando el módulo random, genere una contraseña aleatoria a partir de dos parámetros, que indican el largo mínimo y el largo máximo de esta, donde el mínimo es 8 por defecto. La función debe llevar por nombre `gen_pw` y cumplir con las siguientes reglas:
1. Debe tener al menos una letra minúscula de la tabla  ASCII (es decir, sin tildes).
2. Debe tener al menos una letra mayúscula de la tabla ASCII (es decir, sin tildes).
3. Debe tener al menos un número.
4. Debe tener al menos un símbolo entre ?, !, @, #, $, %, ^, & y *.
5. La cantidad de caracteres debe estar entre los parámetros entregados.
6. No puede tener la misma cantidad de tipos de caracteres (es decir, si la clave tiene ocho caracteres, no puede tener dos mayúsculas, dos minúsculas, dos números y dos símbolos).


## Entradas

La función debe tener dos entradas, una obligatoria, correspondiente a un número entero que representa la cantidad máxima de caracteres en la contraseña a generar, y otro opcional, con la cantidad mínima, que por defecto debe ser 8.

## Salida

Un string con la contraseña generada, cumpliendo las reglas señaladas previamente.

## Consideraciones
- Si bien la mejor alternativa para generar secuencias [criptográficamente seguras](https://stackoverflow.com/a/47882876) en Python es la biblioteca [`secrets`](https://docs.python.org/3/library/secrets.html), en este ejercicio se utilizará la biblioteca [`random`](https://docs.python.org/3/library/random.html).
- La evaluación de las contraseñas generadas en este problema, como son aleatorias, será con mecanismos que determinen la validez de la respuesta entregada, en lugar de comparación de respuestas exactas.
- Si la cantidad máxima de caracteres es menor que la cantidad mínima, se debe entregar un string vacío como respuesta.

## Ejemplos

### Ejemplo 1
Entrada:
```python
gen_pw(10)
```

Salidas de ejemplo tras llamar a la función cinco veces:
```python
'31T??ak!w#'
'y58N5$77'
'Ppb@6b3$V6'
'x8TAVrQ^1h'
'G4xhn9#l58'
```

### Ejemplo 2
Entrada:
```python
gen_pw(16, 8)
```

Salidas de ejemplo tras llamar a la función cinco veces:
```
'25%%!iAqdpm',
'1vel2LR6JiWw@D8V',
'41m%rJ6l*NdesI^',
'2L2?o%DT341!',
'Co2&Dmwe'
```
