from Proceso import Proceso

class Nodo:
    def __init__(self, proceso: Proceso):
        self.proceso = proceso
        self.left = None
        self.right = None
        self.parent = None