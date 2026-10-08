"""En este modulo se integra el modelo junto al view, completando asi el 
modelo MVC.

Datos para el renderizado de la UI:
- Los nombre de las playlist.
- Las canciones de la playlist activa.

Datos para la actualizacion del modelo:
- Una instruccion.
- Los datos para la instruccion.

Interface:
{ "instruction":"", "data":"" }

add_playlist(name:str)
- instruction: 'add_playlist'
- data: name:str

add_music(playlist:str,title:str,author:str,direction:str)
- instruction: 'add_music'
- data: list[
        playlist:str, 
        { 
            'title':str, 'author':str, 'direction':str 
        }
    ]

get_playlist(name:str)
- instruction: 'get_playlist'
- data: name:str

get_playlist_names()
- instruction: 'get_playlist_names'
- data: ''

get_music(playlist:str,title:str)
- instruction: 'get_music'
- data: [playlist:str, title:str]

get_music_titles(playlist:str)
- intruction: 'get_music_titles'
- data: playlist:str

get_music_dir(playlist:str,title:str)
- instruction: 'get_music_dir'
- data: [playlist:str, title:str]

remove_playlist(name:str)
- instruction: 'remove_playlist'
- data: name:str

remove_music(playlist:str,title:str)
- instruction: 'remove_music'
- data: [
    plalist:str,
    title:str
]

next(playlist:str,loop:bool)
- instruction: 'next'
- data: [playlist:str, loop:bool]

prev(playlist:str,loop:bool)
- instruction: 'prev'
- data: [playlist:str, loop:bool]

restart(playlist:str)
- instruction: 'restart'
- data: playlist:str

"""

# Functions
from ..models.logistic_engine import DataModel

data_model: DataModel = DataModel()
data_model.load('data.json')

def model_interface(instruction: str, data: any):
    match(instruction):
        case 'add_playlist':
            try:
                data_model.add_playlist(data)
            except NameError:
                return (
                    '{ '  
                    f'"message":"Error: playlist {data} already exist!"'
                    ' }'
                    )
            return '{ ' + '"message":"Success!"' + ' }'

        case 'add_music':
            try:
                data_model.add_music(
                    data[0], 
                    data[1]['title'], 
                    data[1]['author'], 
                    data[1]['direction']
                )
            except NameError:
                return (
                    '{ '
                    f'"message":"Error: {data[0]} does not exist or song is '
                    'already in the Library!"'
                    ' }'
                )

            return '{ ' + '"message":"Success!"' + ' }'

        case 'get_playlist':
            try:
                return data_model.get_playlist(data)
            except NameError:
                return (
                    '{ '
                    f'"message":"Error: playlist {data} not found!"'
                    ' }'
                )

        case 'get_playlist_names':
            return data_model.get_playlist_names()

        case 'get_music':
            try:
                return data_model.get_music(data[0], data[1])
            except NameError:
                return (
                    '{ '
                    f'"message":"Error: song {data[1]} not found in playlist '
                    f'{data[0]}"'
                    ' }'
                )

        case 'get_music_titles':
            try:
                return data_model.get_music_titles(data)
            except NameError:
                return (
                    '{ '
                    f'"message":"Error: playlist {data} not found!"'
                    ' }'
                )

        case 'get_music_dir':
            return '[ "' + data_model.get_music_dir(data[0], data[1]) + '" ]'

        case 'remove_playlist':
            try:
                data_model.remove_playlist(data)
            except NameError:
                return (
                    '{ '
                    f'"message":"Error: playlist {data} not found!"'
                    ' }'
                )
            return '{ ' + '"message":"Success!"' + ' }'

        case 'remove_music':
            try:
                data_model.remove_music(data[0], data[1])
            except NameError:
                return (
                    '{ '
                    f'"message":"Error: song {data[0]} not found in playlist '
                    f'{data[1]}"'
                    ' }'
                )
            return '{ ' + '"message":"Success!"' + ' }'

        case 'next':
            try:
                return data_model.next(data[0], data[1])
            except StopIteration:
                return '{ ' + '"message":"StopIteration!"' + ' }'

        case 'prev':
            try:
                return data_model.prev(data[0], data[1])
            except StopIteration:
                return '{ ' + '"message":"StopIteration!"' + ' }'

        case 'restart':
            data_model.restart(data)
            return '{ ' + '"message":"Success!"' + ' }'


# Blueprint
from flask import Blueprint, render_template, request, jsonify
import json

bp: Blueprint = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

#   Datos para el renderizado
#   Datos para el modelo
@bp.route('/data', methods=("GET", "POST"))
def data():
    if request.method == "POST":
        request_data = request.json
        return model_interface(request_data['instruction'], request_data['data'])

    return data_model.to_json()