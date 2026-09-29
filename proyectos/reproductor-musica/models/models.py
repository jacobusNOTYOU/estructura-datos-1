"""Modelos del projecto:
- EmptyError.
- Lista enlazada.
"""

class EmptyError(Exception):
    """Error para objetos vacios."""
    def __init__(self, args = None):
        self.args = args
        super().__init__(self.args)

    def __str__(self) -> str:
        excep = ''
        for i in self.args:
            for j in i:
                excep += str(j)
        return excep

class Library:
    """Contiene canciones."""

    class _Node:
        def __init__(self, title, artist, duration):
            self.datos: list() = [title, artist, duration]
            self.next: "_Node"|None = None

        def to_dict(self):
            return {
                "title":self.datos[0],
                "artist":self.datos[1],
                "duration":self.datos[2]
            }

    def __init__(self, name):
        self.name = name
        self.head = None

    def add_music(self, title: str, artist: str, duration: int|float) -> None:

        music: self._Node = self._Node(title, artist, duration)
        if self.head is None:
            self.head = music
            return
        
        actual = self.head
        while actual.next is not None:
            actual = actual.next
        
        actual.next = music

    def seek_by_title(self, title):
        if self.head is None:
            return None

        actual = self.head
        while actual is not None and actual.datos[0] != title:
            actual = actual.next
        
        if actual is None:
            return None
        
        return actual.datos

    def seek_by_artist(self, artist):
        if self.head is None:
            return None

        music_lsit = []
        actual = self.head
        while actual is not None:
            if actual.datos[1] == artist:
                music_lsit.append(actual.datos)
            actual = actual.next
        
        return music_lsit

    def remove_song(self, title):
        if self.head is None:
            return

        actual = self.head
        previous = None
        while actual is not None and actual.datos[0] != title:
            previous = actual
            actual = actual.next

        if actual is None:
            return

        previous.next = actual.next

    def create_playlist(self, name, music_list = None) -> "Library":
        """
        Parametros:
        - music_list: lista musicas, cada musica es una lista de la forma:
            [title, artist, duration].
        """

        new_playlist = Library(name)

        if music_list is None:
            return new_playlist

        for music in music_list:
            new_playlist.add_music(music[0], music[1], music[2])

        return new_playlist

    def to_list(self):
        """Transforma 'Library' en formato json."""
        result = []

        actual = self.head
        while actual is not None:
            result.append(actual.to_dict())
            actual = actual.next

        return result



class ListOfLibraries:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new = self._Node(data)

        if self.head is None:
            self.head = new
            return
        
        actual = self.head
        while actual.next is not None:
            actual = actual.next
        
        actual.next = new
    
    def delete_by_number(self, number):
        if self.head is None:
            raise EmptyError("List is empty!") 

        actual = self.head
        previous = None
        count = 0
        while actual is not None and count != number:
            previous = actual
            actual = actual.next
            count += 1

        if actual is None:
            return

        previous.next = actual.next

    def delete_by_name(self, name):
        if self.head is None:
            raise EmptyError("List is empty!") 

        actual = self.head
        previous = None
        while actual is not None and actual.data.name != name:
            previous = actual
            actual = actual.next

        if actual is None:
            return

        if previous is not None:
            previous.next = actual.next
        elif actual.data.name == name:
            self.head = actual.next
        else:
            self.head = None

    def clear(self):
        self.head = None

    def to_dict(self):
        result = {}
        actual = self.head
        while actual is not None:
            result[actual.data.name] = actual.data.to_list()
            actual = actual.next

        return result

    def _from_list_to_library(self, library_name, library_list):
        library = Library(library_name)
        for item in library_list:
            library.add_music(item["title"], item["artist"], item["duration"])

        return library

    def fill_from_dict(self, dic):
        keys = list(dic)

        for key in keys:
            self.append(
                self._from_list_to_library(key, dic[key])
            )


# Helper Functions
def execute_instruction(instruction, input, library_list):
    match(instruction):
        case "add-playlist":
            new_playlist = Library(input)
            library_list.append(new_playlist)
        case "remove-playlist":
            library_list.delete_by_name(input)
        case "add-music":
            pass
        case "remove-music":
            pass
        case _:
            pass