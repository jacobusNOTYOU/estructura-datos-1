"""Este modulo busca unir el modelo y la interfaz grafica en perfecta armonia."""


class Controler:
    """Sirve de pegamento entre el 'model' y el 'view'.
    
    No llame a metodos en sus instacias.
    """
    def __init__(self, view: 'View', model: 'Polinomio') -> None:
        self.view: 'View' = view
        self.model: 'Polinomio' = model

        # Configurar Eventos
        self.view.button.configure(command=self.button_cliked)

    def button_cliked(self) -> None:
        """Crea un polinomio a partir de la entrada (contenido de 
        'entry') y lo muestra en 'label' si es que la entrada es valido, 
        si no, muestra un mesagen de error en 'label'."""
        polinomio: str = self.view.get_entry()
        try:
            self.model.crear_polinomio(polinomio)
            self.view.update_label(str(self.model))
            self.model.borrar()
        except ValueError:
            self.view.update_label('Entrada invalida!\n'
                                   'La entrada debe ser un polinomio de la '
                                   'forma:\nax^n+bx^n-1+...+cx+d, donde a, b'
                                   ', c, d son numeros reales.')
