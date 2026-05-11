from abc import ABC, abstractmethod
import random

class Jugador(ABC):
    def __init__ (self, nombre):
        self.nombre = nombre
        self.__vida = 100

    def recibir_daño (self,cantidad):
        self.__vida -= cantidad
        print(f"{self.nombre} tiene {self.__vida} puntos de vida")

    def sigue_vivo (self):
        if self.__vida > 0:
            return True
        else:
            print(f"{self.nombre}: Me han derrotado")
            return False

    def daño_random (self,min,max):
        return random.randint(min,max)

    @abstractmethod 
    def atacar (self,enemigo,cantidad):
        pass

class Guerrero(Jugador):
    def grito_batalla(self):
        print(f"{self.nombre}: acabare contigo!!!")

    def atacar(self,enemigo,cantidad):
        enemigo.recibir_daño(cantidad)
        print(f"{self.nombre} ataca a {enemigo.nombre} infligiendole {cantidad} de daño")

class Mago(Jugador):
    def atacar(self,enemigo,cantidad):
        enemigo.recibir_daño(cantidad)
        print(f"¡El mago {self.nombre} lanza una bola de fuego a {enemigo.nombre} por {cantidad} de daño!")

class Arquero(Jugador):
    def atacar(self,enemigo,cantidad):
        enemigo.recibir_daño(cantidad)
        print(f"{self.nombre} ataca a {enemigo.nombre} con una flecha por {cantidad} de daño")

jugador_1 = Guerrero("Aragorn")
jugador_2 = Mago("Gandalf")

## LOGICA DE JUEGO

while jugador_1.sigue_vivo() and jugador_2.sigue_vivo():
    jugador_1.atacar(jugador_2, jugador_1.daño_random(30,50))
    if jugador_2.sigue_vivo():
        jugador_2.atacar(jugador_1, jugador_2.daño_random(30,50))