from Person.director import Directeur
from Person.mageBuilder import MageBuilder
def main():
   # Initialisation
    directeur = Directeur()
    mage_builder = MageBuilder()

    # Fabrication d'un Mage
    directeur.builder = mage_builder
    directeur.construire_personnage_complet()
    mon_mage = mage_builder.personnage

    print(mon_mage)


if __name__ == "__main__":
    main()