class InventaireSujet:
    "**Le Sujet : l'inventaire que l'on surveille**"
    def __init__(self):
        self._observateurs = []
        self._objets = []

    def attacher(self, observateur):
        self._observateurs.append(observateur)

    def notifier(self, objet_nom):
        for obs in self._observateurs:
            obs.actualiser(objet_nom)

    def ajouter_objet(self, nom):
        self._objets.append(nom)
        print(f"Objet trouvé : {nom}")
        self.notifier(nom)

