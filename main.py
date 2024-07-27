from estadistica import Estadistica

#Archivo principal que empieza la ejecucion del Programa estadistico

#Se crea un objeto de la clase estadistica.
estadistica= Estadistica()

#Se llaman los metodos que realizan los calculos que se pueden realizar a los datos cualitativos y cuantitativos
#En el condicional se evalua que los datos ingresados sean de tipo cuantitativo ya que a estos se le pueden realizar mas calculos en comparacion a los datos cualitativos.
#Se usa la funcion all() para identificar si todos los datos que hay en estadistica.tipos sean del tipo cuantitativos
if all(t=="cuantitativo" for t in estadistica.tipos):
        estadistica.calcular_Moda()
        print("------------------------------------------------")
        print("¿Desea distribuir la frecuencia en intervalos? \n 1.Si - 2.No")
        eleccion= (input())
        while eleccion !="1" and eleccion!="2":
                print("Ingrese un valor valido por favor \n 1.Si - 2.No")
                eleccion= (input())
                
        if(eleccion=="1"):
                while True:
                        try:
                        # Solicita al usuario que ingrese la cantidad de datos
                                num_intervalos=int(input("Ingrese la cantidad de intervalos deseada: "))
                                if num_intervalos > 0:
                                        break
                                else:
                                        print("Por favor, ingrese un número positivo.")
                        except ValueError:
                                print("Por favor, ingrese un número válido.")
                estadistica.calcular_Intervalos_frecuencia(num_intervalos)
                estadistica.calcular_Frecuencia_Relativa_Intervalos(num_intervalos)
                estadistica.calcular_Frecuencia_Porcentual_Intervalos(num_intervalos)
                estadistica.graficar_Histograma(num_intervalos)
        else:
                estadistica.calcular_Frecuencia_Acumulada()
                print("------------------------------------------------")
                estadistica.calcular_Frecuencia_Relativa()
                print("------------------------------------------------")
                estadistica.calcular_Frecuencia_Porcentual()
        print("------------------------------------------------")

        print("¿Desea calcular un cuartil o un percentil? \n 1. Cuartil \n 2. Percentil")
        opcion=input("Ingrese su opcion (1 o 2): ")
        # Verifica que la opción ingresada sea válida (1 o 2)
        while opcion!="1" and opcion!="2":
                print("Opcion Invalida. Por favor ingresa una opcion valida (1 o 2): ")
                opcion=input("Ingrese su opcion (1 o 2): ")
        if opcion =="1":
                print("¿Que cuartil desea calcular?")
                cuartil=input("Ingrese 1 para el primer cuartil, 2 para el segundo cuartil o 3 para el tercer cuartil: ")
                # Verifica que la opción de cuartil sea válida (1, 2 o 3)
                while cuartil!="1" and cuartil!="2" and cuartil!="3":
                        print("Opcion Invalida. Por favor ingresa una opcion valida (1,2 o 3): ")
                        cuartil=input("Ingrese su opcion (1,2 o 3): ")
                estadistica.calcular_cuartil(cuartil)
        elif opcion=="2":
                booleano=True
                while booleano:
                        try:
                                percentil=int(input("Por favor digite el percentil que desea calcular: "))  
                                while percentil<1 or percentil>100:
                                        percentil=int(input("Por favor ingrese un valor entre 1 y 100: "))    
                                booleano=False
                        except ValueError:
                                print("Porfavor ingresa un numero.")
                estadistica.calcular_percentil(percentil)
        print("------------------------------------------------")
        estadistica.calcular_media()
        print("------------------------------------------------")
        estadistica.calcular_mediana()
        print("------------------------------------------------")
        estadistica.calcular_Rango()
        print("------------------------------------------------")
        estadistica.calcular_IQ()
        print("------------------------------------------------")
        print(" 1. Varianza Muestral \n 2. Varianza Poblacional")
        opcion=input("Ingrese su opcion (1 o 2): ")
        # Verifica que la opción ingresada sea válida (1 o 2)
        while opcion!="1" and opcion!="2":
                print("Opcion Invalida. Por favor ingresa una opcion valida (1 o 2): ")
                opcion=input("Ingrese su opcion (1 o 2): ")
        if opcion =="1":
                estadistica.calcular_VarianzaMuestral(True)
                estadistica.calcular_DesviacionEstandar_Muestral()
                print("------------------------------------------------")
                print("¿Desea evaluar algun punto Z? \n 1. Si \n 2. No")
                opcion2=input()
                # Verifica que la opción ingresada sea válida (1 o 2)
                while opcion2!="1" and opcion2!="2":
                        print("Opcion Invalida. Por favor ingresa una opcion valida (1 o 2): ")
                        opcion2=input()
                if (opcion2=="1"):
                        booleano2=True
                        while booleano2:
                                try:
                                        punto=input("Ingrese un dato: ")
                                        punto=float(punto)
                                except ValueError:
                                        print("Dato invalido por favor ingresa un numero")
                                estadistica.calcular_PuntoZ(punto)
                                repetir=input("¿Desea calcular otro punto Z?\n1.Si - 2.No\n")
                                while repetir!="1" and repetir!="2":
                                        repetir=input("Ingrese un numero valido porfavor \n1.Si - 2.No\n")
                                if repetir=="2":
                                        booleano2=False
                
        elif opcion=="2":
                estadistica.calcular_VarianzaPoblacional(True)
                estadistica.calcular_DesviacionEstandar_Poblacional()
        print("------------------------------------------------")

else:
        estadistica.calcular_Moda()
        print("------------------------------------------------")
        estadistica.calcular_Frecuencia_Acumulada()
        print("------------------------------------------------")
        estadistica.calcular_Frecuencia_Porcentual()
        print("------------------------------------------------")
        estadistica.calcular_Frecuencia_Relativa()
        print("------------------------------------------------")