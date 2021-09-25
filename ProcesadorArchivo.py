class ProcesadorArchivo:

    def __init__(self, fh):
        self.__archivo = fh
        self.__cantPrendas = 0
        self.__cantIncompatib = 0
        self.__matrizIncompatib = []
        self.__vectorLavados = []

    def crearMatrizCuadrada(self):
        matriz = []
        for i in range (self.__cantPrendas):
            fila = []
            for j in range (self.__cantPrendas):
                fila.append(False)
            matriz.append(fila)

        return matriz

    def procesarIncompatibilidades(self):
        self.__matrizIncompatib = self.crearMatrizCuadrada()
        for i in range(0, self.__cantIncompatib):
            linea = self.__archivo.leerLinea()
            self.__matrizIncompatib[int(linea[1]) - 1][int(linea[2]) - 1] = True

    def procesarTiempoLavados(self):
        for i in range (0, self.__cantPrendas):
            linea = self.__archivo.leerLinea()
            self.__vectorLavados.append([int(linea[1]) , int(linea[2])]) #prenda, tiempoLavado
        self.__vectorLavados = sorted(self.__vectorLavados, key=lambda x:x[1])

    def procesarArchivoEntrada(self):
        linea = self.__archivo.procesarArchivoEntrada(self.__archivo.leerLinea())
        self.__cantPrendas, self.__cantIncompatib = int(linea[2]), int(linea[3])
        self.procesarIncompatibilidades()
        self.procesarTiempoLavados()

    def getResultados(self):
        return(self.__cantPrendas, self.__cantIncompatib, self.__matrizIncompatib, self.__vectorLavados)


    def guardarEnArchivo(self,fhWrite,lavados,cantLavados):
        self.archivoGuardado = fhWrite
        for nroLavado in range(cantLavados):
            for prenda in lavados[nroLavado][1]:
                self.__archivo.escribirLinea(prenda, nroLavado + 1)

