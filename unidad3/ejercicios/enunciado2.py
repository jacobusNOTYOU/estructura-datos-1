"""2) Pila estatica y dinamica

Implementa dos pilas:
- PilaEstatica (capacidad fija),
- PilaDinamica (nodos enlazados).

Comparar el comportamiento ante desbordamiento y bajo uso intensivo de
`apilar/desapilar`.
"""

from abc import ABC, abstractmethod

class PilaADT(ABC):
    """Interfaz abstracta del ADT Pila
    
    Metodos:
    - apilar(dato)
    - desapilar()
    - vacio()
    """

    @abstractmethod
    def apilar(self, dato: any) -> None:
        """Agrega un elemento a la pila.
        
        Parametros:
        - dato: El dato a apilar.
        """
        pass

    @abstractmethod
    def desapilar(self) -> any:
        """Retorna el ultimo dato en apilarse y lo elimina de la Pila."""
        pass

    @abstractmethod
    def vacio() -> bool:
        """Verifica si la Pila esta vacia."""
        pass


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


class PilaEstatica(PilaADT):
    """Implementacion de la Pila usando un arreglo con un limite de 
    elementos que puede contener.

    Metodos:
    - apilar(dato)
    - desapilar()
    - vacio()
    - lleno()
    """

    def __init__(self, capacidad: int) -> None:
        self._datos: list[any] = [None] * capacidad
        self._capacidad: int = capacidad
        self._n: int = 0

    def apilar(self, dato: any) -> None:
        """Agrega un elemento a la pila.
        
        Parametros:
        - dato: El dato a apilar.

        Excepciones:
        - OverflowError: Si la Pila ya esta lleno.

        Complejidad: O(1).
        """
        if self.lleno():
            raise OverflowError("Error: La pila ya esta llena!")

        self._n += 1
        self._datos.append(dato)

    def desapilar(self) -> any:
        """Retorna el ultimo dato en apilarse y lo elimina de la Pila.
        
        Excepciones:
        - EmptyError: Se la Pila esta vacia.

        Complejidad: O(1).
        """
        if self.vacio():
            raise EmptyError("Error: La Pila esta vacia!")

        elemento: any = self._datos[self._n]
        self._n -= 1
        return elemento

    def vacio(self) -> bool:
        """Verifica si la Pila esta vacia."""
        return self._n == 0

    def lleno(self) -> bool:
        """Verifica si la Pila llego a su capacidad maxima"""
        return self._n == self._capacidad


class PilaDinamica(PilaADT):
    """Implementacion de Pila dinamica (lista enlazada simple).
    
    Metodos:
    - apilar(dato)
    - desapilar()
    - vacio()
    """

    class _Nodo:
        def __init__(self, dato: any) -> None:
            self.dato: any = dato
            self.siguiente: '_Nodo'|None = None

    def __init__(self) -> None:
        self._cabeza: self._Node|None = None

    def apilar(self, dato: any) -> None:
        """Agrega un elemento a la pila.
        
        Parametros:
        - dato: El dato a apilar.

        Complejidad: O(1).
        """

        nuevo: self._Nodo = self._Nodo(dato)
        if self.vacio():
            self._cabeza = nuevo
        else:
            nuevo.siguiente = self._cabeza
            self._cabeza = nuevo

    def desapilar(self) -> any:
        """Retorna el ultimo dato en apilarse y lo elimina de la Pila.
        
        Excepciones:
        - EmptyError: Si la Pila esta vacia.

        Complejidad: O(1).
        """

        if self.vacio():
            raise EmptyError("Error: La Pila esta vacia!")

        elemento: any = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        return elemento

    def vacio(self) -> bool:
        """Verifica si la Pila esta vacia."""
        return self._cabeza is None

def main():
    print('Comparacion de la PilaEstatica y la PilaDinamica:')
    print('-------------------------------------------------')
    print()

    print('Complejidad de apilar/desapilar:')
    print()
    print('|------------------------------------|')
    print('| Pila         | apilar  | desapilar |')
    print('|------------------------------------|')
    print('| PilaEstatica |   O(1)  |   O(1)    |')
    print('|------------------------------------|')
    print('| PilaDinamica |   O(1)  |   O(1)    |')
    print('|------------------------------------|')
    print()

    n: int = 1000
    estatica: PilaEstatica = PilaEstatica(n) 
    dinamica: PilaDinamica = PilaDinamica()
    datos: list[int] = []
    for i in range(n):
        datos.append(i)

    print('Uso intencivo de apilar/desapilar para 1000 datos(memoria):')
    print('----------------------------------')
    print()
    import tracemalloc

    print('PilaEstatica')

    tracemalloc.start()
    # Apilado
    for i in datos:
        estatica.apilar(i)
    estatica_size, estatica_peak = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()

    # Desapilado
    for i in datos:
        estatica.desapilar()
    estatica_size_d, estatica_peak_d = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()
    tracemalloc.stop()

    print('Uso de memoria apilado:')
    print(f'Memoria: {estatica_size} , Maxima: {estatica_peak}.')
    print('Uso de memoria desapilado:')
    print(f'Memoria: {estatica_size_d} , Maxima: {estatica_peak_d}.')
    print()

    print('PilaDinamica')

    tracemalloc.start()
    # Apilado
    for i in datos:
        dinamica.apilar(i)
    dinamica_size, dinamica_peak = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()

    # Desapilado
    for i in datos:
        dinamica.desapilar()
    dinamica_size_d, dinamica_peak_d = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()
    tracemalloc.stop()

    print('Uso de memoria apilado:')
    print(f'Memoria: {dinamica_size} , Maxima: {dinamica_peak}.')
    print('Uso de memoria desapilado:')
    print(f'Memoria: {dinamica_size_d} , Maxima: {dinamica_peak_d}.')
    print()

    print('Comportamiento ante desbordamiento:')
    print('-----------------------------------')
    print()

    # Reapilado
    for i in datos:
        estatica.apilar(i)

    # Reapilado
    for i in datos:
        dinamica.apilar(i)

    print('La PilaEstatica tiene una capacidad de 1000 elementos.')
    print('La PilaEstatica esta llena en este momento.')
    print('Si le agregarmos un elemento:')
    try:
        estatica.apilar(1001)
    except OverflowError:
        print(OverflowError)
    print()

    print('La PilaDinamica no tiene un limite en si.')
    print('Igualmente la PilaDinamica posee 1000 elementos en este momento.')
    print('Si le agregarmos un elemento:')
    try:
        dinamica.apilar(1001)
    except OverflowError:
        print(OverflowError)
    else:
        print('El dato se apilo.')
    print()

    print()
    print('Conclusion:')
    print('-----------')
    print()
    print('Se puede concluir que, la pila estatica tiene la ventaja de usar\n'
          'menos memoria al estar llena, pero, siempre usa la misma cantidad\n'
          'de memoria sin importar si esta llena y su capacidad es fija.\n\n'
          'La pila dinamica tiene la ventaja de no tener una capacidad fija\n'
          'y el espacio que usa varia deacuerdo a la cantidad de elementos que\n'
          'contiene, pero, usa mas memoria que la pila estatica cuando esta\n'
          'esta en su maxima capacidad.\n'
    )


if __name__ == '__main__':
    main()