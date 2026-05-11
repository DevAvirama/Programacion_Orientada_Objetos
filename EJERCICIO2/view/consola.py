from logic.entidades import Medico, Cita, Paciente
from logic.gestor_clinica import GestorClinica

gestor = GestorClinica()

def registrar_cita():
    print("--- Registro de Cita ---")
    id_paciente = input("Ingrese el ID del paciente: ")
    
    if id_paciente not in gestor.diccionario_pacientes:
        nombre_p = input("Paciente nuevo. Ingrese el nombre: ")
        nuevo_paciente = Paciente(nombre_p, id_paciente)
        gestor.diccionario_pacientes[id_paciente] = nuevo_paciente
        print("✅ Paciente registrado en el sistema.")

    print("Datos del Médico:")
    nombre_m = input("Nombre: ")
    especialidad = input("Especialidad: ")
    id_m = input("ID Médico: ")
    obj_medico = Medico(nombre_m, especialidad, id_m)

    fecha = input("Fecha (DD/MM/AAAA): ")
    hora = input("Hora (HH:MM): ")
    
    nueva_cita = Cita(fecha, hora, obj_medico)

    resultado = gestor.programar_cita(id_paciente, nueva_cita)
    
    if resultado == True:
        print("🎉 ¡Cita registrada exitosamente!")
    elif resultado == False:
        print("❌ Error: El paciente ya tiene el máximo de 3 citas.")
    else:
        print(f"{resultado}")

def mostrar_agenda():
    print("--- Consultar Agenda ---")
    id_paciente = input("Ingrese el ID del paciente: ")

    if id_paciente in gestor.diccionario_pacientes:
        paciente = gestor.diccionario_pacientes[id_paciente]
        print(f"Agenda de: {paciente.nombre}")
        
        if not paciente.lista_citas:
            print("No tiene citas programadas.")
        
        for cita in paciente.lista_citas:
            print(f"- {cita.fecha} a las {cita.hora} con el Dr(a). {cita.medico.nombre} ({cita.medico.especialidad})")
    else:
        print("El paciente no existe en el sistema.")

def menu_principal():
    while True:
        print("==== SISTEMA CLÍNICO ====")
        print("1. Registrar cita")
        print("2. Mostrar agenda")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cita()
        elif opcion == "2":
            mostrar_agenda()
        elif opcion == "3":
            print("Saliendo del sistema... ¡Adiós!")
            break
        else:
            print("Opción no válida.")
