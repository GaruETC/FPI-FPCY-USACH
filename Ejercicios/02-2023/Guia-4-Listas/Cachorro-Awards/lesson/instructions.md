![logo](./assets/logo_usach.png)

# Cachorro Awards

Se busca dar un reconocimiento a los mejores estudiantes de cada carrera. Para esto, se tienen los datos de varios alumnos, en los que se encuentra el RUN, edad, carrera y 3 notas. El programa debe mostrar el mejor estudiante de cada carrera obteniendo el promedio simple entre las 3 notas.

## Entradas

La entrada es un único texto donde vienen los datos de cada estudiente. cada estudiante viene separado del siguiente por un punto y coma (`";"`) y los datos de un estudiante están separados por comas (`","`). Debe solicitar la entrada con el mensaje `Ingrese los datos de los alumnos: `:

```
Ingrese los datos de los alumnos: <datos de los alumnos>
```

Los datos de cada estudiante vienen ordenados según:
```
<RUT>,<edad>,<carrera>,<nota_1>,<nota_2>,<nota_3>
```

## Salida

Debe mostrar por cada carrera ingresada: el nombre de la carrera seguida de un dos puntos y un espacio (`": "`), el RUN del estudiante, seguido de un espacio y el promedio del estudiante entre paréntesis (`"()"`). Las carreras deben mostrarse en el orden de aparición en el texto de entrada:

```
<carrera>: <RUN> (<promedio>)
<carrera>: <RUN> (<promedio>)
<carrera>: <RUN> (<promedio>)
...
<carrera>: <RUN> (<promedio>)
```

## Consideraciones
- Calcule los promedios con un decimal de precisión.
- En la salida, las carreras deben mostrarse en el mismo orden que aparecen en la entrada.

## Ejemplos

