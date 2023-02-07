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

## Configuración con Anaconda y Jupyter
Con el fin de analizar la estructura (terriblemente fea) de los datos tal y como se ofrecen, usar Jupyter notebooks es de las opciones más interesantes.Para ello, el primer paso es instalar Anaconda. Esto es sencillo y simplemente se consigue entrando en su web y siguiendo las instrucciones.
Una vez hecho esto, si el directorio donde se descargan los archivos está fuera del lugar desde donde se ejecuta Jupyter (lo cual es probable), hay que arrancar Jupyter desde la línea de comandos, especificando el directorio donde se desea que esté la raiz.
`jupyter notebook --notebook-dir [directorio/deseado]`
donde [directorio/deseado] es donde queremos guardar el notebook. Para más detalle, ver esta respuesta en [StackOverflow](https://stackoverflow.com/questions/46755604/how-to-navigate-to-a-different-directory-in-jupyter-notebook).

También hay otra forma de configurar Jupyter de manera que siempre se abra en el directorio donde hacemos los desarrollos, tal y como se puede ver [aquí](https://stackoverflow.com/questions/35254852/how-to-change-the-jupyter-start-up-folder).

### Python Environments
Idealmente, deberíamos crear un environment con `virtualenv`o similares funcionalidades (`venv` o `pyenv`). Sin embargo, aún no he conseguido configurarlo correctamente. En este caso, debido a que en mi entorno de desarrollo solo voy a usar python para data science, puedo ignorarlo. Pero es algo a tener en cuenta, dependiendo de tu caso particular.

## TODOs
### Inmediatos
- [ ]  Perfeccionar la descarga de archivos y la carga y formateo básico.
    - [ ] Desarrollar el data model básico.
    - [ ] Guardado de datos preprocesados en DB o archivo en disco?
    - [ ] Establecer la descarga automática de nuevos datos.
- [ ] Añadir módulo de visualización. Primera fase, dibujar gráficas de líneas de evolución histórica y tendencia.

### A Futuro
- [ ] Presentación de los datos en un notebook estilo Jupyter.
- [ ] Gráficas de datos interactivas que permitan modificar los rangos de fechas y otros parámetros de los datos (como zona geográfica de las estaciones a mostrar) y que se actualicen las gráficas (idealmente en tiempo real). Valorar (Streamlit)[https://github.com/streamlit/streamlit/] para este punto.

## Referencias y Datos
- La web del ayuntamiento donde se pueden consultar estos datos es (esta)[https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD].
- Hay más datos y enlaces relevantes en la web para posibles adiciones a este proyecto u otros que puedan surgir de este. (Catálogo de Datos del Ayuntamiento de Madrid)[https://datos.madrid.es/portal/site/egob/menuitem.9e1e2f6404558187cf35cf3584f1a5a0/?vgnextoid=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default]
