# Proyecto indivicual N°1

El proyecto consiste en la descarga, pre-preparacion, procesamiento de datos y desarrollo de una API que disponibilice la informacin de la empresa. Para esto usaremos las herramientas de FastApi para la creacion de API, Python para el procesamiento de la imformacion y Render para el deploy de la API.

La informacion que se utilizara esta localizada en la carpeta **datasets**.

Los procesos solicitados para la preparacion y el procesamiento de datos son los siguientes:

- Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)
- Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”
- De haber fechas, deberán tener el formato AAAA-mm-dd
- Los campos de texto deberán estar en minúsculas, sin excepciones
- El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

Posterior al procesamientos de datos se unifican la informacion para que al momento de crear la API se utililce un unico archivo y de esta forma al realizar el deploy sea mas sencillo.

Las Querys solicitadas para este proyecto son las siguientes:

1. Pelicula con mayor duracion segun año, plataforma (Amazon,Netflix,Hulu,Disney) y tipo de duracion (Min, Season/s).
2. Cantidad de **peliculas** segun plataforma (Amazon,Netflix,Hulu,Disney), año y con un puntaje mayor a XX (0-5).
3. Cantidad de pelicula segun plataforma (Amazon,Netflix,Hulu,Disney).
4. Actor que mas se repite segun año y plataforma (Amazon,Netflix,Hulu,Disney).
5. Cantidad de contenido (todo lo disponible en streaming) que se publicó segun año y pais.
6. Cantidad de contenido (todo lo disponible en streaming) segun el rating de audiencia dado (Ej: pg-13, tv-ma, pg, tv-14, etc).

Una vez creada la API con Fasapi se procede a realizar el deploy en Render.

Link Render: https://pi-henry.onrender.com/docs

Link Video en drive: https://drive.google.com/drive/folders/10kGB_X9jxY1sOXJFwfnO8BWFj4_hBAv6?usp=share_link
