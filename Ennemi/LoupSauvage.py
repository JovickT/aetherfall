from Ennemi.Ennemi import Ennemi

class LoupSauvage(Ennemi):
    def __init__(self):
        super().__init__("Loup Sauvage", "Ennemi Standard", 50, 15)

    def attaquer(self):
        return f"{LoupSauvage(Ennemi).nom} Attaque multiple ! (Dégâts: {LoupSauvage(Ennemi).atq})"
    
    def recevoir_degat(self, degat):
        self.hp -= degat
        print(f"Le Loup Sauvage a reçu {degat} dégâts. PV: {self.hp}")