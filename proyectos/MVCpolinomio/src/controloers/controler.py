"""Este modulo busca unir el modelo y la interfaz grafica en perfecta armonia."""

def cvn(expresion: str) -> int|float:
    """Convierte la expresion en float si es necesario, si no, lo 
    convierte en int.
    
    Parametros:
    - expresion: una cadena con el valor a convertir.

    Excepciones:
    - ValueError: si es que no se pudo convertir 'expresion' en int
    ni en float.
    """

    conversion: int|float
    try:
        conversion = int(expresion)
    except ValueError:
        conversion = float(expresion)
    return conversion

class Controler:
    """Sirve de pegamento entre el 'model' y el 'view'.
    
    No llame a metodos en sus instacias.
    """
    def __init__(self, view: 'View', model: 'Polinomio') -> None:
        self.view: 'View' = view
        self.model: 'Polinomio' = model

        # Configurar Eventos
        self.view.bnt_add.configure(command=self.button_cliked)
        self.view.bnt_clear.configure(command=self.button_clear)
        self.view.bnt_eval.configure(command=self.button_eval)

    def button_cliked(self) -> None:
        """Crea un polinomio a partir de la entrada (contenido de 
        'entry') y lo muestra en 'label' si es que la entrada es valido, 
        si no, muestra un mesagen de error en 'label'."""
        polinomio: str = self.view.get_entry1()
        try:
            self.model.crear_polinomio(polinomio)
            self.view.update_label4(str(self.model))
        except ValueError:
            self.view.update_label4('Entrada invalida!\n'
                                   'La entrada debe ser un polinomio de la '
                                   'forma:\nax^n+bx^n-1+...+cx+d, donde a, b'
                                   ', c, d son numeros reales.')

    def button_clear(self) -> None:
        """Limpia los componentes de la GUI y elimina el polinomio."""
        self.view.set_entry1('')
        self.view.set_entry2('')
        self.view.update_label4('')
        self.model.borrar()

    def button_eval(self) -> None:
        """Evalua la exprecion en base al valor dado de 'x'."""
        x: str = self.view.get_entry2()
        if  not x.isdigit():
            self.view.update_label4('Error: x tiene que ser un numero!')
        else:
            resultado: int|float = self.model.eval(cvn(x))
            self.view.update_label4(resultado)
