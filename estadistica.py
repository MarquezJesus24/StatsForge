from datos import Datos
from percentil import Percentil
from media import Media
from mediana import Mediana
from moda import Moda
from frecuencia import Frecuencia
from frecuencia_porcentual import FrecuenciaPorcentual
from frecuencia_relativa import FrecuenciaRelativa
from intervalos_frecuencia import DistribucionFrecuenciaIntervalos
from frec_acumulada import FrecuenciaAcumulada
from cuartil import Cuartil
from rango import Rango
from rango_intercuartilico import Rango_Intercuartilico
from varianza import Varianza
from desviacionEstandar import Desviacion_Estandar
from punto_Z import Punto_Z
from histograma import  GraficosHistograma

"""La clase estadistica es la encargada de realizar los llamados a las demas clases segun sea necesario
    Realiza los llamados creando un  objeto de la clase respectiva y llamando al metodo de esa clase que realiza el calculo necesario"""

class Estadistica:
    
    def __init__(self):
        # Crea una instancia de la clase Datos para obtener los datos ingresados por el usuario
        self.datos=Datos()
        
        # Crea instancias de las clases Moda, Frecuencia, FrecuenciaPorcentual y FrecuenciaRelativa
        
        self.tipos=self.datos.tipos
        self.frecuencia_acumulada=FrecuenciaAcumulada(self.datos)
        self.frecuencia=Frecuencia(self.datos)
        self.frecuencia_porcentual=FrecuenciaPorcentual(self.datos)
        self.frecuencia_relativa=FrecuenciaRelativa(self.datos)
        self.moda=Moda(self.frecuencia)
        self.graficoHisto=GraficosHistograma(self.datos)
        
        # Si todos los datos son cuantitativos, crea instancias de las clases Percentil, Media, DistribucionFrecuencia y Mediana
        if all(t=="cuantitativo" for t in self.tipos):
            self.percentil= Percentil(self.datos)
            self.cuartil= Cuartil(self.datos)
            self.media=Media(self.datos)
            self.intervalos_frecuencia= DistribucionFrecuenciaIntervalos(self.datos)
            self.mediana= Mediana(self.datos)
            self.rango=Rango(self.datos)
            self.rangoIQ=Rango_Intercuartilico(self.datos)
            self.varianza=Varianza(self.datos,self.media)
            self.desviacion=Desviacion_Estandar(self.varianza)
            self.punto_z=Punto_Z(self.datos,self.varianza,self.media)
            
    
    #Metodo Encargado de Llamar a la clase encargada de calcular la Moda
    def calcular_Moda(self):
        print(f"Moda: {self.moda.calcular_moda()}")
    
    #Metodo Encargado de Llamar a la clase encargada de la Frecuencia y Frecuencia acumulada
    def calcular_Frecuencia_Acumulada(self):
        self.frecuencia_acumulada.calcular()
        
    #Metodo Encargado de Llamar a la clase encargada de la Frecuencia %    
    def calcular_Frecuencia_Porcentual(self):
        print(f"Frecuencia porcentual: ")
        self.frecuencia_porcentual.calcular_acumulada_porcentual()
    
    def calcular_Frecuencia_Porcentual_Intervalos(self,num_intervalos):
        self.frecuencia_porcentual.calcular_Acumulada_Porcentual_Intervalos(num_intervalos)
    
    #Metodos Encargado de Llamar a la clase encargada de  Frecuencia Relativa
    def calcular_Frecuencia_Relativa(self):
        print(f"Frecuencia relativa: ")
        self.frecuencia_relativa.calcular_acumulada_relativa()
    
    def calcular_Frecuencia_Relativa_Intervalos(self,numero_intervalos):
        self.frecuencia_relativa.calcular_acumulada_relativa_en_intervalos(numero_intervalos)
    
    #Metodo Encargado de Llamar a la clase encargada de  Distribuir los Datos en intervalos y su frecuencia   
    def calcular_Intervalos_frecuencia(self,numero_intervalos):
        self.intervalos_frecuencia.imprimir_intervalos(numero_intervalos)
    
    #Metodo Encargado de Llamar a la clase encargada de Calcular el Rango
    def calcular_Rango(self):
        self.rango.calcularRango()
    
    #Metodo Encargado de Llamar a la clase encargada de calcular el Rango Intercuartilico
    def calcular_IQ(self):
        self.rangoIQ.calcular_IQ()
    
    #Metodo Encargado de Llamar a la clase encargada de Calcular la varianza
    def calcular_VarianzaMuestral(self,no_print):
        self.varianza.calcular_Varianza_Muestral(no_print)

    def calcular_VarianzaPoblacional(self,no_print):
        self.varianza.calcular_Varianza_Poblacional(no_print)
    
    #Metodo Encargado de Llamar a la clase encargada de Calcular la Desviacion Estandar
    def calcular_DesviacionEstandar_Muestral(self):
        self.desviacion.calcular_Desviacion_Estandar_Muestral()
    
    def calcular_DesviacionEstandar_Poblacional(self):
        self.desviacion.calcular_Desviacion_Estandar_Poblacional()
    
    #Metodo Encargado de Llamar a la clase encargada de calcular el percentil
    def calcular_percentil(self,num_percentil):
        print(f"Percentil: {self.percentil.calcularPercentil(num_percentil)}")
    
    #Metodo Encargado de Llamar a la clase encargada de calcular el cuartil    
    def calcular_cuartil(self, num_cuartil):
        print(f"Cuartil: {self.cuartil.calcularCuartil(num_cuartil)}")
    
    #Metodo Encargado de Llamar a la clase encargada de calcular la media
    def calcular_media(self):
        print(f"Media: {self.media.calcular_Media()}")
    
    #Metodo Encargado de Llamar a la clase encargada de calcular la mediana
    def calcular_mediana(self):
        print(f"Mediana: {self.mediana.calcular()}")
    
    #Metodo Encargado de Llamar a la clase encargada de calcular los puntos Z
    def calcular_PuntoZ(self,punto):
        self.punto_z.imprimir_Punto_Z(punto)
    
    def graficar_Histograma(self,numero_intervalos):
        self.graficoHisto.histograma(numero_intervalos)