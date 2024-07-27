# Esta clase se encarga de calcular las frecuencias de los datos, tanto la frecuencia simple como la frecuencia acumulada.
class Frecuencia:
    def __init__(self, datos) :
        # Inicializa los atributos self.datos y self.tipos con los datos y tipos recibidos
        self.datos=datos.datos
        self.tipos= datos.tipos
        self.n=len(datos.datos)
    
    def calcular(self):
        # Crea un diccionario vacío para almacenar las frecuencias
        frecuencia= {}
        
        # Recorre cada dato en self.datos
        for dato in self.datos:
            # Si el dato ya está en el diccionario, incrementa su valor en 1
            # Si no está, lo agrega con valor inicial 1
            frecuencia[dato]= frecuencia.get(dato,0) + 1
        # Devuelve el diccionario de frecuencias
        return frecuencia