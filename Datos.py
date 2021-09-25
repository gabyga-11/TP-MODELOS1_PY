class Datos:
    def __init__(self,cantPrendas,cantIncompatib,matrizIncompatib,vectorLavados):
        self.__cantPrendas = cantPrendas
        self.__cantIncompatib = cantIncompatib
        self.__matrizIncompatib = matrizIncompatib
        self.__vectorLavadosYTiempos = vectorLavados
        self.__lavados = [] #FORMATO: [ [tiempo,[prenda,prenda2]] , [tiempo2,[prenda3,prenda4]] , ...]
        self.__cantLavados = 0

    def esCompatible(self,lavado,prendaNueva): #matrizLavados[i][1] -- ACA SE REVISA UN UNICO LAVADO
        compatible = True
        posPrendaEnElLavado = 0

        while compatible and posPrendaEnElLavado < len(lavado):
            if self.__matrizIncompatib[prendaNueva - 1][lavado[posPrendaEnElLavado] - 1]:
                compatible = False
            posPrendaEnElLavado += 1

        return compatible

    def agregarPrimerPrendaDeLavado(self,prendaNueva,tiempoPrendaNueva):
        self.__lavados.append([tiempoPrendaNueva , [prendaNueva]]) #Primer prenda del lavado
        self.__cantLavados += 1

    def verificarTiempoLavado(self,tiempoPrendaNueva,tiempoLavado,nroDeLavado): #La ultima es tiempoLavado
        if tiempoPrendaNueva > tiempoLavado:
            self.__lavados[nroDeLavado][0] = tiempoPrendaNueva

    def agregarPrenda(self,prendaNueva,tiempoPrendaNueva):
        if self.__lavados == []:
            self.agregarPrimerPrendaDeLavado(prendaNueva,tiempoPrendaNueva)
        else:
            seLeAsignoUnLavado = False
            nroDeLavado = 0
            while not seLeAsignoUnLavado and nroDeLavado < self.__cantLavados:
                if self.esCompatible(self.__lavados[nroDeLavado][1], prendaNueva):
                    seLeAsignoUnLavado = True
                    self.__lavados[nroDeLavado][1].append(prendaNueva)
                    self.verificarTiempoLavado(tiempoPrendaNueva, self.__lavados[nroDeLavado][0], nroDeLavado) #La ultima es tiempoLavado
                nroDeLavado += 1

            if not seLeAsignoUnLavado:
                self.agregarPrimerPrendaDeLavado(prendaNueva,tiempoPrendaNueva)

        del(self.__vectorLavadosYTiempos[-1])


    def asignarPrendasEnLavados(self):
        for i in range(self.__cantPrendas - 1, -1, -1):
            self.agregarPrenda(self.__vectorLavadosYTiempos[i][0], self.__vectorLavadosYTiempos[i][1])

    def obtenerTiempoTotalLavado(self, cantLavarropas):
        tiempos=[]
        for i in range(cantLavarropas):
            tiempoUnLavarropas = 0
            for nroPrenda in range(i, self.__cantLavados, cantLavarropas):
                tiempoUnLavarropas += self.__lavados[nroPrenda][0]
            tiempos.append(tiempoUnLavarropas)

        return(max(tiempos))

    def devolverResultados(self):
        return self.__lavados, self.__cantLavados
