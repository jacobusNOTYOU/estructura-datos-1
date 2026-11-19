"""Desafío
Construye un mini sistema de turnos:
- cola para atención,
- hash para búsqueda rápida de turno por código,
- persistencia opcional al finalizar.
"""

import time
import json

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
        self._cabeza: self._Nodo|None = None

    def encolar(self, dato: any) -> None:
        """Encola un dato en la cola."""
        if self._cabeza is None:
            self._cabeza = self._Nodo(dato) 
            return
        
        actual: self._Nodo|None = self._cabeza
        while actual.sig is not None:
            actual = actual.sig
        
        actual.sig = self._Nodo(dato)
    
    def desencolar(self) -> any|None:
        """Desencola un elemento de la cola. Retorna None si esta vacio."""
        if self._cabeza is None:
            return None
        
        dato: any = self._cabeza.dato
        resto: self._Nodo = self._cabeza.sig
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

        actual: self._Nodo|None = self._cabeza
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
    def __init__(self, capacidad: int = 16) -> None:
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
        if element is not None:
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
    def __init__(self, numero_turno: int = 0) -> None:
        self._cola: Cola = Cola()
        self._historial: TablaHash = TablaHash()
        self._numero_turno: int = numero_turno
    
    def agregar(self, nombre: str) -> None:
        codigo: str = f"N-{self._numero_turno}"
        self._numero_turno += 1
        turno: dict = {
            "codigo" : codigo,
            "nombre" : nombre,
            "tiempo" : ''
        }
        self._cola.encolar(turno)
        self._historial.insertar(codigo, turno)

    def siguiente(self) -> str|None:
        siguiente_turno: dict = self._cola.siguiente()
        if not siguiente_turno:
            return None
        if siguiente_turno['tiempo'] != '':
            atendido = siguiente_turno['tiempo']
        else:
            atendido = 'Todavia no se atendio'
        return (
            f"codigo: {siguiente_turno['codigo']},"
            f" nombre: {siguiente_turno['nombre']},"
            f" se atendio: {atendido}."
        )

    def buscar(self, clave: str) -> str:
        try:
            turno: dict = self._historial.buscar(clave)
        except KeyError:
            return f"Error: No se encontro el turno {clave} en el historial."
        else:
            if turno["tiempo"] != '':
                atendido = turno["tiempo"]
            else:
                atendido = 'Todavia no se atendio'

            return (
                f"codigo: {turno["codigo"]},"
                f" nombre: {turno["nombre"]},"
                f" se atendio: {atendido}."
                )

    def atender(self) -> str:
        t = time.gmtime()
        turno: dict = self._cola.desencolar()
        turno["tiempo"] = f"{t[2]}/{t[1]}/{t[0]}: {t[3]}:{t[4]}:{t[5]}"
        return turno['codigo']
    
    def to_dict(self) -> dict:
        return {
            "historial" : self._historial.listar(),
            "cola" : self._cola.listar(),
            "numero_turno" : self._numero_turno
        }
    
    def from_dict(self, dic) -> None:
        self._historial.cargar_lista(dic['historial'])
        self._cola.cargar_lista(dic['cola'])
        self._numero_turno = dic['numero_turno']

    def guardar(self, archivo: str) -> None:
        with open(archivo, 'w') as f:
            json.dump(self.to_dict(), f)        
    
    def cargar(self, archivo: str) -> None:
        with open(archivo, 'r') as f:
            self.from_dict(json.load(f))
    
    def listar_historial(self) -> list:
        return self._historial.listar()

def parse(s: SistemDeTurnos, inp: any) -> None:
    """
    Opciones:
    '1': agregar turno.
    '2': ver el siguiente turno.
    '3': atender turno.
    '4': buscar turno.
    '5': ver historial.
    '6': guardar archivo.
    '7': cargar de archivo.
    """
    match inp:
        case '1':
            nombre: str = input("Nombre: ")
            if not nombre.isalpha():
                print('Error: El nombre solo debe contener letras!')
            else:
                s.agregar(nombre)
                print('Agregado exitosamente!')
        case '2':
            turno: str|None = s.siguiente()
            if not turno:
                print("No hay turnos pendientes!")
            else:
                print(turno)
        case '3':
            codigo: str = s.atender()
            print(f"Se ha atendido con exito el turno: {codigo}")
            print(s.buscar(codigo))
            pass
        case '4':
            codigo: str = input("Ingrese el codigo: ")
            turno: str = s.buscar(codigo)
            print(turno)
        case '5':
            historial: list = s.listar_historial()
            for h in historial:
                if h is not None:
                    his = h[1]
                    print(
                        f"Codigo: {his["codigo"]}, "
                        f"Nombre: {his["nombre"]}, "
                        f"se atendio: {his["tiempo"]}."
                    )
        case '6':
            s.guardar('unidad3/ejercicios/turnos.json')
        case '7':
            s.cargar('unidad3/ejercicios/turnos.json')
        case _:
            print(
                f"Error: opcion inexistente {inp}!"
            )

def main():
    sis: SistemDeTurnos = SistemDeTurnos()

    print("Bienveido al sistema de turnos!")
    while True:
        print('Elige una opcion:')
        print('1. agregar un turno.')
        print('2. ver siguiente turno.')
        print('3. atender turno.')
        print('4. buscar turno.')
        print('5. ver historial.')
        print('6. guardar archivo.')
        print('7. cargar archivo.')
        inp = input(">")
        if inp == 'q':
            break
        parse(sis, inp)
        input()

if __name__ == '__main__':
    main()