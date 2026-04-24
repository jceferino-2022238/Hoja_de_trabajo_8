from Nodo import Nodo

class NodoRedBlack(Nodo):
    def __init__(self, proceso):
        super().__init__(proceso)
        self.color = "RED"
        