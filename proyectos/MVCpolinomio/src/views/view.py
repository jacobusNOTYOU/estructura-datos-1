"""Este modulo se encargar de la GUI.

Contiene la clase View.
"""

from tkinter import ttk, Button, Label, Frame, StringVar

class View:
    """Encargado de servir un simple GUI.
    
    Metodos Publicos:
    - get_entry
    - update_label
    """
    def __init__(self, master: 'Tk') -> None:
        self.frame = ttk.Frame(master)
        self.frame.grid(column=0, row=0)

        self.entry = ttk.Entry(self.frame)
        self.entry.grid(column=0, row=0)

        self.label = ttk.Label(self.frame, text='Hello, World')
        self.label.grid(column=0, row=1, sticky='we')

        self.button = ttk.Button(self.frame, text='Click me!', command=self.button_event)
        self.button.grid(column=0, row=2)

    def button_event(self) -> None:
        """Evento del boton por defecto."""
        self.update_label('Algo paso')

    def get_entry(self) -> None:
        """Retorna el contenido de 'entry'."""
        return self.entry.get()

    def update_label(self, text: str) -> None:
        """Actualiza el contenido de 'label' a 'text'.
        
        Parametros:
        - text: Texto con el cual actualizar 'label'."""
        self.label.configure(text=text)
