"""Este modulo contiene la clase Pila. La cual es una implementacion de
   la estructura de datos 'pila'.
"""


class Pila():
    """Implementacion de la estructura de datos 'pila'.

    Funciones Publicas:
    - apilar
    - desapilar
    - tope
    - esta_vacia
    """

    def __init__(self) -> None: 
        self._datos: list[Any] = []

    def __len__(self) -> int:
        return len(self._datos)

    def apilar(self, dato: Any) -> None:
        """Agrega un dato al final de la pila.

        Parametros:
        - dato: el dato que se va a apilar a la pila.
        """

        self._datos.append(dato)

    def desapilar(self) -> Any:
        """Desapila el ultimo dato de la pila(removiendolo).

        Retorna el ultimo dato de la pila y elimina dicho dato de la 
        pila.
        """
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._datos.pop()

    def tope(self) -> Any:
        """Retorna el ultimo valor de la pila sin eliminarlo.

        Excepciones:
        - IndexError: Cuando la pila esta vacia.
        """
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._datos[-1]

    def esta_vacia(self) -> bool:
        """Verifica si la pila esta vacia."""
        return len(self._datos) == 0

