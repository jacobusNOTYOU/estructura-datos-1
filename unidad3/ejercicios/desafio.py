"""Desafío
Construye un mini sistema de turnos:
- cola para atención,
- hash para búsqueda rápida de turno por código,
- persistencia opcional al finalizar.
"""

class Cola:
    """Una cola dinamica.
    Metodos:
    - encolar
    - desencolar
    - siguiente
    """

    class _Nodo:
        def __init__(self, dato: any) -> None:
            self.dato: any = dato
            self.sig: '_Nodo'|None = None

    def __init__(self) -> None:
        self._cabeza: __Nodo|None = None

    def encolar(self, dato: any) -> None:
        """Encola un dato en la cola."""
        if self._cabeza is None:
            self._cabeza = _Nodo(dato) 
            return
        
        actual: _Nodo|None = self._cabeza
        while actual.sig is not None:
            actual = actual.sig
        
        actual.sig = _Nodo(dato)
    
    def desencolar(self) -> any|None:
        """Desencola un elemento de la cola. Retorna None si esta vacio."""
        if self._cabeza is None:
            return None
        
        dato: any = self._cabeza.dato
        resto: _Nodo = self._cabeza.sig
        self._cabeza.sig = None
        self._cabeza = resto
        return dato
    
    def siguiente(self) -> any|None:
        """Retorna el elemento que sigue en la cola (el que se va a desencolar 
        despues).
        """

        if self._cabeza is None:
            return None
        
        return self._cabeza.dato

    def listar(self) -> list[any]:
        """Retorna los elementos en una lista ordenada de primero a ultimo."""
        if self._cabeza is None:
            return [None]

        actual: _Nodo|None = self._cabeza
        result: list[any] = []
        while actual is not None:
            result.append(actual.dato)
            actual = actual.sig

        return result

    def cargar_lista(self, lista: list[any]) -> None:
        """Consume una lista ordenada de primero a ultimo."""
        for l in lista:
            self.encolar(l)

class TablaHash:
    """Implementacion de una table hash. Usa encadenamiento para resolver conflictos.
    Metodos:
    - insertar
    - buscar
    - eliminar
    - lista
    - cargar_lista
    """
    def __init__(self, capacidad: int) -> None:
        """Inicializa la tabla hash con una capacidad."""
        self._datos: list[tuple(str, any)] = [None] * capacidad
        self._capacidad: int = capacidad

    def insertar(self, llave: str, valor: any) -> None:
        """Inserta un elemento al diccionario. Si la llave ya esta presente,
        actualiza su valor.
        """
        index: int = self._index(llave)

        if self._datos[index] is None:
            self._datos[index] = []
            self._datos[index].append((llave, valor)) 
        else:
            for i in range(len(self._datos[index])):
                if self._datos[index][i][0] == llave:
                    self._datos[index][i] = (llave, valor)
                    return
            self._datos[index].append((llave, valor))

    def buscar(self, llave: str) -> any:
        """Busca un elemento cuya llave sea `llave`.
        Excepciones:
        - KeyError: si la llave no se encuentra.
        """
        index: int = self._index(llave)
        element = self._datos[index]
        for e in element:
            if e[0] == llave:
                return e[1]
        raise KeyError(
            f"Error: La llave {llave} no existe!"
        )

    def eliminar(self, llave: str) -> None:
        """Elimina un elemento cuya llave sea `llave`.
        Excepciones:
        - KeyError: si la llave no existe.
        """
        index: int = self._index(llave)
        elementos = self._datos[index]
        for e in elementos:
            if e[0] == llave:
                if len(elementos) == 1:
                    self._datos[index] = None
                else:
                    elementos.remove(e)
                return
        raise KeyError(
            f"Error: La llave {llave} no existe!"
        )

    def listar(self) -> list[(str, any)]:
        """Retorna una lista de pares llave-valor."""
        result: list[tuple(str, any)] = []

        for i in self._datos:
            if i is not None:
                for j in i:
                    result.append(j)
            else:
                result.append(None)
        return result


    def cargar_lista(self, lista: list[(str, any)]) -> None:
        """Consume una lista de pares llave-valor."""
        for l in lista:
            if l is not None:
                self.insertar(l[0], l[1])

    def _hash(self, llave: str) -> int:
        h: int = 1979
        for c in llave:
            h += ord(c) + 2 * (h<<2)
        return h
    
    def _index(self, llave) -> int:
        return self._hash(llave) % self._capacidad


class SistemDeTurnos:
    """"""
    def __init__(self) -> None:
        self._cola: Cola = Cola()
        self._historial: TablaHash = TablaHash()
    
    def agregar(self, nombre: str) -> None:
        pass

    def siguiente(self) -> str:
        pass

    def buscar(self, llave: str) -> (str, bool):
        pass

    def atender(self, llave: str) -> None:
        pass


def main():
    t = TablaHash(16)
    t.insertar('main', 134)
    t.insertar('master', 14)
    t.insertar('main', 86)
    l = t.listar()
    print(l)
    u = TablaHash(16)
    u.cargar_lista(l)
    print(u.listar())
    u.eliminar('main')
    print(u.listar())

if __name__ == '__main__':
    main()