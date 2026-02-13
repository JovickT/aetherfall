from abc import ABC, abstractmethod

class Observateur(ABC):
    @abstractmethod
    def actualiser(self, objet_nom):
        pass