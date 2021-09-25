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
        posPrendaEnElLavado = 0

        if prendaNueva==2:
            print("")

        while compatible and posPrendaEnElLavado < len(lavado):
            if self.matrizIncompatib[prendaNueva-1][lavado[posPrendaEnElLavado]-1]:
                compatible = False
                print(lavado[posPrendaEnElLavado], "no es compatible con la prenda",prendaNueva)
            posPrendaEnElLavado += 1

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
                print("Es compatible",prendaNueva,"con",self.lavados[nroDeLavado][1],"?",self.esCompatible(self.lavados[nroDeLavado][1],prendaNueva))
                if self.esCompatible(self.lavados[nroDeLavado][1],prendaNueva):
                    seLeAsignoUnLavado = True
                    self.lavados[nroDeLavado][1].append(prendaNueva)
                    self.verificarTiempoLavado(tiempoPrendaNueva,self.lavados[nroDeLavado][0],nroDeLavado) #La ultima es tiempoLavado
                nroDeLavado += 1

            if not seLeAsignoUnLavado:
                self.agregarPrimerPrendaDeLavado(prendaNueva,tiempoPrendaNueva)

        print("---------------------------")
        print(self.lavados)
        del(self.vectorLavadosYTiempos[-1])
        print(self.vectorLavadosYTiempos)
        print("---------------------------")


    def asignarPrendasEnLavados(self):
        for i in range(self.cantPrendas-1,-1,-1):
            self.agregarPrenda(self.vectorLavadosYTiempos[i][0],self.vectorLavadosYTiempos[i][1])

    def obtenerTiempoTotalLavado(self,cantLavarropas):
        tiempos=[]
        for i in range(cantLavarropas):
            tiempoAcum = 0
            for nroPrenda in range(i,self.cantLavados,i+1): #TODO: Aca ver que no quede out of range
                tiempoAcum += self.lavados[nroPrenda][0]


            tiempos.append()
