"""Resolucion de los enunciados de la Unidad 1

Objetivo:
Comprender y aplicar los modelos de representación de datos: abstracto, estático, dinámico y persistente.
"""

from abc import ABC, abstractmethod
from typing import Any
import random
import timeit
import tracemalloc


# ENUNCIADO #1
# ADT de Pila
class ADTPila(ABC):
    """ Interfaz de pila.
    
    Funciones y Metodos:
    - apilar
    - desapilar]
    - tope
    - esta_vacia
    """
    @abstractmethod
    def apilar(self, dato: Any) -> None:
        """Inserta el dato al final de la pila.
        
        Args:
        - dato: El dato a apilar.
        """
        pass

    @abstractmethod
    def desapilar(self) -> Any:
        """Retorna el ultimo elemento y lo elimina de l apila."""
        pass

    @abstractmethod
    def tope(self) -> Any:
        """Retorna el ultimo elemento de la pile sin eliminarlo"""
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        """Verifica si esta vacia."""
        pass


# PilaArray
class PilaArray(ADTPila):
    """ Implementacion de ADTPila en base de un arreglo.
    
    Funciones y Metodos:
    - apilar
    - desapilar
    - tope
    - esta_vacia
    """

    def __init__(self) -> None:
        self._pila: list[Any] = []

    def apilar(self, dato: Any) -> None:
        """Inserta el dato al final de la pila.
        
        Args:
        - dato: El dato a apilar.
        """
        self._pila.append(dato)

    def desapilar(self) -> Any:
        """Retorna el ultimo elemento y lo elimina de l apila.
        
        Excepcion:
        - IndexError: si la pila esta vacia.
        """
        if self.esta_vacia():
            raise IndexError('La pila esta vacia!')
        result = self._pila[-1]
        del self._pila[-1]
        return result

    def tope(self) -> Any:
        """Retorna el ultimo elemento de la pile sin eliminarlo.
        
        Excepcion:
        - IndexError: si la pila esta vacia.
        """
        if self.esta_vacia():
            raise IndexError('La pila esta vacia!')
        return self._pila[-1]

    def esta_vacia(self) -> bool:
        """Verifica si esta vacia."""
        return len(self._pila) <= 0


class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class PilaLista(ADTPila):
    """Implemetacion de ADTPila usando Nodos."""
    def __init__(self) -> None:
        self.ultimo: Nodo | None = None 

    def apilar(self, dato) -> None:
        """Agrega un dato al final de la pila.
        
        Parametros:
        - dato: El dato a insertar.
        """
        nuevo = Nodo(dato)
        nuevo.siguiente = self.ultimo
        self.ultimo = nuevo

    def desapilar(self) -> Any:
        """Retorna el ultimo elemento y lo elimina.
        
        Excepciones:
        - IndexError: si la pila esta vacia.
        """
        
        if self.esta_vacia():
            raise IndexError('La pila esta vacia!')
        dato = self.ultimo.dato
        self.ultimo = self.ultimo.siguiente
        return dato

    def tope(self) -> Any:
        """Retorna el ultimo elemento sin eliminarlo.
        
        Excepciones:
        - IndexError: si la pila esta vacia.
        """

        if self.esta_vacia():
            raise IndexError('La pila esta vacia!')
        return self.ultimo.dato

    def esta_vacia(self) -> bool:
        """Verifica si la pila esta vacia."""
        return self.ultimo is None


def llenar_pila(pila: ADTPila, cantidad: int) -> list[Any]:
    for i in range(cantidad):
        pila.apilar(i)

    l: list[Any] = []
    for i in range(cantidad):
        l.append(pila.desapilar())

    return l

# Demos
print('Demos de ADT')
print('-------------')
# PilaArray
print('Demo de PilaArray:')
pila_array = PilaArray()
print(llenar_pila(pila_array, 10))

# PilaLista
print('Demo de PilaLista:')
pila_lista = PilaLista()
print(llenar_pila(pila_lista, 10))


# ENUNCIADO #2  
# Estatico vs Dinamico

