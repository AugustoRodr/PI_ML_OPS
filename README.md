# Proyecto indivicual N°1

El proyecto consiste en la descarga, pre-preparacion, procesamiento de datos y desarrollo de una API que disponibilice la informacin de la empresa.

La informacion que se utilizara esta localizada en la carpeta **datasets**.

Los procesos solicitados para la preparacion y el procesamiento de datos son los siguientes:

- Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)
- Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”
- De haber fechas, deberán tener el formato AAAA-mm-dd
- Los campos de texto deberán estar en minúsculas, sin excepciones
- El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

Posterior al procesamientos de datos se unifican la informacion para que al momento de crear la API se utililce un unico archivo y de esta forma al realizar el deploy sea mas sencillo.

Las Querys solicitadas para este proyecto son las siguientes:

1- Pelicula con mayor duracion segun año, plataforma (Amazon,Netflix,Hulu,Disney) y tipo de duracion (Min, Season/s)
