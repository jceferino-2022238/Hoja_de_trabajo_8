class ResultadoBenchmark:
    def __init__(self, nombre_arbol, escenario, iteraciones_promedio):
        self.nombre_arbol = nombre_arbol
        self.escenario = escenario
        self.iteraciones_promedio = iteraciones_promedio

    def __repr__(self):
        return f"{self.nombre_arbol} - {self.escenario}: {self.iteraciones_promedio}"