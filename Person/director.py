class Directeur:
    def __init__(self):
        self._builder = None

    @property
    def builder(self): return self._builder

    @builder.setter
    def builder(self, builder): self._builder = builder

    def construire_personnage_complet(self):
        self.builder.set_stats()
        self.builder.set_equipment()