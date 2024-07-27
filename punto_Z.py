from desviacionEstandar import Desviacion_Estandar
from frecuencia import Frecuencia
class Punto_Z:
    def __init__(self, datos,varianza,media) :
        # Inicializa los atributos de la clase con los datos, varianza y media recibidos
        self.datos=datos
        self.varianza=varianza
        self.media=media
        # Crea una instancia de la clase Frecuencia con los datos recibidos
        self.frecuencia=Frecuencia(datos)
        # Crea una instancia de la clase Desviacion_Estandar con la varianza recibida
        self.desviacion_estandar=Desviacion_Estandar(varianza)
    
    def calcular_Punto_Z(self,punto):
        # Calcula la desviación estándar muestral utilizando el método de la clase Desviacion_Estandar
        desviacion=self.desviacion_estandar.calcular_Desviacion_Estandar_Muestral()
        # Calcula la media utilizando el método de la clase asociada a self.media
        media=float(self.media.calcular_Media())
        # Calcula las frecuencias utilizando el método de la clase Frecuencia
        frecuencia=self.frecuencia.calcular()
        try:
            if punto in frecuencia:
                # Si el punto existe en las frecuencias, calcula el punto Z
                    punto_z=(punto-media)/desviacion
            else:
                # Si el punto no existe en las frecuencias, lanza una excepción KeyError
                raise KeyError 
        except:
            # Si se captura una excepción, se asigna un mensaje indicando que el punto no existe
            punto_z=(f"El punto {punto} no existe.")
            
        
        return punto_z
    
    def imprimir_Punto_Z(self,punto):
        punto_z_=self.calcular_Punto_Z(punto)
        booleano=True
        while booleano:
            try:
                punto_z=float(punto_z_)
                print(f"Punto Z del punto {punto} : {punto_z}")
                
            except ValueError:
                print(punto_z_)
            booleano=False        
        