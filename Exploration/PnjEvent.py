from Exploration.Evenement import Evenement

class PnjEvent(Evenement):
    def declencher(self):
        print("PNJ : 'Veux-tu aller en forêt ?'")
        choix = input("(oui/non) : ")

        if choix == "oui":
            return True
        else: 
            return False