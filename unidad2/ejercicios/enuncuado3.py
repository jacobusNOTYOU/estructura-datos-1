"""3) Matriz Dispersa
Implementa ``Matriz Dispersa(filas, columnas) usando diccionario de 
coordenadas. Debe soportar:

- establecer(i, j, valor),
- obtener(i, j),
- transponer(),
- densidad().
Evalua su eficience contra una matriz densa para un caso con pocos no-cero.
"""

import tracemalloc


class MatrizDispersa:
    """Matriz Dispersa. Implementado con un diccionario. Indices comienzan
    en (0,0)

    Instanciacion requiere de especificar las dimenciones de la matriz.
    
    Metodos
    - obtener
    - establecer
    - transponer
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

tracemalloc.start()
matriz_dispersa = MatrizDispersa(5, 5)
dict_size, dict_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
tracemalloc.stop()

print('Matriz dispersa:')
print(f'Tamano: {dict_size}, pico: {dict_peak}.')
"""
Cosas que faltan:
- La matriz densa 
- llenarlos de los mismos datos 
- Hacer la comparacion de memoria
- Comparar tiempo en operaciones
"""