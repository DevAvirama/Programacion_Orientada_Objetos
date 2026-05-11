class GestorClinica:
    def __init__(self):
        self.diccionario_pacientes = {}

    def programar_cita(self, id_paciente:int, objeto_cita:str):
        if id_paciente in self.diccionario_pacientes:
            paciente = self.diccionario_pacientes[id_paciente]
            resultado = paciente.agregar_cita(objeto_cita)
            return resultado
        else:
            return "Error, el paciente no esta registrado en el sistema."

    
        
