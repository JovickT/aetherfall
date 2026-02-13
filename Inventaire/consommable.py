from .objet import Objet
class Consommable(Objet):
    def __init__(self,poison = None):
        super.__init__(self.nom)
        super.__init__(self.pv_bonus)
        super.__init__(self.atq_bonus)
        super.__init__(self.poison)

        