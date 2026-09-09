from typing import Any

class NodoPolinomio:
    """Contiene la informacion de un termino."""
    def __init__(self, coeficiente: int, grado: int) -> None:
        self.coeficiente: int = coeficiente
        self.grado: int = grado
        self.siguiente: 'NodoPolinomio' = None


class Polinomio:
    """Contiene y administra 'NodoPolinomio's para formar un polinomio.
    
    Metodos:
    - agregar
    """

    def __init__(self) -> None:
        self.cabeza: 'NodoPolinomio' = None

    def agregar(self, coeficiente: int, grado: int) -> None:
        """Agrega un termino al polinomio.
        
        Parametros:
        - coeficiente: coeficiente del nuevo termino.
        - grado: del nuevo termino.
        """

        nuevo = NodoPolinomio(coeficiente, grado)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual: 'NodoPolinomio' = self.cabeza
            anterior: 'NodoPolinomio' = None
            while actual is not None and actual.grado > nuevo.grado:
                anterior = actual
                actual = actual.siguiente
            if actual is None:
                anterior.siguiente = nuevo
            elif actual.grado == nuevo.grado:
                actual.coeficiente += nuevo.coeficiente
            else:
                nuevo.siguiente = actual
                if anterior is None:
                    self.cabeza = nuevo
                else: 
                    anterior.siguiente = nuevo

    def __str__(self) -> str:
        if self.cabeza is None:
            return ''

        result: str = ''
        actual: 'NodoPolinomio' = self.cabeza
        primero: bool = True
        while actual is not None:
            if actual.coeficiente != 0:
                # Signo
                if actual.coeficiente > 0:
                    if primero:
                        primero = False
                    else:
                        result += '+'
                # Coeficiente
                if actual.coeficiente != 1 or actual.grado == 0:
                    if actual.coeficiente == -1:
                        result += '-'
                    else:
                        result += str(actual.coeficiente)
                # Grado
                if actual.grado != 0:
                    result += 'x'
                    if actual.grado != 1:
                        result += '^' + str(actual.grado)
            actual = actual.siguiente

        return result


# Demo
print('Demo')
p = Polinomio()
print(f'Polinomio creado: {p}')
p.agregar(1, 2)
print(f'Se le agrega x^2: {p}')
p.agregar(-1, 1)
print(f'Se le agrega -x: {p}')
p.agregar(-13, 0)
print(f'Se le agrega -13: {p}')
p.agregar(4, 5)
print(f'Se le agrega 4x^5: {p}')
p.agregar(7, 3)
print(f'Se le agrega 7x^3: {p}')
p.agregar(1, 2)
print(f'Se le agrega x^2 de nuevo: {p}')
print('Notece que si se le agrega un termino del mismo grado que\n'
      'otro termino en el polinomio, los coeficientes se suman.'
)
