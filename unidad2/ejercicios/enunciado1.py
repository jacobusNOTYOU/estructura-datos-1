"""ADT Polinomio

Implementar la clase 'Polinomio' con:
- agregar_termino(coef, exp)
- evaluar(x)
- sumar(otro)
- restar(otro)
- derivar
- representacion lejible en texto.
Prueba con al menos 3 polinomios distintos."""


class _Termino:
    def __init__(self, coeficiente: int|float, exponente: int) -> None:
        self.coeficiente: int|float = coeficiente
        self.exponente: int = exponente
        self.siguiente: _Termino|None = None

        
class Polinomio:
    """Implementacion de un polinomio usando listas enlazadas.
    
    Metodos:
    - agregar_termino(coef, exp)
    - evaluar(x)
    - sunar(otro)
    - restar(otro)
    - derivar
    """

    def __init__(self) -> None:
        self._terminos: _Termino = None

    def agregar_termino(self, coeficiente: int|float, exponente: int) -> None:
        """Agrega un termino al polinomio, manteniendolo ordenado.
        
        *Nota: Si ya existe un termino en el polinomio que el que se quiere 
        agregar, estos se suman.
        
        Parametros:
        - coeficiente: el coeficiente del nuevo termino.
        - exponente: el exponente del nuevo termino.
        """

        nuevo = _Termino(coeficiente, exponente)
        if self._terminos is None:
            self._terminos = nuevo
        else:
            actual = self._terminos
            anterior = None
            while((actual is not None) 
                  and (actual.exponente > nuevo.exponente)):
                  anterior = actual
                  actual = actual.siguiente
            if actual is None:
                anterior.siguiente = nuevo
            elif actual.exponente == nuevo.exponente:
                actual.coeficiente += nuevo.coeficiente
            else:
                if anterior is not None:
                    anterior.siguiente = nuevo
                    nuevo.siguiente = actual
                else:
                    self._terminos = nuevo
                    nuevo.siguiente = actual

    def evaluar(self, x: int) -> int|float:
        """Evalua el polinomio con el valor dado de 'x'.
        
        Parametros:
        - x: es el valor con el que se evaluara la variable del polinomio.
        """

        if self._terminos is None:
            return 0

        actual: _Termino = self._terminos
        evaluacion: int|float = 0
        while actual is not None:
            evaluacion += actual.coeficiente * (x**actual.exponente)
            actual = actual.siguiente

        return evaluacion

    def suma(self, otro: 'Polinomio') -> 'Polinomio':
        """Retorna la suma dos polinomios.
        
        Parametros:
        - otro: el segundo polinomio con el cual sumar.
        """
        resultado: 'Polinomio' = Polinomio()
        actual: _Termino = self._terminos
        while actual is not None:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        actual = otro._terminos
        while actual is not None:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        return resultado

    def resta(self, otro: 'Polinomio') -> 'Polinomio':
        """Retorna la resta dos polinomios.
        
        Parametros:
        - otro: el segundo polinomio con el cual resta.
        """
        resultado: 'Polinomio' = Polinomio()
        actual: _Termino = self._terminos
        while actual is not None:
            resultado.agregar_termino(actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        actual = otro._terminos
        while actual is not None:
            resultado.agregar_termino(-actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        return resultado

    def derivar(self) -> 'Polinomio':
        """Retorna la derivada del polinomio."""
        derivada: 'Polinomio' = Polinomio()
        if self._terminos is None:
            derivada.agregar_termino(0, 0)
            return derivada

        actual: _Termino = self._terminos
        while actual is not None:
            if actual.exponente != 0:
                derivada.agregar_termino(actual.coeficiente*actual.exponente, 
                                         actual.exponente-1)
            actual = actual.siguiente

        return derivada

    def __str__(self) -> str:
        if self._terminos is None:
            return ''

        result: str = ''
        actual: '_Termino' = self._terminos
        primero: bool = True
        while actual is not None:
            if actual.coeficiente != 0:
                # Signo
                if primero:
                    primero = False
                else:
                    if actual.coeficiente > 0:
                        result += '+'
                # Coeficiente
                if actual.coeficiente != 1 or actual.exponente == 0:
                    if actual.coeficiente == -1 and actual.exponente != 0:
                        result += '-'
                    else:
                        result += str(actual.coeficiente)
                # Grado
                if actual.exponente != 0:
                    result += 'x'
                    if actual.exponente != 1:
                        result += '^' + str(actual.exponente)
            actual = actual.siguiente

        return result


# DEMO
print('Unidad2: enunciado 1')
print('--------------------')
print()

print('Polinomio p:')
p = Polinomio()
print(p)
print('agregar el termino "1" a p:')
p.agregar_termino(1, 0)
print(p)
print('agregar el termino "4x" a p:')
p.agregar_termino(4, 1)
print(p)
print('agregar el termino "x^2" a p:')
p.agregar_termino(1, 2)
print(p)
print('Evaluar p(5)')
print(p.evaluar(5))
print()

print('Polinomio q:')
q = Polinomio()
print(q)
print('agregar el termino "x^3" a q:')
q.agregar_termino(1, 3)
print(q)
print('agregar el termino "-2x" a q:')
q.agregar_termino(-2, 1)
print(q)
print('agregar el termino "-13" a q:')
q.agregar_termino(-13, 0)
print(q)
print('Evaluar q(-3)')
print(q.evaluar(-3))
print()

print('Polinomio r:')
r = Polinomio()
print(r)
print('agregar el termino "-7x^5"')
r.agregar_termino(-7, 5)
print(r)
print('agregar el termino "40"')
r.agregar_termino(40, 0)
print(r)
print('agregar el termino "2x^2"')
r.agregar_termino(2, 2)
print(r)
print('agregar el termino "-11"')
r.agregar_termino(-11, 0)
print(r)
print('Evaluar r(2)')
print(r.evaluar(2))
print()

print('Sumar p + q:')
print(p.suma(q))
print()

print('Restar p - q')
print(p.resta(q))
print()

print('Restar p - r')
print(p.resta(r))
print()

print('Derivada de p')
print(p.derivar())
print()

print('Derivada de q')
print(q.derivar())
print()

print('Derivada de r')
print(r.derivar())
print()
