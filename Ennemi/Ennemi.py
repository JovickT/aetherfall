from abc import ABC, abstractmethod

class Ennemi(ABC):
    def __init__(self, nom, level, hp, atq):
        self.nom = nom
        self.level = level
        self.hp = hp
        self.atq = atq

    @abstractmethod
    def attaquer(self):
        pass