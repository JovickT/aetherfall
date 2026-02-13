
class Game:
    def __init__(self):
   
        self.hero = Explorateur()
        self.inventaire = InventaireObserver()
        
        
        self.porte = PorteDonjon()
        self.inventaire.attacher(self.porte)
        
        self.en_cours = True

    def lancer_jeu(self):
        print("=== BIENVENUE DANS L'AVENTURE ===")
        while self.en_cours:
            print("\nQue voulez-vous faire ?")
            choix = input("1. Se déplacer | 2. Voir Inventaire | 3. Quitter : ")
            
            if choix == "1":
                self.tour_d_exploration()
            elif choix == "2":
                print(f"Sacs : {self.inventaire._objets}")
            elif choix == "3":
                self.en_cours = False

    def tour_d_exploration(self):
        
        self.hero.se_deplacer()
        
       
        if self.porte.debloque and isinstance(self.hero.zone_actuelle, ForetStrategy):
            print(" Un portail s'ouvre vers le Donjon !")
            self.hero.changer_zone(DonjonStrategy())