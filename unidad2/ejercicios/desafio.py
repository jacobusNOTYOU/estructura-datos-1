"""Desafio
Implementa multiplicación de polinomios y suma de matrices dispersas con 
validación de dimensiones.
"""

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
    - sumar(otro)
    - restar(otro)
    - derivar
    - mult(otro)
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

    def mult(self, otro: 'Polinomio') -> 'Polinomio':
        """Multiplica este polinomio con `otro`.
        
        Parametros:
        - otro: el otro polinomio con el que multiplicar este polinomio.
        """

        resultado: 'Polinomio' = Polinomio()
        if (self._terminos is not None) and (otro is not None):
            actual: _Termino = self._terminos
            while actual is not None:
                actual_otro: _Termino = otro._terminos
                while actual_otro is not None:
                    resultado.agregar_termino(
                        actual.coeficiente * actual_otro.coeficiente,
                        actual.exponente + actual_otro.exponente
                    )
                    actual_otro = actual_otro.siguiente
                actual = actual.siguiente
            
            return resultado
        
        return resultado.agregar_termino(0, 0)

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


class MatrizDispersa:
    """Matriz Dispersa. Implementado con un diccionario. Indices comienzan
    en (0,0)

    Instanciacion requiere de especificar las dimenciones de la matriz.
    
    Metodos
    - obtener
    - establecer
    - transponer
    - densidad
    - suma
    """

    def __init__(self, filas: int, columnas: int) -> None:
        self.max_filas: int = filas
        self.max_columnas: int = columnas
        self.elementos: dict[(int, int), any] = {}

    def obtener(self, i: int, j: int) -> any:
        """Retorna el elemento que esta en la fila i y columna j.
        
        Parametros:
        - i: La fila en la que se encuentra el elemento.
        - j: La columna en la que se encuentra el elemento.

        Excepciones:
        - IndexError: Si la posicion (i,j) esta fuera del rango 
        (]0;self.max_filas], ]0;self.max_columnas]).
        """

        if (i<self.max_filas) and (j<self.max_columnas):
            if (i,j) in self.elementos:
                return self.elementos[(i,j)]
            else:
                return 0
        else:
            raise IndexError(f"Error: posicion ({i},{j}) fuera de rango!")

    def establecer(self, i: int, j: int, valor: any) -> None:
        """Establece el valor del elemento ubicado en (i,j).
        
        Parametros:
        - i: La fila del elemento a establecer.
        - j: La columna del elemento a establecer.
        - valor: El valor a establecer.

        Excepciones:
        - IndexError: Si la posicion (i,j) esta fuera del rango 
        (]0;self.max_filas], ]0;self.max_columnas]).
        """

        if (i<self.max_filas) and (j<self.max_columnas):
            self.elementos[(i,j)] = valor
        else:
            raise IndexError(f"Error: posicion ({i},{j}) fuera de rango!")

    def traspuesta(self) -> 'MatrizDispersa':
        """Retorna la traspuesta de la matriz."""
        resultado = MatrizDispersa(self.max_columnas, self.max_filas)
        for i in range(self.max_filas):
            for j in range(self.max_columnas):
                valor = self.obtener(i, j)
                if valor != 0:
                    resultado.establecer(j, i, valor)

        return resultado

    def densidad(self) -> float:
        """Retorna el porcentaje de elementos no-cero de la matriz."""
        contador = 0
        for i in range(self.max_filas):
            for j in range(self.max_columnas):
                if self.obtener(i, j) != 0:
                    contador += 1

        cantidad = self.max_filas * self.max_columnas
        return (contador / cantidad) * 100

    def suma(self, otro: 'MatrizDispersa') -> 'MatrizDispersa':
        """Suma dos matrices dispersas con validacion de dimensiones.
        
        Parametros:
        - otro: la matriz con la que sumar esta matriz.

        Excepciones:
        - DimensionError: cuando las matrices difieren en dimension.
        """

        if (
            self.max_filas != otro.max_filas or
            self.max_columnas != otro.max_columnas
            ):
            raise DimensionError(
                f"Error: No se pueden sumar matrices de diferentes dimensiones!"
            )
        
        result: 'MatrizDispersa' = MatrizDispersa(
                                    self.max_filas, 
                                    self.max_columnas
                                    )
        for i in range(self.max_filas):
            for j in range(self.max_columnas):
                sum = self.obtener(i, j) + otro.obtener(i,j)
                if sum != 0:
                    result.establecer(i, j, sum)
        
        return result

    def __str__(self) -> str:
        cadena = ''
        for i in range(self.max_filas):
            cadena = cadena + '['
            for j in range(self.max_columnas):
                if j != 0:
                    cadena = cadena + ', '
                cadena = cadena + str(self.obtener(i, j))
            cadena = cadena + ']\n'

        return cadena


def main():
    print(f"Multiplicacion de polinomios:")
    p1: Polinomio = Polinomio()
    p1.agregar_termino(13, 0)
    p1.agregar_termino(2, 3)
    p1.agregar_termino(1, 2)
    print(f"Polinomio #1: {p1}")
    p2: Polinomio = Polinomio()
    p2.agregar_termino(5, 0)
    p2.agregar_termino(1, 10)
    p2.agregar_termino(2, 2)
    p2.agregar_termino(5, 1)
    print(f"Polinomio #2: {p2}")
    print(f"Resultado: {p1.mult(p2)}")
    print()

    print(f"Suma de Matrices Dispersas:")
    m1: MatrizDispersa = MatrizDispersa(4, 4)
    m1.establecer(0, 0, 1)
    m1.establecer(1, 1, 2)
    m1.establecer(2, 2, 3)
    m1.establecer(3, 3, 4)
    m1.establecer(0, 1, 2)
    print(f"Matriz #1:")
    print(m1)
    m2: MatrizDispersa = MatrizDispersa(4, 4)
    m2.establecer(0, 3, 1)
    m2.establecer(1, 2, 2)
    m2.establecer(2, 1, 3)
    m2.establecer(3, 0, 4)
    m2.establecer(0, 1, 4)
    print(f"Matriz #2:")
    print(m2)
    print(f"Suma de las matrices:")
    print(m1.suma(m2))
    print()

if __name__ == '__main__':
    main()