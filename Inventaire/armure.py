from .objet import Objet
class Armure(Objet):
    def __init__(self):
        super().__init__(self.nom)
        super().__init__(self.int_bonus)
        super().__init__(self.def_bonus)
        