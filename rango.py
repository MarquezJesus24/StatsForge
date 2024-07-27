class Rango:
    def __init__(self, datos) :
        self.datos=datos
    
    def calcularRango(self):
        valor_max=self.datos.datos[-1]
        valor_min=self.datos.datos[0]
        
        rango=valor_max-valor_min
        print("Rango: " + str(rango))
        return rango