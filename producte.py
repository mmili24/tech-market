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

    def llegir_stock(self):
        return self.__stock

    def vendre(self, stock):
        if self.__stock == 0:
            return f"❌ Error: No hi ha prou stock de a"
        else:
            self.__stock = self.__stock - stock
            return f"✅ Venda realitzada: 1 de 1"