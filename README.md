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
- Opción 

Uso:

