class Desviacion_Estandar:
    def __init__(self, varianza):
        self.varianza=varianza
    
    
    def calcular_Desviacion_Estandar_Muestral(self):
        """ Se guarda el valor de la varianza que se obtiene desde el metodo calcular_Varianza_() de la clase varianza 
            en la variable varianza. """
        varianza=self.varianza.calcular_Varianza_Muestral(False)
        
        desviacion=varianza**0.5
        print(f"Desviacion estandar: {desviacion:.4f}")
        return desviacion
    
    def calcular_Desviacion_Estandar_Poblacional(self):
        varianza=self.varianza.calcular_Varianza_Poblacional(False)
        
        desviacion=varianza**0.5
        print(f"Desviacion estandar: {desviacion:.4f}")
        return desviacion