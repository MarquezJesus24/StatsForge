# Esta clase calcula la moda de los datos.
class Moda:
    def __init__(self, frecuencia) :
        #  Inicializa el atributo self.frecuencia con el objeto Frecuencia recibido
        self.frecuencia=frecuencia
    
    def calcular_moda(self):
        # Obtiene el diccionario de frecuencias de la clase Frecuencia
        datos_moda=self.frecuencia.calcular()
        
        # Encuentra la moda como el dato con la máxima frecuencia utilizando el diccionario de frecuencias
        moda= max(datos_moda.items(), key=lambda x:x[1])
        
        return moda[0]