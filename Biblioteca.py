import json

class Libro:
    def __init__(self, titulo, autor, año, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año
        self.disponible = True
        self.unidades = unidades

class Biblioteca:
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.libros = []
    def agregar(self, libro):
        self.libros.append(libro)

    def mostrar_libros_disponibles(self):
        for libro in self.libros:
            if libro.disponible:
                print(f"{libro.titulo} ({libro.autor}) - Disponible")
    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f"Se prestó el libro: {libro.titulo}")
                return
        print(f"No se encontró el libro '{titulo}' o no está disponible.")
    def recibir_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                print(f"Se recibió el libro: {libro.titulo}")
                return
        print(f"No se encontró el libro '{titulo}' o ya está disponible.")
    def guardar_en_json(self, archivo):
        json_libros = []
        for libro in self.libros:
            aux = {
                "Titulo": libro.titulo,
                "Autor": libro.autor,
                "Anio": libro.año_publicacion,
                "Disponible": libro.disponible,
                "Unidades": libro.unidades
            }
            json_libros.append(aux)

        with open(archivo, 'w') as archivo_json:
            json.dump(json_libros, archivo_json, ensure_ascii=False, indent=2)
            print(f"Los libros se han guardado en '{archivo}'.")
while True:
    print("Seleccione Opción: ")
    print("1-Agregar Libro: ")
    print("2-Prestar Libro: ")
    print("3-Recibir Libro: ")
    print("4-Salir: ")
    opcion=input("Ingrese Opcion:")
    biblioteca1 = Biblioteca("CIC Mendoza")
    biblioteca2 = Biblioteca("Universidad Tecnologica Nacional")
    if opcion==1:
        l1 = Libro("Python", "Marcela Aguero", 1990, 3)
        l2 = Libro("Java", "Giulius", 1980, 2)
        biblioteca1.agregar(l1)
        biblioteca2.agregar(l2)
      
    elif opcion==2:
        biblioteca1.prestar_libro("Python")
        
    elif opcion==3:
        biblioteca2.recibir_libro("Python")
    elif opcion==4: 
        break

    biblioteca1.guardar_en_json("biblioteca1.json")
    biblioteca2.guardar_en_json("biblioteca2.json")