### Ejemplo 1
Entrada:
```
Ingrese los datos de los alumnos: 12.644.426-8,20,Mecánica,4.1,4.2,1.3;18.929.453-1,44,Biomédica,5.6,2.8,6.9;16.384.224-1,30,Telemática,4.3,2.5,3.2;22.863.093-2,31,Eléctrica,5.9,2.1,2.0;28.277.435-K,42,Geomensura,3.5,6.5,5.5;18.813.316-0,39,Mecánica,6.0,4.0,3.2;11.163.727-1,59,Ambiente,1.7,3.4,6.4;13.695.273-0,21,Ambiente,4.0,1.0,3.0;25.456.545-6,26,Eléctrica,1.0,6.1,5.3;12.200.843-5,33,Química,4.9,6.1,6.9;14.857.059-5,23,Industrial,6.1,5.0,4.2;24.423.785-4,40,Biomédica,5.9,4.7,5.1;17.444.941-8,49,Mecatrónica,6.5,4.8,1.4;18.782.221-K,25,Geomensura,4.4,5.8,3.9;14.133.702-0,40,Mecatrónica,4.4,5.0,1.2;19.728.564-2,54,Ambiente,4.7,5.1,6.0;21.290.318-1,56,Eléctrica,4.7,5.3,4.4;21.268.593-5,16,Mecatrónica,3.8,2.9,2.6;21.057.904-4,34,Ambiente,1.2,1.6,2.1;28.749.381-1,55,Industrial,1.0,2.7,4.3;21.456.932-8,44,Geomensura,5.2,2.5,5.6;28.479.104-2,17,Mecánica,2.6,6.8,4.1;22.567.748-5,37,Geomensura,1.1,3.0,3.5;19.393.046-6,24,Metalurgia,6.2,6.3,2.3;27.542.385-6,51,Mecánica,5.1,3.5,5.4;24.364.025-1,46,Geomensura,5.0,1.0,4.6;10.735.004-7,36,Eléctrica,3.0,6.3,4.3;12.670.637-2,62,Industrial,6.5,5.7,2.0;21.015.424-2,47,Mecatrónica,6.8,6.4,6.6;10.819.833-5,45,Geomensura,5.7,1.2,3.3;19.877.059-3,61,Eléctrica,6.6,5.9,3.4;22.982.086-7,46,Informática,2.1,1.8,5.5;13.553.496-K,52,Industrial,6.6,1.2,5.9;18.172.700-2,46,Geomensura,1.0,5.0,1.1;28.355.756-4,20,Ambiente,5.8,3.6,1.9;21.971.302-7,38,Ambiente,4.6,3.0,3.7;15.218.685-1,17,Industrial,4.7,4.4,3.9;22.636.234-0,51,Eléctrica,3.3,3.1,6.8;24.173.394-6,33,Ambiente,5.4,1.1,1.3;16.025.967-5,23,Industrial,5.7,1.1,4.9;17.001.002-3,36,Ambiente,1.4,1.2,6.1;18.341.420-4,47,Geomensura,4.4,6.6,2.9;20.172.164-4,22,Mecánica,4.4,3.1,4.8;28.877.705-8,51,Geomensura,6.6,5.6,5.0;24.219.491-1,32,Química,3.1,1.3,2.7;26.225.082-3,35,Eléctrica,2.6,6.9,5.5;28.290.157-2,32,Mecánica,6.5,4.5,5.7;18.738.141-5,59,Metalurgia,6.8,3.6,6.9;17.922.572-1,21,Industrial,4.2,4.6,1.1;15.647.199-3,40,Minas,4.4,4.8,4.4;25.519.861-7,33,Informática,2.0,5.7,4.4;21.304.132-3,50,Eléctrica,4.4,6.3,3.5;27.008.224-5,49,Mecánica,3.3,2.1,6.3;22.302.868-K,17,Mecatrónica,2.8,6.6,4.2;15.271.307-1,16,Mecánica,4.9,3.2,1.2;29.197.644-8,49,Geomensura,5.9,6.5,5.9;18.045.241-2,31,Química,4.5,2.7,3.9;11.251.085-5,52,Química,3.0,6.1,4.8;21.829.063-4,57,Mecánica,3.9,2.4,2.3;28.493.436-4,63,Biomédica,6.3,3.4,2.0;26.255.488-6,52,Geomensura,3.3,6.0,5.2;17.623.654-5,35,Informática,3.3,3.9,5.0;23.328.517-2,43,Informática,3.8,3.1,1.0;10.383.063-1,49,Geomensura,6.8,1.3,3.5;13.027.221-6,44,Metalurgia,1.5,6.6,2.6;20.054.992-5,54,Informática,3.2,5.0,3.3;28.726.309-5,50,Química,5.8,6.3,6.1;25.190.240-8,61,Mecánica,3.6,6.3,5.8;14.650.814-2,47,Telemática,1.0,6.9,2.8;20.470.047-3,53,Mecánica,3.5,1.5,6.4;29.336.974-8,57,Geomensura,6.3,2.7,6.4;21.465.302-4,46,Industrial,1.2,1.3,3.6;18.439.808-3,21,Telemática,3.7,4.7,4.9;10.649.264-5,64,Industrial,5.4,2.2,2.1;12.382.705-6,38,Metalurgia,5.6,2.4,5.9;21.855.701-7,17,Eléctrica,4.8,3.5,3.4;10.797.473-7,22,Eléctrica,2.9,5.3,6.6;11.884.524-0,39,Biomédica,1.6,2.6,4.2;10.005.689-4,51,Química,1.9,3.5,6.3;22.107.999-1,45,Minas,3.0,3.5,4.9;14.413.226-0,31,Ambiente,5.1,4.6,6.5;27.422.470-2,60,Informática,1.4,3.7,6.9;26.087.012-2,60,Industrial,2.3,2.8,2.1;13.977.034-0,38,Eléctrica,6.8,1.3,4.4;18.482.466-4,46,Minas,5.0,3.1,1.3;20.404.402-2,39,Informática,3.4,1.1,2.8;12.278.994-K,31,Metalurgia,1.0,1.5,1.3;11.337.731-1,47,Mecánica,4.0,6.0,3.7;17.352.053-6,32,Metalurgia,4.4,1.5,6.1;14.379.703-0,25,Mecánica,2.6,1.1,5.7;26.457.781-1,16,Biomédica,1.0,1.3,1.4;13.994.956-0,30,Industrial,5.6,1.9,3.5;20.711.855-2,16,Ambiente,5.6,1.7,4.2;20.130.839-1,19,Metalurgia,4.6,4.7,3.0;29.795.730-1,20,Telemática,5.6,1.8,1.2;27.295.651-8,34,Informática,6.9,5.5,2.7;26.327.179-1,59,Telemática,2.6,1.3,1.5;26.756.521-6,55,Ambiente,3.2,5.6,1.7;21.756.782-7,34,Mecánica,2.9,1.5,3.6;17.224.813-1,59,Mecánica,1.4,1.8,4.8
```

