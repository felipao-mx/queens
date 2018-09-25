from abc import ABC, abstractmethod


class Position(ABC):
    def __init__(self):
        self.vector = []

    def getVector(self):
        return self.vector

    @abstractmethod
    def setVector(self, vector):
        pass