from Exploration.CombatEvent import CombatEvent
from Exploration.CoffreEvent import CoffreEvent
from Exploration.MarchandEvent import MarchandEvent

class EvenementFactory:
    @staticmethod
    def creer(type_event):
        if type_event == "combat":
            return CombatEvent()
        if type_event == "coffre":
            return CoffreEvent()
        if type_event == "marchant":
            return MarchandEvent()
        raise ValueError("Type d'évènement inconnu")