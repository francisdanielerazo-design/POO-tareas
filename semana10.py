import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"

    def to_line(self):

        return f"{self._id},{self._nombre},{self._cantidad},{self._precio}\n"


# ==============================
# CLASE INVENTARIO
# ==============================
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):

        try:
            if not os.path.exists(self.archivo):
                # Si no existe, lo crea vacío
                open(self.archivo, "w").close()
                print("Archivo inventario.txt creado automáticamente")
                return

            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_producto = datos[0]
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])

                        producto = Producto(id_producto, nombre, cantidad, precio)
                        self.productos.append(producto)

            print("Inventario cargado correctamente desde archivo")

        except FileNotFoundError:
            print("Error: Archivo no encontrado.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    def guardar_en_archivo(self):

        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_line())
            print("Inventario guardado correctamente en archivo.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Ya existe un producto con ese ID.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            print("Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Lista de productos:")
            for p in self.productos:
                print(p)

def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("Ingrese ID: ")
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))

                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)

            except ValueError:
                print("Error: Cantidad debe ser entero y precio decimal.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            try:
                id_producto = input("Ingrese ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
                precio = input("Nuevo precio (dejar vacío si no cambia): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("Error: Valores inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()