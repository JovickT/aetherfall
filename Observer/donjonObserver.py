class DonjonObserver:
    "**L'Observateur : le Donjon qui attend la clé**"
    def __init__(self):
        self.est_verrouille = True

    def actualiser(self, objet_nom):
        if objet_nom == "Clé du Donjon":
            self.est_verrouille = False
            print("[EVENT] Le Donjon est désormais accessible !")