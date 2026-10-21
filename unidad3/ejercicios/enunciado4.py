"""4) Bicola
Implementa Bicola con operaciones en ambos extremos y muestra cómo simular:

- una pila,
- una cola.
"""

class EmptyError(Exception):
    def __init__(self, args = None):
        self.args = args
        super().__init__(self.args)

    def __str__(self) -> str:
        excep = ''
        for i in self.args:
            for j in i:
                excep += str(j)
        return excep


class DoubleNode:
    def __init__(self, data) -> None:
        self.data: any = data
        self.next: 'DoubleNode'|None = None
        self.prev: 'DoubleNode'|None = None


class DeQueue:
    """Implementacion de la Bicola usando una lista enlazada doble.
    Metodos:
    - insert_head(data:any)
    - insert_tail(data:any)
    - pop_head()
    - pop_tail()
    - is_empty()
    - __len__()
    - __str__()
    """

    def __init__(self) ->  None:
        self._head: DoubleNode|None = None
        self._tail: DoubleNode|None = None
        self._size: int = 0
    
    def insert_head(self, data: any) -> None:
        """Inserta una dato al principio de la bicola.
        Parametros:
        - data: El dato a insertar.
        """

        new_node: DoubleNode = DoubleNode(data)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._head.prev = new_node
            new_node.next = self._head
            self._head = new_node

        self._size += 1

    def insert_tail(self, data: any) -> None:
        """Inserta una dato al final de la bicola.
        Parametros:
        - data: El dato a insertar.
        """

        new_node: DoubleNode = DoubleNode(data)

        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node

        self._size += 1

    def pop_head(self) -> any:
        """Retorna el elemento del principio de la bicola y lo elimina.
        Excepciones:
        - EmptyError: Si la bicola esta vacia.
        """

        if self.is_empty():
            raise EmptyError(
                f"Error: La bicola esta vacia."
            )
        
        data: any = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        self._size -= 1

        return data

    def pop_tail(self) -> any:
        """Retorna el elemento del final de la bicola y lo elimina.
        Excepciones:
        - EmptyError: Si la bicola esta vacia.
        """

        if self.is_empty():
            raise EmptyError(
                f"Error: La bicola esta vacia."
            )
        
        data: any = self._tail.data
        self._tail = self._tail.prev
        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None
        self._size -= 1

        return data
    
    def is_empty(self) -> bool:
        """Verifica si la bicola esta vacia."""
        return self._size == 0
    
    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        """Retorna una cadena de caracteres que representa la bicola."""
        result: str = '['
        current: DoubleNode = self._head
        while current is not None:
            if current != self._head:
                result += ', '
            result += str(current.data)
            current = current.next
        result += ']'
        return result


def main():
    print(f"Demo:")
    d: DeQueue = DeQueue()

    print(f"Simulacion de una pila:")
    print(f"Se puede hacer insertando al inicio y eliminando al inicio:")
    d.insert_head(0)
    print(f"Insertar Inicio {0} : {str(d)}")
    d.insert_head(1)
    print(f"Insertar Inicio {1} : {str(d)}")
    d.insert_head(2)
    print(f"Insertar Inicio {2} : {str(d)}")
    print()

    print(f"Eliminar Inicio {d.pop_head()} : {str(d)}")
    print(f"Eliminar Inicio {d.pop_head()} : {str(d)}")
    print(f"Eliminar Inicio {d.pop_head()} : {str(d)}")
    print()

    print(f"Simulacion de una cola:")
    print(f"Se puede simular una cola insertando al inicio y eliminando al final:")
    d.insert_head(0)
    print(f"Insertar Inicio {0} : {str(d)}")
    d.insert_head(1)
    print(f"Insertar Inicio {1} : {str(d)}")
    d.insert_head(2)
    print(f"Insertar Inicio {2} : {str(d)}")
    print()

    print(f"Eliminar Final {d.pop_tail()} : {str(d)}")
    print(f"Eliminar Final {d.pop_tail()} : {str(d)}")
    print(f"Eliminar Final {d.pop_tail()} : {str(d)}")
    print()

    print(f"Simulacion de una pila:")
    print(f"Se puede hacer insertando al final y eliminando al final:")
    d.insert_tail(0)
    print(f"Insertar Final {0} : {str(d)}")
    d.insert_tail(1)
    print(f"Insertar Final {1} : {str(d)}")
    d.insert_tail(2)
    print(f"Insertar Final {2} : {str(d)}")
    print()

    print(f"Eliminar Final {d.pop_tail()} : {str(d)}")
    print(f"Eliminar Final {d.pop_tail()} : {str(d)}")
    print(f"Eliminar Final {d.pop_tail()} : {str(d)}")
    print()

    print(f"Simulacion de una cola:")
    print(f"Se puede simular una cola insertando al final y eliminando al inicio:")
    d.insert_tail(0)
    print(f"Insertar Final {0} : {str(d)}")
    d.insert_tail(1)
    print(f"Insertar Final {1} : {str(d)}")
    d.insert_tail(2)
    print(f"Insertar Final {2} : {str(d)}")
    print()

    print(f"Eliminar Inicio {d.pop_head()} : {str(d)}")
    print(f"Eliminar Inicio {d.pop_head()} : {str(d)}")
    print(f"Eliminar Inicio {d.pop_head()} : {str(d)}")
    print()


if __name__ == "__main__":
    main()