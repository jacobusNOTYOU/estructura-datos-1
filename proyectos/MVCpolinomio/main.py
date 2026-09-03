from tkinter import Tk
from src.views.view import View
from src.models.model import Polinomio
from src.controloers.controler import Controler

def main():
    root = Tk()
    root.title('Polinomio')

    model = Polinomio()
    view = View(root, 14, 15)
    controler = Controler(view, model)

    root.mainloop()


if __name__ == "__main__":
    main()
