

class ProcesadorArchivo:

    def __init__(self,fhRead):
        self.archivo = fhRead
        self.cantPrendas = 0
        self.cantIncompatib = 0
        self.matrizIncompatib = []
        self.vectorLavados = []

    def crearMatrizCuadrada(self):
        matriz = []
        for i in range (self.cantPrendas):
            fila = []
            for j in range (self.cantPrendas):
                fila.append(False)
            matriz.append(fila)

        return matriz

    def procesarIncompatibilidades(self):
        self.matrizIncompatib = self.crearMatrizCuadrada()
        for i in range(0,self.cantIncompatib):
            linea = self.archivo.leerLinea()
            print("matrizIncompatib[",int(linea[1])-1,"][",int(linea[2])-1,"] = True")
            self.matrizIncompatib[int(linea[1])-1][int(linea[2])-1] = True

    def procesarTiempoLavados(self):
        for i in range (0,self.cantPrendas):
            linea = self.archivo.leerLinea()
            self.vectorLavados.append( [ int(linea[1]) , int(linea[2]) ] ) #prenda, tiempoLavado
        self.vectorLavados = sorted(self.vectorLavados, key=lambda x:x[1])

    def procesarArchivoEntrada(self):
        linea = self.archivo.leerLinea()
        self.cantPrendas,self.cantIncompatib = int(linea[2]),int(linea[3])
        self.procesarIncompatibilidades()
        self.procesarTiempoLavados()

    def getResultados(self):
        return(self.cantPrendas,self.cantIncompatib,self.matrizIncompatib,self.vectorLavados)
