import ProcesadorArchivo as proc
import Filehandler as fh
import Datos as dat
import Menu

def main():
    menu = Menu.Menu()

    fhRead = fh.Filehandler(menu.obtenerNombreEntrada(), "r")
    archivoCarga = proc.ProcesadorArchivo(fhRead)

    archivoCarga.procesarArchivoEntrada()
    cantPrendas,cantIncompatib,matrizIncompatib,vectorLavados = archivoCarga.getResultados()

    menu.cambioCantLavarropas(cantPrendas)

    datos = dat.Datos(cantPrendas,cantIncompatib,matrizIncompatib,vectorLavados)
    datos.asignarPrendasEnLavados()

    lavados,cantLavados = datos.devolverResultados()
    menu.mostrarResultadosPorLavado(lavados,cantLavados)

    fhWrite = fh.Filehandler(menu.obtenerNombreSalida(),"w")
    archivoGuardado = proc.ProcesadorArchivo(fhWrite)
    archivoGuardado.guardarEnArchivo(fhWrite,lavados,cantLavados)

    tiempoTotal = datos.obtenerTiempoTotalLavado(menu.obtenerCantLavarropas())
    menu.mostrarTiempoTotalLavados(tiempoTotal, menu.obtenerCantLavarropas())

    fhRead.cerrarArchivo()
    fhWrite.cerrarArchivo()

main()
