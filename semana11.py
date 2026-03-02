
import json
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

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def to_dict(self):

        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data):

        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"

class Inventario:


    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario {id: Producto}
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Ya existe un producto con ese ID.")
            return

        self.productos[producto.get_id()] = producto
        self.guardar_en_archivo()
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]

            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)

            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)

            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):

        resultados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if resultados:
            print("Productos encontrados:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos.")

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("Lista de productos:")
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self):

        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                json.dump(
                    {id_: p.to_dict() for id_, p in self.productos.items()},
                    file,
                    indent=4
                )
        except PermissionError:
            print("No tienes permisos para escribir el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")

    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):

                with open(self.archivo, "w", encoding="utf-8") as file:
                    json.dump({}, file)
                print("Archivo inventario.json creado.")
                return

            with open(self.archivo, "r", encoding="utf-8") as file:
                data = json.load(file)

                for id_, producto_data in data.items():
                    self.productos[id_] = Producto.from_dict(producto_data)

            print("Inventario cargado correctamente.")

        except FileNotFoundError:
            print("Archivo no encontrado.")
        except json.JSONDecodeError:
            print("Error en el formato del archivo JSON.")
        except PermissionError:
            print("No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f" Error inesperado al cargar: {e}")
def mostrar_menu():
    print("\n SISTEMA DE INVENTARIO ")
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
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            except ValueError:
                print("Cantidad debe ser entero y precio decimal.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            try:
                id_producto = input("ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("Valores inválidos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
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