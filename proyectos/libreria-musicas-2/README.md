# Libreria de Musica Web

Una simple libreria de musica en el que se puede organizar canciones en 
playlists. Es un WSGI web aplication. Esta pensado para un solo usuario.
Esta es la v2 de libreria-musicas, esta version presenta un cambio en las estructuras de datos utilizadas.

# Objetivo de los cambios

El objetivo de los cambios es la mejora en eficiencia del programa.

# Metodologia de Benchmarking

Para el benchmarking se le agrega a la configuracion del programa la opcion
`benchmark`, al darle el valor de `true` se toma medidas del uso de memoria y
el tiempo tardado en realizar un cierto numero de operaciones. Estas medidas se
guardan en un archivo de texto, `memory-benchmark.txt` para memoria y 
`time-benchmark.txt` para tiempo. Para obtener las estadisticas se dispone de 
del script `benchmark.py`, el cual, obtiene los datos de los correspondientes
archivos, calcula las estadisticas y los guarda en un archivo llamado 
`result-benchmark.txt`.

## Memoria

Se hace uso del modulo `tracemalloc` de la libreria estandar de python, para
medir el uso total de memoria del programa. Esta medida tiene el objetivo de 
medir el impacto en el uso de la memoria total del programa de las estructuras
de datos.

## Tiempo

Se hizo la medicion del tiempo en el que se realizan las operaciones en el 
modulo `controller.py`. La tecnica que se uso es el de obtener el tiempo actual
antes de realizar la operacion, luego de ejecutada la operacion se vuelve a 
obtner el tiempo, y por ultimo se hace la diferencia entre ambos tiempo. el 
reloj que se uso fue `time.perf_counter`. Las operaciones que se miden son las
ofrecidas en el metodo `model_interface` en `controllers.py`, y se registran 
con el nombre que se les da en los pedidos del cliente.

# Cambios Realizados

La estructura de datos que se cambio fue la de la libreria principal, estas son
 las propiedades que esta posee: elementos unicos, solo se agregan elementos al
arrancar el programa y nunca se eliminan elementos. Estas propiedades la hacen
una buena candidata a tabla hash, sin embargo, la alteracion en el orden y las
operacions de `pre` (reproducir anterior) y `next` (reproducir siguiente) son
muy ineficientes en la tabla hash por no estar ordenada y tener posiciones 
vacia de por medio. Por estas razones, se opto por usa un arreglo para guardar 
los datos de `Library` y indexarla con una tabla hash, de esta manera, se 
mantiene la velocidad de busqueda de una tabla hash, las operaciones de `prev` 
y `next` son comparables al de la lista enlazada doble y, aunque eliminar datos
sea mas lento, esta operacion ni siquiera se realiza en toda la ejecucion del 
programa.

# Resultados

En el uso de la memoria, como es de esperarse, se uso mas memoria. En promedio
el uso de la memoria aumento en un 4.38% resultando en una diferencia de 
76.248 kb. En la maxima se llego a un 1.43% mas que la enterios version. Y como
minimo se uso un 9.75% mas. Como se puede observar, este aumento en memoria no
es muy significativa, ya que, si tenemos 1000 instancias del mismo programa en 
promedio se gastarian 76.248 mb mas.

Encuanto al tiempo, solo se toman en cuenta las operaciones: `play`, `next`, 
`prev` y `get_playlist`. Esto debido a que, son las unicas que el cliente es
capaza de realizar en la playlist 'Library', por las restricciones que tiene
(no se puede eliminar ni agregar canciones a 'Library' desde el cliente).

Comenzando por `play`, en promedio, los cambios resultaron ser un 12.26% mas
rapido, con una maxima 25.11% menor a la vesion previa y un minimo del 51.86%
mas lento. Estos cambios entonces, solo es mas lento en el minimo que la vesion
anterior, pero, es mas constante en todos los casos, y aun mejor, mas rapido en
el peor caso.

