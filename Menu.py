import os,time

class Menu:
    def __init__(self):
        self.cantPrendas = None
        self.cantLavarropas = 0
        self.nombreEntrada = "entrada.txt"
        self.nombreSalida = "resultado.txt"
        self.cantLavarropas = 1
        self.iniciarMenu()


    def iniciarMenu(self):
        self.mensajeBienvenida()
        self.objetivo()
        self.cambiosDelUsuario()

    def mensajeBienvenida(self):
        print("{:^60}".format(" PROGRAMA DE LAVADOS 1.0 "))
        print("{:^60}".format(" por Gabriel Carniglia \n"))

    def objetivo(self):
        print("El objetivo de este programa es determinar las prendas de cada programa de lavado")
        print("en función de la compatibilidad entre prendas (si tiñen o destiñen)")
        print("Luego, emite un archivo con los resultados PRENDA-LAVADO correspondiente")
        print("Como función extra, muestra el tiempo total de los lavados en funcion de la cantidad de lavarropas")
        print("indicando la composicion de cada lavado")

    def cambiosDelUsuario(self):
        print("PRESIONE [ENTER] PARA CONTINUAR..")
        self.cambioNombreArchivoEntrada()
        self.limpiar(1)
        self.cambioNombreArchivoSalida()
        self.limpiar(1)


    def cambioNombreArchivoEntrada(self):
        print("Por defecto, se ha colocado entrada.txt como nombre al archivo del problema")
        opcion = input("Desea cambiar el nombre? S/N")
        opcion = self.opcionValidaSN(opcion)
        if opcion in ["S", "s"]:
            self.nombre = str(input("Ingrese nombre del archivo del problema (no ponga '.txt'): ")+".txt")

    def cambioNombreArchivoSalida(self):
        print("Por defecto, se ha colocado resultado.txt como nombre al archivo de la solución")
        opcion = input("Desea cambiar el nombre? S/N")
        opcion = self.opcionValidaSN(opcion)
        if opcion in ["S", "s"]:
            self.nombre = str(input("Ingrese nombre del archivo de la solución (no ponga '.txt'): ")+".txt")

    def cambioCantLavarropas(self,cantPrendas):
        print("Por defecto, se ha colocado un solo lavarropas en la lavandería")
        opcion = input("Desea cambiar la cantidad? S/N")
        opcion = self.opcionNumValida(opcion,1,cantPrendas)
        if opcion in ["S","s"]:
            self.cantLavarropas = int(input("Ingrese la cantidad de lavarropas: "))
        self.limpiar(1)

    def mostrarResultadosPorLavado(self,lavados,cantLavados):
        print("{:^60}".format("-"))
        nroLavado = 1
        for tiempo,prendas in lavados:
            print("LAVADO NRO {}".format(nroLavado))
            print("Duración del lavado: ",tiempo,"minutos")
            print("Prendas del lavado:"," ".join([str(prenda) for prenda in prendas]))
            print("{:^60}".format("-"))
            nroLavado += 1
            if nroLavado >= cantLavados:
                input("--  [ENTER] --> SIGUIENTE LAVADO  --")

        print("CANTIDAD DE LAVADOS: {}".format(cantLavados))
        input("PRESIONE ENTER PARA CONTINUAR..")



    def limpiar(self,tiempo):
        time.sleep(tiempo)
        if os.name=="posix":
            os.system("clear")
        elif os.name in ("ce","nt","dos"):
            os.system("cls")

    def opcionValidaSN(self,opcion):
        while not opcion in ["S","N","s","n"]:
            opcion = input("Ingrese una opción valida S/N ")
        return opcion

    def opcionNumValida(self,opcion,min,max):
        while not (opcion >= min or opcion <= max):
            opcion = input("Ingrese una opcion valida! ")
        return opcion

    def mostrarTiempoTotalLavados(self,tiempoTotal,cantLavarropas):
        self.limpiar(1)
        print("El tiempo total de lavado es de {} minutos, para un total de {} lavarropa/s".format(tiempoTotal,cantLavarropas))
