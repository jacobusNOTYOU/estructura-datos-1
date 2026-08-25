from typing import Any

# Conjunto Dinamico
class ConjuntoDinamico():
    """Contiene elementos unicos y desordenados.
  
    Metodos:
    - agregar()
    - eliminar()
    - esta()
    - es_subconjunto()
    - union()
    - interseccion()
    - diferencia_relativa()
    - diferecia_simetrica()
    """

    def __init__(self) -> None:
        self._elementos: list[Any] = []

    def agregar(self, elemento: Any) -> None:
        """Agrega un elemento al conjunto si es que es unico.

        Un elementoo es unico cuando no hay otro igual en el conjunto.
        
        Parametros:
        - elemento: El elemento a agregar.
        """

        if elemento not in self._elementos:
            self._elementos.append(elemento)

    def eliminar(self, elemento: Any) -> None:
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

    def esta(self, elemento: Any) -> bool:
        """Retorna 'True' si 'elemento' esta en el conjunto.
        
        Parametros:
        - elemento: elemento a verificar si pertence al conjunto.
        """

        result: bool
        try:
            self._elementos.index(elemento)
            result = True
        except ValueError:
            result = False

        return result

    def es_subconjunto(self, conjunto: ConjuntoDinamico) -> bool:
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

    def union(self, conjunto: ConjuntoDinamico) -> ConjuntoDinamico:
        """Une dos conjuntos y retorna el resultado de la union.
        
        Parametros:
        - conjunto: conjunto a unir con 'self'.
        """

        return self._elementos + conjunto.diferecia_relativa(self)._elementos

    def interseccion(self, conjunto: ConjuntoDinamico) -> ConjuntoDinamico:
        """Retorna la interseccion entre 'self' y 'conjunto'.
        
        Parametros: 
        - conjunto: el conjunto con el cual hace la interseccion.
        """

        result: ConjuntoDinamico = ConjuntoDinamico()
        for elemento in self._elementos:
            if elemento in conjunto._elementos:
                result.agregar(elemento)

        return result

    def diferecia_relativa(self, conjunto: ConjuntoDinamico) -> ConjuntoDinamico:
        """Realiza la Diferecia Relativa entre 'self' y 'conjunto'(self - conjunto).
        
        Parametros:
        - conjunto: El conjunto con el cual hacer la diferecia relativa.
        """

        result: ConjuntoDinamico = ConjuntoDinamico()
        for elemento in self._elementos:
            if elemento not in conjunto._elementos:
                result.agregar(elemento)

        return result

    def diferencia_simetrica(self, conjunto: ConjuntoDinamico) -> ConjuntoDinamico:
        """Realiza la diferencia simetrica entre 'self' y 'conjunto'.
        
        Parametros:
        - conjunto: Conjunto con el cual hacer la diferencia simetrica.
        """

        conjunto_izq: ConjuntoDinamico = self.diferecia_relativa(conjunto)
        conjunto_der: ConjuntoDinamico = conjunto.diferecia_relativa(self)
        return conjunto_izq.union(conjunto_der)

    def __str__(self) -> str:
        return '{' + ','.join(map(str, self._elementos)) + '}'

    def __len__(self) -> int:
        return len(self._elementos)


print('DEMO: ConjuntoDinamico:')
print('-----------------------')
conjunto = ConjuntoDinamico()
for i in range(10):
  conjunto.agregar(i*2 + 1)
conjunto.agregar(2)
conjunto.agregar(8)

conjunto1 = ConjuntoDinamico()
for i in range(10):
  conjunto1.agregar(i * 2)
conjunto1.agregar(7)
conjunto1.agregar(5)

print(f'Conjunto A: {conjunto}')
print(f'Conjunto B: {conjunto1}')

print()
print('Pertenencia')
print('1 esta en el conjunto A?')
if conjunto.esta(1):
  print('Si')
else:
  print('No')
print('0 esta en el conjunto A?')
if conjunto.esta(0):
  print('Si')
else:
  print('No')

print()
print('Union')
print(f'AUB: {conjunto.union(conjunto1)}')

print()
print('Interseccion')
print(f'A∩B: {conjunto.interseccion(conjunto1)}')

print()
print('Diferencia Relativa')
print(f'A-B: {conjunto.diferecia_relativa(conjunto1)}')
print(f'B-A: {conjunto1.diferecia_relativa(conjunto)}')

print()
print('Diferencia Simetrica')
print(f'AΔB: {conjunto.diferencia_simetrica(conjunto1)}')


