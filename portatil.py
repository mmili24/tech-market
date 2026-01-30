from producte import Producte

class Portatil(Producte):
    def __init__(self, ram, cpu):
        super().__init__(nom, preu, stock)
        self.ram = ram
        self.cpu = cpu

    def __str__(self):
        return f"PORTÀTIL:{self.nom} | ramGB {self.ram} | {self.cpu}"