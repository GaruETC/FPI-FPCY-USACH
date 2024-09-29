![logo](./assets/logo_usach.png)

# Comprobar Serie

Se requiere comprobar que se ingresen todos los valores de una serie en una secuencia. Para esto, cree un programa que pida números enteros hasta ingresar la palabra `'FIN'`. Una vez ingresados todos los valores, indique si se ingresaron todos los números enteros que estén en el rango comprendido desde el número más pequeño ingresado hasta el número más grande ingresado, incluyendo ambos extremos, al menos una vez.

Por ejemplo, para la secuencia de valores `6, 4, 1, 2, 3, 4, 1, 2, 2, 3, 1, 1, 5, 1, 5, 1`, se encuentra que la serie está completa, pues el menor número del rango es 1 y el mayor, 6, y se encuentran todos los números enteros desde 1 a 6 (`Serie completa`). Por otra parte, para la secuencia `6, 5, 3, 1, 2, 1`, la serie no se encuentra completa (`Serie incompleta`), pues el número 4 no se encuentra.

## Entradas

Se ingresan números enteros, uno a uno, hasta que se ingresa la palabra `'FIN'`. Se deben solicitar con el mensaje `"Ingrese un número entero o ingrese 'FIN' para terminar: "`. Note que hay un espacio luego de los dos puntos:
```
Ingrese un número entero o ingrese 'FIN' para terminar: <número o FIN>
```

## Salida

Se debe indicar si están todos los números del rango al menos una vez con el siguiente mensaje:
```
Serie completa
```

En caso contrario, se debe mostrar este otro mensaje:
```
Serie incompleta
```

## Consideraciones o Restricciones
- Deben estar todos los números enteros al menos una vez incluyendo los extremos.
- Los valores de la secuencia pueden estar en cualquier orden y aparecer cada elemento cualquier cantidad de veces.
- La secuencia puede tener cualquier largo.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese un número entero o ingrese 'FIN' para terminar: 3
Ingrese un número entero o ingrese 'FIN' para terminar: 1
Ingrese un número entero o ingrese 'FIN' para terminar: 4
Ingrese un número entero o ingrese 'FIN' para terminar: 5
Ingrese un número entero o ingrese 'FIN' para terminar: 3
Ingrese un número entero o ingrese 'FIN' para terminar: 2
Ingrese un número entero o ingrese 'FIN' para terminar: FIN
```

Salida:
```
Serie completa
```
**Explicación:** El menor número es 1 y el mayor es 5. Se encuentran todos los números del 1 al 5 al menos una vez.

### Ejemplo 2
Entrada:
```
Ingrese un número entero o ingrese 'FIN' para terminar: 23
Ingrese un número entero o ingrese 'FIN' para terminar: 21
Ingrese un número entero o ingrese 'FIN' para terminar: 25
Ingrese un número entero o ingrese 'FIN' para terminar: 25
Ingrese un número entero o ingrese 'FIN' para terminar: 23
Ingrese un número entero o ingrese 'FIN' para terminar: 22
Ingrese un número entero o ingrese 'FIN' para terminar: FIN
```

Salida:
```
Serie incompleta
```
**Explicación:** El menor número es 21 y el mayor es 25. No se encuentran todos los números del 21 al 25 al menos una vez (falta el 24).
