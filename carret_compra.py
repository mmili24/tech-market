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
          
  def checkout(self):
      result = f"\n--- TIQUET DE COMPRA ---\n"
      total = 0
      for producte in self.lista_productes:
          total = total + producte.llegir_preu()
          result = result + f"- {producte.nom}: {producte.llegir_preu()}€\n"    
      result = result + f"------------------------\nTOTAL A PAGAR: {total}€"
      return result