# ArrayEstatico
class ArrayEstatico:
    """ Una secuencia de valores con una capacidad fija desde su instanciacion.
    
    Funciones y Metodos:
    - agregar
    - obtener
    - eliminar
    - modificar
    - capacidad
    - tamano
    """

    def __init__(self, capacidad: int) -> None:
        """El objeto se inicializa con una capacidad que no va a cambiar."""
        self._array: list[Any] = [None] * capacidad
        self._capacidad: int = capacidad
        self._tamano: int = 0

    def agregar(self, dato: Any) -> None:
        """Agrega un valor al final del arreglo e incrementa el tamano.
        
        Parametros:
        - dato: El dato a agregar.

        Excepciones:
        - OverflowError: Si se suprera la capacidad del arreglo.

        Complejidad: O(1)

        *Nota: No se debe superar la capacidad del arreglo.
        """

        if self._tamano == self._capacidad:
            raise OverflowError("Se ha superado la capacidad del arreglo!")
        self._array[self._tamano] = dato
        self._tamano += 1

    def obtener(self, indice: int) -> Any:
        """Obtiene el elemento que esta en el indice.
        
        Parametros:
        - indice: La posicion del elemento a obtener.

        Excepciones:
        - IndexError: Se el indice esta fuera del rango:
                        0 <= indice < tamano

        Complejidad: O(1)
        """

        if indice < 0 or self._tamano <= indice:
            raise IndexError('Indice fuera de rango.')
        return self._array[indice]

    def eliminar(self, indice: int) -> None:
        """Eliminar el elemento que esta en el indice.
        
        Parametros:
        - indice: La posicion del elemto a eliminar.
        """

        if indice < 0 or self._tamano <= indice:
            raise IndexError('El indice esta fuera de rango.')
        izquierda: list[Any] = self._array[:indice]
        derecha: list[Any] = self._array[indice + 1:] # Revisar el caso en el que array esta lleno e indice es el ultimo elemento!
        self._array = izquierda + derecha + []
        self._tamano -= 1

    def modificar(self, indice: int, dato: int) -> None:
        """Asigna el dato en el elemento que esta en la posicion del indice.
        
        Parametros:
        - indice: Posicion del elemento a modificar.
        - dato: Dato a asignar en la posicion especificada.

        Excepciones:
        - IndexError: Se el indice esta fuera del rango:
                        0 <= indice < tamano
        """ 

        if indice < 0 or self._tamano <= indice:
            raise IndexError('Indice fuera de rango.')
        self._array[indice] = dato

    def capacidad(self) -> int:
        """Retorna la capacidad del array."""
        return self._capacidad

    def tamano(self) -> int:
        """Retorna la cantidad de elementos en el array."""
        return self._tamano


# ArrayDinamico
class _Nodo:
    def __init__(self, dato: Any) -> None:
        self.valor: Any = dato
        self.siguiente: _Nodo | None = None


class ArrayDinamico:
    """Lista enlacada de tamano variable.
    
    Funciones y Parametros:
    - insertar_inicio
    - insertar_fin
    - obtener
    - modificar
    - eliminar
    - tamano
    """

    def __init__(self) -> None:
        self._extremo: _Nodo | None = None
        self._tamano = 0

    def insertar_inicio(self, dato: Any) -> None:
        """Inserta un dato al inicio de la estructura.
        
        Parametros:
        - dato: Dato a insertar.
    
        Complejidad: O(1)
        """

        nuevo = _Nodo(dato)
        nuevo.siguiente = self._extremo
        self._extremo = nuevo
        self._tamano += 1

    def insertar_fin(self, dato) -> None:
        """Inserta un dato al final de la estructura.
        
        Parametros:
        - dato: Dato a insertar.

        Complejidad: O(n)
        """

        nodo = self._extremo
        nuevo = _Nodo(dato)
        if nodo is not None:
            while nodo.siguiente is not None:
                nodo = nodo.siguiente
            nodo.siguiente = nuevo
        else:
            self._extremo = nuevo
        self._tamano += 1


    def obtener(self, indice: int) -> Any:
        """Retorna el elemento que esta en la posicion dada.
        
        Parametros:
        - indice: posicion del elemento.

        Exepciones:
        - IndexError: si el indice esta fuera de rango.

        Complejidad: O(n)
        """

        if indice < 0 or self._tamano <= indice:
            raise IndexError('Indice fuera de rango!')
        actual: _Nodo = self._extremo
        for i in range(indice):
            actual = actual.siguiente
        return actual.valor

    def modificar(self, indice: int, dato: Any) -> None:
        """Modifica el elemento en el indice dado.
        
        Parametros:
        - indice: posicion del elemento a modificar.
        - dato: Dato a asignar.

        Excepcion:
        - IndexError: si el indice esta fuera de rango.

        Complejidad: MC: O(1) y PC: O(n)
        """

        if indice < 0 or self._tamano <= indice:
            raise IndexError('Indece fuera de rango!')
        actual: _Nodo = self._extremo
        for i in range(indice):
            actual = actual.siguiente
        actual.valor = dato

    def eliminar(self, indice: int) -> None:
        """Elimina el elemento que esta en la posicion dada.
        
        Parametros:
        - indice: posicion del elemento.

        Exepciones:
        - IndexError: si el indice esta fuera de rango.

        Complejidad: MC: O(1) y PC: O(n)
        """

        if indice < 0 or self._tamano <= indice:
            raise IndexError('Indice fuera de rango!')
        actual: _Nodo = self._extremo
        anterior: _Nodo = None
        for i in range(indice):
            anterior = actual
            actual = actual.siguiente
        anterior.siguiente = actual.siguiente
        self._tamano -= 1

    def tamano(self) -> int:
        """Retorn el tamano de la estructura."""
        return self._tamano


