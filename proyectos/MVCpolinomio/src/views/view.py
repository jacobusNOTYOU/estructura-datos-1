"""Este modulo se encargar de la GUI.

Contiene la clase View.
"""

import tkinter as Tk
from tkinter import *
from tkinter import ttk

class View:
    """Encargado de servir un simple GUI.
    
    Metodos Publicos:
    - get_entry
    - update_label
    """
    def __init__(self, master: 'Tk', font_size=14, padding=0) -> None:
        ttk.Style().configure('TButton', 
                              font=f'Helvetica {font_size}',
                              padding=padding)
        ttk.Style().configure('TFrame', 
                              font=f'Helvetica {font_size}'
                              )
        ttk.Style().configure('TLabel', 
                              font=f'Helvetica {font_size}',
                              padding=padding
                              )
        ttk.Style().configure('TEntry', 
                              padding=padding
                              )

        self.frame1 = ttk.Frame(master, padding=padding)
        self.frame1.grid(column=0, row=0)

        self.bnt_clear = ttk.Button(self.frame1, text='Limpiar')
        self.bnt_clear.grid(column=0, row=0)

        self.bnt_add = ttk.Button(self.frame1, text='Agregar')
        self.bnt_add.grid(column=0, row=1)

        self.bnt_eval = ttk.Button(self.frame1, text='Evaluar')
        self.bnt_eval.grid(column=0, row=2)

        self.frame2 = ttk.Frame(master, padding=padding)
        self.frame2.grid(column=1, row=0)

        self.label1 = ttk.Label(self.frame2, text='Ingresa un polinomio.')
        self.label1.grid(column=0, row=0)

        self._var_entry1 = StringVar()
        self.entry1 = ttk.Entry(self.frame2, 
                                font=f'Helvica {font_size}',
                                textvariable=self._var_entry1
                                )
        self.entry1.grid(column=0, row=1)

        self.label2 = ttk.Label(self.frame2, text='Valor de "x":')
        self.label2.grid(column=0, row=2)

        self._var_entry2 = StringVar()
        self.entry2 = ttk.Entry(self.frame2, 
                                font=f'Helvica {font_size}',
                                textvariable=self._var_entry2)
        self.entry2.grid(column=0, row=3)

        self.label3 = ttk.Label(self.frame2, text='El resultado es:')
        self.label3.grid(column=0, row=4)

        self.label4 = ttk.Label(self.frame2)
        self.label4.grid(column=0, row=5)

    def get_entry1(self) -> str:
        """Retorna el contenido de 'entry1'."""
        return self.entry1.get()

    def get_entry2(self) -> str:
        """Retorna el contenido de 'entry2'."""
        return self.entry2.get()

    def set_entry1(self, dato: str) -> None:
        """Actualiza 'entry1' para contener 'dato'.
        
        Parametros:
        - dato: El contenido con el cual actualizar 'entry1'.
        """
        self._var_entry1.set(dato)

    def set_entry2(self, dato: str) -> None:
        """Actualiza 'entry2' para contener 'dato'.
        
        Parametros:
        - dato: El contenido con el cual actualizar 'entry2'.
        """
        self._var_entry2.set(dato)

    def update_label1(self, text: str) -> None:
        """Actualiza el contenido de 'label1' a 'text'.
        
        Parametros:
        - text: Texto con el cual actualizar 'label1'."""
        self.label1.configure(text=text)

    def update_label2(self, text: str) -> None:
        """Actualiza el contenido de 'label2' a 'text'.
        
        Parametros:
        - text: Texto con el cual actualizar 'label2'."""
        self.label2.configure(text=text)

    def update_label3(self, text: str) -> None:
        """Actualiza el contenido de 'label3' a 'text'.
        
        Parametros:
        - text: Texto con el cual actualizar 'label3'."""
        self.label3.configure(text=text)

    def update_label4(self, text: str) -> None:
        """Actualiza el contenido de 'label' a 'text'.
        
        Parametros:
        - text: Texto con el cual actualizar 'label'."""
        self.label4.configure(text=text)
