from .entidades import Persona

lista_personas = []

def agragar_paciente(persona):
    lista_personas.append(persona)
    print("Paciente agregado correctamente")

def buscar_paciente(apellido):
    for persona in lista_personas:
        if persona.apellido == apellido:
            return persona
    return None

def actualizar_datos(apellido, nuevo_peso, nuevo_altura):
    persona = buscar_paciente(apellido)
    if persona:
        persona.peso = nuevo_peso
        persona.altura = nuevo_altura
        print("Datos actualizados correctamente")
    else:
        print("Paciente no encontrado")