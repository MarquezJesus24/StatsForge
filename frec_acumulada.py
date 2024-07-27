from frecuencia import Frecuencia

class FrecuenciaAcumulada(Frecuencia):
    def __init__(self, datos):
        super().__init__(datos)
            
    def calcular(self):
        print("Frecuencia")
        #Se guarda la frecuencia que se obitene desde la clase padre Frecuencia en el diccionario frecuencia 
        frecuencia =super().calcular()
        acumulado = 0
        print("Dato   | Frecuencia Absoluta  | Frecuencia Acumulada")
        for dato, frec in frecuencia.items():
            acumulado += frec
            print(f"{dato:<6} | {frec:<20} | {acumulado}")
        