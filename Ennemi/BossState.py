from abc import ABC, abstractmethod

class BossState(ABC):
    @abstractmethod
    def attaquer(self):
        pass
