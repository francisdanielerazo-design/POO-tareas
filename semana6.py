class Empleado:
    def __init__(self, nombre, salario):
        # Encapsulación: atributo privado
        self.nombre = nombre
        self.__salario = salario

    # encapsulación
    def get_salario(self):
        return self.__salario

    #  polimorfismo
    def calcular_salario(self):
        return self.__salario

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Salario: {self.calcular_salario()}")


# herencia
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, bono):
        # Llamada al constructor de la clase base
        super().__init__(nombre, salario)
        self.bono = bono

    # Polimorfismo
    def calcular_salario(self):
        return self.get_salario() + self.bono


# Método principal
def main():
    # Creación de objetos (instancias)
    empleado1 = Empleado("Carlos", 500)
    empleado2 = EmpleadoTiempoCompleto("Ana", 500, 200)

    # Uso del polimorfismo
    empleado1.mostrar_info()
    empleado2.mostrar_info()


# Ejecución del programa
if __name__ == "__main__":
    main()