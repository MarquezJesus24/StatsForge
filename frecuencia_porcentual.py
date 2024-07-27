from frecuencia import Frecuencia
from intervalos_frecuencia import DistribucionFrecuenciaIntervalos

# Esta clase calcula la frecuencia porcentual y la frecuencia porcentual acumulada de los datos.
class FrecuenciaPorcentual(Frecuencia):
    def __init__(self, datos):
        # Llama al constructor de la clase padre (Frecuencia)
        super().__init__(datos)
        # Almacena la cantidad total de datos
        self.intervalos_frecuencia=DistribucionFrecuenciaIntervalos(datos)
        
    def calcular(self):
        # Calcula la frecuencia  utilizando el método de la clase padre
        frecuencia=super().calcular()
        # Crea un diccionario con la frecuencia porcentual para cada dato
        return {dato:(frec/self.n)*100 for dato, frec in frecuencia.items()}
    
    def calcular_acumulada_porcentual(self):#Total porcentual
        # Calcula la frecuencia porcentual
        frecuencia_porcentual=self.calcular()
        # Imprime cada dato y su frecuencia porcentual
        acumulado=0
        print("Dato   | Frecuencia %  | Frecuencia %  Acumulada")
        for dato, porcentaje in frecuencia_porcentual.items():
            acumulado+=porcentaje
            print(f"{dato:<6} | {porcentaje:<6.3f}% | {acumulado:<6.3f}")
    
    def calcular_Porcentual_Intervalos(self,num_intervalos):
        # Calcula la frecuencia  utilizando el método de la clase padre
        frecuencia=self.intervalos_frecuencia.calcular(num_intervalos)
        # Crea un diccionario con la frecuencia porcentual para cada dato
        return {dato:(frec/self.n)*100 for dato, frec in frecuencia.items()}
    
    def calcular_Acumulada_Porcentual_Intervalos(self,num_intervalo):#Total porcentual
        # Calcula la frecuencia porcentual
        frecuencia_porcentual=self.calcular_Porcentual_Intervalos(num_intervalo)
        print("------------------------------------------------")
        # Imprime cada dato y su frecuencia porcentual
        acumulado=0
        print("Datos        | Frecuencia %  | Frecuencia %  Acumulada")
        for intervalo, porcentaje in frecuencia_porcentual.items():
            acumulado+=porcentaje
            print(f"{str(intervalo):<6} | {porcentaje:<12.3f}% | {acumulado:<6.3f}")