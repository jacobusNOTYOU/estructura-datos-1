class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # ERROR: Lógica invertida
        # CORRECCION: '>' -> '<='
        return len(self.items) <= 0

    def push(self, item):
        # ERROR: No está agregando el item recibido
        # CORRECCION: usar 'append()'
        self.items.append(item)

    def pop(self):
        # ERROR: No verifica si hay elementos antes de borrar
        # y no retorna el elemento eliminado
        # CORRECCION: Verificar primero si esta vacio, y si los esta lanzar
        # una excepcion.
        if self.is_empty():
            raise IndexError('El "Stack" esta vacio!')
        # CORRECCION: Guardar el ultimo elemnto en una variable antes de
        # eliminarlo y devolverlo despues.
        result = self.items[-1]
        # CORRECCION: En 'remove(x)' x se refiere a un elemento no a una
        # posicion, el ultimo elemento de puede eliminar de la siguiente
        # forma:
        del self.items[-1]
        return result

# --- Prueba del Alumno ---
mi_pila = Stack()
mi_pila.push("A")
mi_pila.push("B")

print("¿Está vacía?", mi_pila.is_empty())
print("Elemento sacado:", mi_pila.pop())

# TODO: Corregir la clase Stack para que cumpla con el comportamiento LIFO
