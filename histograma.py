from intervalos_frecuencia import DistribucionFrecuenciaIntervalos

class GraficosHistograma:
    def __init__(self, datos) :
        self.datos=datos
        self.distribucion_Intervalos=DistribucionFrecuenciaIntervalos(self.datos)


#Método para generar un histograma a partir de frecuencias e intervalos dados
    def histograma(self, num_intervalos):
        #Determina la frecuencia máxima para establecer la altura del histograma
        distribucion_intervalos=self.distribucion_Intervalos.calcular(num_intervalos)
        frecuencias = []
        intervalos = []

        for inter,frec in distribucion_intervalos.items():
            frecuencias.append(frec)
            intervalos.append(inter)
        
        max_frec = max(frecuencias)
        min_frec=min(frecuencias)

        
        #Establece el ancho de cada barra del histograma
        bar_width = 1 
        
        #Calcula el número total de barras basado en la longitud de las frecuencias
        num_bars = len(frecuencias)
        diferencia_frec=(max_frec-min_frec)//len(frecuencias)

        #Itera desde la frecuencia máxima hacia abajo para construir cada nivel del histograma
        for i in range(max_frec, 0, -diferencia_frec):
            #Prepara una cadena para imprimir el nivel actual del histograma
            line =(f"{(str(i).rjust(2)):<5} -")   #Añade el número de la escala vertical al principio
            
            #Construye la línea del histogramas
            for freq in frecuencias:
                #Si la frecuencia actual es mayor o igual al nivel actual, dibuja barras
                if freq >= i:
                    line += "    ███      " * bar_width + "     "
                else: 
                    #De lo contrario, deja espacio vacío
                    line += "         " * (bar_width + 1)
            #Imprime la línea del histograma
            print(line)

        #Dibuja una línea divisoria inferior debajo del histograma
        print("------" * (num_bars * (bar_width + 1) + 2))

        #Muestra los intervalos en la parte inferior del histograma
        for interval in intervalos:
            #Formatea y muestra cada intervalo
            print("        "f"({(interval[0])}-{(interval[1])})", end="" * (bar_width + 1))
            # print(f"")
        print("\n")  #Finaliza la línea con un salto de línea