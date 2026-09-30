# Libreria de Musica Web

Una simple libreria de musica en el que se puede organizar canciones en 
playlists. Es un WSGI web aplication. No reproduce musica, solo la organiza.

# Estructura del proyecto

```
librerira-musicas/
├── controllers/    <-- El pegamento que una la UI con los datos
├── models/         <-- El manejo de los datos (Estructura de datos)
├── static/         <-- Algunos scripts de apoyo para la UI
├── templates/      <-- Los templates html del projecto
├── test/           <-- Pruebas
├── app.py          <-- Inico de la WSGI
└── README.md      
```

# Instrucciones de Uso

## Setup

```
python -m venv .venv
source .venv/bin/activate #para linux
pip install flask
```

## Correr el codigo

```
source .venv/bin/activate #para linux
flask run
```