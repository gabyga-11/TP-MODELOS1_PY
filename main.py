import ProcesadorArchivo

def main():
    datos = ProcesadorArchivo.ProcesadorArchivo("entrada.txt", "r")
    datos.procesar()

#LO QUE SIGUE AHORA ES
# UNA FUNCION QUE SE ENCARGUE DE EMPAREJAR LAS PRENDAS CON MAYOR TIEMPO (Si es que son compatibles)
# Se crea una matriz diferente donde cada fila es el nro_lavado y c/elem son los datos PRENDA-TIEMPO
# Se guarda el ultimo elemento de vectorLavados para la matriz [[[2,10]]] y se saca de vectorLAvados
# (hay una variable contador del nro lavado)
# Se mira al anteultimo y nos fijamos si es compatible. Si lo es, se agrega [[[2,10],[7,10]]] y
# se saca de vectorLAvados. Si no es compatible, se sigue recorriendo la lista hasta encontrar
# Si no hay compatibilidad, se arranca un lavado nuevo y comenzamos desde el ultimo elemento que haya
main()
