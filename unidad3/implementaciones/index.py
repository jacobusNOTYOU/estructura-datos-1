"""Este modulo implementa la lista enlazada simple con un index para comprobar
la eficiencia, con respecto al tiempo, que se gana con el uso del index.
"""

from tabla_hash import HashTable
from faker import Faker
from time import time

class _Nodo:
    """Nodo de ListaSimple."""
    def __init__(self, dato: any) -> None:
        self._dato: any = dato
        self._siguiente: '_Nodo'|None = None


class ListaSimple:
    """Implementacion de la Lista Simple.

    Metodos:
    - insertar(dato)
    - eliminar(dato)
    - buscar(dato)

    - insertar_idx(dato)
    - eliminar_idx(dato)
    - buscar_idx(dato)
    """

    def __init__(self) -> None:
        self._cabeza: _Nodo|None = None
        self._tamanio: int = 0
        self._index: HashTable = HashTable()

    def insertar(self, dato: any) -> None:
        """Inserta un dato al inicio de la Lista.
        
        Parametros:
        - dato: el dato a insertar.
        """

        if not self.buscar(dato):
            nuevo: _Nodo = _Nodo(dato)
            nuevo._siguiente = self._cabeza
            self._cabeza = nuevo
            self._tamanio += 1
            self._index.insert(dato, nuevo)

    def eliminar(self, dato) -> None:
        """Elimina dato de la Lista si existe.
        
        Parametros:
        - dato: dato a eliminar.
        """
        if self._cabeza is not None:
            actual: _Nodo = self._cabeza
            anterior: _Nodo|None = None
            while actual is not None and actual._dato != dato:
                anterior = actual
                actual = actual._siguiente
            
            if actual is not None:
                anterior._siguiente = actual._siguiente
                self._index.remove(dato)
                self._tamanio -= 1

    def buscar(self, dato: any) -> bool:
        """Busca el dato en la Lista y retorna True si lo encuentra, sino False
        
        Parametros:
        - dato: dato a buscar.
        """

        if self._cabeza is None:
            return False
        
        actual: _Nodo = self._cabeza
        while actual is not None and actual._dato != dato:
            actual = actual._siguiente
        
        if actual is not None:
            return True

        return False

    def insertar_idx(self, dato: any) -> None:
        """Inserta (usando indice) un dato al inicio de la Lista.
        
        Parametros:
        - dato: el dato a insertar.
        """

        if not self.buscar_idx(dato):
            nuevo: _Nodo = _Nodo(dato)
            nuevo._siguiente = self._cabeza
            self._cabeza = nuevo
            self._tamanio += 1
            self._index.insert(dato, nuevo)

    def eliminar_idx(self, dato) -> None:
        """Elimina (usando indice) dato de la Lista si existe.
        
        Parametros:
        - dato: dato a eliminar.
        """

        if self.buscar_idx(dato):
            if self._cabeza is not None:
                actual: _Nodo = self._cabeza
                anterior: _Nodo|None = None
                while actual is not None and actual._dato != dato:
                    anterior = actual
                    actual = actual._siguiente
                
                if actual is not None:
                    anterior._siguiente = actual._siguiente
                    self._index.remove(dato)
                    self._tamanio -= 1

    def buscar_idx(self, dato: any) -> bool:
        """Busca (usando indice) el dato en la Lista y retorna True si lo 
        encuentra, sino False.
        
        Parametros:
        - dato: dato a buscar.
        """

        try:
            self._table.get(key)
        except:
            return False
        else:
            return True


def get_data(index, lista):
    nodo = lista._cabeza
    for i in range(index):
        if nodo is not None:
            nodo = nodo._siguiente
        else:
            break
    if nodo is not None:
        return nodo._dato
    raise IndexError(f'Error: {index} esta fuera del rango!')


def main(num_datos = 1000):
    fake = Faker()

    print(f'Indexacion de una lista')
    print()

    lista1: ListaSimple = ListaSimple()
    print(f'Insertando {num_datos} datos sin index:')
    start = time()
    for i in range(num_datos):
        lista1.insertar(fake.name())
    end = time()
    print(f"{end - start}s")
    print()

    lista: ListaSimple = ListaSimple()
    print(f'Insertando {num_datos} datos con index:')
    start = time()
    for i in range(num_datos):
        lista.insertar_idx(fake.name())
    end = time()
    print(f"{end - start}s")
    print()

    dato = get_data(int(num_datos/2), lista)
    print()

    dato = get_data(int(num_datos/2), lista)

    print(f"Buscar datos:")
    print()

    print(f'Buscar "{dato}" sin index:')
    start = time()
    lista.buscar(dato)
    end = time()
    print(f"duracion: {end - start} s")
    print()

    print(f'Buscar "*{dato}" con index:')
    start = time()
    lista.buscar_idx(dato)
    end = time()
    print(f"duracion: {end - start} s")
    print()

    print(f'Buscar "*" sin index:')
    start = time()
    lista.buscar('*')
    end = time()
    print(f"duracion: {end - start} s")
    print()

    print(f'Buscar "*" con index:')
    start = time()
    lista.buscar_idx('*')
    end = time()
    print(f"duracion: {end - start} s")
    print()

    print(f"Eliminar datos:")
    print()

    print(f"Eliminar '{dato}' sin index:")
    start = time()
    lista.eliminar(dato)
    end = time()
    print(f"duracion: {end - start} s")
    print()

    lista.insertar_idx(dato)
    print(f"Eliminar '{dato}' con index:")
    start = time()
    lista.eliminar_idx(dato)
    end = time()
    print(f"duracion: {end - start} s")
    print()

    print(f"Eliminar '*' sin index:")
    start = time()
    lista.eliminar('*')
    end = time()
    print(f"duracion: {end - start} s")
    print()

    print(f"Eliminar '*' con index:")
    start = time()
    lista.eliminar_idx('*')
    end = time()
    print(f"duracion: {end - start} s")
    print()

if __name__ == '__main__':
    main(10000)