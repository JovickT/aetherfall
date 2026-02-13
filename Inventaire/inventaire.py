class Inventaire:
    def __init__(self, max_slot = 10):
        self.max_slot = max_slot
        self.objet = []

    def ajouter(self, objet):
        if len(objet) <= self.max_slot:
            self.objet.append(objet)
        return "Espace inventaire insufisant !"