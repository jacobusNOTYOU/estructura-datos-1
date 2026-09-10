"""1) Lista enlazada simple
Implementa `ListaSimple con:
- insertar al inicio y al final,
- buscar,
- eliminar por valor,
- recorrido/impresion.
Incluye control de lista vacia.
"""


class EmptyError(Exception):
    """Error para objetos vacios."""
    def __init__(self, args = None):
        self.args = args
        super().__init__(self.args)

    def __str__(self) -> str:
        excep = ''
        for i in self.args:
            for j in i:
                excep += str(j)
        return excep


class _Nodo:
    """Nodo de ListaSimple."""
    def __init__(self, dato: any) -> None:
        self.dato: any = dato
        self.siguiente: '_Nodo'|None = None


class ListaSimple:
    """Implementacion de la Lista Simple.

    Metodos:
    - insertar_inicio(dato)
    - insertar_final(dato)
    - insertar_en(indice, dato)
    - eliminar_inicio()
    - eliminar(dato)
    - buscar(dato)

    Metodos recursivos:
    - insertar_final_rec(dato)
    - insertar_en_rec(indice, dato)
    - eliminar_rec(dato)
    - buscar_rec(dato)
    - str_rec()
    """

    def __init__(self) -> None:
        self.cabeza: _Nodo|None = None
        self.tamanio: int = 0

    def insertar_inicio(self, dato: any) -> None:
        """Inserta un dato al inicio de la Lista.
        
        Parametros:
        - dato: el dato a insertar.
        """

        nuevo: _Nodo = _Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamanio += 1

    def insertar_final(self, dato: any) -> None:
        """Inserta un dato al final de la Lista.
        
        Parametros:
        - dato: el dato a insertar.
        """

        nuevo: _Nodo = _Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual: _Nodo = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        self.tamanio += 1

    def insertar_en(self, indice: int, dato: any) -> None:
        """Inserta un dato en la posicion del indice.
        
        Parametros:
        - indice: la posicion en la que se insertara el dato.
        - dato: el dato a insertar.

        Excepciones:
        - IndexError: si el indice esta fuera de rango.
        """

        if indice < 0 or self.tamanio <= indice:
            raise IndexError(f'Error: Indice {indice} fuera de rango!')

        nuevo: _Nodo = _Nodo(dato)
        actual: _Nodo = self.cabeza
        anterior: _Nodo|None = None
        for i in range(indice):
            anterior = actual
            actual = actual.siguiente

        anterior.siguiente = nuevo
        nuevo.siguiente = actual

        self.tamanio += 1

    def eliminar_inicio(self) -> None:
        """Elimina el primer dato de la lista."""
        if self.cabeza is not None:
            self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
        else:
            raise EmptyError('La ListaSimple esta vacia!')
    
    def eliminar(self, dato) -> None:
        """Elimina dato de la Lista si existe.
        
        Parametros:
        - dato: dato a eliminar.
        """
        if self.cabeza is not None:
            actual: _Nodo = self.cabeza
            anterior: _Nodo|None = None
            while actual is not None and actual.dato != dato:
                anterior = actual
                actual = actual.siguiente
            
            if actual is not None:
                anterior.siguiente = actual.siguiente
                self.tamanio -= 1
            else:
                raise EmptyError(f'El elemento "{dato}" no esta en la '
                                  'ListaSimple!'
                )


    def buscar(self, dato: any) -> bool:
        """Busca el dato en la Lista y retorna True si lo encuentra, sino False
        
        Parametros:
        - dato: dato a buscar.
        """

        if self.cabeza is None:
            return False
        
        actual: _Nodo = self.cabeza
        while actual is not None and actual.dato != dato:
            actual = actual.siguiente
        
        if actual is not None:
            return True

        return False

    # Recursivos
    def insertar_final_rec(self, dato: any) -> None:
        """Inserta un dato al final de la Lista. Recursivo.
        
        Parametros:
        - dato: el dato a insertar.
        """

        if self.cabeza is None:
            nuevo: _Nodo = _Nodo(dato)
            self.cabeza = nuevo
        else:
            actual: _Nodo = self._rec_indice(self.tamanio - 1, nodo=self.cabeza)

            nuevo: _Nodo = _Nodo(dato)
            actual.siguiente = nuevo

        self.tamanio += 1

    def insertar_en_rec(self, indice: int, dato: any) -> None:
        """Inserta un dato en la posicion del indice. Recursivo.
        
        Parametros:
        - indice: la posicion en la que se insertara el dato.
        - dato: el dato a insertar.

        Excepciones:
        - IndexError: si el indice esta fuera de rango.
        """

        if indice < 0 or self.tamanio <= indice:
            raise IndexError(f'Error: Indice {indice} fuera de rango!')

        nuevo: _Nodo = _Nodo(dato)
        if indice > 0:
            actual: _Nodo = self._rec_indice(indice - 1, nodo=self.cabeza)
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

        self.tamanio += 1

    def eliminar_rec(self, dato) -> None:
        """Elimina dato de la Lista si existe. Recursivo.
        
        Parametros:
        - dato: dato a eliminar.
        """
        if self.cabeza is not None:
            anterior, el_nodo = self._buscar_rec_y_anterior(dato, 
                                                            nodo=self.cabeza
                                )
            if el_nodo is not None:
                anterior.siguiente = el_nodo.siguiente
                self.tamanio -= 1
            else:
                raise EmptyError(f'El elemento "{dato}" no esta en la '
                                  'ListaSimple!'
                )

    def buscar_rec(self, dato: any) -> bool:
        """Busca el dato en la Lista y retorna True si lo encuentra, sino False
        .Recursivo.
        
        Parametros:
        - dato: dato a buscar.
        """

        if self.cabeza is None:
            return False
        
        el_nodo: _Nodo = self._buscar_rec(dato, nodo=self.cabeza)
        
        if el_nodo is not None:
            return True

        return False

    def str_rec(self) -> str:
        """Retorna la version en cadena de la Lista."""
        return self._str_rec(self.cabeza)

    # Privados
    def _str_rec(self, nodo: _Nodo|None) -> str:
        """Retorna la version en cadena de la Lista."""
        if nodo is None:
            return 'None'
        else:
            un_nodo: str = '[' + str(nodo.dato) + '] -> '
            return un_nodo + self._str_rec(nodo.siguiente)


    def _rec_indice(self, indice: int, 
                    contador: int = 0, 
                    nodo: _Nodo|None = None
    ) -> _Nodo:
        if indice < 0 or self.tamanio <= indice:
            raise IndexError(f'Error: Indice {indice} fuera de rango!')
        
        if indice == contador:
            return nodo
        else:
            nodo = self._rec_indice(indice, contador + 1, nodo.siguiente)
            return nodo

    def _buscar_rec_y_anterior(self, dato: any, nodo: _Nodo|None = None,
                                anterior: _Nodo|None = None
    ) -> tuple(_Nodo, _Nodo):
        if nodo is None:
            return None, None
        if nodo.dato == dato:
            return anterior, nodo
        else:
            return self._buscar_rec_y_anterior(dato, nodo.siguiente, nodo)

    def _buscar_rec(self, dato: any, nodo: _Nodo|None) -> _Nodo:
        return (self._buscar_rec_y_anterior(dato, nodo))[1]

    def __str__(self) -> str:
        if self.cabeza is None:
            return 'None'

        resultado: str = ''
        actual: _Nodo = self.cabeza
        while actual is not None:
            resultado += '[' + str(actual.dato) + '] -> '
            actual = actual.siguiente
        resultado += 'None'
        return resultado

    def __len__(self) -> int:
        return self.tamanio

