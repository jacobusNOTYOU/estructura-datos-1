# CÓDIGO CON ERROR
original_data = [10, 20, 30]

# La asigancion solo pasa la referencia de "original_data" a "copy_data"
copy_data = original_data

# Para realmente copiar el contenido de "original_data" a "copy_data"
# se va a usar la funcion "copy()" y asignar esa copia a "copy_data"
copy_data = original_data.copy()

# Debido que "copy_data" ya no hace referencia al mismo objeto que 
# "original_data", "original_data" queda intacto al modificar "copy_data"
copy_data.append(40)

print(f"Original: {original_data}")
print(f"Copia: {copy_data}")
