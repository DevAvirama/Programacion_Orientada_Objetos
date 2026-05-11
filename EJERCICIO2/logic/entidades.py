class Medico:
    def __init__(self, nombre:str,especialidad:str,id_medico:int):
        self.nombre = nombre
        self.especialidad = especialidad
        self.id_medico = id_medico

class Cita:
    def __init__(self, fecha:str,hora:str, medico):
        self.fecha = fecha
        self.hora = hora
        self.medico = medico

class Paciente:
    def __init__(self, nombre:str, id_paciente:int):
        self.nombre = nombre
        self.id_paciente = id_paciente
        self.lista_citas = []

    def agregar_cita(self, nueva_cita):
        if len(self.lista_citas) < 3:
            self.lista_citas.append(nueva_cita)
            return True
        else:
            return False
