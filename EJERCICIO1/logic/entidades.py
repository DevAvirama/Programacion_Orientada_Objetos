class Persona:
    def __init__(self,nombre:str,apellido:str,edad:int,peso:float,altura:float):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso
        self.altura = altura
    
    def calcularIMC(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    
    def obtener_estado(self): 
        if self.calcularIMC() < 18.5:
            return "Bajo peso"
        elif self.calcularIMC() >= 18.5 and self.calcularIMC() < 25:
            return "Peso normal"
        elif self.calcularIMC() >= 25 and self.calcularIMC() < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"