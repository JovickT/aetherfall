from abc import ABC, abstractmethod

class PersonBuilder(ABC):
    @abstractmethod
    def reset(self): pass
    
    @abstractmethod
    def set_stats(self): pass
    
    @abstractmethod
    def set_equipment(self): pass
