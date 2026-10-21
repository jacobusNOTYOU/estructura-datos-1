"""5) Tabla hash
Implementa TablaHash con encadenamiento. Incluye:

- insertar,
- buscar,
- eliminar,
- actualización de clave existente.
"""

def hashy(s):
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

class TablaHash:
    def __init__(self, capacity: int = 16) -> None:
        self._buckets: list[list[tuple[any,any]]] = [[]] * capacity
        self._lenght: int = 0

    def insertar(self, key: any, value: any) -> None:
        index: int = self._index(key)
        bucket: list[tuple[any, any]] = self._buckets[index]

        if len(bucket) != 0:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket[i][1] = value
                    self._lenght += 1
                    return
            bucket.append((key, value))
            self._lenght += 1
        else:
            self._buckets[index] = [(key, value)]
            self._lenght += 1

    def buscar(self, key: any) -> any|None:
        bucket: list[tuple[any, any]] = self._buckets[self._index(key)]

        if len(bucket) != 0:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return bucket[i][1]
        return None
        

    def eliminar(self, key: any) -> None:
        bucket: list[tuple[any, any]] = self._buckets[self._index(key)]

        if len(bucket) != 0:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    del bucket[i]
        return 

    def __len__(self) -> int:
        return self._lenght

    def _index(self, key: any) -> int:
        return hashy(key) % len(self._buckets)

def main():
    th = TablaHash()
    data_keys = [
        "Pedro", "Lucas", "Marcos", "Juan", 
        "Marta", "Maria", "Esteban", "Natanael"
        ]
    data_values = [
        22, 34, 28, 23,
        25, 24, 33, 40
        ]
    
    print("Demo:")
    print()

    print("Insercion:")
    print(f"Claves: {data_keys}")
    print(f"Valores: {data_values}")
    for i in range(len(data_keys)):
        th.insertar(data_keys[i], data_values[i])
    print(f"Cantidad de elementos: {len(th)}")
    print()

    print("Busqueda:")
    print(f"Buscar '{data_keys[3]}': {th.buscar(data_keys[3])}.")
    print(f"Buscar '{data_keys[6]}': {th.buscar(data_keys[6])}.")
    print(f"Buscar '{data_keys[0]}': {th.buscar(data_keys[0])}.")
    print(
        f"Buscar '{data_keys[len(data_keys) - 1]}': "
        f"{th.buscar(data_keys[len(data_keys) - 1])}."
        )
    print()
    
    print("Eliminacion:")
    print(f"Eliminar {data_keys[4]}")
    th.eliminar(data_keys[4])
    print(f"Eliminar {data_keys[5]}")
    th.eliminar(data_keys[5])
    for i in range(len(data_keys)):
        print(f"Buscar {data_keys[i]}: {th.buscar(data_keys[i])}") 
    print()

if __name__ == "__main__":
    main()