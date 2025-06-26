# base de datos en memoria
libros = []
socios = []
axiContador = 0

def mostrar_menu():
    '''Muestra las opciones del menu'''
    print("📚 MINIBIBLIOTECA")
    print("1. Registrar libro")
    print("2. Registrar socio")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Ver libros prestados")
    print("6. Ver todos los libros")
    print("7. Ver todos los socios")
    print("0. Salir")

def registrar_libro():
    global libros
    
    print("============================================")
    print("Registrar Libros 📘")
    print("============================================")
    print("Digite 0 si quiere cancelar la creación")
    
    
    titulo = input("Titulo del libro: ").strip().lower()  # convierte a minusculas y elimina espacios en blanco
    
    if titulo == '0':
        print("📚 Registro de libro cancelado. 📚")
        return
    
    if not titulo:
        print("❌ El título no puede estar vacío. ❌")
        return
        #registrar_libro() si deseo verificar el titulo
        
    autor = input("Autor del libro: ").strip().lower()
    
    if not autor:
        print("❌ El autor no puede estar vacío. ❌")
        return
    
    isbn = input("ISBN del libro: ").strip().lower()
    
    if not isbn:
        print("❌ El ISBN no puede estar vacío. ❌")
        return
    
    for libro in libros:
        if libro['isbn'] == isbn:
            print("❌ Ya existe un libro con el ISBN ❌")
            return
    
    #crear el nuevo libro
    nuevo_libro = {
        'isbn': isbn,
        'titulo': titulo,
        'autor': autor,
        'estado': 'disponible',  # Estado del libro: disponible, prestado, reservado
        'socio_prestado': None  # Socio al que se le ha prestado el libro
    }
    
    libros.append(nuevo_libro)
    print("✅ Libro Registrado Exitosamente. 📘")
    print(f"📘 Título: {titulo} - Autor: {autor}")
    print(f"ISBN: {isbn}")
    print("============================================")
    

def registrar_socio():
    pass

def prestar_libro():
    pass

def devolver_libro():
    pass

def ver_libro_prestado():
    pass

def ver_todos_libros():
    print("============================================")
    print("Mostrando todos los libros")
    print("============================================")
    
    if not libros:
        print("No hay libros registrados en la biblioteca")
        return
    
    for i, libro in enumerate(libros, 1):
        print(f"{1}. nombre del libro: {libro["titulo"]}")
        print(f"     Autor: {libro["autor"]}")
        print(f"     ISBN: {libro["isbn"]}")
        print(f"     Estado: {libro["estado"]}")    
    
def ver_todo_socios():
    pass
    
def main():
    '''Función principal del programa'''
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-7): ").strip() #elimina espacios en blanco
        '''
        opcion de condicional 
        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        '''
        match opcion:
            case '1':
                registrar_libro()
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':           
                ver_todos_libros()
            case '7':
                pass
            case '0':   
                print("📚Gracias por usar MiniBiblio! ... 📚")
                print("📚 Hasta Luego")
                break
            case _:
                print("Opción no válida. Por favor selecciones una opcion del 0 - 7.")       
                
                
if __name__ == "__main__":
    main()
    