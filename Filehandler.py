
class Filehandler:
    def __init__(self,nombreArchivo,tipoArchivo):
        self._fh = open(nombreArchivo,tipoArchivo)

    def leerLinea(self):
        linea = self._fh.readline()
        if linea:
            linea = linea.rstrip("\n").split(" ")
        return linea

    def procesarArchivoEntrada(self,linea):
        while linea[0]=="c":
            linea = self.leerLinea()
        return linea

    def escribirLinea(self,nroLavado,prenda):
        self._fh.write(str(nroLavado)+" "+str(prenda)+"\n")

    def cerrarArchivo(self):
        self._fh.close()
