from BST import BST

class SplayTree(BST):

    def rotate_left(self, x):
        y = x.right
        if not y: return
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
        if not y: return
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

    def splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x.parent.left == x:
                    self.rotate_right(x.parent)
                else:
                    self.rotate_left(x.parent)
            else:
                p = x.parent
                g = p.parent

                if p.left == x and g.left == p:
                    self.rotate_right(g)
                    self.rotate_right(p)
                elif p.right == x and g.right == p:
                    self.rotate_left(g)
                    self.rotate_left(p)
                elif p.left == x and g.right == p:
                    self.rotate_right(p)
                    self.rotate_left(g)
                else:
                    self.rotate_left(p)
                    self.rotate_right(g)

    def search(self, vruntime):
        nodo, it = super().search(vruntime)
        if nodo:
            self.splay(nodo)
        return nodo, it