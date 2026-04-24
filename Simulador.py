import random
import matplotlib.pyplot as plt
from graphviz import Digraph

from Proceso import Proceso
from BST import BST
from SplayTree import SplayTree
from RedBlackTree import RedBlackTree


class Simulador:

    def generar_procesos(self, n):
        return [Proceso(i, random.random()) for i in range(n)]

    def graficar(self, root, nombre):
        dot = Digraph()

        def recorrer(n):
            if not n: return
            dot.node(str(id(n)), str(round(n.proceso.vruntime, 3)))
            if n.left:
                dot.edge(str(id(n)), str(id(n.left)))
                recorrer(n.left)
            if n.right:
                dot.edge(str(id(n)), str(id(n.right)))
                recorrer(n.right)

        recorrer(root)
        dot.render(nombre, format="png", cleanup=True)

    def escenarioA(self):
        procesos = self.generar_procesos(1000)

        bst = BST()
        splay = SplayTree()
        rbt = RedBlackTree()

        for p in procesos:
            bst.insert(p)
            splay.insert(p)
            rbt.insert(p)

        try:
            self.graficar(bst.root, "bst_aleatorio")
        except:
            print("Graphviz no instalado, se omite la gráfica del árbol")

        resultados = {"BST": [], "SPLAY": [], "RBT": []}

        for p in random.sample(procesos, 100):
            resultados["BST"].append(bst.search(p.vruntime)[1])
            resultados["SPLAY"].append(splay.search(p.vruntime)[1])
            resultados["RBT"].append(rbt.search(p.vruntime)[1])

        for k in resultados:
            print(k, "promedio:", sum(resultados[k]) / 100)

        plt.figure()
        plt.plot(resultados["BST"])
        plt.plot(resultados["SPLAY"])
        plt.plot(resultados["RBT"])
        plt.title("Escenario A")
        plt.savefig("escenarioA.png")

    def escenarioB(self):
        procesos = [Proceso(i, i) for i in range(1000)]

        bst = BST()
        splay = SplayTree()
        rbt = RedBlackTree()

        for p in procesos:
            bst.insert(p)
            splay.insert(p)
            rbt.insert(p)
        try:
            self.graficar(bst.root, "bst_secuencial")
        except:
            print("Graphviz no instalado, se omite la gráfica del árbol")
        print("BST:", bst.search(999)[1])
        print("SPLAY:", splay.search(999)[1])
        print("RBT:", rbt.search(999)[1])

    def escenarioC(self):
        procesos = self.generar_procesos(1000)

        splay = SplayTree()
        rbt = RedBlackTree()

        for p in procesos:
            splay.insert(p)
            rbt.insert(p)

        objetivo = procesos[500]

        splay_it = []
        rbt_it = []

        for _ in range(50):
            splay_it.append(splay.search(objetivo.vruntime)[1])
            rbt_it.append(rbt.search(objetivo.vruntime)[1])

        print("Splay promedio:", sum(splay_it)/50)
        print("RBT promedio:", sum(rbt_it)/50)

        plt.figure()
        plt.plot(splay_it)
        plt.plot(rbt_it)
        plt.title("Escenario C")
        plt.savefig("escenarioC.png")