'''
Created on 23 ene. 2017

@author: iri_m_000
@author: alejodiazg
'''
from datetime import*
#import sys

MIN_MINUTES = 15
MIN_SECONDS = 60 * MIN_MINUTES

def introDatos()-> (date, date):
    formato = "%d/%m/%Y %H:%M:%S"
    fecha_desde = input("fecha(dd/mm/aaaa hh:mm:ss) de inicio del servicio: ")
    fecha_hasta = input("fecha (dd/mm/aaaa) de final de servicio")            
    fecha_desde = datetime.strptime(fecha_desde, formato)
    fecha_hasta = datetime.strptime(fecha_hasta, formato)      
    return(fecha_desde,fecha_hasta)

def tiempoServicio(fecha_desde: date, fecha_hasta: date) -> int:
    tiempoTotal = (fecha_hasta.day-fecha_desde.day)* 24
    tiempoMinSeg = (fecha_hasta.hour + (fecha_hasta.minute/60) + ((fecha_hasta.second/60)/60))- (fecha_desde.hour+ (fecha_desde.minute/60)+ ((fecha_desde.second/60)/60)) 
    tiempoTotal = tiempoTotal + tiempoMinSeg
    return(tiempoTotal)


#valida la diferencia entre dos fechas
def validarDiferencia(inicio , fin) -> bool:
    dif = fin - inicio
    if(dif.days < 0 or dif.days > 7):
        return False
    if(dif.days == 7 and dif.seconds > 0):
        return False
    if(dif.seconds < 0):
        return False
    return True

#funcion para validad si se cumplen los minutos minimos
def validarMinutosMinimos(inicio , fin) -> bool:
    dif = fin - inicio
    print(dif.seconds)
    if (dif.days == 0 and dif.seconds < MIN_SECONDS):
        return False
    return True

#oobtine el proximo dia
def obtenerManana(fecha) -> date:
    manana = fecha + datetime.timedelta(1)
    return manana

#calcula el costo de las horas trabajadas
def calcularCosto(tarifa , horas) -> float:
    return tarifa * horas

#obtiene la tarifa segun el dia de la semana
def obtenerTarifaDia(tarifas , diasemana) -> float:
    #segun el dia de la semana obtener la tarifa
    return 0.1

#calcula las tarifas de las horas trabajadas cada dia
def calcularParticionado(inicio , fin , tarifas) -> float:
    suma = 0.0
    dia = datetime.weekday(inicio)
    tarifa = obtenerTarifaDia(tarifas, dia)
    if(inicio.day != fin.day or inicio.month != fin.month or inicio.year != fin.year):
        siguiente = obtenerManana(inicio)
        horas = tiempoServicio(inicio , siguiente)
        suma = calcularCosto(tarifa , horas) + calcularParticionado(siguiente , fin)
    else:
        horas = tiempoServicio(inicio , fin)
        suma = calcularCosto(tarifa, horas)
    return suma
 
if __name__ == '__main__':
    while True:
        (fecha_desde, fecha_hasta) = introDatos()
        diaI = datetime.weekday(fecha_desde)
        diaF = datetime.weekday(fecha_hasta)
        
        if(validarDiferencia(fecha_desde, fecha_hasta)):
            print('las fecha son validas')
        
        if(validarMinutosMinimos(fecha_desde, fecha_hasta)):
            print('la cantidad de minutos minimos es valida')
        else:
            print('la cantidad de minutos minimos no es valida')
    
        print("fecha1: ", diaI)
        print("fecha1: ", diaF)
