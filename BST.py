from Nodo import Nodo

class BST:
    def __init__(self):
        self.root = None

    def insert(self, proceso):
        nuevo = Nodo(proceso)

        if self.root is None:
            self.root = nuevo
            return

        actual = self.root
        while True:
            if proceso.vruntime < actual.proceso.vruntime:
                if actual.left is None:
                    actual.left = nuevo
                    nuevo.parent = actual
                    return
                actual = actual.left
            else:
                if actual.right is None:
                    actual.right = nuevo
                    nuevo.parent = actual
                    return
                actual = actual.right

    def search(self, vruntime):
        actual = self.root
        iteraciones = 0

        while actual:
            iteraciones += 1

            if vruntime == actual.proceso.vruntime:
                return actual, iteraciones
            elif vruntime < actual.proceso.vruntime:
                actual = actual.left
            else:
                actual = actual.right

        return None, iteraciones