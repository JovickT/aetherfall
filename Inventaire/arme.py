from .objet import Objet

class Arme(Objet):
    def __init__(self):
        super.__init__(self.nom)
        super.__init__(self.atq_bonus)
        super.__init__(self.int_bonus)