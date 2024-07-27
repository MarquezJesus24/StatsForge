from frecuencia import Frecuencia
from intervalos_frecuencia import DistribucionFrecuenciaIntervalos
# Esta clase calcula la frecuencia relativa y la frecuencia relativa acumulada de los datos.

class FrecuenciaRelativa (Frecuencia):
    def __init__(self, datos):
        # Llama al constructor de la clase padre (Frecuencia)
        super().__init__(datos)
        self.intervalos=DistribucionFrecuenciaIntervalos(datos)
        # Almacena la cantidad total de datos 
        # self.n=len(datos.datos)
        
    def calcular(self):
        # Calcula la frecuencia absoluta utilizando el método de la clase padre
        frecuencia=super().calcular()
        # Crea un diccionario con la frecuencia relativa para cada dato
        return {dato:(frec/self.n) for dato, frec in frecuencia.items()}

    def calcular_acumulada_relativa(self):
        # Calcula la frecuencia relativa
        frecuencia_relativa=self.calcular()
        # Imprime cada dato y su frecuencia relativa
        acumulado=0
        print("Dato   | Relativa  | Relativa  Acumulada")
        for dato, relativa in frecuencia_relativa.items():
            acumulado+=relativa
            print(f"{dato:<6}| {relativa:<6.4f} | {acumulado:<6.4f}")    
    

    def calcular_Relativa_Intervalos(self,num_intervalos):
        # Calcula la frecuencia absoluta utilizando el método de la clase padre
        frecuencia=self.intervalos.calcular(num_intervalos)
        # Crea un diccionario con la frecuencia relativa para cada dato
        return {intervalo:(frec/self.n) for intervalo, frec in frecuencia.items()}
    
    def calcular_acumulada_relativa_en_intervalos(self,num_intervalos):
        # Calcula la frecuencia relativa
        frecuencia_relativa=self.calcular_Relativa_Intervalos(num_intervalos)
        print("------------------------------------------------")
        # Imprime cada dato y su frecuencia relativa
        acumulado=0
        print("Dato        | Relativa  | Relativa  Acumulada")
        for dato, relativa in frecuencia_relativa.items():
            acumulado+=relativa
            print(f"{str(dato):<6}| {relativa:<9.4f} | {acumulado:<6.4f}")