if __name__ == '__main__':
    print("DEMO")
    print()
    lista_simple = ListaSimple()
    print('Se inicializa la Lista Simple.')
    print(f'Longitud: {len(lista_simple)}')
    print()

    lista_simple.insertar_final(1)
    lista_simple.insertar_final(2)
    lista_simple.insertar_final(4)
    lista_simple.insertar_final(5)
    print('La lista se le agrega [1, 2, 4, 5] a la Lista.')
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()

    print('Se inserta al inicio "0".')
    lista_simple.insertar_inicio(0)
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()

    print('se inserta en la posicion 3 el "3".')
    lista_simple.insertar_en(3, 3)
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()

    print('Se inserta al final el numero "6"')
    lista_simple.insertar_final(6)
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()

    print('Se elimina el elemento del inicio')
    lista_simple.eliminar_inicio()
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()

    print('Se elimina el elemento "3')
    lista_simple.eliminar(3)
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()

    print('Se busca el "2"')
    print(lista_simple.buscar(2))
    print('Se busca el "3"')
    print(lista_simple.buscar(3))

    print()
    print('Recursive Edition!')
    print('-------------------')
    print()
    print('Insertal al final el "7".')
    lista_simple.insertar_final_rec(7)
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()
    print('Inserta en 2 el "3"')
    lista_simple.insertar_en_rec(2, 3)
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()
    print('Eliminar el "3".')
    lista_simple.eliminar_rec(3)
    print(lista_simple)
    print(f'Longitud: {len(lista_simple)}')
    print()
    print('Buscar el "4".')
    print(lista_simple.buscar_rec(4))
    print('Buscar el "3".')
    print(lista_simple.buscar_rec(3))
    print()
    print('__str__ recursivo!')
    print(lista_simple.str_rec())
    print()
