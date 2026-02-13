from abc import ABC, abstractmethod

class Evenement(ABC):
    @abstractmethod
    def declencher(self):
        pass