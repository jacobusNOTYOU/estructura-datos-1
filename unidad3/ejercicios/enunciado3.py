"""3) Cola circular
Implementa `ColaCircular` sobre arreglo con índices circulares. Demuestra que 
reutiliza espacios liberados al desencolar.
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

class CircularQueue:
    """Cola circular implementada estaticamente con un arreglo.

    Metodos:
    - enqueue(data:any)
    - dequeue()
    - peek()
    - is_full()
    - is_empty()
    - __len__()
    """

    def __init__(self, size: any) -> None:
        """Inicializa la clase.
        Parametros:
        - size: la capacidad de la cola circular.
        """

        self._data: list[any] = [None] * size
        self._size: int = size
        self._front: int = -1
        self._rear: int = -1
        self._lenght: int = 0

    def enqueue(self, data: any) -> None:
        """Encola `data` al final de la estructura.
        Parametros:
        - data: el dato a encolar.

        Excepciones:
        - OverflowError: si la cola circular ya esta llena.
        """

        if self.is_full():
            raise OverflowError(
                f"Error: La cola circular ya esta llena!"
            )
        
        if self._front == -1:
            self._front = 0

        self._rear = (self._rear + 1) % self._size
        self._data[self._rear] = data
        self._lenght += 1

    def dequeue(self) -> any:
        """Retorna el element que esta al frente de la cola, siguiendo el 
        principio del FIFO.
        Excepciones:
        - EmptyError: cuando la cola circular esta vacia.
        """

        if self.is_empty():
            raise EmptyError(
                f"Error: La cola circular esta vacia!"
            )

        data: any = self._data[self._front]
        if self._front == self._rear:
            self._front = -1
            self._rear = -1
        else:
            self._front = (self._front + 1) % self._size
        return data

    def peek(self) -> any:
        """Retorna el elemento del frente de la cola, sin eliminarlo.
        Excepciones:
        - EmptyError: cuando la cola circular esta vacia.
        """

        if self.is_empty():
            raise EmptyError(
                f"Error: La cola circular esta vacia!"
            )
        return self._data[self._front]

    def is_full(self) -> bool:
        """Verifica si la cola circular esta llene."""
        return ((self._rear+1) % self._size) == self._front

    def is_empty(self) -> bool:
        """Verifica si la cola circular esta vacia."""
        return self._front == -1

    def capacity(self) -> int:
        """Retorna la capacidad de la cola circular."""
        return self._size

    def __len__(self) -> int:
        """Retorn la longitud de la cola circular (no la capacidad)."""
        return self._lenght


def main():
    print("Presentacion de la Cola Circular:")
    print()

    max_size = 7
    q: CircularQueue = CircularQueue(max_size)

    print(f"Comprobando si esta vacia: {q.is_empty()}")
    print(f"Comprobando si esta llena: {q.is_full()}")
    print()

    print(f"Llenandola con los siguientes datos:")
    data_1 = [0, 1, 1, 2, 3, 5, 8]
    print(data_1)
    for e in data_1:
        q.enqueue(e)
    print()

    print(f"Comprobando si esta vacia: {q.is_empty()}")
    print(f"Comprobando si esta llena: {q.is_full()}")
    print()

    print("Desencolando sus elementos:")
    for i in range(len(data_1)):
        print(f"{i}: {q.dequeue()}")
    print()

    print(f"Comprobando si esta vacia: {q.is_empty()}")
    print(f"Comprobando si esta llena: {q.is_full()}")
    print()

    print(f"Demostracion de que reutiliza los espacios")
    print()

    print(f"Llenandola con los siguientes datos:")
    data_2 = [13, 21, 34, 55, 89]
    print(data_2)
    for e in data_2:
        q.enqueue(e)
    print()

    print(f"Comprobando si esta vacia: {q.is_empty()}")
    print(f"Comprobando si esta llena: {q.is_full()}")
    print()

    print(
        f"Imprimimos en patalla los datos del arreglo que usa la cola circular"
    )
    for i in range(max_size):
        print(f"{i}: {q._data[i]}")
    print(f"Tal como se ve todavia quedan restos de los datos anteriores.")
    print()

    print(f"Si la desencolamos:")
    i = 0
    while not q.is_empty():
        print(f"{i}: {q.dequeue()}")
        i += 1
    
    print(f"Podemos apreciar que solo se imprimen los valores:")
    print(data_2)
    print()



if __name__ == "__main__":
    main()