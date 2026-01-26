class GestorArchivo:
    def __init__(self, nombre_archivo):
        """
        Constructor:
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        """
        if not self.archivo.closed:
            self.archivo.write(texto + "\n")
        else:
            print("No se puede escribir, el archivo está cerrado.")

    def __del__(self):
        """
        Destructor:
        """
        if hasattr(self, 'archivo') and not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")
        else:
            print("El archivo ya estaba cerrado o no existe.")

# Programa principal

def main():
    gestor = GestorArchivo("ejemplo.txt")
    gestor.escribir("Hola, este es un ejemplo de constructor y destructor.")
    gestor.escribir("Python maneja recursos automáticamente.")

    # Eliminamos el objeto manualmente para forzar la ejecución del destructor

if __name__ == "__main__":
    main()
