from abc import ABC, abstractmethod


class Piece(ABC):

    def __init__(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    @abstractmethod
    def isInCollision(self, piece):
        pass
