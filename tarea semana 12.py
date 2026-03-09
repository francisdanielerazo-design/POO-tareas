
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):

        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        return f"Título: {self.obtener_titulo()}, Autor: {self.obtener_autor()}, Categoría: {self.categoria}, ISBN: {self.isbn}"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, isbn):
        self.libros_prestados.append(isbn)

    def devolver_libro(self, isbn):
        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = {}  # Diccionario {ID: Usuario}
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro añadido correctamente")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado")
        else:
            print("ID de usuario ya existe")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if not libro.prestado:
                libro.prestado = True
                usuario.prestar_libro(isbn)
                print("Libro prestado correctamente")
            else:
                print("El libro ya está prestado")
        else:
            print("Libro o usuario no encontrado")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if isbn in usuario.libros_prestados:
                libro.prestado = False
                usuario.devolver_libro(isbn)
                print("Libro devuelto correctamente")
            else:
                print("El usuario no tiene este libro")
        else:
            print("Libro o usuario no encontrado")

    # Buscar libros
    def buscar_libro(self, criterio, valor):
        resultados = []

        for libro in self.libros.values():
            if criterio == "titulo" and libro.obtener_titulo().lower() == valor.lower():
                resultados.append(libro)

            elif criterio == "autor" and libro.obtener_autor().lower() == valor.lower():
                resultados.append(libro)

            elif criterio == "categoria" and libro.categoria.lower() == valor.lower():
                resultados.append(libro)

        return resultados

    # Listar libros prestados a un usuario
    def listar_libros_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado")
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", "111")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "222")

# Añadir libros
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Francis", "U1")
usuario2 = Usuario("Daniel", "U2")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("111", "U1")

# Ver libros prestados
print("Libros prestados a Francis:", biblioteca.listar_libros_usuario("U1"))

# Devolver libro
biblioteca.devolver_libro("111", "U1")

# Buscar libro por título
resultados = biblioteca.buscar_libro("titulo", "El principito")

print("Resultados de búsqueda:")
for libro in resultados:
    print(libro)