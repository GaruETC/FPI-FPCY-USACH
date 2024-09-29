![logo](./assets/logo_usach.png)

# Sumando 10

Se requiere que cree un programa que reciba un número entero positivo y elimine los pares de dígitos consecutivos que sumen 10. 

Por ejemplo el número `1645`, los digitos `6` y `4` están consecutivos y suman 10 por lo que se borran y queda el número `15`.

Este proceso se debe realizar tantas veces como fuese posible, por ejemplo en el número 427385, el par de dígitos 7 y 3 están consecutivos en el número y suman 10 por que se borran quedando 4285, dónde los dígitos 2 y 8 están consecutivos y suman 10, por lo que se borran quedando 45. Que no puede seguir borrando pares de dígitos. 

## Entradas

se recibe un único número entero positivo con el mensaje "`Ingrese un número entero positivo: `".
```
Ingrese un número entero positivo: <número>
```


## Salida

Se debe mostrar el número original y luego se debe mostrar una vez por cada vez que se borra un par de digitos mostrando como quedó.
```
El cociente es <resultado>.
```

**No deben ir ejemplos de la salida, solo una descripción del tipo de salida y dónde irá o cómo se presentará.**

## Consideraciones o Restricciones
- El par de dígitos a borrar deben ser dos dígitos adyacentes en el número, uno al lado del otro.
- Si hay varios pares que puede borrar, solo debe borrar uno y en la siguiente vuelta puede borrar el otro par. en este caso siempre debe priorisar borrar el primer par que sume 10 según el sentido de lectura de izquierda a derecha.
- Si no queda ningún número debe mostrar una línea en blanco (no un espacio, sino que sin nada).

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese un número entero positivo: 434556713796
```

Salida:
```
434556713796
4346713796
43713796
413796
4196
46
```
Explicación:
Número inicial: `434556713796`
- 434**55**6713796 (si bien 3 y 7 tambien suma 10, 5 y 5 está primero en el sentido de lectura) y queda 4346713796
- 43**46**713796 (se borrará 4 y 6)
- 4**37**13796 (se borrará 3 y 7)
- 41**37**96 (se borrará 3 y 7)
- 4**19**6 (se borrará 1 y 9)
- *46* (se borrará 4 y 6)
- No se puede borrar nada más





### Ejemplo 2
Entrada:
```
Ingrese un número entero positivo: 46564654654684651
```

Salida:
```
46564654654684651
564654654684651
5654654684651
56554684651
564684651
5684651
56851
```
