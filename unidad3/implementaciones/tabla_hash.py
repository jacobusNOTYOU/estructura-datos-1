"""Implementacion de la tabla hash con rehashing y linear probing."""

def hashy(s):
    """Funcion hash para la tabla."""
    if isinstance(s, type('')):
        h: int = 0
        if len(s) < 1:
            return hash(s)
        else:
            h = ord(s[0]) + (h << 6) + (h << 6) - h
        for c in s:
            h = h * 1979
            h = h ^ ord(c)
        return h
    if isinstance(s, type(0)) or isinstance(s, type(0.0)):
        return s


class HashTable:
    """Tabla Hash con Linear Probing y Rehashing.
    Metodos:
    - insert(key:str|number,value:any)
    - remove(key:str|number)
    - get(key:str|number)
    - get_keys()
    - __len__()
    """
    def __init__(self, capacity: int = 16, load_factor: float = 0.75) -> None:
        """Inicializa la tabla.
        Parametros:
        - capacity: la capacidad minima de la tabla.
        - load_factor: que tan llena debe estar la tabla para hacer rehashing(en pro
        porcion)
        """

        self._slots: list[tuple(str|number, any)] = [None] * capacity
        self._lenght: int = 0
        self._load_factor: float = load_factor
        self._min_capacity: int = capacity
    
    def insert(self, key: str|number, value: any) -> None:
        """Inserta un par (clave, valor) a la tabla. Si ya existe, se 
        actualiza el valor del par.

        Parametros:
        - key: la clave del par.
        - value: el valor del par.

        Excepciones:
        - OverflowError: cuando la table esta llena. Quiere decir que
        el rehashing no esta funcionando correctamente.
        """

        self._rehash()
        self._insert(key, value)

    def remove(self, key: str|number) -> None:
        """Eliminar el par cuya clave sea igual a `key`.
        Parametros:
        - key: la clave del par a eliminar.

        Excepciones:
        - KeyError: si no se encontro la clave(no existe el par).
        """
        self._rehash()
        key_hash: int = self._index(key)
        index: int = key_hash
        
        while True:
            if self._slots[index] is not None and self._slots[index][0] == key:
                self._slots[index] = None
                self._lenght -= 1
                return

            index += 1
            if index == len(self._slots):
                index = 0

            if index == key_hash:
                break
        
        raise KeyError(f"Error: Key '{key}' doen't exist!")


    def get(self, key: str|number) -> any:
        """Retorn el valor del par cuya clave coincida con `key`.
        Parametros:
        - key: la clave del par.

        Excepciones:
        - KeyError: si no se encuentra la clave(no existe el par).
        """
        key_hash: int = self._index(key)
        index: int = key_hash
        
        while True:
            if self._slots[index] is not None and self._slots[index][0] == key:
                return self._slots[index][1]

            index += 1
            if index == len(self._slots):
                index = 0

            if index == key_hash:
                break
        
        raise KeyError(f"Error: Key '{key}' doen't exist!")

    def get_keys(self) -> list[str|number]:
        """Retorna una lista de todas las claves."""
        keys: list[str|number] = []

        for s in self._slots:
            if s is not None:
                keys.append(s[0])

        return keys

    def __len__(self) -> int:
        """Retorna la cantidad de elementos la tabla."""
        return self._lenght

    def _index(self, key: str|number) -> int:
        return hashy(key) % len(self._slots)

    def _insert(self, key: str|number, value: any) -> None:
        key_hash: int = self._index(key)
        index: int = key_hash
        
        while True:
            if self._slots[index] == None:
                self._slots[index] = (key, value)
                self._lenght += 1
                return

            if self._slots[index][0] == key:
                self._slots[index][1] = value
                return

            index += 1
            if index == len(self._slots):
                index = 0

            if index == key_hash:
                break
        
        raise OverflowError("Error: HashTable is full!")

    def _rehash(self) -> None:
        capacity: int = len(self._slots)
        load_factor: float = self._lenght / capacity

        if load_factor > self._load_factor:
            capacity *= 2
        elif (capacity > self._min_capacity and 
                load_factor < (self._load_factor/4)):
            capacity /= 2
        else:
            return
        
        old_list: list[tuple(str|number, any)] = self._slots
        self._slots = [None] * int(capacity)
        self._lenght = 0

        for e in old_list:
            if e is not None:
                self._insert(e[0], e[1])


def main():
    th = HashTable(capacity=8)
    data_keys = [
        "Pedro", "Lucas", "Marcos", "Juan", 
        "Marta", "Maria", "Esteban", "Natanael"
        ]
    data_values = [
        22, 34, 28, 23,
        25, 24, 33, 40
        ]
    
    print("Demo:")
    print("Para de mostrar el rehashing tenemos:")
    print(f"Elementos en la tabla: {len(th)}.")
    print(f"Capacidad de la tabla: {len(th._slots)}.")
    print()

    print("Insercion:")
    print(f"Claves: {data_keys}")
    print(f"Valores: {data_values}")
    for i in range(len(data_keys)):
        th.insert(data_keys[i], data_values[i])
    print(f"Cantidad de elementos: {len(th)}")
    print()

    print("Busqueda:")
    print(f"Buscar '{data_keys[3]}': {th.get(data_keys[3])}.")
    print(f"Buscar '{data_keys[6]}': {th.get(data_keys[6])}.")
    print(f"Buscar '{data_keys[0]}': {th.get(data_keys[0])}.")
    print(
        f"Buscar '{data_keys[len(data_keys) - 1]}': "
        f"{th.get(data_keys[len(data_keys) - 1])}."
        )
    print()
    
    print("Eliminacion:")
    print(f"Eliminar {data_keys[4]}")
    th.remove(data_keys[4])
    print(f"Eliminar {data_keys[5]}")
    th.remove(data_keys[5])
    print("La tabla ahora contiene:")
    keys = th.get_keys()
    for k in keys:
        print(f"{k}: {th.get(k)}.")
    print()

    print("Rehashing:")
    print(f"Elementos en la tabla: {len(th)}.")
    print(f"Capacidad de la tabla: {len(th._slots)}.")
    print("Al casi llenarse la tabla hizo el rehashing para evitar coliciones.")
    print()

    
if __name__ == "__main__":
    main()
