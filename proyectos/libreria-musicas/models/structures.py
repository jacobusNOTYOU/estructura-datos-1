"""Este modulo contiene las estructuras de datos del proyecto. Las
cuales son:
- Music
- Node
- Playlist
- Library
"""


class Music:
    """Define las datos que componen una cancion:
    - title: el titulo de la cancion.
    - author: el autor de la cancion.
    """
    def __init__(self, title: str, author: str = "unkown") -> None:
        self.title: str = title
        self.author: str = author


class Node:
    """Esta es una clase de apoyo para implementar las estructuras de 
    datos del proyecto.
    Atributos:
    - data: el dato que guarda el nodo.
    - next: el nodo que le sigue a este nodo
    """
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.next: "Node"|None = None


class Playlist:
    """Es un conjunto nombrado de `Music`, implementado en una lista
    enlazada simple.
    Atributos:
    - name: el nombre de la playlist.
    - head: el comienzo de la Playlist.

    Metodos:
    - append(title: str, author: str="unkown"): agrega una cancion al 
    final de la lista.
    - remove(title: str): borra por titulo una cancion de la lista.
    - get(title: str): obtiene una cancion por titulo.
    - get_titles(): retorna una lista de todos los titulos.
    - is_empty(): verifica si la playlist esta vacia.
    - __len__(): retorna la longitud del la lista al usar la funcion 
        len().
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.head: Node|None = None
        self._len: int = 0

    def append(self, title: str, author: str = "unkown") -> None:
        """Agrega una cancion al final de la lista.
        Parametros:
        - title: titulo de la cancion.
        - author: autor de la cancion.

        Complejiidad: O(n)
        """

        new_music: Music = Music(title, author)
        new_node: Node = Node(new_music)
        if self.is_empty():
            self.head = new_node
            self._len += 1
            return

        if len(self) == 1:
            self.head.next = new_node
            self._len += 1
            return

        actual: Node = self.head
        while actual.next is not None:
            actual = actual.next

        actual.next = new_node
        self._len += 1

    def remove(self, title: str) -> bool:
        """Borra por titulo una cancion de la lista.
        Parametros:
        - title: titulo de la cancion a eliminar.

        Retorna: `True` si encontro la cancion y la borro, de otra manera
        `False`.
        Complejidad: en el peor caso O(n).
        """

        if self.is_empty():
            return False
        
        actual: Node = self.head
        previous: Node|None = None
        while actual is not None and actual.data.title != title:
            previous = actual
            actual = actual.next

        if actual is None:
            return False
        
        if previous is not None:
            previous.next = actual.next
            self._len -= 1
            return True

        self.head = actual.next
        self._len -= 1
        return True

    def get(self, title: str) -> Music:
        """Obtiene una cancion por titulo.
        Parametros:
        - title: titulo de la cancion.
        
        Retorna: si encuentra una cancion(una instancia de `Muisc`) con 
        el titulo dado, lo retorna, si no, retorna None.
        Complejidad: O(n).
        """

        if self.is_empty():
            return None

        actual: Node = self.head
        while actual is not None and actual.data.title != title:
            actual = actual.next

        if actual is None:
            return None

        return actual.data

    def get_titles(self) -> list[str]:
        """Retorna una lista de los titulos de todas las canciones."""
        if self.is_empty():
            return []
        
        actual: Node = self.head
        titles: list[str] = []
        while actual is not None:
            titles.append(actual.data.title)
            actual = actual.next

        return titles

    def is_empty(self) -> bool:
        """Verifica si la lista esta vacia."""
        return len(self) <=0

    def __len__(self) -> int:
        """Retorna la longitud de la lista al plicarse `len()` en ella."""
        return self._len


class Library:
    """Una lista de `Playlist`s, implementada como  una lista enlazada
    simple.
    Atributos:
    - head: el inicio de la lista.

    Metodos:
    - append(name: str): crea una `Playlist` llamada `name` y la agrega 
    al final de la lista.
    - add_music_to_library(name:str,title:str,author:str): agrega una 
    cancion (de titulo `title` y autor `author`) a una playlist llamada
    `name`.
    - remove(name: str): elimina una `Playlist` de la lista.
    - get(name: str): obtiene una lista por nombre.
    - get_names(): retorna una lista que contiene los nombres de las 
    `Playlist`s que guarda la lista.
    - is_empty(): verifica si la lista esta vacia.
    - __len__(): retorna la longitud de la lista al aplicarle `len()`.
    """

    def __init__(self) -> None:
        self.head: Node|None = None
        self._len: int = 0

    def append(self, name: str) -> None:
        """crea una `Playlist` llamada `name` y la agrega al final de la 
        lista.
        Parametros:
        - name: nombre de la playlist a agregar.
        Complejidad: O(n)
        """

        new_playlsit: Node = Node(Playlist(name))
        if self.is_empty():
            self.head = new_playlsit
            self._len += 1
            return

        if len(self) == 1:
            self.head.next = new_playlsit
            self._len += 1
            return

        actual: Node = self.head
        while actual.next is not None:
            actual = actual.next

        actual.next = new_playlsit
        self._len += 1

    def add_music_to_library(self, name: str, title: str, author: str) -> bool:
        """agrega una cancion (de titulo `title` y autor `author`) a una 
        playlist llamada `name`.
        Parametros:
        - name: nombre de la playlist en la cual agregar la cancion.
        - title: titulo de la cancion a agregar.
        - author: autor de la cancion a agregar.

        Retorna: `True` si encuentra una `Playlist` llamada `name` y 
        agrego la cancion, de otra manera, `False`.
        """

        playlist: Playlist|None = self.get(name)
        if playlist is None:
            return False

        playlist.append(title, author)
        return True

    def remove(self, name: str) -> bool:
        """Elimina la primera `Playlist` de la lista cuyo nombre coincide
        con `name`.
        Parametros:
        - name: nombre de la lista a eliminar.

        Retorna: `True` si encontro una `Playlsist` con el mismo nombre y
        la elimino, de otra manera, `False`.
        Complejidad: O(n).
        """

        if self.is_empty():
            return False

        actual: Node = self.head
        previous: Node|None = None
        while actual is not None and actual.data.name != name:
            previous = actual
            actual = actual.next

        if actual is None:
            return False

        if previous is None:
            self.head = actual.next
            self._len -= 1
            return True

        previous.next = actual.next
        self._len -= 1
        return True

    def get(self, name: str) -> Playlist|None:
        """Obtiene una lista por nombre.
        Parametros:
        - name: nombre de la `Playlist` a obtener.

        Retorna: la primera `Playlsit` cuyo nombre coincida con `name`,
        de otra manera, `None`.
        """

        if self.is_empty():
            return None

        actual: Node = self.head
        while actual is not None and actual.data.name != name:
            actual = actual.next

        if actual is None:
            return None

        return actual.data

    def get_names(self) -> list[str]:
        """Retorna una lista que contiene los nombres de las 
        `Playlist`s que guarda la lista.
        """

        if self.is_empty():
            return []

        actual: Node = self.head
        names: list[str] = []
        while actual is not None:
            names.append(actual.data.name)
            actual = actual.next

        return names

    def is_empty(self) -> bool:
        return len(self) <= 0

    def __len__(self) -> int:
        return self._len

