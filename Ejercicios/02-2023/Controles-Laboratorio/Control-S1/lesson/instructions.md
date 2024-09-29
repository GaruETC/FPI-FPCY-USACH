![logo](./assets/logo_usach.png)


# Control 1

## INSTRUCCIONES


* La evaluación, como toda actividad calificada del curso está sujeta a las reglas del [código de honor del curso](https://progra-fing-usach.github.io/2023_2/honor_code). Cualquier falta a ella será sancionada de acuerdo a los procedimientos que ahí se indican.
* La solución debe desarrollarse directamente en Replit y debe entregarse por CampusVirtual. 
* Durante el período de evaluación el estudiante solo puede resolver dudas de enunciado con el profesor de laboratorio.
* El estudiante solo puede usar Replit y el resumen que la coordinación ha subido en Uvirtual. **El uso de cualquier otro instrumento será calificado con la nota mínima. Esto incluye otros códigos previamente hechos en Replit por el estudiante y apuntes de clase**.
* La evaluación es de carácter individual. Cualquier indicio de intervención de otra persona será calificada con nota mínima a la evaluación.
* La entrega de la solución final debe hacerse en el curso de Campus Virtual en el apartado "LABORATORIO -> CONTROL 1". Antes del fin de la hora.
* Entregas que se realicen por vías distintas a Campus Virtual serán calificadas con nota mínima. En caso de que la plataforma presente un problema, puede enviar su archivo como respaldo al correo de contacto del profesor de Laboratorio, y posteriormente subir el archivo a Campus Virtual.
* La subida del archivo es responsabilidad de su autor, por lo que, archivos que no estén en el formato estipulado, que vengan corruptos o con problemas para ser leídos, no serán revisados. 

## ENTREGA 


Se recibirán soluciones hasta el término del horario de clases en la plataforma Campus Virtual, en el espacio habilitado para ello en la pestaña "LABORATORIO -> CONTROL 1".  
Se requiere entregar un único archivo .py con la solución del problema. Este debe ser exactamente idéntico a su última solución en Replit.

Al inicio del archivo .py, se debe añadir el siguiente encabezado del programa, con los datos solicitados para identificar su trabajo (rellene el encabezado del programa con sus datos personales en formato IDÉNTICO al indicado en el ejemplo del código a continuación): 

```python
# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 2-L-1
# PROFESOR DE TEORÍA: FELIPE ROJAS
# PROFESOR DE LABORATORIO: CAMILA RAMIREZ
#
# AUTOR
# NOMBRE: Juan Carlos Pérez González
# RUT: 23.345.432-2
# CARRERA: Ingeniería Civil Mecánica
# <Incluya aquí una breve descripción del programa>

```


Para descargar el archivo, en el proyecto vaya al apartado "Files"

![image](./assets/files.PNG)

Y descargue el archivo en "Download":

![image](./assets/download.PNG)


# **PROBLEMA**

Los números crecientes son aquellos que todos sus dígitos se encuentran ordenados de izquierda a derecha al leerlos, por lo que el siguiente dígito de un número creciente siempre es mayor o igual que el anterior. Por ejemplo el número 1223345.
Los números decrecientes son aquellos que todos sus dígitos se encuentran ordenados descendientemente de izquierda a derecha al leerlos, por lo que el siguiente dígito de un número decreciente siempre es menor o igual que el anterior. Por ejemplo el número 94432211110.

## Entrada
Se entregará solo una entrada con varios números separados por una coma `','`.

#### Ejemplo Entrada
```
82293,18170,41127707,38416,283597688,64947,9438521,85332111,987761,123345799,256,123799,1334778,415336454,830819930,495606946,740645,6757143,998776600,77969,64865180,975300,115558,613654,3520752,66735
```


## Salida

Debe mostrar cuantos números crecientes y decrecientes se ingresaron.
```
crecientes 5
decrecientes 4
```

## Ejemplos

### Ejemplo 1

Entrada:
```
998466065,802812,6993973,238028,2872550,43975854,458612735,6735511,775411100,400371,234689,988765430,8966120
```
Salida:
```
crecientes 1
decrecientes 2
```

### Ejemplo 2

Entrada:
```
81394364,62523844,367185245,787508,24758948,790737,11379,321760,249695666,18818006,80841,44667799,37214956,174897,2537869,3776380,237778,998882220,96523090,12333566,710952371,846,87078,9543331,997543211,3896540,839149692,99873332,1122448,8753138,14478,284948,65555432,55170,34396,262114,1257788,362159,875570,56718107,12234589,7218694,509268,7917850,907609
```

Salida:
```
crecientes 8
decrecientes 5
```
