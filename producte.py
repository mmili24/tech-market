from abc import ABC, abstractmethod

class Producte(ABC):
    def __init__(self, nom, preu, stock):
        self.nom = nom
        self.__preu = preu
        self.__stock = stock

    def llegir_preu(self):
        return self.__preu

    def get_preu_web(self):
        preu_web = self.__preu * 1.21
        return preu_web