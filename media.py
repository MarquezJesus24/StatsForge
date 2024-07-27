# Esta clase calcula la media  de los datos.
class Media:
    def __init__(self,datos) :
        # Inicializa el atributo self.datos con los datos recibidos
        self.datos=datos
        
    def calcular_Media(self):
        # Calcula la media aritmética sumando todos los datos y dividiéndolos por la cantidad total de datos
        media=sum(self.datos.datos)/self.datos.n
        media_formateada=f"{media:.4f}"
        return (media_formateada)
    