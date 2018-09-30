from abc import ABC, abstractmethod


class QueensResolver(ABC):

    @abstractmethod
    def findSolutions(self, pieces):
        pass
    
    