from Ennemi.Ennemi import Ennemi

class Bandit(Ennemi):
    def __init__(self):
        super().__init__("Bandit", "Ennemi Standard", 50, 15)

    def attaquer(self):
        return f"{Bandit(Ennemi).nom} Attaque vol d'objet ! (Dégâts: {Bandit(Ennemi).atq})"
    
    def recevoir_degat(self, degat):
        self.hp -= degat
        print(f"Le Bandit a reçu {degat} dégâts. PV: {self.hp}")