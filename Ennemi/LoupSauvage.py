from Ennemi.Ennemi import Ennemi

class LoupSauvage(Ennemi):
    def __init__(self):
        super().__init__("Loup Sauvage", "Ennemi Standard", 50, 15)