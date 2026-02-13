from Ennemi.BossState import BossState
from Ennemi.Ennemi import Ennemi
from Ennemi.GardienDonjon import GardienDonjon

class Phase2(BossState):
    def attaquer(self):
        atqDevastatrice = GardienDonjon(Ennemi).atq * 1.5
        return f"{GardienDonjon(Ennemi).nom} [Phase 2] Attaque Dévastatrice ! (Dégâts: {atqDevastatrice})"