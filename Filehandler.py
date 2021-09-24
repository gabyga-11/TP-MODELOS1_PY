
class Filehandler:
    def __init__(self,nombreArchivo,tipoArchivo):
        self._fh = open(nombreArchivo,tipoArchivo)

    def leerLinea(self):
        linea = self._fh.readline()
        if linea:
            linea = linea.rstrip("\n").split(" ")
        return linea

    def escribirLinea(self,vector):
        for i in range(len(vector)):
            vector[i] = str(vector[i])
        vector = " ".join(vector)
        self._fh.write(vector)

    def cerrarArchivo(self):
        self._fh.close()
