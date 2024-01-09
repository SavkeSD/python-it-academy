### Javlja se kada se nesto promeni, pa svi observeri da se obaveste ###

from abc import ABC, abstractmethod  
 
 
class ShopOnserver(ABC):  
 
    @abstractmethod  
    def update(self, pen):  
        pass  
    