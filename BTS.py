from Nodo import Nodo

class BST:
    def __init__(self):
        self.root = None

    def insert(self, proceso):
        pass

    def search(self, vruntime):
        pass

    def search(self, vruntime):
    actual = self.root
    iteraciones = 0

    while actual is not None:
        iteraciones += 1

        if vruntime == actual.proceso.vruntime:
            return actual, iteraciones
        elif vruntime < actual.proceso.vruntime:
            actual = actual.left
        else:
            actual = actual.right

    return None, iteraciones