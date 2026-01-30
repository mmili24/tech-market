'''## La base del catàleg

Una web no pot mostrar productes si no tenen una estructura definida. 
Hem de crear una "plantilla" de qualsevol producte que es vengui a la nostra web.

Per poder instanciar un producte necessitarem el nom, el preu i l'stock del mateix.
Necessitem per la seguretat del nostre e-commerce que el preu estigui encapsulat, 
tot pensant en que cap programador junior que toqui el nostre codi pugui accedir-hi
i introduir un preu negatiu per error.

A la web mostrarem el preu dels productes, però hem de tenir en compte he quan ho 
mostrem ho hem de fer amb l'IVA (21%) aplicat.

Si al vendre un producte no hi ha prou stock, s'ha de llançar un error o avisar 
del mateix.'''



# if stock < 0 
# return f"Stock no disponible"




'''class Smartphone(Producte):
    def __init__(self, camara, bateria):
        self.camara = camara
        self.bateria = bateria
    super().__init_


class CarretCompra:

