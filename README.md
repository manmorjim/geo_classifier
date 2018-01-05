# Componentes del clasificador

## Base de datos en SQLite
Crearemos una base de datos en SQLite `classifications.db` con un modelo sencillo que contengan las siguientes tablas:
- **types** (id, name): tipos de archivos: imagen o video.
- **files** (id, path, type): archivos con id (autogenerado), path (ruta absoluta del archivo), type (fk al tipo de archivo en **_types_**).
- **cat_geografico** (id, provincia, municipio, zona_turistica): categorías correspondientes al catálogo geográfico.
- **cat_experiencial** (id, name): categorías correspondientes al catálogo experiencial (Golf,Playa,Rural/Naturaleza,Ocio,Compras,Gastronomía,Enoturismo,Idiomatico,Deporte,Fiestas,Lujo,Reuniones/Congresos,Ornitología,Flamenco,Cultura,Cruceros,Transportes,Actividad profesional Turismo Andaluz).
- **cat_vivencial** (id, name): categorías correspondientes al catálogo vivencial (Seniors,Jóvenes,Familias,Singles,Lgtb,Negocios).
- **cat_temporal** (id, name): categorías correspondientes al catálogo temporal (Primavera,Verano,Otoño,Invierno,Navidad,Semana Santa).
- **classifications** (id, file, cat_geo, cat_exp, cat_viv, cat_temp): clasificaciones realizadas por cada archivo con id (autogenerado) y file fk a **_files_** y cada categoría como fk.

Rellenamos las tablas del modelo con conocimientos que poseemos sobre el modelo de negocio. En este caso, rellenamos las tablas con conocimiento previo que poseemos, por ejemplo, las categorías geográficas (provincias y municipios) obenidas del [IECA](http://www.juntadeandalucia.es/institutodeestadisticaycartografia/iea/visualizar.jsp?codConsulta=72066&CodOper=104&props=S).

## Modelos deep learning
Parte de la clasificación se realizará analizando el contenido de los distintos archivos y para ello haremos uso de modelos de deep learning creados con [Keras](https://keras.io/). Los distintos modelos serán entrenados a partir de diversas fuentes de datos como como [Google Images](https://images.google.com/) o [Flickr](https://www.flickr.com/) e incluso un subconjunto de archivos porporcionados por la agencia.
Se crearán los siguientes modelos:
- **provincias**: Este modelo permitiriá catalogar una imagen o vídeo en una de las 8 provincias de Andalucía.
- **municipios**: Este modelo permitirá catalogar una imagen o vídeo en un municipio específico de los 778 que conforman Andalucía.
- **mun_almeria**: Este modelo permitirá catalogar una imagen o vídeo en uno de los 103 municipios que conforman Almería.
- **mun_cadiz**: Este modelo permitirá catalogar una imagen o vídeo en uno de los 44 municipios que conforman Cádiz.
- **mun_cordoba**: Este modelo permitirá catalogar una imagen o vídeo en uno de los 75 municipios que conforman Córdoba.
- **mun_granada**: Este modelo permitirá catalogar una imagen o vídeo en uno de los 172 municipios que conforman Granada.
- **mun_huelva**: Este modelo permitirá catalogar una imagen o vídeo en uno de los 79 municipios que conforman Huelva.
- **mun_jaen**: Este modelo permitirá catalogar una imagen o vídeo en uno de los 97 municipios que conforman Jaén.
- **mun_malaga**: Este modelo permitirá catalogar una imagen o vídeo en uno de los 103 municipios que conforman Málaga.
- **mun_sevilla**: Este modelo permitirá catalogar una imagen o vídeo en uno de los 105 municipios que conforman Sevilla.
- **experiencial**: Este modelo será capaz de distinguir únicamente entre las siguientes categorías experienciales: golf, playa, naturaleza, cruceros, flamenco.
- **temporal**: Este modelo permitirá catalogar una imagen o vídeo únicamente entre las siguientes categorías temporales: Navidad y Semana Santa.


# Clasificación

### Pasos previos
Rellenamos la tabla de `files` con los archivos que queremos clasificar ejecutando el siguiente comando:

```sh
$ python read_files.py ${directorio}
```

Este comando en Python limpiará las tablas `classifications` y `files` y rellenará ésta última con todos los archivos que contenga la ruta especificada en `${directorio}`

### Procedimiento
Una vez que se han rellenado las tablas `files` con las imágenes y vídeos del directorio se pasa a realizar la catalogación mediante el siguiente comando:

```sh
$ python classify_files.py
```
La clasficiación se hará de la siguiente forma:

---

#### Catalogación Geográifca
Cada imagen o vídeo debe catalogarse en base a su localización:
- Provincia
- Municipio/pedanía
- Zona turística

La catalogación la realizaremos

##### Según sus metadatos
Primero intentaremos una clasificación mediante los metadatos que posea los archivos.

##### Según el nombre y ruta del archivo
En numerosas ocasiones el nombre de los archivos o carpetas suelen poseer bastante información sobre su contenido. Se plantea hacer una clasificación previa por el nombre de carpetas o archivos.

##### Según el contenido del archivo
Aquellos archivos que no hayan podido clasificarse a través del nombre se pasará a clasificar por su contenido.

---

#### Catalogación Geográifca
Cada imagen o vídeo debe catalogarse en base a su localización:
- Provincia
- Municipio/pedanía
- Zona turística

La catalogación la realizaremos

##### Según sus metadatos
Primero intentaremos una clasificación mediante los metadatos que posea los archivos.

##### Según el nombre y ruta del archivo
En numerosas ocasiones el nombre de los archivos o carpetas suelen poseer bastante información sobre su contenido. Se plantea hacer una clasificación previa por el nombre de carpetas o archivos.

##### Según el contenido del archivo
Aquellos archivos que no hayan podido clasificarse a través del nombre se pasará a clasificar por su contenido.

---