Salida:
```
Mecánica: 28.290.157-2 (5.6)
Biomédica: 24.423.785-4 (5.2)
Telemática: 18.439.808-3 (4.4)
Eléctrica: 19.877.059-3 (5.3)
Geomensura: 29.197.644-8 (6.1)
Ambiente: 14.413.226-0 (5.4)
Química: 28.726.309-5 (6.1)
Industrial: 14.857.059-5 (5.1)
Mecatrónica: 21.015.424-2 (6.6)
Metalurgia: 18.738.141-5 (5.8)
Informática: 27.295.651-8 (5.0)
Minas: 15.647.199-3 (4.5)
```

### Ejemplo 2
Entrada:
```
Ingrese los datos de los alumnos: 29.887.168-6,40,Metalurgia,6.9,5.9,4.9;19.373.087-K,64,Mecánica,4.0,1.3,4.5;27.921.917-2,34,Biomédica,5.3,5.5,6.9;13.803.391-8,37,Telemática,5.0,3.7,1.0;11.985.024-K,33,Geomensura,5.1,4.0,3.9;29.475.461-3,32,Eléctrica,4.4,3.3,2.5;17.597.342-K,63,Industrial,3.5,4.9,2.4;17.048.799-7,21,Ambiente,2.4,5.8,5.4;26.301.322-5,29,Ambiente,3.2,4.3,3.5;16.081.839-7,44,Mecatrónica,5.9,2.3,1.6;18.179.235-3,64,Minas,1.9,3.3,2.5;18.068.887-0,31,Telemática,5.2,5.1,1.8;20.643.360-6,18,Mecánica,4.2,1.2,1.8;16.582.727-4,51,Minas,5.0,5.0,3.1;21.407.234-7,56,Biomédica,3.6,5.9,4.9;12.932.388-7,20,Ambiente,1.4,2.8,2.1;15.290.341-2,20,Industrial,4.2,3.4,1.0;22.868.556-5,31,Minas,2.4,4.4,6.6;28.630.677-0,56,Informática,3.6,6.5,6.9;27.496.424-5,29,Geomensura,1.1,6.7,6.3;13.866.776-0,60,Mecánica,4.7,4.7,1.0;10.488.832-6,20,Eléctrica,2.4,6.0,4.1;16.283.330-6,18,Informática,6.6,4.6,5.4;26.353.099-1,27,Geomensura,1.1,2.1,3.1;14.480.575-0,54,Informática,4.5,3.1,4.8;20.324.883-5,29,Geomensura,5.1,3.2,1.9;21.665.530-7,44,Mecatrónica,6.9,1.7,1.7;10.801.937-5,63,Industrial,2.8,4.2,4.0;29.952.839-6,64,Química,3.5,4.9,5.7;12.719.243-6,50,Geomensura,1.5,1.8,3.5;23.669.371-5,36,Minas,6.2,2.0,6.3;17.074.152-4,42,Mecatrónica,2.5,3.9,6.7;26.001.587-8,16,Ambiente,1.9,2.2,2.3;21.623.680-2,34,Informática,1.8,5.0,6.8;27.367.101-2,23,Mecatrónica,6.8,2.0,4.0;20.455.198-K,28,Eléctrica,2.9,3.5,6.9;25.579.366-3,22,Ambiente,4.8,1.4,5.9;14.847.341-6,32,Química,1.9,4.9,1.0;11.131.053-0,17,Ambiente,3.1,4.8,6.0;14.241.209-K,52,Industrial,1.9,6.8,5.7;17.254.371-6,62,Eléctrica,6.8,6.0,4.8;11.207.423-2,30,Metalurgia,5.4,3.1,5.5;16.740.967-3,63,Informática,4.5,2.7,3.9;29.970.940-8,38,Ambiente,4.7,2.2,3.5;22.354.173-4,37,Telemática,4.2,3.6,4.0;18.216.261-5,57,Industrial,2.8,1.5,6.5;13.442.652-K,65,Telemática,6.6,1.3,5.8;13.220.693-K,17,Geomensura,3.4,4.6,3.3;24.229.332-6,33,Mecánica,1.4,2.2,1.0;24.201.167-8,64,Eléctrica,6.9,6.4,5.4;27.421.841-7,60,Mecánica,6.8,3.3,2.6;20.234.795-4,44,Ambiente,6.9,5.3,3.4;28.014.117-0,27,Eléctrica,2.6,1.6,2.9;26.828.618-5,52,Ambiente,1.4,1.6,1.5;28.609.514-2,19,Industrial,5.4,4.2,1.8;14.322.425-0,38,Informática,4.2,2.3,3.1;15.937.876-1,62,Ambiente,3.0,5.5,2.2;27.939.827-1,20,Biomédica,2.8,3.3,6.4;18.435.504-6,57,Química,3.1,4.1,6.5;22.763.394-5,57,Eléctrica,2.5,3.1,5.3;25.762.346-1,16,Minas,4.9,6.4,3.3;17.296.531-6,46,Mecánica,2.9,6.4,2.5;15.735.706-K,49,Metalurgia,2.8,1.9,4.3;12.118.556-2,47,Telemática,6.5,3.9,3.1;15.031.776-4,50,Mecánica,3.4,5.3,1.2;27.053.795-5,53,Biomédica,2.0,2.0,5.4;21.331.842-4,20,Química,3.0,5.4,1.3;24.496.390-6,34,Informática,6.1,6.8,1.6;26.711.661-2,16,Geomensura,6.4,2.0,3.0;25.270.952-K,64,Geomensura,6.3,6.1,5.5;12.391.440-1,16,Telemática,3.5,1.3,2.4;12.683.199-0,57,Industrial,2.8,6.7,4.7;21.735.697-2,16,Mecatrónica,2.4,2.5,3.6;23.882.414-2,36,Eléctrica,1.0,6.6,1.7;26.793.576-2,50,Industrial,5.6,1.0,6.8;24.573.126-8,62,Química,4.2,6.0,1.9;24.104.617-3,46,Química,1.1,5.0,1.4;19.097.167-2,36,Minas,3.1,2.0,5.8;27.446.704-3,41,Geomensura,6.3,4.3,5.0;21.363.664-8,46,Eléctrica,6.6,5.8,5.0;12.905.530-8,63,Ambiente,1.2,6.4,1.7;15.447.921-5,42,Biomédica,4.0,4.2,5.4;21.626.846-0,47,Metalurgia,3.4,4.4,5.2;20.418.464-3,17,Eléctrica,2.8,2.6,4.7;13.317.297-2,61,Ambiente,2.5,6.3,5.4;25.237.874-1,23,Biomédica,2.7,6.4,6.6;20.337.697-4,44,Minas,4.6,5.2,6.0;16.548.419-1,45,Eléctrica,4.7,6.0,6.7;21.603.727-4,40,Química,6.5,1.0,5.7;10.927.023-6,47,Informática,6.2,2.7,6.2;27.785.595-3,32,Metalurgia,4.6,5.7,3.9;11.324.809-5,43,Informática,1.0,1.2,4.6;13.442.752-2,27,Minas,1.8,4.8,4.1;17.324.813-0,56,Biomédica,5.9,4.1,5.3;29.412.220-1,37,Industrial,5.2,4.4,4.1;23.335.365-1,55,Biomédica,5.3,1.1,6.6;27.709.791-6,61,Mecatrónica,1.5,3.1,1.5;28.878.662-0,21,Metalurgia,6.2,6.9,3.9;23.800.382-4,42,Industrial,3.4,1.6,6.8;28.866.819-8,46,Informática,2.7,3.3,6.9
```

Salida:
```
Metalurgia: 29.887.168-6 (5.9)
Mecánica: 27.421.841-7 (4.2)
Biomédica: 27.921.917-2 (5.9)
Telemática: 13.442.652-K (4.6)
Geomensura: 25.270.952-K (6.0)
Eléctrica: 24.201.167-8 (6.2)
Industrial: 14.241.209-K (4.8)
Ambiente: 20.234.795-4 (5.2)
Mecatrónica: 17.074.152-4 (4.4)
Minas: 20.337.697-4 (5.3)
Informática: 28.630.677-0 (5.7)
Química: 29.952.839-6 (4.7)
```
