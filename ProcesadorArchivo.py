
class filehandler:
    def __init__(self,nombreArchivo,tipoArchivo):
        self.fh = open(nombreArchivo,tipoArchivo)

    def leerLinea(self):
        linea = self.fh.readline()
        if linea:
            linea = linea.rstrip("\n").split(" ")
        return linea

    def escribirLinea(self,vector):
        for i in range(len(vector)):
            vector[i] = str(vector[i])
        vector = " ".join(vector)
        self.fh.write(vector)

    def cerrarArchivo(self):
        self.fh.close()




class ProcesadorArchivo:
    def __init__(self,nombreArchivo,tipoArchivo):
        self.archivo = filehandler(nombreArchivo,tipoArchivo)
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
            self.matrizIncompatib[int(linea[1])-1][int(linea[2])-1] = True

    def procesarTiempoLavados(self):
        for i in range (0,self.cantPrendas):
            linea = self.archivo.leerLinea()
            self.vectorLavados.append( [ int(linea[1]) , int(linea[2]) ] ) #prenda, tiempoLavado
        self.vectorLavados = sorted(self.vectorLavados, key=lambda x:x[1])

    def procesar(self):
        linea = self.archivo.leerLinea()
        self.cantPrendas,self.cantIncompatib = int(linea[2]),int(linea[3])
        self.procesarIncompatibilidades()
        self.procesarTiempoLavados()
