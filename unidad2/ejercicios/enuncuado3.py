"""3) Matriz Dispersa
Implementa ``Matriz Dispersa(filas, columnas) usando diccionario de 
coordenadas. Debe soportar:

- establecer(i, j, valor),
- obtener(i, j),
- transponer(),
- densidad().
Evalua su eficience contra una matriz densa para un caso con pocos no-cero.
"""

from sys import getsizeof
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

filas = 10
columnas = 10
datos = [[None] * filas] * columnas
for i in range(filas):
    sub_data = [None] * columnas
    for j in range(columnas):
        sub_data[j] = i
    datos[i] = sub_data


#Memoria de Matriz Dispersa
tracemalloc.start()
matriz_dispersa = MatrizDispersa(filas, columnas)
dict_size, dict_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
# Establecer
for i in range(filas):
    for j in range(columnas):
        matriz_dispersa.establecer(i, j, datos[i][j])
dict_fill_size , dict_fill_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
# Obtener
dict_str = ''
for i in range(filas):
    for j in range(columnas):
        dict_str =  dict_str + str(matriz_dispersa.obtener(i, j)) + ','
    dict_str = dict_str + '\n'
dict_get_size , dict_get_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
# Traspuesta
dict_traspuesta = matriz_dispersa.traspuesta()
dict_tras_size , dict_tras_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
# Densidad
dict_densidad = matriz_dispersa.densidad()
dict_den_size , dict_den_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
tracemalloc.stop()

# Memoria de matriz densa
tracemalloc.start()
matriz_densa = [[None] * filas] * columnas
array_size, array_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
# Establecer
for i in range(filas):
    sub_matriz = [None] * columnas
    for j in range(columnas):
        sub_matriz[j] = datos[i][j]
        matriz_densa[i] = sub_matriz
array_fill_size, array_fill_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
# Obtener
array_str = ''
for i in range(filas):
    for j in range(columnas):
        array_str = array_str + str(matriz_densa[i][j]) + ','
    array_str = array_str + '\n'
array_get_size, array_get_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
# Traspuesta
array_traspuesta = [[None] * filas] * columnas
for i in range(filas):
    array_row = [None] * columnas
    for j in range(columnas):
        array_row[j] = matriz_densa[j][i]
    array_traspuesta[i] = array_row
array_tras_size, array_tras_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
# Densidad
cont = 0
for i in range(filas):
    for j in range(columnas):
        if matriz_densa[i][j] != 0:
            cont += 1
array_den = (cont/(filas * columnas)) * 100
array_den_size, array_den_peak = tracemalloc.get_traced_memory()
tracemalloc.reset_peak()
tracemalloc.stop()

print('En esta demostracion se mide la memoria usada por el programa '
      'en el momento de la inicializacion de la respectiva matriz. '
      'Tomar en cuenta el peso agregado de variables para iterar y '
      'guardar las medidas tomadas. Con todo esto, debido a tener '
      'circunstances aproximadamente equitativas para ambas matrices, '
      'es posible hacer una debida comparacion. '
)
print()

print('Memoria:')
print('---------')
print()

print('Matriz dispersa:')
print(f'Memoria en uso: {dict_size}.')
print()

print('Se llena la Matriz Dispersa con datos:')
print(matriz_dispersa)
print(f'Memoria en uso: {dict_fill_size}.')
print(f'Memoria aprox. de Matiz: {dict_fill_size}')
print()

print('Se obtienen los datos y se los guardan en una cadena:')
print(dict_str)
print(f'Memoria en uso: {dict_get_size}.')
dict_str_size = getsizeof(dict_str)
print(f'Contando la cadena({getsizeof(dict_str)}).')
print(f'Memoria aprox. de Matiz: {dict_get_size - dict_str_size}')
print()

print('Se obtiene la traspuesta:')
print(dict_traspuesta)
print(f'Memoria en uso: {dict_tras_size}.')
print(f'Contando la cadena({dict_str_size}) y un segundo diccionario'
      f'({dict_size}).'
)
print(f'Memoria aprox. de Matiz: {dict_tras_size - dict_str_size - dict_size}'
      ' , agregando el peso de algunas variables.'
)
print()

print('Se obtiene su densidad:')
print(dict_densidad)
print(f'Memoria en uso: {dict_den_size}.')
print(f'Contando la cadena({dict_str_size}) y un segundo diccionario'
      f'({dict_size}).'
)
print(f'Memoria aprox. de Matiz: {dict_tras_size - dict_str_size - dict_size}'
      ' , agregando el peso de algunas variables.'
)
print()


print('Matriz densa:')
print(f'Memoria en uso: {array_size}.')
print()

print('Se llena la Matriz Densa con datos:')
for i in range(5):
    print(matriz_densa[i])
print(f'Memoria en uso: {array_fill_size}.')
print(f'Memoria aprox. de Matriz: {array_fill_size}')
print()

print('Se obtienen los datos y se los guardan en una cadena:')
print(array_str)
print(f'Memoria en uso: {array_get_size}.')
array_str_s = getsizeof(array_str)
print(f'Contando la cadena({array_str_s}).')
print(f'Memoria aprox. de Matriz: {array_get_size - array_str_s}')
print()

print('Se obtiene la traspuesta:')
for i in range(5):
    print(array_traspuesta[i])
print(f'Memoria en uso: {array_tras_size}.')
print(f'Contando la cadena({array_str_s}). y una matriz auxiliar({array_size}).')
print(f'Memoria aprox. de Matriz: {array_tras_size - array_str_s - array_size}'
      ' , agregando el peso de algunas variables.'
)
print()

print('Densidad de la Matriz Densa:')
print(array_den)
print(f'Memoria en uso: {array_den_size}.')
print(f'Contando la cadena({array_str_s}). y una matriz auxiliar({array_size}).')
print(f'Memoria aprox. de Matriz: {array_tras_size - array_str_s - array_size}'
      ' , agregando el peso de algunas variables.'
)
print()


print('Resultados:')
print()

print('Uso de memoria:')
print(f'La matriz dispersa (implementada con diccionario) usa entre {dict_size}'
      f' y {dict_get_size - dict_str_size}.'
)
print(f'Mientras que la matriz densa usa entre {array_size} y '
      f'{array_get_size - array_str_s}'
)

print()
print('Complejidad de tiempo de operaciones:')
print('|-----------------------------------------------|')
print('|             | Matriz Dispersa |  Matriz Densa |')
print('|-----------------------------------------------|')
print('| establecer: |    O(1)         |       O(1)    |')
print('| obtener:    |    O(1)         |       O(1)    |')
print('| traspuesta: |    O(n)         |       O(n)    |')
print('| densidad:   |    O(n)         |       O(n)    |')
print('|-----------------------------------------------|')
