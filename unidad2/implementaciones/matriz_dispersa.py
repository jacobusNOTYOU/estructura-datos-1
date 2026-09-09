"""Implementacion de la matriz dispersa usando un diccionario."""


class MatrizDispersa:
    """Matriz Dispersa. Implementado con un diccionario. Indices comienzan
    en (0,0)

    Instanciacion requiere de especificar las dimenciones de la matriz.
    
    Metodos
    - obtener
    - establecer
    - sumar
    - transponer
    - multiplicar
    - densidad
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

    def sumar(self, otro: 'MatrizDispersa') -> 'MatrizDispersa':
        """Suma dos 'MatrizDispersa' y retorna una 'MatrizDispersa' con
        el resultado.
        
        Parametros:
        - otro: La 'MatrizDispersa' con la que se va a sumarse la matriz.

        Excepciones:
        - ArithmeticError: se 'otro' no tiene las misma dimenciones que 'self'.
        """

        if ((self.max_filas==otro.max_filas) 
            and (self.max_columnas==otro.max_columnas)):
            resultado = MatrizDispersa(self.max_filas, self.max_columnas)
            for i in range(self.max_filas):
                for j in range(self.max_columnas):
                    valor = self.obtener(i, j) + otro.obtener(i, j)
                    if valor != 0:
                        resultado.establecer(i, j, valor)

            return resultado
        else:
            raise ArithmeticError("Error: las matrices deben tener "
                                  "las mismas dimenciones!")

    def traspuesta(self) -> 'MatrizDispersa':
        """Retorna la traspuesta de la matriz."""
        resultado = MatrizDispersa(self.max_columnas, self.max_filas)
        for i in range(self.max_filas):
            for j in range(self.max_columnas):
                valor = self.obtener(i, j)
                if valor != 0:
                    resultado.establecer(j, i, valor)

        return resultado

    def multiplicar(self, otro: 'MatrizDispersa') -> 'MatrizDispersa':
        """Retorna el producto de dos 'MatrizDispersa'.
        
        Parametros:
        - otro: La 'MatrizDispersa' con la que se va a sumarse la matriz.

        Excepciones:
        - ArithmeticError: si las columnas de la primera deben coincidir 
        con la segunda.
        """

        if self.max_columnas != otro.max_filas:
            raise ArithmeticError("Error: las columnas de la primera "
                                  "deben coincidir con la segunda!")
        
        resultado = MatrizDispersa(self.max_filas, otro.max_columnas)
        for i in range(self.max_filas):
            for j in range(otro.max_columnas):
                suma = 0
                for k in range(self.max_columnas):
                    fi = self.obtener(i, k)
                    co = otro.obtener(k, j)
                    if fi != 0 and co != 0:
                        suma += fi * co
                resultado.establecer(i, j, suma)

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


# DEMO
m = MatrizDispersa(5, 5)
m.establecer(0, 0, 1)
m.establecer(1, 0, 1)
m.establecer(2, 1, 1)
m.establecer(3, 0, 1)
m.establecer(4, 0, 1)
m.establecer(2, 2, 1)

print('matriz m:')
print(m)

n = MatrizDispersa(5, 5)
n.establecer(0, 4, 1)
n.establecer(1, 4, 1)
n.establecer(2, 4, 1)
n.establecer(3, 4, 1)
n.establecer(4, 4, 1)
n.establecer(0, 3, 1)
n.establecer(1, 3, 1)
n.establecer(2, 2, 1)

print('matriz n:')
print(n)

print('Sumar m+n:')
print(m.sumar(n))
print()

print('Trasponer m:')
print(m.traspuesta())
print()

p = m.multiplicar(n)
print('Multiplicar mn:')
print(m.multiplicar(n))
print()

print('Densidad de m:')
print(m.densidad())
