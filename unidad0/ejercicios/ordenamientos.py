"""Este modulo esta compuesto de diversos ordenamientos de listas de numeros.

Metodos y Funciones:
- bubble_sort
- selection_sort
- quick_sort
- merge_sort
"""

from numbers import Number as number

def _intercambiar(lista: list[number], pos1: int, pos2: int) -> None:
    """Intercambia los elementos de la lista de numeros que estan en las 
       posiciones pos1 y pos2.

    Parametros:
    - lista: La lista en al que se realizara el intercambio.
    - pos1: La posicion de uno de los elementos a intercambiar.
    - pos2: La posicion de el otro elemento a intercambiar.

    *Nota: Se asume que pos1 y pos2 son posiciones diferentes.
    """

    aux: number = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = aux


def bubble_sort(lista: list[number]) -> None:
    """Ordena una lista de numeros ascendentemente por Bubble Sort.

    Parametros:
    - lista: Es la list de numeros a ordenar.

    Efectos secundarios:
    - Modifica las posiciones de los elementos si es que la lista no 
      esta ordenada.

    Complejidad: O(n^2)
    """

    n = len(lista)
    limite: int = n - 1
    while limite > 2:                                   
        mayor: int = 0                                  
        while mayor < limite:                           
            if lista[mayor] > lista[mayor + 1]:         
                _intercambiar(lista, mayor, mayor + 1)  
            mayor = mayor + 1                           
        limite = limite - 1                             


def selection_sort(lista: list[number]) -> None:
    """Ordena una lista de numeros ascendentemente por Selection Sort.

    Parametros:
    - lista: Es la list de numeros a ordenar.

    Efectos secundarios:
    - Modifica las posiciones de los elementos si es que la lista no 
      esta ordenada.

    Complejidad: O(n^2)
    """

    limite = len(lista)
    while limite > 1:
        index = 1
        pos_mayor = 0
        while index < limite:
            if lista[index] > lista[pos_mayor]:
                pos_mayor = index
            index = index + 1
        _intercambiar(lista, pos_mayor, limite - 1)
        limite = limite - 1


def _pivotear(lista: list[number], inicio: int, fin: int) -> int:
    """(Funcion Privado) Calcula el pivote.

    Parametros:
    - Lista: Lista de numeros a pivotear.
    - inicio: Comienzo del rango.
    - fin: Final del rango.

    Retorna: Un numero que representa al pivote.

    Efectos Secundarios: 
    - Modifica la lista para obtener el pivote.
    
    Complejidad: O(n)
    """

    a = inicio
    b = fin
    sw: bool = True
    while a < b:
        if lista[a] > lista[b]:
            _intercambiar(lista, a, b)
            sw = not sw
        if sw:
            a = a + 1
        else:
            b = b - 1
    return a


def _quick_sort(lista: list[number], inicio: int, fin: int) -> None:
    """(Metodo Privado) Ordena el rango de elementos especificado de una 
       lista de numeros por Quick Sort.

    Parametros:
    - lista: La lista de numeros a ordenar.
    - inicio: El inicio del rango.
    - fin: final del rango.
    
    Efectos secundarios:
    - Modifica las posiciones de los elementos si es que la lista no 
      esta ordenada.

    Complejidad:
    - Mejor Caso: O(nlog(n))
    - Peor Caso: O(n^2)

    *Nota: El rango es inclusivo.
    **Nota: La lista sera modificada.
    """

    n = fin - inicio + 1
    if n > 1:
        pivote: int = _pivotear(lista, inicio, fin)
        _quick_sort(lista, inicio, pivote - 1)
        _quick_sort(lista, pivote + 1, fin)


def quick_sort(lista: list[number]) -> None:
    """Ordena una lista de numeros ascendentemente por Quick Sort.

    Parametros:
    - lista: Es la list de numeros a ordenar.

    Efectos secundarios:
    - Modifica las posiciones de los elementos si es que la lista no 
      esta ordenada.

    Complejidad: 
    - Mejor Caso: O(nlog_{2}(n))
    - Peor Caso: O(n^2)
    """

    _quick_sort(lista, 0, len(lista) - 1)

def _merge(lista: list[number], inicio: int, medio: int, fin: int) ->None:
    """(Metodo Privada) 

    Parametros:
    - lista: La lista en la se realiza el merge.
    - inicio: Comienzo del rango de elementos.
    - medio: Mitad del rango de elementos.
    - fin: Final del rango de elementos.

    Complejidad: O(n)
    """

    i: int = inicio         # indice uno(ahora inicio)
    j: int = medio + 1      # indice dos (medio + 1)
    lista_aux: lista[number] = []
    while (i <= medio) and (j <= fin):
        if lista[i] <= lista[j]:
            lista_aux.append(lista[i])
            i = i + 1
        else:
            lista_aux.append(lista[j])
            j = j + 1

    while i <= medio:
        lista_aux.append(lista[i])
        i = i + 1

    while j <= fin:
        lista_aux.append(lista[j])
        j = j + 1

    i = inicio
    for ele in lista_aux:
        lista[i] = ele
        i = i + 1


def _merge_sort(lista: list[number], inicio: int, fin: int) -> None:
    """(Metodo Privado) Ordena una lista de numeros por Merge Sort en
       un rango [inicio; fin] inclusivo.

    Parametros:
    - lista: La lista de numeros a ordenar.
    - inicio: Comienzo del rango de elementos a ordenar.
    - fin : Final del rango de elementos a ordenar.

    Efectos Secundarios:
    - Modifica la lista para ordenarla si es que no esta ordenada.

    Complejidad: O(nlog_{2}(n))
    """

    n: int = fin - inicio + 1
    if n > 1:
        medio: int = (inicio + fin) // 2
        _merge_sort(lista, inicio, medio)
        _merge_sort(lista, medio + 1, fin)
        _merge(lista, inicio, medio, fin)


def merge_sort(lista: list[number]) -> None:
    """Ordena una lista de numeros por Merge Sort.

    Parametros:
    - lista: La lista de numeros a ordenar.

    Efectos Secundarios:
    - Modifica la lista si es que no esta ordenada.

    Complejidad: O(nlog_{2}(n))
    """

    _merge_sort(lista, 0, len(lista) - 1)

