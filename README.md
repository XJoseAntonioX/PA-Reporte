# Proyecto Purple Air 

A continuación se describirá el contenido y características de la página web de Purple Air: [Purple Air](https://purpleairproject.streamlit.app/), que tiene como finalidad ser guía del enfoque y actualizaciones con las que cuenta el proyecto.

## Contenidos

### Purple Air API

**Petición de datos:** Este apartado es para solicitar datos a la API de los sensores ubicados en distintas regiones del estado. Se necesita llenar el formulario mostrado, mismo que se autorellena en ciertos campos tras rellenar manualmente otros. Hasta el momento solo se cuentan con las opciones de los municipios, sensores y columnas que han sido de intéres hasta la fecha (Agosto de 2024). En caso de hacer algún otro cambio de cualquier índole se necesitaría modificar el script de python correspondiente a la página web.

**Campos a rellenar:**
- **Fecha y tiempo inicial:** Corresponden al momento de inicio donde se desean recolectar datos.
- **Fecha y tiempo final:** Corresponden al momento final donde se desean recolectar datos.
- **Lugar de donde se extraeran datos:** Como se indica, definir el lugar de la descarga.
- **Columnas de intéres:** Corresponden a aquellos datos de intéres a descargar de los sensores (Checar API si se requieren agregar otros).
- **API key:** Aquella llave que posiibilita la descarga de datos (Se debe de haber creado en [API key](https://www.google.com/url?q=https%3A%2F%2Fdevelop.purpleair.com%2F).
- **Periodo:** Corresponde a los lapsos de descarga de dato a dato.
- **Indice del sensor:** Corresponde al índice del sensor en cuestión de donde se descargan los datos (Este campo se autorellena tras seleccionar el lugar de extracción).
- **Opción para observar ID's de los sensores con los que ya se cuenta**

**Uso:** Tras completar el forms se da click al botón "Ejecutar Request", se mostrará un informe de la información que se está requiriendo y, por último, un botón de descarga. Si se desea concatenar los datos previamente descargados con los consecuentes (y así sucesivamente) se debe rellenar el forms otra vez con estos mismos datos consecuentes y el resultado de la descarga va a ser el resultado de la concatenación. Es importante a notar que si el objetivo principal es ese entonces no es necesario hacer la descarga en cada iteración tras querer hacer la concatenación porque al final lo que hace posible este proceso es cuando das click al botón "Ejecutar Request". 

Para dar por terminado este proceso de concatenación se debe dar clicken "Clear cache" en el siguiente menú de la página:

![image](https://github.com/user-attachments/assets/55ce71e6-58a4-42dc-8003-5ebeb99da924)

> [!CAUTION]
> Siempre observar en el informe que efectivamente no hay ninguna discrepancia, y más al momento de concatenar puesto que se debe de verificar que los registros vayan aumentando.

### Descarga de documentos

Este apartados cuenta con secciones en las que vienen siendo nuestra base de datos actualizada y de utilidad para el avance del proyecto. Se omitará las características del contenido mostrado, puesto que es intuitivo y corto. 

Solamente para hacer mención de los contenidos están:
- **AireNL**
- **Purple Air**
- **Emparejados**

El último de todos son aquellos datos que surgen del merge adecuado entre datos de AireNL y PurpleAir. 

> [!IMPORTANT]
> Por el momento es necesario actualizar esto con los nuevos datos que se descargaron/se estén descargando de Purple Air.

### Documentación

Como se describe, esta parte es toda la información relevante del proyecto y es recomendable mantener ese criterio en todo momento al igual que la brevedad de información que se debe disponer para no hacer larga la lectura que tenga algún usuario con respecto a la información y resultados del proyecto.

Cuenta con los siguientes contenidos, mismo que tienen los siguiente enfoques:
- **Introducción:** Dar información breve del contexto del proyecto y su objetivo.
- **Desarrollo:** Mostrar procesos y criterios tomados en cuenta para dar con los resultados deseados (Un mejor modelo de predicción), esto involucra, para dar una idea, mencionar el cambio de horario en datos de PA, el uso de los datos Emparejados (Dar una breve descripción de cómo se obtuvieron), el criterio para eliminar outliers, entre otros.
- **Resultados:** Dar una representación visual de los resultados mostrados ("una imágen dice más que mil palabras") esto ayuda a quien sea a entender los resultados de manera más clara y en especial a los stakeholders con nula o bastante entendimiento técnico (por ejemplo a quienes les interese saber sobre el proyecto).

> [!IMPORTANT]
> Por el momento es necesario seguir trabajando en este contenido.

> [!TIP]
> Lo descrito en esta guía no es absoluto, las ideas presentadas, formato y contenidos de las páginas, entre otros, no son reglas a seguir que determinen el correcto y mejor funcionamiento para cumplir con el objetivo deseado de la página. Consecuentemente se aconseja
> dar con nuevas propuestas que puedan mejorarla, de hacer los cambios correspondientes para ello, ya sea modificando scripts o esta guía, siempre procurando mantener buenas prácticas como mantener una copia de lo que se realiza. 











