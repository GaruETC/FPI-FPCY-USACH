![logo](./assets/logo_usach.png)

# Cálculo de Promedio Semestral

Crea un programa que calcule el promedio semestral de un o una estudiante, pidiéndole el nombre y cada una de las notas individuales. El promedio es ponderado y la siguiente tabla muestra estas ponderaciones:
| Evaluación | Porcentaje |
|------------|------------|
| Tarea 1    | 10%        |
| Tarea 2    | 20%        |
| Tarea 3    | 30%        |
| Controles  | 15%        |
| Guías      | 25%        |

Recuerda que los promedios se calculan con solo un decimal.

## Entradas

Las entradas corresponden al nombre del o la estudiante y sus notas:
```
Nombre: <nombre>
Tarea 1: <nota>
Tarea 2: <nota>
Tarea 3: <nota>
Controles: <nota>
Guías: <nota>
```

## Salida

La salida es el siguiente mensaje con el promedio calculado:
```
<nombre>, tu promedio es <promedio>.
```

## Consideraciones
- Para redondear, usa la función `round(n, d)`, que redondea `n` a `d` decimales.

## Ejemplos

### Ejemplo 1
Entrada:
```
Nombre: Fulano
Tarea 1: 5.0
Tarea 2: 6.5
Tarea 3: 4.0
Controles: 5.5
Guías: 6.0
```

Salida:
```
Fulano, tu promedio es 5.3
```

### Ejemplo 2
Entrada:
```
Nombre: Perengana
Tarea 1: 6.5
Tarea 2: 6.0
Tarea 3: 7.0
Controles: 5.5
Guías: 6.5
```

Salida:
```
Perengana, tu promedio es 6.4
```
