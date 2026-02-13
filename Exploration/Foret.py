from Exploration.Zone import Zone
from Exploration.CombatEvent import CombatEvent

class Foret(Zone):
    def generer_evenement(self):
        return CombatEvent()
    
# CoffreEvent() à rajouter plus tard