from logic.entidades import Persona
from logic.logica import lista_personas, buscar_paciente, actualizar_datos

def registrar_paciente (): 
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    peso = float(input("Ingrese el peso del paciente: "))
    altura = float(input("Ingrese la altura del paciente: "))
    
    paciente = Persona(nombre,apellido,edad,peso,altura)
    lista_personas.append(paciente)
    return print("Paciente agregado correctamente")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Paciente")
        print("2. Ver lista de pacientes")
        print("3. Actualizar Datos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            if not lista_personas:
                print("No hay pacientes registrados.")
            for paciente in lista_personas:
                print(f"Nombre: {paciente.nombre}")
                print(f"Apellido: {paciente.apellido}")
                print(f"Edad: {paciente.edad}")
                print(f"Peso: {paciente.peso} kg")
                print(f"Altura: {paciente.altura} m")
                print(f"IMC: {paciente.calcularIMC():.2f}")
                print(f"Estado: {paciente.obtener_estado()}")
                print("-" * 25)
        elif opcion == "3":
            apellido = input("Ingrese el apellido del paciente: ")
            if buscar_paciente(apellido):
                nuevo_peso = float(input("Ingrese el nuevo peso: "))
                nuevo_altura = float(input("Ingrese la nueva altura: "))
                actualizar_datos(apellido,nuevo_peso,nuevo_altura)
            else:
                print("Paciente no encontrado")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")