# Esta clase calcula la mediana de los datos.
class Mediana:
    def __init__(self, datos) :
        # Inicializa el atributo self.datos con los datos recibidos
        self.datos=datos.datos
        
    def calcular(self):
        # Ordena los datos de forma ascendente
        datos_ordenados= sorted(self.datos)
        n=len(datos_ordenados)
        
        # Calcula la mediana para un número par de datos
        if n% 2==0:
            indice_mediana_1=n // 2-1
            indice_mediana_2=indice_mediana_1 + 1
            mediana=(datos_ordenados[indice_mediana_1] + datos_ordenados[indice_mediana_2])/2
        # Calcula la mediana para un número impar de datos
        else:
            indice_mediana= n // 2
            mediana=datos_ordenados[indice_mediana]
        return mediana