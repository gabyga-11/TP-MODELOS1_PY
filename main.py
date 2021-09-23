import ProcesadorArchivo

def main():
    datos = ProcesadorArchivo.ProcesadorArchivo("entrada.txt", "r")
    datos.procesar()

    print(datos.cantPrendas)
    print(datos.cantIncompatib)
    print(datos.matrizIncompatib)
    print(datos.vectorLavados)
main()
