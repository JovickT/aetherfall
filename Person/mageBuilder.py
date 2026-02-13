from .personBuilder import PersonBuilder
from .personnage import Personnage

class MageBuilder(PersonBuilder):
    def __init__(self): self.reset()
    def reset(self): self.personnage = Personnage()
    
    def set_stats(self):
        self.personnage.classe = "Mage"
        self.personnage.hp = 70
        self.personnage.mana = 200
        
    def set_equipment(self):
        self.personnage.competence.append("Boule de feu")
        self.personnage.competence.append("Bouclier arcanique")