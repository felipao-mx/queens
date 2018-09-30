from abc import ABC, abstractmethod


class Position(ABC):
    def __init__(self, vector=None):
        if vector is None:
            self.vector = []
        else:
            self.vector = vector

    def getVector(self):
        return self.vector

    @abstractmethod
    def setVector(self, vector):
        pass
