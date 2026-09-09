"""2) ADT Conjunto
Implementa un `ConjuntoADT` con:
- union, 
- interseccion,
- diferencia,
- diferencia_simetrica,
- es_subconjunto.
Incluye al menos dos casos de pruebas con datos numericos y uuna con cadians."""

class ConjuntoADT:
    """Contiene elementos unicos y desordenados.
  
    Metodos:
    - agregar()
    - eliminar()
    - union()
    - interseccion()
    - diferencia()
    - diferecia_simetrica()
    - es_subconjunto()
    """

    def __init__(self) -> None:
        self._elementos: list[any] = []

    def agregar(self, elemento: any) -> None:
        """Agrega un elemento al conjunto si es que es unico.

        Un elementoo es unico cuando no hay otro igual en el conjunto.
        
        Parametros:
        - elemento: El elemento a agregar.
        """

        if elemento not in self._elementos:
            self._elementos.append(elemento)

    def eliminar(self, elemento: any) -> None:
        """Elimina un elemento del conjunto. No hace nada si el elemento
        no esta en el conjunto.
        
        Parametros:
        - elemento: elemento a eliminar.
        """

        try:
            indice = self._elementos.index(elemento)
            del self._elementos[indice]
        except ValueError:
            pass


    def union(self, conjunto: 'ConjuntoADT') -> 'ConjuntoADT':
        """Une dos conjuntos y retorna el resultado de la union.
        
        Parametros:
        - conjunto: conjunto a unir con 'self'.
        """

        return self._elementos + conjunto.diferecia(self)._elementos

    def interseccion(self, conjunto: 'ConjuntoADT') -> 'ConjuntoADT':
        """Retorna la interseccion entre 'self' y 'conjunto'.
        
        Parametros: 
        - conjunto: el conjunto con el cual hace la interseccion.
        """

        result: 'ConjuntoADT' = ConjuntoADT()
        for elemento in self._elementos:
            if elemento in conjunto._elementos:
                result.agregar(elemento)

        return result

    def diferecia(self, conjunto: 'ConjuntoADT') -> 'ConjuntoADT':
        """Realiza la Diferecia Relativa entre 'self' y 'conjunto'(self - conjunto).
        
        Parametros:
        - conjunto: El conjunto con el cual hacer la diferecia relativa.
        """

        result: 'ConjuntoADT' = ConjuntoADT()
        for elemento in self._elementos:
            if elemento not in conjunto._elementos:
                result.agregar(elemento)

        return result

    def diferencia_simetrica(self, conjunto: 'ConjuntoADT') -> 'ConjuntoADT':
        """Realiza la diferencia simetrica entre 'self' y 'conjunto'.
        
        Parametros:
        - conjunto: Conjunto con el cual hacer la diferencia simetrica.
        """

        conjunto_izq: 'ConjuntoADT' = self.diferecia(conjunto)
        conjunto_der: 'ConjuntoADT' = conjunto.diferecia(self)
        return conjunto_izq.union(conjunto_der)

    def es_subconjunto(self, conjunto: 'ConjuntoADT') -> bool:
        """Verificar si 'self' es subconjunto de 'conjunto'.
        
        Parametros:
        - conjunto: conjunto a comparar con self.
        """

        indice: int = 0
        n: int = len(self._elementos)
        hallado: bool = True
        while indice < n and hallado:
            if self._elementos[indice] not in conjunto._elementos:
                hallado = False
            indice += 1

        return hallado

    def __str__(self) -> str:
        return '{' + ','.join(map(str, self._elementos)) + '}'


print('Unidad2: enunciado 2')
print('--------------------')
print()

print('Sea conjunto A:')
A = ConjuntoADT()
A.agregar(0)
A.agregar(2)
A.agregar(4)
A.agregar(6)
A.agregar(8)
A.agregar(10)
A.agregar(12)
print(A)
print()

print('Sea el conjunto B')
B = ConjuntoADT()
B.agregar(1)
B.agregar(3)
B.agregar(7)
B.agregar(9)
B.agregar(10)
B.agregar(12)
B.agregar(13)
print(B)
print()

print('A union B:')
print(A.union(B))
print()

print('A interseccion B:')
print(A.interseccion(B))
print()

print('A diferencia relativa B:')
print(A.diferecia(B))
print()

print('B diferencia relativa A:')
print(B.diferecia(A))
print()

print('A diferencia simetrica B:')
print(A.diferencia_simetrica(B))
print()

# Problemita: uncion retorna una tupla!
print("Problemita: uncion retorna una tupla!")
