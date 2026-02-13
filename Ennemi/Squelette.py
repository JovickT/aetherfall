from Ennemi.Ennemi import Ennemi

class Squelette(Ennemi):
    def __init__(self):
        super().__init__("Squelette", "Ennemi Standard", 50, 15)

    def attaquer(self):
        return f"{Squelette(Ennemi).nom} Attaque multiple ! (Dégâts: {Squelette(Ennemi).atq})"
    
    def recevoir_degat(self, degat):
        self.hp -= degat
        print(f"Le Squelette a reçu {degat} dégâts. PV: {self.hp}")