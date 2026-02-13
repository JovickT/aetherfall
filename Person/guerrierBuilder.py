from .personBuilder import PersonBuilder
from .personnage import Personnage

class GuerrierBuilder(PersonBuilder):
    def __init__(self): self.reset()
    def reset(self): self.personnage = Personnage()
    
    def set_stats(self):
        self.personnage.classe = "Guerrier"
        self.personnage.hp = 150
        self.personnage.mana = 20
        
    def set_equipment(self):
        self.personnage.competence.append("Coup puissant")
        self.personnage.competence.append("Charge héroïque")