class Cuartil():
    def __init__(self,datos):
        # Inicializa el atributo self.datos con los datos recibidos
        self.datos=datos
        
    def calcularCuartil(self,cuartil):
        # Calcula el índice correspondiente al cuartil seleccionado
        if cuartil=="1":
            indice=((25/100)*(self.datos.n))-1
        elif cuartil=="2":
            indice=((50/100)*(self.datos.n))-1
        else:
            indice=((75/100)*(self.datos.n))-1
        # Verifica si el índice es un número entero
        es_entero=indice.is_integer()
        
        # Si el índice es entero, calcula el valor como el promedio de los dos valores adyacentes
        if es_entero==True:     
            # Calcula los índices inferior y superior
            indice_inferior=indice
            indice_superior=indice_inferior + 1
            valor=(self.datos.datos[indice_inferior]+self.datos.datos[indice_superior])/2
        
        # Si el índice no es entero, entonces el valor toma el dato de la siguiente posicion como valor final. 
        else:
            indice_aprox=int(indice) + 1
            valor= self.datos.datos[indice_aprox]
            
        return valor