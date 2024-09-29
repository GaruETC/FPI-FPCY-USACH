![logo](./assets/logo_usach.png)

# Palabras con Vocal

El código presentado tiene por objetivo recibir 10 palabras, guardarlos en una lista y, finalmente,  mostrar los elementos de la lista por pantalla.

```python
# CÓDIGO BASE 
#Entrada

lista = []
while len(lista) < 10:
    lista.append(input("Ingrese una palabra: "))

#Salida
for e in lista:
    print(e)
```

Usando como base este código, modifíquelo para que muestre las palabras que comiencen en vocal.

## Entradas

La entrada son 10 palabras. Se solicitan con el texto `'Ingrese una palabra: '` con mayúscula al inicio y un espacio luego de los dos puntos.
```
Ingrese una palabra: <palabra>
```

## Salida

La salida debe ser solo las palabras de la lista  que comiencen en vocal, en el mismo orden que se ingresaron.
```
<palabra con vocal 1>
<palabra con vocal 2>
<palabra con vocal 3>
...
<palabra con vocal n>
```


## Consideraciones o Restricciones
- Las palabras están en español y pueden estar escritas en mayusculas o minúsculas.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese una palabra: casa
Ingrese una palabra: perro
Ingrese una palabra: árbol
Ingrese una palabra: isla
Ingrese una palabra: oso
Ingrese una palabra: silla
Ingrese una palabra: mesa
Ingrese una palabra: hipopótamo
Ingrese una palabra: gato
Ingrese una palabra: león
```

Salida:
```
árbol
isla
oso

```

### Ejemplo 2
Entrada:
```
Ingrese una palabra: Árbol
Ingrese una palabra: Abeja
Ingrese una palabra: Bicicleta
Ingrese una palabra: Cebra
Ingrese una palabra: Dorado
Ingrese una palabra: Elefante
Ingrese una palabra: Fútbol
Ingrese una palabra: Guitarra
Ingrese una palabra: Héroe
Ingrese una palabra: Isla
```

Salida:
```
Árbol
Abeja
Elefante
Isla
```
