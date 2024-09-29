![logo](./assets/logo_usach.png)

# Calculadora Prefija

Se le pide construir un programa que reciba como entrada una expresión de la forma `<s><a> <b>`, donde `<s>` es un símbolo de operación matemática (`+`, `-`, `*` o `/`) y `<a>`, `<b>` números enteros. El programa debe entregar el resultado de la operación dada por el símbolo `s`, donde todas son las operaciones normales, salvo por `/`, que debe ser la división entera.

Este tipo de notación, que antepone el operador a los operandos, se conoce como notación prefija o polaca (en contraste con la que habitualmente utilizamos, que es la infija). Fue propuesta por el matemático polaco [Jan Łukasiewicz](https://es.wikipedia.org/wiki/Jan_%C5%81ukasiewicz) y tiene la particularidad de no necesitar paréntesis, pero no nos adentraremos en los detalles en este problema.

## Entradas

La entrada es una operación dada como string:
```
Operación:
<símbolo><primer operando> <segundo operando>
```
En la que el símbolo (alguno entre `+`, `-`, `*`, `/`) nunca se separa del primer operando y el segundo está separado del primero por un espacio. Los operandos son números enteros.

## Salida

La salida es el resultado de la operación, que debe corresponder a un número entero:
```
<resultado>
```
A menos que el símbolo ingresado no sea un operador válido, en cuyo caso debe mostrar como salida:
```
Operación inválida
```

## Consideraciones
- Note que tanto los valores de entrada como de salida son números enteros.
- La entrada es un único string que debe separarse.

## Ayuda
- Recuerde que tiene el método `str.split`, que permite separar elementos.
- Note que no debe separar la entrada completa, solo desde el segundo carácter en adelante, pues el primero es el símbolo.
- Si `s` es un string, `l = s.split(" ")` es una lista con los elementos de la separación. Sus elementos se pueden acceder igual que los caracteres en un string.

## Ejemplos

### Ejemplo 1
Entrada:
```
Operación:
+1 2
```

Salida:
```
3
```

### Ejemplo 2
Entrada:
```
Operación:
*-5 8
```

Salida:
```
-40
```