El siguiente es `next`, el cual es en promedio un 17.55% mas lento, este, junto
 a `prev`, es uno de los casos en los que se sabe que la nueva version es mas
lenta.

Continuamos con `prev`, el cual en promedio es un 11.12% mas lento. Es tentador
concluir que los cambios realizados terminaron en un empeoramiento, ya que se 
esperaria un mayor uso de `next` y `prev` en un reproductor de musica que de 
`play`, sin embargo, la idea de la playlist 'Library' es el de contener todas 
las caciones y que el usuario cree sus playlist con las canciones que desee y 
use sus playlist para escuchar musica. Es debido a esto, que es mas probable
que se realice la operacion de `play` en la playlist 'Library' que las de 
`next` y `prev`, y que esta expectativa se invierta en las playlist creadas por
el usuario.

Finalmente, `get_playlist`, en promedio es un 13.74% mas rapido, su maximo es
un 13.77% menor y en su minimo es un 0.96% mas lento.

En conclucion, las mejoras se ven en las operaciones de `play` y `get_playlist`
. Las cuales son las que mas se realizan en la playlist 'Library', siendo 
`get_playlist` las mas costosa. La velocidad de degrada en las operaciones 
`next` y `prev`, las cuales se esperan no seran frecuentes. Es por estas
razones que se considera que los cambios son beneficos, en especial si se 
agregan mas datos. El costo en memoria es lo suficientemente baja como para
que valga la pena la mejoria en los tiempos. Un obsevacion importante es que, 
la unica operacion en la que se nota la diferencia desde la perspectiva del 
usario, es la de `get_playlist` por ser la mas tardada.

# Estructura del proyecto

```
librerira-musicas/
├── libreria_musicas/       
|   ├── controllers/        <-- El pegamento que una la UI con los datos
|   ├── models/             <-- El manejo de los datos (Estructura de datos)
|   ├── static/             <-- Algunos scripts de apoyo para la UI y png
|   ├── templates/          <-- Los templates html del projecto
|   ├── __init__.py         
|   └── app.py              <-- Inico de la WSGI
├── test/                   <-- Pruebas
├── pyproject.toml          <-- Configuracion de enpaquetado
├── README.md               <-- Descripcion y documentacion del proyecto
└── test.py                 <-- Script para correr las pruebas
```

# Enpaqutamiento

## Hacer instalable el proyecto

```
pip install -e .
```

## Empaquetado en  wheel

```
python -m build --wheel
```

# Instalacion del wheel

```
pip install libreria_musicas-x.x-py2.py3-none-any.whl
```

**Nota: el nombre puede variar, x.x es la version configurada en "pyproject.toml".**


# Instrucciones para desarrollo

## Setup

```
git clone https://github.com/jacobusNOTYOU/estructura-datos-1.git
python -m venv .venv
source .venv/bin/activate #para linux
pip install flask
```

## Correr el codigo

```
source .venv/bin/activate #para linux
flask run
```

## Correr Pruebas
```
python test.py
```

# Configuracion

La configuracion debe estar ubicado en `/direccion/a/libreria_musicas/.config
/config.json`, donde 'libreria_musicas' es el archivo del mismo nombre en el 
proyecto o un archivo en el mismo directorio del .whl.

```
{
    "library_path":"/direccion/a/la/libreria.json",
    "music_path":"/direccion/a/las/canciones/"
}
```

# Libreria de musicas

La libreria es un objeto json, cuyas propiedades son las playlists. La playlist
'Library' es necesaria para el correcto funcionamiento del programa. Se describe 
de la siguiente forma:

```
{
    "Library": [
        {
            "title":"titulo de la cancion",
            "author":"autor de la cancion",
            "direction":"direccion a la cancion"
        },
        ...
    ]
    ...
}
```

Donde "direccion a la cancion" inicia desde la direccion dada en "music_path" en 
la configuracion (vease configuracion).