from NodoRedBlack import NodoRedBlack

class RedBlackTree:
    def __init__(self):
        self.root = None

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def insert(self, proceso):
        nodo = NodoRedBlack(proceso)

        if not self.root:
            nodo.color = "BLACK"
            self.root = nodo
            return

        actual = self.root
        while True:
            if proceso.vruntime < actual.proceso.vruntime:
                if not actual.left:
                    actual.left = nodo
                    break
                actual = actual.left
            else:
                if not actual.right:
                    actual.right = nodo
                    break
                actual = actual.right

        nodo.parent = actual
        self.fix_insert(nodo)

    def fix_insert(self, k):
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right

                if u and u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left

                if u and u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.rotate_left(k.parent.parent)

        self.root.color = "BLACK"

    def search(self, vruntime):
        actual = self.root
        it = 0

        while actual:
            it += 1
            if vruntime == actual.proceso.vruntime:
                return actual, it
            elif vruntime < actual.proceso.vruntime:
                actual = actual.left
            else:
                actual = actual.right

        return None, it