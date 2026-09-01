"""Este module es el encargado del manejo de datos.

Clases Publicas:
- Polinomio
"""

from copy import copy

class NodoPolinomio:
    def __init__(self, coeficiente: int|float, exponente: int):
        self.coeficiente: int|float = coeficiente
        self.exponente: int = exponente
        self.siguiente: 'NodoPolinomio' = None

class Polinomio:
    """Representa un polinomio de una sola variable.
    
    Metodos:
    - agregar_termino
    - crear_polinomio
    - borrar
    """
    def __init__(self) -> None:
        self.cabeza: NodoPolinomio|None = None

    def agregar_termino(self, coeficiente: int|float, exponente: int) -> None:
        """Agrega un termino al polinomio.
        
        Parametros:
        - coeficiente: Coeficiente del termino.
        - exponenete: Exponente del termino.
        """
        nuevo_nodo: NodoPolinomio = NodoPolinomio(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual: NodoPolinomio = self.cabeza
            anterior: NodoPolinomio = None
            while actual is not None and actual.exponente > exponente:
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo
            else:
                anterior.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = actual

    def crear_polinomio(self, polinomio: str) -> None:
        """Crea un polinomio en base a un str, y lo agregar al existente
        si es que ya hay un polinomio.
        
        Parametros:
        - polinomio: Una cadena de caracteres que contiene un polinomio
        de la forma: ax^n+bx^n-1+...+cx+d, donde a, b, c y d son reales.

        Excepciones:
        - ValueError: si 'polinomio' no es valido, es decir no sigue la 
        forma indicada en 'Parametros:'.

        *Nota: No se soportan 'polinomios' con exponentes negativos.
        """
        if polinomio != '':
            try:
                terminos = self._parse_terminos(polinomio)
            except ValueError:
                raise

            for t in terminos:
                self.agregar_termino(t.coeficiente, t.exponente)

    def borrar(self) -> None:
        """Elimina el polinomio dejandolo en None."""
        self.cabeza = None

    def _parse_terminos(self, polinomio: str) -> list[NodoPolinomio]:
        """Parsea los terminos de 'polinomio'.
        
        Retorna: terminos: list[NodoPolinomio].

        Parametros:
        - polinomio: Una cadena de caracteres que contiene un polinomio
        de la forma: ax^n+bx^n-1+...+cx+d, donde a, b, c y d son reales.

        Excepciones:
        - ValueError: si 'polinomio' no es valido, es decir no sigue la 
        forma indicada en 'Parametros:'.

        *Nota: No se soportan 'polinomios' con exponentes negativos.
        """
        terminos: list[NodoPolinomio] = []
        copia: str = copy(polinomio)
        while copia != '':
            pos_sig_pos: int = copia.find('+')
            pos_sig_neg: int = copia.find('-')
            sig: str = ''
            if pos_sig_pos == 0 or pos_sig_neg == 0:
                sig = copia[:1]
                copia = copia[1:]
                pos_sig_pos = copia.find('+')
                pos_sig_neg = copia.find('-')

            if pos_sig_pos == -1 and pos_sig_neg == -1:
                terminos.append(self._crear_nodopolinomio(sig + copia))
                copia = ''
            elif pos_sig_pos == -1:
                terminos.append(self._crear_nodopolinomio(sig + copia[:pos_sig_neg]))
                copia = copia[pos_sig_neg:]
            elif pos_sig_neg == -1:
                terminos.append(self._crear_nodopolinomio(sig + copia[:pos_sig_pos]))
                copia = copia[pos_sig_pos:]
            elif pos_sig_pos < pos_sig_neg:
                terminos.append(self._crear_nodopolinomio(sig + copia[:pos_sig_pos]))
                copia = copia[pos_sig_pos:]
            else:
                terminos.append(self._crear_nodopolinomio(sig + copia[:pos_sig_neg]))
                copia = copia[pos_sig_neg:]
        return terminos

    def _crear_nodopolinomio(self, termino: str) -> NodoPolinomio:
        """Toma un unico termino y retorna un 'NodoPolinomio'.
        
        Retorna: NodoPolinomio

        Parametros:
        - termino: Cadena de caracteres que contiene la forma:
        'ax^n' o 'ax', donde a es un real, y n es un numero natural.

        Excepciones:
        - ValueError: si es que 'termino' es invalido segun se definio
        en la seccion 'Parametros'.

        *Nota: No se soportan 'terminos' con exponentes negativos.
        """
        if termino != '':
            pos_coef: int = termino.find('x')
            pos_exp: int = termino.find('^')
            if pos_coef == -1 and pos_exp == -1:
                return NodoPolinomio(int(termino), 0)
            elif pos_coef != -1 and pos_exp != -1: 
                if pos_coef == 0:
                    return NodoPolinomio(1, int(termino[pos_exp + 1:]))
                if pos_coef == 1:
                    coeficiente = termino[:1]
                    if coeficiente == '+':
                        return NodoPolinomio(1, int(termino[pos_exp + 1:]))
                    elif coeficiente == '-':
                        return NodoPolinomio(-1, int(termino[pos_exp + 1:]))
                    elif termino[:1].isdecimal():
                        return NodoPolinomio(int(termino[:pos_coef]), int(termino[pos_exp + 1:]))
                    else:
                        raise ValueError('coeficiente invalido!')
                else:
                    return NodoPolinomio(int(termino[:pos_coef]), int(termino[pos_exp + 1:]))
            elif pos_coef != -1 and pos_exp == -1: 
                if pos_coef == 0:
                    return NodoPolinomio(1, 1)
                if pos_coef == 1:
                    coeficiente = termino[:1]
                    if coeficiente == '+':
                        return NodoPolinomio(1, 1)
                    elif coeficiente == '-':
                        return NodoPolinomio(-1, 1)
                    elif termino[:1].isdecimal():
                        return NodoPolinomio(int(termino[:pos_coef]), 1)
                    else:
                        raise ValueError('coeficiente invalido!')
                else:
                    return NodoPolinomio(int(termino[:pos_coef]), 1)
            else:
                raise ValueError('"termino" es invalido!')

    def __str__(self) -> None:
        """Retorna el contenido del polinomio en formato 'str'."""
        if self.cabeza is None:
            return "0"

        resultado: str = ""
        actual: NodoPolinomio = self.cabeza
        while actual is not None:
            if actual.coeficiente != 0:  # Ignorar términos con coeficiente 0
                if actual.coeficiente > 0 and len(resultado)>0:
                  resultado += "+"
                if actual.coeficiente == -1 and actual.exponente != 0:
                    resultado += "-"
                elif actual.coeficiente != 1 or actual.exponente == 0:
                    resultado += str(actual.coeficiente)
                if actual.exponente > 0:
                    resultado += "x"
                    if actual.exponente > 1:
                        resultado += "^" + str(actual.exponente)
            actual = actual.siguiente
        return resultado if resultado else "0"
