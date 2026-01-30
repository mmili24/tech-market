from producte import Producte

class Smartphone(Producte):
    def __init__(self, nom, preu, stock, camara):
        super().__init__(nom, preu, stock)
        self.camara = camara

   ''' def get_preu_impost(self):
        preu_web_iva = super().get_preu_web

        return preu_web_iva 
    '''
