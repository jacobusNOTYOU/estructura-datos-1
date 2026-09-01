from tkinter import Tk
from src.views.view import View
from src.models.model import Polinomio
from src.controloers.controler import Controler

def main():
    root = Tk()

    model = Polinomio()
    view = View(root)
    controler = Controler(view, model)

    root.mainloop()


if __name__ == "__main__":
    main()
