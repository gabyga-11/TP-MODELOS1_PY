import os

class Menu:
    def __init__(self):
        self.cantLavarropas = 0
        self.iniciarMenu()
        self.nombre = None
        self.cantLavarropas = 1

    def limpiar(self):
        if os.name=="posix":
            os.system("clear")
        elif os.name in ("ce","nt","dos"):
            os.system("cls")

    def opcionValidaSN(self,opcion):
        while not opcion in ["S","N","s","n"]:
            opcion = input("Ingrese una opción valida S/N")
        return opcion

    def opcionNumValida(self,opcion,min,max):
        while not (opcion >= min or opcion <= max):
            opcion = input("Ingrese una opcion valida!")
        return opcion

    def devolverModificacionesUsuario(self):
        return()

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
        print("Por defecto, se ha colocado entrada.txt como nombre al archivo del problema")
        opcion = input("Desea cambiar el nombre? S/N")
        opcion = self.opcionValidaSN(opcion)
        if opcion in ["S","s"]:
            self.nombre = str(input("Ingrese nombre del archivo del problema (no ponga '.txt'): ")+".txt")


    def cambioNombreArchivoEntrada(self):

    def cambioCantLavarropas(self):
        print("Por defecto, se ha colocado un solo lavarropas")
        opcion = input("Desea cambiar la cantidad? S/N")
        opcion = self.opcionValidaSN(opcion)
        if opcion in ["S","s"]:
            self.cantidadLavarropas = int(input("Ingrese la cantidad de lavarropas: "))

