class Datos:
    def __init__(self,cantPrendas,cantIncompatib,matrizIncompatib,vectorLavados):
        self.cantPrendas = cantPrendas
        self.cantIncompatib = cantIncompatib
        self.matrizIncompatib = matrizIncompatib
        self.vectorLavadosYTiempos = vectorLavados
        self.lavados = [] #FORMATO: [ [nro lavado,tiempo,[prenda,prenda2]] , [nro lavado,tiempo2,[prenda3,prenda4]] , ...]
        self.cantLavados = 0

    def esCompatible(self,lavado,prendaNueva): #matrizLavados[i][1] -- ACA SE REVISA UN UNICO LAVADO
        compatible = True
        prendaEnElLavado = 1

        while compatible and prendaEnElLavado < len(lavado)-1:
            if not self.matrizIncompatib[prendaNueva-1][prendaEnElLavado-1]:
                compatible = False
            prendaEnElLavado += 1

        return compatible

    def agregarPrimerPrendaDeLavado(self,prendaNueva,tiempoPrendaNueva):
        self.lavados.append( [ tiempoPrendaNueva , [prendaNueva] ] ) #Primer prenda del lavado
        self.cantLavados += 1

    def verificarTiempoLavado(self,tiempoPrendaNueva,tiempoLavado,nroDeLavado): #La ultima es tiempoLavado
        if tiempoPrendaNueva > tiempoLavado:
            self.lavados[nroDeLavado][0] = tiempoPrendaNueva

    def agregarPrenda(self,prendaNueva,tiempoPrendaNueva):
        if self.lavados == []:
            self.agregarPrimerPrendaDeLavado(prendaNueva,tiempoPrendaNueva)
        else:
            seLeAsignoUnLavado = False
            nroDeLavado = 0
            while not seLeAsignoUnLavado and nroDeLavado < self.cantLavados:
                if self.esCompatible(self.lavados[nroDeLavado][1],prendaNueva):
                    seLeAsignoUnLavado = True
                    self.lavados[nroDeLavado][1].append(prendaNueva)
                    self.verificarTiempoLavado(tiempoPrendaNueva,self.lavados[nroDeLavado][0],nroDeLavado) #La ultima es tiempoLavado
                nroDeLavado += 1

            if not seLeAsignoUnLavado:
                self.agregarPrimerPrendaDeLavado(prendaNueva,tiempoPrendaNueva)

        del(self.vectorLavadosYTiempos[-1])
        #TODO: Seria necesario ordenar lavados en funcione de su tiempo cada vez que se agrega algo?

    def asignarPrendasEnLavados(self):
        for i in range(self.cantPrendas-1,-1,-1):
            self.agregarPrenda(self.vectorLavadosYTiempos[i][0],self.vectorLavadosYTiempos[i][1])
