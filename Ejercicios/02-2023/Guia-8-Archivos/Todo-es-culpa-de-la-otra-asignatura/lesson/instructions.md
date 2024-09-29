![logo](./assets/logo_usach.png)

# Comparando

Se posee un archivo llamado `"Alumnos.csv"`. En este viene la información de varios estudiantes de diferentes carreras y universidades. En particular, se tiene por cada estudiante su Nombre, Edad, RUN, Universidad, Carrera, Mail, Nota en Cálculo, Nota en Álgebra, Nota en Física y Nota en FPI. Cada uno de estos datos viene separado por un punto y coma (`";"`). 

Lo que se desea es poder buscar correlaciones entre las notas de las asignaturas. Esto puede ayudar a entender mejor las razones del bajo rendimiento de algunos estudiantes. Por ejemplo, si muchos estudiantes que reprueban física, también reprueban álgebra y puede llegar a indicar que uno de los factores es una mala base matemática que repercute en la asignatura de física.

Para esto, se le indicará una universidad y dos asignaturas y su trabajo consiste en indicar cuántos estudiantes de esa universidad reprobaron ambas asignaturas. 

Cree la función 
```
comparar(universidad, asignatura1, asignatura2)
```
que recibe tres strings: la universidad y dos asignaturas a comparar.

Ejemplo del archivo `"Alumnos.csv"`:

```
Nombre;Edad;RUN;Universidad;Carrera;Mail;Calculo;Algebra;Fisica;FPI
Dulcinea;24;10.881.360-3;UCatolica;Quimica;Dulcinea@UCatolica.com;4.4;4.2;1.8;3.5
Morena;32;10.566.206-2;UTEM;Electrica;Morena@UTEM.cl;1.3;6.6;2.3;6.2
Alecia;27;16.511.823-4;UTEM;Informatica;Alecia@UTEM.com;6.5;3.2;4.3;6.7
Rivalee;40;16.856.753-8;UdChile;Quimica;Rivalee@UdChile.edu;5.6;3.1;6.2;5.0
Phaedra;49;29.110.149-5;UdChile;Bachi;Phaedra@UdChile.cl;2.5;2.3;5.8;1.1
Myrah;24;12.266.914-5;Usach;Quimica;Myrah@Usach.com;3.2;3.4;4.9;4.6
```

## Entradas

La función recibe tres strings, la universidad y dos asignaturas a comparar:
```
comparar( <universidad> , <asignatura1> , <asignatura2> )
```

## Salida

El retorno de la función es un entero y representa cuántos estudiantes de esa universidad reprobaron tanto la asignatura1 como la asignatura2.

```
<Número_de_estudiantes>
```

## Consideraciones
- El archivo "Alumnos.csv", en la primera línea, tiene una cabecera (nombres de las columnas).
- El archivo "Alumnos.csv" siempre mantendrá el mismo formato presentado y orden de las columnas, pero los datos de los estudiantes se regenaran creando nuevos estudiantes y datos para ellos cada tres test. 

## Ejemplo

Si el contenido del archivo `"Alumnos.csv" fuese el siguiente:
```
Nombre;Edad;RUN;Universidad;Carrera;Mail;Calculo;Algebra;Fisica;FPI
Cathryn;54;26.327.290-4;UTEM;Obras;Cathryn@UTEM.com;4.5;1.9;3.9;4.1
Idelle;52;25.409.118-9;UTEM;Quimica;Idelle@UTEM.cl;1.4;3.9;1.1;5.0
Merline;42;26.017.030-5;Usach;Obras;Merline@Usach.com;1.3;1.5;4.9;2.1
Dasie;39;28.942.284-8;Usach;Quimica;Dasie@Usach.com;5.0;1.0;6.7;3.5
Row;27;21.555.617-6;Usach;Quimica;Row@Usach.cl;3.2;1.4;4.9;1.8
Christabella;40;29.727.289-7;UTEM;Bachi;Christabella@UTEM.cl;6.8;3.9;2.4;1.9
Orelie;41;20.997.620-7;UTEM;Obras;Orelie@UTEM.cl;1.7;1.9;5.9;1.9
Cally;46;13.404.968-K;UTEM;Informatica;Cally@UTEM.com;4.4;3.3;3.4;4.1
```

Entrada:
```
comparar( "UTEM" , "Fisica" , "Algebra" )
```

Salida:

```
4
```
