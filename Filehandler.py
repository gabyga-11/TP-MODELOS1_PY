
class Filehandler:
    def __init__(self,nombreArchivo,tipoArchivo):
        self.__fh = open(nombreArchivo, tipoArchivo)

    def leerLinea(self):
        linea = self.__fh.readline()
        if linea and not linea[0] == "c":
            linea = linea.rstrip("\n").split(" ")
        return linea

    def procesarArchivoEntrada(self,linea):
        while linea[0]=="c":
            linea = self.leerLinea()
        return linea

    def escribirLinea(self,nroLavado,prenda):
        self.__fh.write(str(nroLavado) + " " + str(prenda) + "\n")

    def cerrarArchivo(self):
        self.__fh.close()
