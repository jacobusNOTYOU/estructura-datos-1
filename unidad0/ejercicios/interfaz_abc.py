"""Este modulo contiene:
   - EstructuraLineal: Interfaz abstracta para estructuras lienales.
   - Pila: Implementacion de 'pila' usando EstructuraLineal.
   - Cola: Implementacion de 'cola' usando EstructuraLineal.
"""

from abc import ABC, abstractmethod
from typing import Any
from collections import deque


class EstructuraLineal(ABC):
    """Interfaz abstracta para estructuras lineales.
       
       Metodos y Funciones:
       - insertar
       - eliminar
       - esta_vacia
    """

    @abstractmethod
    def insertar(self, dato: Any) -> None:
        """Inserta un dato a la estructura.

        Parametros:
        - dato: Dato a insertar.
        """
        pass

    @abstractmethod
    def eliminar(self) -> None:
        """Elimina un dato de la estructura."""
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        """Verifica si la estructura esta vacia."""
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Retorna la longitud de la estructura."""
        pass


class Pila(EstructuraLineal):
    """Implementacion de 'pila', subclase de EstructuraLineal.

    Un contenedor de datos que sigue el principo FILO para la insercion
    y extraccion de datos.

    Metodos y Funciones:
    - insertar
    - extraer
    - eliminar
    - esta_vacia
    - tope
    """

    def insertar(self, dato: Any) -> None:
        """Apila un dato al final de la pila.

        Parametros:
        - dato: Dato a apilar.
        """

        self._datos.append(dato)

    def extraer(self) -> Any:
        """retorna el ultimo dato agregado a la pila y lo elimina.

        Excepciones:
        - IndexError: Cuando la lista esta vacia.
        """

        if self.esta_vacia():
            raise IndexError('La pila esta vacia!')
        return self._datos.pop()

    def eliminar(self) -> None:
        """Elimina el ultimo dato en ser agregado a la pila.

        Excepciones:
        - IndexError: Cuando la lista esta vacia.
        """

        if self.esta_vacia():
            raise IndexError('La pila esta vacia!')
        self._datos.pop()

    def esta_vacia(self) -> bool:
        """Verifica si la pila esta vacia."""
        return len(self._datos) == 0

    def tope(self) -> Any:
        """Retorn el ultimo dato en ser agregado a la pila sin eliminarlo.

        Excepciones:
        - IndexError: Cuando la lista esta vacia.
        """

        if self.esta_vacia():
            raise IndexError('La pila esta vacia!')
        return _datos[-1]

    
    def __init__(self) -> None:
        self._datos: list[Any] = []

    def __len__(self) -> int:
        """Retorn la cantidad de datos en la pila."""
        return len(self._datos)

class Cola(EstructuraLineal):
    """Implementa la 'cola', subclase de EstructuraLineal.

    Una estructura de datos que sigue el principio de FIFO.

    Funciones y Metodos:
    - insertar
    - extraer
    - eliminar
    - tope
    - esta_vacia
    """

    def insertar(self, dato: Any) -> None:
        """Inserta un elemento al final de la cola.

        Parametros:
        - dato: Dato a insertar.
        """

        self._datos.append(dato)

    def extraer(self) -> Any:
        """Retorna el dato mas viejo de la cola y lo elimina.

        Excepciones:
        - IndexError: Cuando la cola esta vacia.
        """
        if self.esta_vacia():
            raise IndexError('La cola esta vacia!')
        return self._datos.popleft()

    def eliminar(self) -> None:
        """Elimina el dato mas viejo de la cola.

        Excepciones:
        - IndexError: Cuando la cola esta vacia.
        """
        if self.esta_vacia():
            raise IndexError('La cola esta vacia!')
        self._datos.popleft()

    def tope(self) -> Any:
        """Retorna el dato ma viejo sin eliminarlo.

        Excepciones:
        - IndexError: Cuando la cola esta vacia.
        """
        if self.esta_vacia():
            raise IndexError('La cola esta vacia!')
        self._datos[0]

    def esta_vacia(self) -> bool:
        """Verifica si la cola esta vacia."""
        return len(self._datos) == 0



    def __init__(self) -> None:
        self._datos = deque()

    def __len__(self) -> int:
        """Retorna la longitud de la cola."""
        return len(self._datos)


def guardar_lista(lista: list[Any], contenedor: EstructuraLineal) -> None:
    """Guarda el contenido de lista en contenedor."""
    for item in lista:
        contenedor.insertar(item)


def graficar(contenedor: EstructuraLineal) -> None:
    """Grafica la estructura de datos segun su orden de extraccion."""
    while contenedor:
        print(contenedor.extraer())


lista: list[int] = [1, 2, 3, 4, 5]
pila = Pila()
cola = Cola()
guardar_lista(lista, pila)
print('Grafica de pila:')
graficar(pila)
print('\n')
guardar_lista(lista, cola)
print('Grafica de cola:')
graficar(cola)
