"""Provee de la clase 'ListOrd', la cual, representa una lista que 
   siempre esta ordenada.
"""
from typing import Any

class ListaOrd():
    """ Una lista que siempre esta ordenada.

    Metodos y Funciones:
    1. insertar
    2. extraer
    3. eliminar
    4. esta
    5. esta_vacio
    6. obtener
    7. cantidad

    *Nota: Solo sirve para almacenar int, float o str.
    **Nota: La lista es 'Homogenea', es decir, todos los elementos de la
            lista deben ser del mismo tipo.
    """

    def __init__(self) -> None:
        self._lista: list[Any] = []
      
    def insertar(self, valor: Any) -> None:
        """ Inserta un valor en su lugar en la lista.

        *Nota: El valor a insertar debe ser igual al resto de elementos en la 
        lista.

        Parametros:
        - valor: el valor a insertar.

        Excepciones:
        - TypeError: Cuando valor no es de tipo int, float o str. O cuando
        valor no es del mismo tipo que el resto de elementos de la lista.
        """

        if not (isinstance(valor, type(0)) 
            or isinstance(valor, type(0.0)) 
            or isinstance(valor, type('a'))):
                raise TypeError('La lista solo puede contener int, float o str!')

        if self.esta_vacio():
                self._lista = [valor]
        elif not isinstance(valor, type(self._lista[0])):
            raise TypeError('Los elementos de la lista deben ser del mismo tipo!')
        else:
            pos: int = 0
            hallado: bool = False
            while pos < self.cantidad() and not hallado:
                if self._comparar(valor, self._lista[pos]):
                    hallado = True
                else:
                    pos += 1
            izquierda: list[Any] = self._lista[:pos]
            derecha: list[Any] = self._lista[pos:]
            self._lista = izquierda + [valor] + derecha

    def extraer(self, pos: int) -> Any:
        """ Retorna el elemento en la posicion 'pos' y elimina dicho elemento.

        Parametros:
        - pos: posicion del elemento a extraer.

        Excepciones:
        - IndexError: Si 'pos' esta fuera de rango.
        """
        if pos >= self.cantidad():
            raise IndexError('Fuera de rango')
        result: Any = self._lista[pos]
        self.eliminar(pos)
        return result
    
    def eliminar(self, pos: int) -> None:
        """ Elimina el elemento en la posicion 'pos'.

        Parametros:
        - pos: posicion del elemento a eliminar.
        
        Excepciones:
        - IndexError: Si 'pos' esta fuera de rango.
        """
        if pos >= self.cantidad():
            raise IndexError('Fuera de rango')
        del self._lista[pos]

    def esta(self, valor: Any) -> bool:
        """ Verifica si valor esta en la lista.
        
        Parametros:
        - valor: El valor a buscar.
        """
        if self.esta_vacio():
            return False
        hallado: bool = False
        indice: int = 0
        while indice < self.cantidad() and not hallado:
            if valor == self._lista[indice]:
                hallado = True
            indice += 1
        return hallado

    def esta_vacio(self) -> bool:
        """ Verifica si la lista esta vacia."""
        return len(self._lista) <= 0

    def obtener(self, pos: int) -> Any:
        """ Retorna el elemento en la posicion 'pos' sin eliminarlo.

        Parametros:
        - pos: posicion del elemento a obtener.

        Excepciones:
        - IndexError: Si 'pos' esta fuera de rango.
        """
        if pos >= self.cantidad():
            raise IndexError('Fuera de rango')
        return self._lista[pos]

    def cantidad(self) -> int:
        """ Retorna la cantidad de elementos en la lista."""
        return len(self._lista)


    def _comparar(self, primero: Any, segundo: Any) -> bool:
        """ Realiza la comparacion 'primero <= segundo'.

        Parametros:
        - primero: El primer elemento en la comparacion, puede ser de 
        tipo int, float o str.
        - segundo: El segundo elemento en la comparacion, puede ser de 
        tipo int, float o str.

        Retorna el valor de la comparacion 'primero <= segundo'.

        Excepcion:
        - TypeError: Cuando primero no es de tipo int, float o str.

        *Nota: Se asume que ambos parametros son del mismo tipo.
        """

        match type(primero):
            case x if isinstance(0, x):
                return primero <= segundo
            case x if isinstance(0.0, x):
                return primero <= segundo
            case x if isinstance('a', x):
                return self._comparar_str(primero, segundo)
            case _:
                raise TypeError('Solo se puede comparar int, float o str!')

    def _comparar_str(self, primero: str, segundo: str) -> bool:
        """ Realiza la comparacion 'primero <= segundo' para str.

        Parametros:
        - primero: El primer elemento en la comparacion, solo puede ser de 
        tipo str.
        - segundo: El segundo elemento en la comparacion, solo puede ser de 
        tipo str.

        Retorna el valor de la comparacion 'primero <= segundo'.

        *Nota: Se asume que ambos parametros son del mismo tipo.
        """

        abc: str = '0123456789AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnÑñOoÓóPpQqRrSsTtUuÚúÜüVvXxYyZz'
        menor_que: bool = True
        iterar: bool = True
        indice: int = 0
        while (indice < len(primero)) and (indice < len(segundo)) and iterar:
            if abc.find(primero[indice]) != abc.find(segundo[indice]):
                iterar = False
            if abc.find(primero[indice]) > abc.find(segundo[indice]):
                menor_que = False
            indice += 1
        return menor_que


# DEMOS
l = ListaOrd()
# Demo con numeros
print('Demo con numeros.')
l.insertar(0)
l.insertar(1)
l.insertar(2)
l.insertar(3)

print(f'Esta vacio?: {l.esta_vacio()}')
print(f'Cantidad de elementos: {l.cantidad()}')
for i in range(0, l.cantidad()):
    print(f'[{i}] {l.obtener(i)}')
print(f'Extraer el elemento #2: {l.extraer(2)}')

print(f'Cantidad de elementos: {l.cantidad()}')
for i in range(0, l.cantidad()):
    print(f'[{i}] {l.obtener(i)}')

print('Eliminar el elemento #1')
l.eliminar(1)
print(f'Cantidad de elementos: {l.cantidad()}')
for i in range(0, l.cantidad()):
    print(f'[{i}] {l.obtener(i)}')

l.eliminar(0)
l.eliminar(0)

# Demo con str
print('Demo con str.')
l.insertar('Juan')
l.insertar('Ñuflo de Chavez')
l.insertar('Carlos')
l.insertar('Adolfo')

print(f'Esta vacio?: {l.esta_vacio()}')
print(f'Cantidad de elementos: {l.cantidad()}')
for i in range(0, l.cantidad()):
    print(f'[{i}] {l.obtener(i)}')
print(f'Extraer el elemento #2: {l.extraer(2)}')

print(f'Cantidad de elementos: {l.cantidad()}')
for i in range(0, l.cantidad()):
    print(f'[{i}] {l.obtener(i)}')

print('Eliminar el elemento #1')
l.eliminar(1)
print(f'Cantidad de elementos: {l.cantidad()}')
for i in range(0, l.cantidad()):
    print(f'[{i}] {l.obtener(i)}')
