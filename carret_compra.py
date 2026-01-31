'''## El carret de Compra
L'usuari navega per la web i va afegint coses al carret. 
Necessitem una classe que gestioni una llista d'objectes heterogenis 
(barreja de mòbils i portàtils).
Hem de crear una classe carret compra que pugui afegir productes i 
ens permeti poder mostrar el total a pagar.'''

from producte import Producte
from portatil import Portatil
from smartphone import Smartphone

class CarretCompra:
  def __init__(self):
      self.lista_productes = []

  def afegir(self, producte):
      self.lista_productes.append(producte)

  '''def checkout(self):
      total = 0
      for producte in self.lista_productes:
          total = total + producte.get_preu_web()
      return f"\n--- TIQUET DE COMPRA ---\n- #y mas cosas aqui'''