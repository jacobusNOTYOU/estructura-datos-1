"""Este modulo contiene las estructuras de datos del proyecto. Las
cuales son:
- Music
- Node
- DoubleNode
- Playlist
- Library
"""

class Music:
    """Define las datos que componen una cancion:
    - title: el titulo de la cancion.
    - author: el autor de la cancion.
    """
    def __init__(self, title: str, author: str = "unkown", direction: str = "") -> None:
        self.title: str = title
        self.author: str = author
        self.direction: str = direction     

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


class DoubleNode:
    """Un nodo con dos punteros, uno apuntando  al siguiente y el otro 
    apuntando al anterior.
    Atributos:
    - data: el dato que guarda el nodo.
    - next: el nodo que le sigue a este nodo
    - prev: el nodo anterior a este nodo
    """
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.next: "DoubleNode"|None = None
        self.prev: "DoubleNode"|None = None


class Playlist:
    """Es un conjunto nombrado de `Music`, implementado en una lista
    enlazada doble.
    Atributos:
    - name: el nombre de la playlist.
    - head: el comienzo de la Playlist.

    Metodos:
    - append(title:str,author:str="unkown",direction:str="")    

    - remove(title: str)

    - get(title: str)
    - get_titles()
    - get_authors()
    - get_dir(title:str)

    - play()
    - next()
    - prev()
    - restart()

    - is_empty()
    - __len__()
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.head: DoubleNode|None = None
        self._actual: DoubleNode|None = self.head
        self._len: int = 0

    def append(self, title: str, author: str = "unkown", direction: str = "") -> None:
        """Agrega una cancion al final de la lista.
        Parametros:
        - title: titulo de la cancion.
        - author: autor de la cancion.
        - direction: la direccion en la que se encuetra la cancion.

        Complejiidad: O(n)
        """

        new_music: Music = Music(title, author, direction)
        new_node: DoubleNode = DoubleNode(new_music)
        at_start: bool = False
        if self._actual == self.head:
            at_start = True

        if self.is_empty():
            self.head = new_node

            if at_start:
                self._actual = self.head

            self._len += 1
            return

        if len(self) == 1:
            self.head.next = new_node
            new_node.prev = self.head
            self._len += 1
            return

        actual: DoubleNode = self.head
        while actual.next is not None:
            actual = actual.next

        actual.next = new_node
        new_node.prev = actual
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
        
        at_start: bool = False
        if self._actual == self.head:
            at_start = True

        actual: DoubleNode = self.head
        previous: DoubleNode|None = None
        while actual is not None and actual.data.title != title:
            previous = actual
            actual = actual.next

        if actual is None:
            return False
        
        if previous is not None:
            previous.next = actual.next
            if actual.next is not None:
                actual.next.prev = previous
            self._len -= 1
            return True

        self.head = actual.next
        if actual.next is not None:
            actual.next.prev = None
        if at_start:
            self._actual = self.head
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

        actual: DoubleNode = self.head
        while actual is not None and actual.data.title != title:
            actual = actual.next

        if actual is None:
            return None

        return actual.data

    def get_titles(self) -> list[str]:
        """Retorna una lista de los titulos de todas las canciones."""
        if self.is_empty():
            return []
        
        actual: DoubleNode = self.head
        titles: list[str] = []
        while actual is not None:
            titles.append(actual.data.title)
            actual = actual.next

        return titles

    def get_authors(self) -> list[str]:
        """Retorna una lista de los autores de todas las canciones."""
        if self.is_empty():
            return []
        
        actual: DoubleNode = self.head
        authors: list[str] = []
        while actual is not None:
            authors.append(actual.data.author)
            actual = actual.next

        return authors

    def get_dir(self, title: str) -> str:
        """Retorna la direccion de la primera cancion titulada `title`.
        Parametros:
        - title: el titulo de la cancion de la cual obtener la direccion.

        Retorna: si encuentra una cancion(una instancia de `Muisc`) con 
        el titulo dado, retorna su direccion.

        Excepciones:
        - NameError: si no se encuentra una cancion titulada `title` o si esta
        vacia.

        Complejidad: O(n).
        """

        if self.is_empty():
            raise NameError(
                f"Error: La playlist esta vacia!"
                )
        
        actual: DoubleNode = self.head
        previous: DoubleNode|None = None
        while actual is not None and actual.data.title != title:
            previous = actual
            actual = actual.next

        if actual is None:
            raise NameError(
                f"Error: No se encontro una cancion titulada {title}!"
                )
        
        return actual.data.direction

    def is_empty(self) -> bool:
        """Verifica si la lista esta vacia."""
        return len(self) <=0

    def play(self, title) -> Music:
        """Retorna la cacion `title` y actualiza el puntero a este."""
        actual: Node|None = self.head
        while actual is not None and actual.data.title != title:
            actual = actual.next
        
        if actual is None:
            raise NameError(
                f"Error: No  se encontro una cancio titulada {title}!"
            )

        self._actual = actual
        return self._actual.data

    def next(self, loop: bool = False) -> Music:
        """Retorn el que sigue."""
        if loop:
            if self._actual.next is None:
                self._actual = self.head
            else:
                self._actual = self._actual.next
        else:
            if self._actual.next is None:
                raise StopIteration("Se llego al final de la playlist.")
            else:
                self._actual = self._actual.next
        play: Music = self._actual.data
        return play

    def prev(self, loop: bool = False) -> Music:
        """Retorna el anterior."""
        if loop:
            if self._actual.prev is None:
                actual: Node = self.head
                while actual.next is not None:
                    actual = actual.next
                self._actual = actual
            else:
                self._actual = self._actual.prev
        else:
            if self._actual.prev is None:
                raise StopIteration("Se llego al principio de la playlist.")
            else:
                self._actual = self._actual.prev
        play: Music = self._actual.data
        return play

    def restart(self) -> None:
        """Mueve el recorrido al inicio."""
        self._actual = self.head

    def __len__(self) -> int:
        """Retorna la longitud de la lista al plicarse `len()` en ella."""
        return self._len

    def __iter__(self) -> "Playlist":
        actual = self.head
        while actual is not None:
            yield actual.data
            actual = actual.next


class StaticPlaylist:
    """Es un conjunto nombrado de `Music`, implementado en una lista
    estatica.
    Atributos:
    - name: el nombre de la playlist.
    - musics: la lista de musicas.

    Metodos:
    - append(title:str,author:str="unkown",direction:str="")    

    - remove(title: str)

    - get(title: str)
    - get_titles()
    - get_authors()
    - get_dir(title:str)

    - play()
    - next()
    - prev()
    - restart()

    - is_empty()
    - __len__()
    - is_in()
    """

    def __init__(self, name: str, capacity: int) -> None:
        """Crea la lista estatica con el nombre `name` y una capacidad de 
        `capacity`.
        Parametros:
        - name: el nombre de la playlist.
        - capacity: la capacidad de la playlist.
        """
        self.name: str = name
        self.musics: list[Music] = [None] * capacity
        self._current: int = 0
        self._len: int = 0
    
    def append(
        self, title: str, author: str = 'unkown', direction: str = '') -> None:
        """Agrega una `Music` y lo agrega a la lista.
        Parametros:
        - title: el titulo del `Music`.
        - author: el autor del `Music`.
        - direction: la direccion del `Music`.
        """

        self.musics[self._len] = Music(title, author, direction)
        self._len += 1
    
    def remove(self, title: str) -> None:
        """Elimina una `Music` de la playlist.
        Parametros:
        - title: el titulo del `Music`.
        """

        pos: int = self.is_in(title)
        if pos >= 0:
            del self.musics[pos] 
            self.musics.append(None)
            self._len -= 1

    def get(self, title) -> Music:
        """Retorna el `Music` cuyo titulo sea `title`.
        Parametros:
        - title: el titulo del `Music` que se quiere.
        """

        pos: int = self.is_in(title)
        if pos >= 0:
            return self.musics[pos]
        
        return None
    
    def get_titles(self) -> list[str]:
        """Retorna una lista de los titulos de los `Music` contenidos en la
        playlist.
        """
        
        if len(self) == 0:
            return []
        
        titles: list[str] = []
        for m in self.musics:
            titles.append(m.title)
        
        return titles
    
    def get_authors(self) -> list[str]:
        """Retorna una lista de los autores de los `Music` de la playlist."""
        if len(self) == 0:
            return []
        
        authors: list[str] = []
        for m in self.musics:
            authors.append(m.author)
        
        return authors
    
    def get_dir(self, title: str) -> str:
        """Retorna la direction del `Music` titulado `title`.
        Parametros:
        - title: titulo del `Music` cuya direccion se desea.

        Excepciones:
        - NameError: si no se encuetra un `Music` titulado `title`.
        """

        pos: int = self.is_in(title)
        if pos >= -1:
            return self.musics[pos].direction
        
        raise NameError(
            f"Error: No se encontro una cancion titulada {title}!"
        )

    def play(self, title: str) -> Music:
        """Retorna el `Music` titulado `title` y actualiza el puntero de la 
        playlist a este.
        Parametros:
        - title: el titulo del `Music` que se desea reproducir.

        Excepciones:
        - NameError: si es que no se encuentra un `Music` cuyo titulo sea 
        `title`.
        """

        pos: int = self.is_in(title)
        if pos >= 0:
            self._current = pos
            return self.musics[pos]

        raise NameError(
            f"Error: No se encontro una cancion titulada {title}!"
        )
    
    def next(self, loop: bool = False) -> Music:
        """Retorna el `Music` que sigue.
        Parametros:
        - loop: indica si se debe loopear la playlist.

        Excepcioes:
        - StopIteration: si es que `loop` es falso y se llego al ultimo 
        `Music`.
        """

        if loop:
            if self._current >= self._len:
                self._current = 0
            else:
                self._current += 1
        else:
            if self._current >= self._len:
                raise StopIteration(
                    f"Se llego al final de la playlist!"
                )
            else:
                self._current += 1
        
        return self.musics[self._current]

    def prev(self, loop: bool = False) -> Music:
        """Retorna el `Music` anterior.
        Parametros:
        - loop: indica si se debe loopear la playlist.

        Excepcioes:
        - StopIteration: si es que `loop` es falso y se llego al primer 
        `Music`.
        """

        if loop:
            if self._current <= 0:
                self._current = self._len
            else:
                self._current -= 1
        else:
            if self._current <= 0:
                raise StopIteration(
                    f"Se llego al final de la playlist!"
                )
            else:
                self._current -= 1
        
        return self.musics[self._current]

    def restart(self) -> None:
        """Retorna el puntero de la playlist al inicio."""
        self._current = 0

    def is_in(self, title: str) -> int:
        if len(self) == 0:
            return -1
        
        i = 0
        while i < len(self):
            if self.musics[i].title == title:
                break
            i += 1

        return i

    def is_empty(self) -> bool:
        """Verifica si la playlist esta vacia."""
        return self._len == 0
    
    def __len__(self) -> int:
        return self._len


class Library:
    """Una lista de `Playlist`s, implementada como  una lista enlazada
    simple.
    Atributos:
    - head: el inicio de la lista.

    Metodos:
    - append(name: str)
    - add_music(name:str,title:str,author:str,direction:str)

    - remove(name: str)
    - remove_music(name:str,title:str)

    - get(name: str)
    - get_names()
    - get_music(name:str,title:str)
    - get_music_dir(name:str,title:str)

    - play(name:str,title:str)
    - next(name:str)
    - prev(name:str)
    - restart(name:str)

    - is_empty()
    - __len__()
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

    def add_music(
        self, name: str, title: str, author: str = "unkown", direction: str = ""
    ) -> bool:
        """agrega una cancion (de titulo `title` y autor `author`) a una 
        playlist llamada `name`.
        Parametros:
        - name: nombre de la playlist en la cual agregar la cancion.
        - title: titulo de la cancion a agregar.
        - author: autor de la cancion a agregar.
        - direction: direccion en la que se encuentra la cancion.

        Retorna: `True` si encuentra una `Playlist` llamada `name` y 
        agrego la cancion, de otra manera, `False`.
        """

        playlist: Playlist|None = self.get(name)
        if playlist is None:
            return False

        playlist.append(title, author, direction)
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

    def remove_music(self, name: str, title: str) -> bool:
        """Elimina el primer `Music` titulado `title` que se encuentra en la
        `Playlist` llamada `name` si es que se encuentra.
        Parametros:
        - name: el nombre de la `Playlist` de la cual eliminar el `Music`.
        - title: el titulo de la cancion a eliminar.     

        Retorna: `True` si se encuentra una `Playlist` llamada `name` y si esta
        contiene un `Music` titulado `title`, si no, `False`.
        """

        playlist: Playlist|None = self.get(name)
        if playlist is None:
            return False
        
        return playlist.remove(title)

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

    def get_music(self, name: str, title: str) -> Music:
        """Retorna la primera cancion titulada `title` de la playlist llamada
        `name`, si es que la encuentra.
        Parametros:
        - name: el nombre de la playlist a la que pertenece la cancion.
        - title: el titulo de la cancion que se esta buscando.

        Retorna: Un `Music` si es que se encontro una playlist llamda `name` y
        en esa playlist una cancion titulada `title`.
        """

        playlist: Playlist|None = self.get(name)
        if playlist is None:
            return None
        
        music: Music|None = playlist.get(title)
        return music

    def get_music_dir(self, name: str, title: str) -> str:
        """Retorna la direccion de la primera cancion titulada `title` en la
        playlist llamada `name`.
        Parametros:
        - name: el nombre de la playlist en la que se encuentra la cancion.
        - title: el titulo de la cancion.

        Excepciones:
        - NameError: si no se encuentra la una cancion titulada `title` en la 
        playlist llamada `name`.
        """

        playlist: Playlist|None = self.get(name)
        if playlist is None:
            raise NameError(
                f"Error: No se encontro una playlist llamada '{name}'!"
            )
        
        try:
            direction: str = playlist.get_dir(title)
        except NameError:
            raise NameError(
                f"Error: No se encontro una cancion titulada '{title}' en la "
                f"playlist '{name}'!"
            )
        
        return direction

    def play(self, name: str, title: str) -> Music:
        """Retorna la cancion titulada `title` y mueve el puntero a dicha 
        cancion.
        """
        playlist: Playlist|None = self.get(name)
        if playlist is None:
            raise NameError(
                f"Error: no se encontro una playlist llamada '{name}'!"
            )

        return playlist.play(title)

    def next(self, name: str, loop: bool = False) -> Music:
        """Retorna el que sigue en la playlist `name`."""
        playlist: Playlist|None = self.get(name)
        if playlist is None:
            raise NameError(
                f"Error: no se encontro una playlist llamada '{name}'!"
            )
        return playlist.next(loop)

    def prev(self, name: str, loop: bool = False) -> Music:
        """Retorna el anterior en la playlist `name`."""
        playlist: Playlist|None = self.get(name)
        if playlist is None:
            raise NameError(
                f"Error: no se encontro una playlist llamada '{name}'!"
            )
        return playlist.prev(loop)

    def restart(self, name: str) -> None:
        """Retorna el anterior en la playlist `name`."""
        playlist: Playlist|None = self.get(name)
        if playlist is None:
            raise NameError(
                f"Error: no se encontro una playlist llamada '{name}'!"
            )
        return playlist.restart()

    def is_empty(self) -> bool:
        return len(self) <= 0

    def __len__(self) -> int:
        return self._len

    def __iter__(self):
        actual = self.head
        while actual is not None:
            yield actual.data
            actual = actual.next
