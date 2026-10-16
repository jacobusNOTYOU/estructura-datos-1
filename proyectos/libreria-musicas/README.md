# Libreria de Musica Web

Una simple libreria de musica en el que se puede organizar canciones en 
playlists. Es un WSGI web aplication.

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