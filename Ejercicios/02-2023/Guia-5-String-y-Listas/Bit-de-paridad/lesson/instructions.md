![logo](./assets/logo_usach.png)

# Bit de Paridad

Al momento de enviar información, es necesario tener formas de corroborar que los mensajes son correctos. Una de estas formas es validar un bit de paridad.

Los mensajes están compuestos por una serie de bits (ceros y unos). En particular, un mensaje se compone por 8 bits (conocido como byte), por lo que un mensaje está compuesto por una combinación de 8 ceros y unos. En este mensaje se 'sacrifica' uno de esos bits para realizar una validación utilizando los primeros 7 para el mensaje y el último solo para validar.

La validación que se realiza es que, si el mensaje (los 7 primeros bits) tiene una cantidad impar de unos, el bit de paridad (octavo bit) debe ser un uno y, en caso de que el mensaje tenga una cantidad par de unos, el bit de paridad debiese ser un cero. 

Si se envia lo siguiente: 01101111
- Los primeros 7 son el mensaje: 0110111
- El último bit es el bit de paridad: 1
En este caso el mensaje tiene una cantidad impar de unos, por lo que el bit de paridad debe ser un uno y lo es, por lo que el mensaje es correcto y no hubo un fallo de comunicación.

Si se envía lo siguiente: 11011001
- El mensaje es 1101100
- El bit de paridad es: 1
como el mensaje tiene una cantidad par de unos, el bit de paridad debiese ser un cero, pero no corresponde, por lo que el mensaje está corrupto y hubo un fallo en el envío.

Se le hace entrega de un flujo de mensajes y se necesita validar si se han enviado correctamente clasificando si más de la mitad de los mensajes son correctos o no. 
## Entradas

La entrada es un único texto que contienen varios bytes de información separados por espacios. Se debe solicitar esta entrada con el mensaje: "`Ingrese la serie de mensajes: `".
```
Ingrese la serie de mensajes: <flujo de bytes>
```

## Salida

La salida debe ser el análisis de los mensajes indicando si la cantidad de mensajes correctos es mayor, igual o menor al 50%. Este mensaje debe mostrarse con el siguiente formato:
- En caso que más del 50% sean correctos debe mostrar el mensaje: "`>50% mensajes correctos: <cantidad de mensajes correctos> de <cantidad de mensajes totales>`"
- En caso que sean correctos el 50% debe mostrar el mensaje: "`50% mensajes correctos: <cantidad de mensajes correctos> de <cantidad de mensajes totales>`"
- En caso que menos del 50% sean correctos debe mostrar el mensaje: "`<50% mensajes correctos: <cantidad de mensajes correctos> de <cantidad de mensajes totales>`"

  
```
<Mayor/menor/igual a 50%> mensajes correctos: <cantidad de mensajes correctos> de <cantidad de mensajes totales>
```

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese la serie de mensajes: 00101101 11101000 01001101 00010011 11010011 10000111 00110110 10011000 00101100
```

Salida:
```

>50% mensajes correctos: 5 de 9
```

Explicación:
- 00101101 Correcto (cantidad impar y bit de paridad 1)
- 11101000 Correcto (cantidad par y bit de paridad 0)
- 01001101 Correcto (cantidad impar y bit de paridad 1)
- 00010011 Incorrecto (cantidad par y bit de paridad 1)
- 11010011 Incorrecto (cantidad par y bit de paridad 1)
- 10000111 Correcto (cantidad impar y bit de paridad 1)
- 00110110 Correcto (cantidad par y bit de paridad 0)
- 10011000 Incorrecto (cantidad impar y bit de paridad 0)
- 00101100 Incorrecto (cantidad impar y bit de paridad 0)


### Ejemplo 2
Entrada:
```
Ingrese la serie de mensajes: 11000101 10000101 01100100 01110010 10111110 00001010 11011010 11001000 10111101 00010000
```

Salida:
```
50% mensajes correctos: 5 de 10
```
