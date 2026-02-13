from abc import ABC, abstractmethod

class Zone(ABC):
    @abstractmethod
    def generer_evenement(self):
        pass