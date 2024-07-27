# Esta clase calcula  percentiles específicos de los datos.
class Percentil:
    def __init__(self, datos) :
        # Inicializa el atributo self.datos con los datos recibidos
        self.datos=datos
        
    def calcularPercentil(self,percentil):
        indice=((percentil/100)*(self.datos.n))-1
        
        # Verifica si el índice es un número entero
        es_entero=indice.is_integer()
        
        # Si el índice es entero, calcula el valor como el promedio de los dos valores adyacentes
        if es_entero==True:
            # Calcula los índices inferior y superior
            indice_inferior=indice
            indice_superior=indice_inferior + 1
            valor=(self.datos.datos[indice_inferior]+self.datos.datos[indice_superior])/2
        
        # Si el índice no es entero, calcula el valor como el valor en el índice aproximado
        else:
            indice_aprox=int(indice) + 1
            valor= self.datos.datos[indice_aprox]
        return valor