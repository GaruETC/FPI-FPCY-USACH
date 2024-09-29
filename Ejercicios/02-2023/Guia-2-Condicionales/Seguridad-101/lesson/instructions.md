![logo](./assets/logo_usach.png)

# Seguridad 101

En la era digital en la que vivimos, la seguridad en línea es más importante que nunca. Las contraseñas son una de las principales medidas de seguridad que se utilizan para proteger
nuestras cuentas en línea. Sin embargo, muchas personas no toman en serio la seguridad de sus contraseñas, lo que puede poner en peligro no solo su propia información personal, sino también la información de otras personas.

Los riesgos de tener una contraseña vulnerable son muchos. Un atacante puede robar una contraseña débil para acceder a una cuenta y robar información personal, como nombres, direcciones, números de teléfono, direcciones de correo electrónico y contraseñas de otras cuentas. En casos más graves, los atacantes pueden atacar esas contraseñas débiles para acceder a información confidencial, como datos bancarios o de tarjetas de crédito.

Se le solicita crear un programa que reciba una contraseña y validar que cumpla los siguientes criterios:
- Debe tener un largo de ocho caracteres exactos.
- Una vez validado eso debe comprobar la composición de la contraseña, validando que posea al menos una minúscula, una mayúscula, una letra, un dígito, una coma y un punto y coma. En caso no cumplir estos criterios, debe mostrar los siguientes mensajes, según corresponda en el orden presentado:
    - Debe tener al menos una minúscula.
    - Debe tener al menos una mayúscula.
    - Debe tener al menos una letra.
    - Debe tener al menos una dígito.
    - Debe tener al menos una coma.
    - Debe tener al menos una punto y coma.
- En caso de cumplir todos los criterios descritos, debe mostrar el mensaje:
  ```
  Su password cumple con todas las reglas.
  ```

**Nota**: El problema presentado es con fines pedagógicos, por lo que se redujo la cantidad de caracteres a trabajar a solo 8 para no extender demasiado el desarrollo. Cabe destacar que a 2023, la obtención de una contraseña con 8 caracteres que contenga minúsculas, mayúsculas, números y símbolos se estima en unos 40 minutos, por lo que se recomienda contraseñas más largas y utilizar un segundo factor de autentificación.

## Entrada

Texto que represente una contraseña de ocho dígitos.
```
<password>
```

## Salida

Todos los mensajes que correspondan entre los siguientes, según cuáles criterios no sean cumplidos:

```
Debe tener 8 caracteres.
Debe tener al menos una minúscula.
Debe tener al menos una mayúscula.
Debe tener al menos una letra.
Debe tener al menos una dígito.
Debe tener al menos una coma.
Debe tener al menos una punto y coma.
```

O el mensaje de aceptación de la contraseña:
```
Su password cumple con todas las reglas.
```

**Los mensajes deben aparecer en el orden aquí presentado**. En caso de que no tenga 8 caracteres, las demás condiciones no son validadas (es decir, si no cumple, solo muestra el mensaje respectivo a la condición de 8 caracteres).

## Ejemplos
### Ejemplo 1
Entrada:
```
as;fg,uy
```

Salida:
```
Debe tener al menos una mayúscula.
Debe tener al menos una dígito.
```

### Ejemplo 2
Entradas:
```
asdfg,uy
```

Salida:
```
Debe tener al menos una mayúscula.
Debe tener al menos una dígito.
Debe tener al menos una punto y coma.
```

### Ejemplo 3
Entrada:
```
kg,uGa9;
```

Salida:
```
Su password cumple con todas las reglas.
```
