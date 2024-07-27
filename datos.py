import csv
#La clase datos es la encargada de saber como se almacenaran los datos a evaluar, tambien es la que se encarga de almacenarlos 

class Datos:
    #Constructor
    def __init__(self) :
        #Lista que se encarga de almacenar los datos a evaluar
        self.datos=[]
        #Lista que se encarga de almacenar el tipo de los  datos a evaluar
        self.tipos=[]
        self.leer_Datos()
        #Variable n encagada de tener el tamaño de datos
        self.n=len(self.datos)
        
    
    def leer_Datos(self):
        print("Bienvenido a StatsForge.")
        print("¿Desea leer los datos de un archivo CSV o ingresarlos manualmente?")
        print("1. Leer desde archivo CSV \n2. Ingresar datos manualmente")
        opcion = input("Ingrese su opción (1 o 2): ")

        while opcion != "1" and opcion != "2":
            print("Opción inválida. Por favor, ingrese una opción válida (1 o 2).")
            opcion = input("Ingrese su opción (1 o 2): ")

        if opcion == "1":
            self.leer_Datos_CSV()
        elif opcion == "2":
            self.ingresar_Datos_Manualmente()
    
    
    def ingresar_Datos_Manualmente(self):
        while True:
            try:
            # Solicita al usuario que ingrese la cantidad de datos
                print("Por favor ingrese la cantidad de datos que desea analizar: ")
                n = int(input())
                if n > 0:
                    break
                else:
                    print("Por favor, ingrese un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        print("Ingrese los datos (para datos cualitativos, ingrese una cadena de texto):")
        # Ciclo que se repite 'n' veces para ingresar los datos
        for i in range(n):
            dato= input()
            try:
                # Intenta convertir el dato a un número flotante
                dato= float(dato)
                
                # Si se pudo convertir, se agrega 'cuantitativo' a la lista self.tipos
                self.tipos.append("cuantitativo")
                
            except ValueError:
                # Si no se pudo convertir (ocurrió un ValueError), se agrega 'cualitativo' a la lista self.tipos
                self.tipos.append("cualitativo")
            # Se agrega el dato a la lista self.datos
            self.datos.append(dato)
        # Verifica si todos los elementos de self.tipos son 'cuantitativo'
        
        if all(t=="cuantitativo" for t in self.tipos):
            # Si todos los datos son cuantitativos, ordena la lista self.datos
            self.datos.sort()
        print("------------------------------------------------")
    
    def leer_Datos_CSV(self):
        booleano=True
        while booleano:
            try:
            # Solicita al usuario que ingrese la direccion del archivo csv o la ruta del archivo
                print("Por favor ingrese el nombre o direccion del archivo a analizar(Recuerde agregar la extension .csv): ")
                nombre_Archivo = input() 
                extension_archivo=".csv"
                #Verifica si el nombre del archivo es un archivo csv
                if extension_archivo in nombre_Archivo:
                    
                    with open(nombre_Archivo,'r') as archivo_csv:
                        lectura=csv.reader(archivo_csv)
                        #Se obtienen los nombres de los headers del archivo
                        nombre_columnas=next(lectura)
                        next(lectura)
                        
                        columna=int(input("Ingrese el numero de la columna a analizar: "))
                        while columna>len(nombre_columnas):
                            columna=int(input("Por favor ingreses un numero de columnas valido: "))
                            
                        for fila_inicial in lectura:
                            dato= fila_inicial[columna-1]
                            try:
                                # Identifica si el dato es un dato en blacno ' ', si lo es se lanza un excepcion de TypeError.
                                cantidad_espacios=dato.count(' ')
                                espacios=' '* cantidad_espacios
                                if dato==espacios:
                                    raise TypeError
                                else:
                                    #En caso de que no sea un espacio en blanco, trata de convertir a flotante el dato para identificar que tipo de dato es.
                                    dato= float(dato)
                                    # Si se pudo convertir, se agrega 'cuantitativo' a la lista self.tipos
                                    self.tipos.append("cuantitativo")
                                
                            except TypeError:
                                #Si el dato es un espacio en blanco convierte el dato en 0 y agrega 'cuantitativo' a la lista self.tipos
                                dato=0
                                self.tipos.append("cuantitativo")
                            except ValueError:
                                # Si no se pudo convertir (ocurrió un ValueError), se agrega 'cualitativo' a la lista self.tipos
                                self.tipos.append("cualitativo")
                                
                            # Se agrega el dato a la lista self.datos
                            self.datos.append(dato)
                            
                            # Verifica si todos los elementos de self.tipos son 'cuantitativo'
                            if all(t=="cuantitativo" for t in self.tipos):
                                # Si todos los datos son cuantitativos, ordena la lista self.datos
                                self.datos.sort()
                            booleano=False
            except ValueError:
                print("Por favor, ingrese la direccion correcta del archivo csv.")
        #print (self.datos.__len__())
        # for dato in self.tipos:
        #     print(f"{dato}")
        print("------------------------------------------------")