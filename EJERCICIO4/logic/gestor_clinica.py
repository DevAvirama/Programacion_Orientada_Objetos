class GestorClinica:
    def __init__(self):
        self.diccionario_pacientes = {}

    def registrar_paciente(self, paciente):
        self.diccionario_pacientes[paciente.id_paciente] = paciente

    def programar_cita(self, id_paciente, objeto_cita):
        if id_paciente in self.diccionario_pacientes:
            paciente = self.diccionario_pacientes[id_paciente]
            return paciente.agregar_cita(objeto_cita)
        return False