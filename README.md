# Proyecto Purple Air 

A continuación se describirá el contenido y características de la página web de Purple Air: [Purple Air](https://purpleairproject.streamlit.app/), que tiene como finalidad ser guía del enfoque y actualizaciones con las que cuenta el proyecto.

## Contenidos

### Purple Air API

Petición de datos: Este apartado es para solicitar datos a la API de los sensores ubicados en distintas regiones del estado. Se necesita llenar el formulario mostrado, mismo que se autorellena en ciertos campos tras rellenar manualmente otros. Hasta el momento solo se cuentan con las opciones de los municipios, sensores y columnas que han sido de intéres hasta la fecha (Agosto de 2024). En caso de hacer algún otro cambio de cualquier índole se necesitaría modificar el script de python correspondiente a la página web.

Campos a rellenar:
- Fecha y tiempo inicial: Corresponden al momento de inicio donde se desean recolectar datos.
- Fecha y tiempo final: Corresponden al momento final donde se desean recolectar datos.
- Lugar de donde se extraeran datos: Como se indica, definir el lugar de la descarga.
- Columnas de intéres: Corresponden a aquellos datos de intéres a descargar de los sensores (Checar API si se requieren agregar otros).
- API key: Aquella llave que posiibilita la descarga de datos (Se debe de haber creado en [API key](https://www.google.com/url?q=https%3A%2F%2Fdevelop.purpleair.com%2F).
- Periodo: Corresponde a los lapsos de descarga de dato a dato.
- Indice del sensor: Corresponde al índice del sensor en cuestión de donde se descargan los datos (Este campo se autorellena tras seleccionar el lugar de extracción).
- Opción para observar ID's de los sensores con los que ya se cuenta.

Uso: Tras completar el forms se da click al botón "Ejecutar Request", se mostrará un informe de la información que se está requiriendo y, por último, un botón de descarga. Si se desea concatenar los datos previamente descargados con los consecuentes (y así sucesivamente) se debe rellenar el forms otra vez con estos mismos datos consecuentes y el resultado de la descarga va a ser el resultado de la concatenación. Es importante a notar que si el objetivo principal es ese entonces no es necesario hacer la descarga en cada iteración tras querer hacer la concatenación porque al final lo que hace posible este proceso es cuando das click al botón "Ejecutar Request". 

Para dar por terminado este proceso de concatenación se debe dar clicken "Clear cache" en el siguiente menú de la página:

![image](https://github.com/user-attachments/assets/55ce71e6-58a4-42dc-8003-5ebeb99da924)


Consideraciones para garantizar integridad de los datos: Siempre observar en el informe que efectivamente no hay ninguna discrepancia, y más al momento de concatenar puesto que se debe de verificar que los registros vayan aumentando.

