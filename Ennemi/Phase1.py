from Ennemi.BossState import BossState
from Ennemi.Ennemi import Ennemi
from Ennemi.GardienDonjon import GardienDonjon

class Phase1(BossState):
    def attaquer(self):
        return f"{GardienDonjon(Ennemi).nom} [Phase 1] Attaque Puissante ! (Dégâts: {GardienDonjon(Ennemi).atq})"