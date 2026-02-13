from Ennemi.Ennemi import Ennemi

class Bandit(Ennemi):
    def __init__(self):
        super().__init__("Bandit", "Ennemi Standard", 50, 15)