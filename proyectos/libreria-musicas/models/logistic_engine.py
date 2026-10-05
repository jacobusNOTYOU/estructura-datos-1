"""Maneja los datos de la libreria, las playlists y las canciones. 
Usando las estrucuras de datos definidas en el modulo `structures.py`,
las cuales son: `Music`, `Playlist` y `Library`.
"""

from models.structures import *
import json


class DataModel:
    """Maneja los datos de la libreria usando las estructuras de datos.
    Incluye manejo de persistencia con json, en su comportamiento la libreria
    tiene una playlist no borrable(despues de cargarla libreria del archivo) 
    llamada "Libreria" y sus canciones deben ser unicas (a diferencia de las
    otras playlists) los datos se reciben y retornan en json con las 
    excepciones de `get_playlist-names()` y `get_music_titles()` que 
    retornan listas.

    Methods:
    - add_playlist(name:str)
    - add_music(playlist:str,title:str,author:str,direction:str)

    - get_playlist(name:str)
    - get_playlist_names()
    - get_music(title:str)
    - get_music_titles(playlist:str)
    - get_music_dir(playlist:str,title:str)

    - remove_playlist(name:str)
    - remove_music(playlist:str,titile:str)

    - next(name:str,loop:bool)
    - prev(name:str,loop:bool)
    - restart(name:str)

    - to_json()
    - number_playlists()
    - seek_playlist(name: str)

    - save(file_name:str)
    - load(file_name:str)
    - loads(library:str)
    """

    def __init__(self):
        self._library: Library = Library()

    def add_playlist(self, name: str) -> None:
        """Crea una playlist en la libreria.
        Parametros:
        - name: nombre de la playlist, debe ser unico y diferente a "Library".

        Excepciones:
        - NameError: si `name` es igual a "Library" o si ya existe una playlist 
        llamada `name`,
        """
        if name == "Library":
            raise NameError(
                'Error: Prohibido nombrar "Libreria" a una '
                'playlist!'
                )

        if self.seek_playlist(name):
            raise NameError(f'Error: La playlist "{n}" ya existe!')
        
        self._library.append(name)

    def add_music(
        self, playlist: str, title: str, author: str, direction: str
        ) -> None:
        """Agrea una cancion a una playlist. En el caso de "Library" 
        las no debe haber otra cancion identica en la libreria, esta
        condicion no aplica a cualquier otra playlist.
        Parametros:
        - playlist: nombre de la playlist en la que agregar la cancion.
        - title: titulo de la cancion a agregar.
        - author: autor de la cancion a agregar.
        - direction: direccion en la que se guarda la cancion.

        Excepciones:
        - NameError: si no encuentra una `Playlist` llamada `playlist` en 
        `self._library` o si `playlist` es igual a 'Library' y se encuentra una
        cancion identica en dicha `Playlist`.
        """

        names: list[str] = self._library.get_names()
        if playlist not in names:
            raise NameError(
                f"Error: {playlist} no se encuentra en la libreria."
            )

        if playlist == "Library":
            the_playlist: Playlist = self._library.get("Library")
            titles: list[str] = the_playlist.get_titles()
            authors: list[str] = the_playlist.get_authors()
            if title in titles and author in authors:
                raise NameError(
                    f"Error: Prohibida agregar una cancion dos veces en la "
                    f"playlist 'Library'."
                    )
        
        self._library.add_music(playlist, title, author, direction)

    def get_playlist(self, name: str) -> str:
        """Retorna una lista de canciones de la primera `Playlist` llamada 
        `name` que se encuentre, en formato json.
        Parametros:
        - name: el nombre de la `Playlist` a retornar en formato json.

        Exception:
        - NameError: si no se encuentra una `Playlist` llamada `name`.
        """

        names: list[str] = self.get_playlist_names()
        if name not in names:
            raise NameError(
                f"Error: No se encontro una playlist llamada: {name}!"
            )
        
        titles: list[str] = self.get_music_titles(name)
        playlist: str = '[ '

        for i in range(len(titles)):
            playlist += self.get_music(name, titles[i])
            if i < len(titles) -1:
                playlist += ', '

        playlist += ' ]'

        return playlist

    def get_playlist_names(self) -> list[str]:
        """Retorna una lista de los nombres de las `Playlist`s que contiene
        la libreria.
        """
        return self._library.get_names()

    def get_music(self, playlist: str, title: str) -> str:
        """Retorna una cancion, de una playlist llamada `playlist`, cullo 
        titulo coindide con `title` en formato json.
        Parametros:
        - playlist: el nombre de la playlist.
        - title: el titulo de la cancion.

        Excepciones:
        - NameError: si no se encuentra una `Playlist` llamada `playlist` o,
        si se encuentra, si no encuentra un `Music` titulada `title`.
        """
        
        music: Music|None = self._library.get_music(playlist, title)
        if music is None:
            raise NameError(
                f"Error: No hay una cancion titulada: {title} en una playlist "
                f"llamada {playlist}!"
                )

        return ('{' 
            + '"title": '+ '"' + music.title + '", ' 
            + '"author": '+ '"' + music.author + '", ' 
            + '"direction":' + '"' + music.direction + '"'
            +'}'
        )

    def get_music_titles(self, playlist: str) -> list[str]:
        """Retorna los titulos de las canciones de la `Playlist` llamada 
        `playlist`.
        Parametros:
        - playlist: el nombre de la playlist de la cual obtener los titulos.

        Excepciones:
        - NameError: si no se encuentra una `Playlist` llamada `playlist`.
        """

        the_playlist: Playlist|None = self._library.get(playlist)
        if the_playlist is None:
            raise NameError(
                f"Error: No se encontro 'Playlist` alguna llamada: {playlist}!"
                )

        return the_playlist.get_titles()
    
    def get_music_dir(self, playist: str, title: str) -> str:
        """Retorna la direccion de la primera cancion titulada `title` la 
        playlist llamada `name`.
        Parametros:
        - playlist: el nombre de la playlist en la que se encuetra la cancion. 
        - title: el titulo de la cancion.

        Excepciones:
        - NameError: si no se encuetra una cancion titulada `title` en una 
        playlist llamada `name`.
        """

        return self._library.get_music_dir(playist, title)

    def remove_playlist(self, name: str) -> None:
        """Elimina una `Playlist` de la libreria.
        Parametros:
        - name: el nombre de la `Playlist` a eliminar.

        Excepciones:
        - NameError: si no se encuentra una `Playlist` llamada `name`.
        """

        if not self._library.remove(name):
            raise NameError(
                f"Error: No se encontro una playlist llamada: {name}!"
            )

    def remove_music(self, playlist: str, title: str) -> None:
        """Elimina el primer `Music` titulada `title` de la `Playlist` llamada 
        `name`.
        Parametros:
        - playlist: el nombre de la playlist en la que se encuentra la cancion.
        - title: el titulo de la cancion a eliminar.

        Excepciones:
        - NameError: si no se encuentra una `Playlist` llamada `playlist` o,
        si se encuentra, si no encuentra un `Music` titulada `title`.
        """

        if not self._library.remove_music(playlist, title):
            raise NameError(
                f"Error: No se encontro una cancion titulada: {title} en una"
                f" playlist llamada: {playlist}!"
            )

    def next(self, name: str, loop: bool = False) -> str:
        """Retorna la siguiente cancion en la playlist llamada `name`."""
        return self._library.next(name, loop)

    def prev(self, name: str, loop: bool = False) -> str:
        """Retorna la anterior cancion en la playlist llamada `name`."""
        return self._library.prev(name, loop)

    def restart(self, name: str) -> None:
        """Reinicia la playlist llamada `name`."""
        return self._library.restart(name)

    def to_json(self) -> str:
        """Retorna una cadena que contiene toda la libreria en formato json."""
        names: list[str] = self.get_playlist_names()
        library: str = '{ '
        for i in range(len(names)):
            library += (
                '"' + names[i] + '": ' + self.get_playlist(names[i])
            )
            if i < len(names)-1:
                library += ', '
        library += ' }'
        return library

    def number_playlists(self) -> int:
        """Retorna la cantidad de `Playlist` que contiene la libreria."""
        return len(self._library)

    def seek_playlist(self, name: str) -> bool:
        """Busca una playlist que se llame `name` y retorna `True` si la 
        encuentra, de otra manera, retorna `False`.
        Parametros:
        - name: el nombre de la playlist.
        """
        names: list[str] = self._library.get_names()
        for n in names:
            if name == n:
                return True
        return False

    def save(self, file_name: str) -> None:
        """Guarda la estructura en formato json.
        Parametros:
        - file_name: el nombre del archivo a guardar.

        Excepciones:
        - OSError: si no puede abrir el archivo.
        """

        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(self.to_json())

    def load(self, file_name: str) -> None:
        """Carga una libreria en formato json del almacenamiento.
        Parametros:
        - file_name: el nombre del archivo a cargar.

        Excepciones:
        - OSError: si no puede abrir el archivo.
        """

        with open(file_name, 'r', encoding='utf-8') as f:
            library: str = f.read()
        
        self.loads(library)

    def loads(self, library: str) -> None:
        """Carga una libreria que esta en formato json.
        Parametros:
        - library: la libreria en formato json a cargar.

        Excepciones
        - JSONDecoderError: si `library` no tiene un formato json valido.
        - ValueError: si `library` no se puede convertir a `Library`.
        """

        try:
            library_dict: dict = json.loads(library)
        except json.JSONDecodeError:
            raise json.JSONDecodeError(
                f"Error: No se pudo deserializar {library}!"
            )
        
        playlist_names: list[str] = list(library_dict)
        for n in playlist_names:
            self._library.append(n)
        
        playlists: list[list[dict]] = []
        for n in playlist_names:
            playlists.append(library_dict[n])
        
        try:
            for i in range(len(playlist_names)):
                for j in range(len(playlists[i])):
                    self.add_music(
                        playlist_names[i], 
                        playlists[i][j]["title"], 
                        playlists[i][j]["author"],
                        playlists[i][j]["direction"]
                    )
        except Exception:
            raise ValueError(
                f"Error: Formato invalido de libreria econtrado en: {library}!"
            )
