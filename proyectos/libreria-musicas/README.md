# Libreria de Musica Web

Una simple libreria de musica en el que se puede organizar canciones en 
playlists. Es un WSGI web aplication. Esta pensado para un solo usuario.

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