# Calidad del Aire

## Introducción
Originalmente la idea surgió en una discussión online. A partir de políticas medioambientales del ayuntamiento de Madrid, la discusión era relativa acerca si Madrid Central había reducido la contaminación atmosférica de la ciudad o simplemente la había desplazado a la periferia. La clave para determinar esto era, no solo observar los datos de contaminación de estaciones de cada zona, sino también, ver las tendencias históricas.

Esto derivó en una búsqueda de los datos de contaminación y calidad del aire de las estaciones. Los datos son públicos así que se pueden descargar en varios formatos. Sin embargo, al haber muchos datos separados por fecha, parece lógico dejar que sean las máquinas las que hagan el trabajo sucio. Así nació esta idea, en principio como un simple webcrawler.

## Objetivos
Como se puede ver de la introducción, los objetivos del proyecto cambiaron respecto al inicio. Así que serán actualizados. Por ahora los objetivos principales son los siguientes:
1. Automatizar la obtención de datos. Por ahora, el getter accede a la web del ayuntamiento donde se pueden obtener los archivos, y los descarga. La siguiente fase será que el getter acepte parámetros de entrada como el enlace al que conectar, el formato de los archivos y descargarlos. Además, sería ideal que mantuviese una DB de los datos descargados por fecha, para no tener que descargar todo cada vez que aparezcan nueva información. El repositorio de datos, aunque no esté diseñado como tal de forma eficiente, es histórico y añade nuevos datos cada cierto tiempo (algo a investigar).

2. Creación de otro módulo que lea los archivos descargados y realice análisis de los mismos, como tendencias y desviaciones. Esto implica el desarrollo de un modelo de datos que tenga en cuenta ciertos parámetros adjuntos a los datos que dan información relativa a la toma de los mismos y podría afectar la estadística y los resultados.

3. Visualización de los datos y presentación de tendencias. La idea final es tener automatizado el análisis de los mismos, de forma que se pudeda evaluar si alguna medida política afecta o no la contaminación en la ciudad así como ver la evolución general de la contaminación.

Hay muchas más ideas y posibles fases, pero vamos a restringirnos a estas tres. Cuando se comienza un proyecto, las posibilidades son muchas y es fácil imaginar hasta donde se puede llegar. Lo difícil es hacer el trabajo para llegar allí. Lo mejor es ser modesto en cada paso, e ir incrementando la calidad y funcionalidad del proyecto para mantener la motivación de las personas involucradas (en este caso, solo yo de momento, y me conozco, así que mejor ser modesto en las expectativas).

## TODOs
### Inmediatos
- [ ] Añadir módulo que extraiga los datos en crudo de los archivos y los cargue en el data model
    - [ ] Desarrollar el data model básico.
    - [ ] Determinar si ese data model estará en una DB o archivos propios (protobuf como ejemplo).
- [ ] Añadir módulo de visualización. Primera fase, dibujar gráficas de líneas de evolución histórica y tendencia.

### A Futuro
- [ ] Presentación de los datos en un notebook estilo Jupyter.
- [ ] Gráficas de datos interactivas que permitan modificar los rangos de fechas y otros parámetros de los datos (como zona geográfica de las estaciones a mostrar) y que se actualicen las gráficas (idealmente en tiempo real).
