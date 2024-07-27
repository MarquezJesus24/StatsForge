from cuartil import Cuartil

class Rango_Intercuartilico:
    def __init__(self,datos ) :
        self.datos=datos
        self.cuartil=Cuartil(self.datos)

    def calcular_IQ(self):
        cuartil_uno=self.cuartil.calcularCuartil("1")
        print("Primer cuartil: "+ str(cuartil_uno))
        cuartil_tres=self.cuartil.calcularCuartil("3")
        print("Tercer cuartil: "+ str(cuartil_tres))
        IQ=cuartil_tres-cuartil_uno
        print("Rango Intercuartilico: " + str(IQ))
        
        return IQ