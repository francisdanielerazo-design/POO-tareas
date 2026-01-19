width = float(input("Ingrese el ancho del rectángulo en metros: "))
height = float(input("Ingrese el alto del rectángulo en metros: "))

# Cálculo del área (float)
area = width * height

# Evaluación del tamaño del rectángulo (boolean)
is_large = area >= 20

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Ancho: {width} m")
print(f"Alto: {height} m")
print(f"Área del rectángulo: {area} m²")

# Condición usando boolean
if is_large:
    print("El rectángulo es considerado GRANDE.")
else:
    print("El rectángulo es considerado PEQUEÑO.")
