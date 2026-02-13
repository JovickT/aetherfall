from Ennemi.Ennemi import Ennemi
from Ennemi.Phase1 import Phase1
from Ennemi.Phase2 import Phase2

class GardienDonjon(Ennemi):
    def __init__(self):
        super().__init__("Gardien du Donjon", "Boss Final", 500, 30)
        self.max_hp = 500
        self.etat = Phase1()

    def changer_etat(self, nouvel_etat):
        self.nouvel_etat = nouvel_etat
    
    def recevoir_degat(self, degat):
        self.hp -= degat
        print(f"Le Gardien du Donjon a reçu {degat} dégâts. PV: {self.hp}")
        if self.hp <= self.max_hp / 2 :
            print("LE GARDIEN S'ENRAGE !!!")
            self.changer_etat(Phase2())

    def attaquer(self):
        print(self.etat.attaquer())

