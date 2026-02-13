from Inventaire.inventaire import Inventaire
class Personnage:
    def __init__(self):
        self.classe = None
        self.hp = 0
        self.mana = 0
        self.competence = []
        self.inventaire = Inventaire()

    def __str__(self):
        return f"[{self.classe}] HP: {self.hp}, Mana: {self.mana}, Skill: {self.competence}, Inventaire: {self.inventaire}"