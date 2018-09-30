from abc import ABC, abstractmethod


class QueensResolver(ABC):

    @abstractmethod
    def resolve(self, rows, columns):
        pass
    
    