from frecuencia import Frecuencia
class Varianza:
    def __init__(self, datos,media) :
        self.datos=datos
        self.media=media
        self.n=len(self.datos.datos)
        self.frec=Frecuencia(self.datos)
    
    def calcular_Varianza_Muestral(self,no_print):
        
        #Se guarda la frecuencia en el atributo frec
        self.frec=Frecuencia.calcular(self.datos)
        suma_cuadrado=0
        #Se guarda la media en la variable promedio
        promedio=self.media.calcular_Media()
        suma_des_res_media_mul_frec=0
        
        
        if no_print : print("Dato   |   Media   | Desviacion respecto a la media (Xi - Media)  | Cuadrado Desviacion | Desviacion respecto a la media (Xi - Media)^2*frecuenciaXi |")
        for dato, f in self.frec.items():
            #Se calcula la desviacion respecto a la media de los datos  
            desviacion_res_media=dato-float(promedio)
            cuadrado=(desviacion_res_media)**2
            
            #Se multiplica el cuadrado de la desviacion respecto a la media de los datos por la frecuencia de los datos 
            desviacion_res_media_mult_Frecuencia=cuadrado*f
            
            if no_print : print (f"{dato:<6} |{float(promedio):<10.4f} | {desviacion_res_media:<44.4f} |{cuadrado:<20.4f} | {desviacion_res_media_mult_Frecuencia:<58.4f} |")
            #Se va sumando los valores de los caudrados de la desviacion respecto a la media de los datos 
            suma_cuadrado+=cuadrado
            suma_des_res_media_mul_frec+=desviacion_res_media_mult_Frecuencia
        
        varianza_muestral=suma_des_res_media_mul_frec/(self.n-1)
        if no_print :
            print (f"Suma (Xi-Media)^2: {suma_cuadrado:.4f}")
            print(f"Suma (Xi-Media)^2*frecuencia: {suma_des_res_media_mul_frec:.4f}")
            print(f"Varianza Muestral:  {varianza_muestral:.4f}")
        
        return varianza_muestral
    
    def calcular_Varianza_Poblacional(self,no_print):
        self.frec=Frecuencia.calcular(self.datos)
        suma_cuadrado=0
        promedio=self.media.calcular_Media()
        suma_des_res_media_mul_frec=0
        
        
        if no_print: print("Dato   |   Media(σ)   | Desviacion respecto a la media (Xi - σ)  | Cuadrado Desviacion | Desviacion respecto a la media (Xi - σ)^2*frecuenciaXi |")
        for dato, f in self.frec.items():
            desviacion_res_media=dato-float(promedio)
            cuadrado=(desviacion_res_media)**2
            desviacion_res_media_mult_Frecuencia=cuadrado*f
            
            if no_print: print(f"{dato:<6} |{float(promedio):<10.4f} | {desviacion_res_media:<44.4f} |{cuadrado:<20.4f} | {desviacion_res_media_mult_Frecuencia:<58.4f} |")
            suma_cuadrado+=cuadrado
            suma_des_res_media_mul_frec+=desviacion_res_media_mult_Frecuencia
        varianza_poblacional=suma_des_res_media_mul_frec/(self.n)
        if no_print:
            print (f"Suma (Xi-σ)^2: {suma_cuadrado:.4f}")
            print(f"Suma (Xi-σ)^2*frecuencia: {suma_des_res_media_mul_frec:.4f}")
            print(f"Varianza Poblacional:  {varianza_poblacional:.4f}")
            
        return varianza_poblacional
    
    