from logic.entidades import Medico, Cita, Paciente
from logic.gestor_clinica import GestorClinica

def gestionar_agenda():
    clinica = GestorClinica()
    
    while True:
        print("\n--- Agenda Médica ---")
        print("1. Registrar Cita")
        print("2. Mostrar Agenda de Paciente")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            id_paciente = input("ID del paciente: ")
            
            # Si el paciente no existe, se crea
            if id_paciente not in clinica.diccionario_pacientes:
                nombre_paciente = input("Nombre del paciente nuevo: ")
                nuevo_paciente = Paciente(nombre_paciente, id_paciente)
                clinica.registrar_paciente(nuevo_paciente)
            
            nombre_medico = input("Nombre del médico: ")
            especialidad = input("Especialidad del médico: ")
            id_medico = input("ID del médico: ")
            medico = Medico(nombre_medico, especialidad, id_medico)
            
            fecha = input("Fecha de la cita (DD/MM/AAAA): ")
            hora = input("Hora de la cita (HH:MM): ")
            cita = Cita(fecha, hora, medico)
            
            exito = clinica.programar_cita(id_paciente, cita)
            if exito:
                print("Cita programada exitosamente.")
            else:
                print("Error: El paciente ya tiene el máximo de 3 citas.")
                
        elif opcion == "2":
            id_paciente = input("ID del paciente para ver su agenda: ")
            if id_paciente in clinica.diccionario_pacientes:
                paciente = clinica.diccionario_pacientes[id_paciente]
                print(f"\nCitas de {paciente.nombre_paciente}:")
                for cita in paciente.lista_citas:
                    print(f"- {cita.fecha} a las {cita.hora} con Dr. {cita.objeto_medico.nombre_medico} ({cita.objeto_medico.especialidad})")
            else:
                print("Paciente no encontrado.")
                
        elif opcion == "3":
            break