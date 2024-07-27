from frecuencia import Frecuencia

# Esta clase calcula la distribución de frecuencias de los datos, dividiendo los datos en intervalos y contando la cantidad de datos en cada intervalo.
class DistribucionFrecuenciaIntervalos(Frecuencia):
    def __init__(self, datos):
        super().__init__(datos)

    def calcular(self,num_intervalos):
            intervalos_distribucion=[]
            
            # Obtiene el valor mínimo y máximo de los datos
            valor_minimo=self.datos[0]
            valor_maximo=self.datos[-1]
            
            # Calcula el rango de los datos
            rango= valor_maximo - valor_minimo
            
            # Calcula la amplitud de cada intervalo
            amplitud_intervalo= rango / num_intervalos
            
            
            # Crea una lista vacía para almacenar los intervalos
            intervalos= []
            
            # Calcula los intervalos y los agrega a la lista
            inicio= valor_minimo
            
            for i in range (num_intervalos):
                fin= (inicio + amplitud_intervalo)
                intervalos.append((inicio, fin))
                inicio= fin
            
            # Crea una lista para almacenar la distribución de frecuencias
            distribucion_frecuencias=[0] * num_intervalos
            
            # Recorre los datos y los cuenta en el intervalo correspondiente
            for x in self.datos:
                for i, intervalo in enumerate(intervalos):
                    #Verifica que el dato se encuentre dentro del intervalo, si esa asi a la frecuencia se le incrementa en 1 
                    if intervalo[0]<= x <intervalo [1]:
                        distribucion_frecuencias[i] += 1
                        break
                    
                    elif i == num_intervalos - 1 and x == valor_maximo:  # Asegura que el valor máximo se incluya en el último intervalo
                        distribucion_frecuencias[i] += 1
            
            #Se crea una lista con los intervalos y distribucion 
            for i, intervalo in enumerate(intervalos):
                intervalos_distribucion.append(((intervalo[0],intervalo[1]),distribucion_frecuencias[i]))
            
            #Se crea un diccionario  que guardara los intervalos con la frecuencia de cada uno 
            dicc_intervalos={}
            
            #Se crea una lista que contendra unicamente los intervalos
            intervalos_ = [intervalo for intervalo, _ in intervalos_distribucion]
            #Se crea un lisra que contendra unicamente la frecuencia de los intervalos
            frecuencias = [frecuencia for _, frecuencia in intervalos_distribucion]
            
            #Se juntas las dos listas intervalos_ y frecuencia en el diccionario dicc_intervalos
            #Siendo las claves del diccionario los intervalos y los valores las frecuencias de los intervalos
            for inter, frec in zip(intervalos_,frecuencias):
                intervalo_redondeado = (round(inter[0], 4), round(inter[1], 4))
                dicc_intervalos[intervalo_redondeado]=frec
                
            return dicc_intervalos
    
    def imprimir_intervalos(self,numero_intervalos):
        intervalos_distribucion=self.calcular(numero_intervalos)
        
        acumulado = 0
        print("Intervalo   | Frecuencia Absoluta | Frecuencia Acumulada")
        for intervalo, frec,  in intervalos_distribucion.items():
            acumulado += frec
            print(f"{str(intervalo):<6}|{frec:<21}| {acumulado:<20.2f}")
                