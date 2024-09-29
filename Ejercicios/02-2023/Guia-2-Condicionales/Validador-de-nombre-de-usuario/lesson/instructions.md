![logo](./assets/logo_usach.png)

# Validador de nombre de usuario

Cierto sitio necesita que los nombres de usuario sean validados de modo que cumplan ciertos estándares. Escriba un programa que valide el nombre de usuario escrito como entrada para que contenga solo caracteres alfanuméricos, tenga un largo mínimo de seis caracteres, no más de 32 y solo el primero sea en mayúsculas.

## Entradas

La entrada corresponde al nombre de usuario a evaluar:
```
Usuario: <nombre de usuario>
```

## Salida

La salida corresponde a una de dos opciones:
- `Válido.`, si este sigue las reglas descritas.
- `Inválido.`, si este no lo hace.

## Consideraciones o Restricciones
- Recuerde que puede usar *slices* para acceder a fragmentos de un string. Por ejemplo, `s[1:]` obtiene todos los caracteres del string, salvo por el primero.

## Ejemplos

### Ejemplo 1
Entrada:
```
Usuario: Juan
```

Salida:
```
Inválido.
```

### Ejemplo 2
Entrada:
```
Terminator420
```

Salida:
```
Válido.
```
