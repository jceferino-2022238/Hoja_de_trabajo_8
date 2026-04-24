from NodoRedBlack import NodoRedBlack

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, proceso):
        pass

    def search(self, vruntime):
        pass

    def rotate_left(self, nodo):
        pass

    def rotate_right(self, nodo):
        pass

    def fix_insert(self, nodo):
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