def generar_alumno() -> dict['campo': Any]:
    """Genera un regestro para un alumno.

    Retorna un diccionario con los siguientes campos:
    - nombre
    - grupo
    - nota
    """
    nombres: list[str] = ['Pedro', 'Juan', 'Esteban', 'Maria', 'Ana', 'Simon']
    grupos: list[str] = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'c1', 'C2', 'C3']
    return {
        "nombre" : random.choice(nombres),
        "grupo" : random.choice(grupos),
        "nota" : round(random.uniform(0, 100), 1)
    }


alumnos = [generar_alumno() for i in range(50)]

def llenar_array_estatico(elementos: list[Any]) -> ArrayEstatico:
    """Retorna un 'ArrayEstatico' con el contenidos de 'elementos'."""
    n = len(elementos)
    array = ArrayEstatico(n)
    for indice in range(n):
        array.agregar(elementos[indice])
    return array


def llenar_array_dinamico(elementos: list[Any]) -> ArrayDinamico:
    """Retorna un 'ArrayDinamico' con el contenido de 'elementos'."""
    n = len(elementos)
    array = ArrayDinamico()
    for indice in range(n):
        array.insertar_fin(elementos[indice])
    return array


print()
print('Comparacion de Estatico vs Dinamico')
print('-----------------------------------')
print('En tiempo:')
tiempo_estatico = timeit.timeit(stmt='llenar_array_estatico(alumnos)', setup='from __main__ import llenar_array_estatico, alumnos', number=10) / 10
tiempo_dinamico = timeit.timeit(stmt='llenar_array_dinamico(alumnos)', setup='from __main__ import llenar_array_dinamico, alumnos', number=10) / 10
print(f'Tiempo medio de insertar 50 datos en ArrayEstatico: {tiempo_estatico} segundos.')
print(f'Tiempo medio de insertar 50 datos en ArrayDinamico: {tiempo_dinamico} segundos.')
diferencia = abs(tiempo_dinamico - tiempo_estatico)
print(f'Diferencia entre ambos es: {diferencia} segundos.')
print()

array1 = llenar_array_estatico(alumnos)
array1_size, array1_peak = tracemalloc.get_traced_memory()
array2 = llenar_array_dinamico(alumnos)
array2_size, array2_peak = tracemalloc.get_traced_memory()


def buscar_array_estatico(array: ArrayEstatico, dato: Any) -> Any:
    """Busca un elemento en el array estatico y devuelve su posicion.
    Retorna '-1' si no lo encuentra.
    """
    tamano = array.tamano()
    posicion = -1
    for i in range(tamano):
        if array.obtener(i) == dato:
            posicion = i
    return posicion


def buscar_array_dinamico(array: ArrayDinamico, dato: Any) -> Any:
    """Busca un elemento en el array dinamico y devuelve su posicion.
    Si no lo encuentra, retorna '-1'
    """
    tamano = array.tamano()
    posicion = -1
    for i in range(tamano):
        if array.obtener(i) == dato:
            posicion = i
    return posicion

print()
print('Busqueda de elementos:')
print('----------------------')
print('ArrayEstatico:')
alumno = {"nombre":'Juan', "grupo":'A1', "nota":71}
array1.modificar(0, alumno)
pos_estatico = buscar_array_estatico(array1, alumno)
if pos_estatico == -1:
    print(f'No se hayo {alumno}')
else:
    print(f'El alumno {alumno} fue allado en {pos_estatico}.')

print('ArrayDinamico:')
array2.modificar(0, alumno)
pos = buscar_array_dinamico(array1, alumno)
if pos == -1:
    print(f'No se hayo {alumno}')
else:
    print(f'El alumno {alumno} fue allado en {pos}.')

print()
tracemalloc.start()
array1 = llenar_array_estatico(alumnos)
array1_size, array1_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
array2 = llenar_array_dinamico(alumnos)
array2_size, array2_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print('Uso de aproximado de memoria:')
print('----------------------------')
print(f'ArrayEstatico: {array1_size} Bs')
print(f'ArrayDinamico: {array2_size} Bs')
