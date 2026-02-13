from Exploration.Zone import Zone
from Exploration.EvenementFactory import EvenementFactory
from Exploration.PnjEvent import PnjEvent

class Village(Zone):
    def __init__(self):
        self.quete_active = False

    def generer_evenement(self):
        if self.quete_active != True:
            return PnjEvent()
        
# MarchantEvent() à rajouter plus tard