# Conjunto Estatico
class ConjuntoEstatico:
    """Contiene elementos unicos y desordenados. Tiene un limite de elementos
    especificados en el momento de creacion.
    
    *Nota: '__len__()' retorna la cantidad de elementos guardados en el 
    conjunto no el maximo de elementos que cabe en un cojunto.

    Metodos:
    - agregar()
    - eliminar()
    - esta_lleno()
    - maximo()
    - esta()
    - es_subconjunto()
    - union()
    - interseccion()
    - diferencia_relativa()
    - diferecia_simetrica()
    """

    def __init__(self, max_elementos: int) -> None:
        self._elementos: list[Any] = []
        self._maximo = max_elementos

    def agregar(self, elemento: Any) -> None:
        """Agrega un elemento al conjunto si es que es unico.

        Un elementoo es unico cuando no hay otro igual en el conjunto.
        
        Parametros:
        - elemento: El elemento a agregar.

        Excepciones:
        - IndexError: si el conjunto ya esta lleno.
        """

        if self.esta_lleno():
            raise IndexError('El conjunto ya esta lleno.')

        if elemento not in self._elementos:
            self._elementos.append(elemento)

    def eliminar(self, elemento: Any) -> None:
        """Elimina un elemento del conjunto. No hace nada si el elemento
        no esta en el conjunto.
        
        Parametros:
        - elemento: elemento a eliminar.
        Excepciones:
        - IndexError: si el conjunto ya esta lleno.
        """

        if self.esta_lleno():
            raise IndexError('El conjunto ya esta lleno.')

        try:
            indice = self._elementos.index(elemento)
            del self._elementos[indice]
        except ValueError:
            pass

    def esta_lleno(self) -> bool:
        """Verifica si el numero de elementos del cojunto a llegado a su 
        maximo"""

        return len(self._elementos) == self._maximo

    def maximo(self) -> int:
        """Retorna el maximo de elementos que cabe en el conjunto."""
        return self._maximo

    def esta(self, elemento: Any) -> bool:
        """Retorna 'True' si 'elemento' esta en el conjunto.
        
        Parametros:
        - elemento: elemento a verificar si pertence al conjunto.
        """

        result: bool
        try:
            self._elementos.index(elemento)
            result = True
        except ValueError:
            result = False

        return result

    def es_subconjunto(self, conjunto: ConjuntoDinamico) -> bool:
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

    def union(self, conjunto: ConjuntoDinamico) -> ConjuntoDinamico:
        """Une dos conjuntos y retorna el resultado de la union.
        
        Parametros:
        - conjunto: conjunto a unir con 'self'.
        """

        return self._elementos + conjunto.diferecia_relativa(self)._elementos

    def interseccion(self, conjunto: ConjuntoDinamico) -> ConjuntoDinamico:
        """Retorna la interseccion entre 'self' y 'conjunto'.
        
        Parametros: 
        - conjunto: el conjunto con el cual hace la interseccion.
        """

        result: ConjuntoDinamico = ConjuntoDinamico()
        for elemento in self._elementos:
            if elemento in conjunto._elementos:
                result.agregar(elemento)

        return result

    def diferecia_relativa(self, conjunto: ConjuntoDinamico) -> ConjuntoDinamico:
        """Realiza la Diferecia Relativa entre 'self' y 'conjunto'(self - conjunto).
        
        Parametros:
        - conjunto: El conjunto con el cual hacer la diferecia relativa.
        """

        result: ConjuntoDinamico = ConjuntoDinamico()
        for elemento in self._elementos:
            if elemento not in conjunto._elementos:
                result.agregar(elemento)

        return result

    def diferencia_simetrica(self, conjunto: ConjuntoDinamico) -> ConjuntoDinamico:
        """Realiza la diferencia simetrica entre 'self' y 'conjunto'.
        
        Parametros:
        - conjunto: Conjunto con el cual hacer la diferencia simetrica.
        """

        conjunto_izq: ConjuntoDinamico = self.diferecia_relativa(conjunto)
        conjunto_der: ConjuntoDinamico = conjunto.diferecia_relativa(self)
        return conjunto_izq.union(conjunto_der)

    def __str__(self) -> str:
        return '{' + ','.join(map(str, self._elementos)) + '}'

    def __len__(self) -> int:
        return len(self._elementos)


print()
print('DEMO: ConjuntoEstatico:')
print('-----------------------')
conjunto = ConjuntoEstatico(12)
for i in range(10):
  conjunto.agregar(i*2 + 1)
conjunto.agregar(2)
conjunto.agregar(8)

conjunto1 = ConjuntoEstatico(13)
for i in range(10):
  conjunto1.agregar(i * 2)
conjunto1.agregar(7)
conjunto1.agregar(5)

print(f'Conjunto A: {conjunto}')
print(f'Conjunto B: {conjunto1}')

print()
print('Capacidad')
print(f'Conjunto A tiene: {len(conjunto)}')
print(f'Conjunto A puede tener hasta {conjunto.maximo()} elementos.')
if conjunto.esta_lleno():
  print('Conjunto A esta lleno.')
else:
  print('Conjunto A no esta lleno.')
print(f'Conjunto B tiene: {len(conjunto1)}')
print(f'Conjunto B puede tener hasta {conjunto1.maximo()} elementos.')
if conjunto1.esta_lleno():
  print('Conjunto B esta lleno.')
else:
  print('Conjunto B no esta lleno.')

print()
print('Pertenencia')
print('1 esta en el conjunto A?')
if conjunto.esta(1):
  print('Si')
else:
  print('No')
print('0 esta en el conjunto A?')
if conjunto.esta(0):
  print('Si')
else:
  print('No')

print()
print('Union')
print(f'AUB: {conjunto.union(conjunto1)}')

print()
print('Interseccion')
print(f'A∩B: {conjunto.interseccion(conjunto1)}')

print()
print('Diferencia Relativa')
print(f'A-B: {conjunto.diferecia_relativa(conjunto1)}')
print(f'B-A: {conjunto1.diferecia_relativa(conjunto)}')

print()
print('Diferencia Simetrica')
print(f'AΔB: {conjunto.diferencia_simetrica(conjunto1)}')
