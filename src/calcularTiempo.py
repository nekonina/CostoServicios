'''
Created on 23 ene. 2017

@author: iri_m_000
'''
from datetime import*
import sys

def introDatos()-> (date, date):
    formato = "%d/%m/%Y %H:%M:%S"


    while True:
        fecha_desde = input("fecha(dd/mm/aaaa hh:mm:ss) de inicio del servicio: ")
        fecha_hasta = input("fecha (dd/mm/aaaa) de final de servicio")            
        fecha_desde = datetime.strptime(fecha_desde, formato)
        fecha_hasta = datetime.strptime(fecha_hasta, formato)
        try:
            assert(fecha_hasta.day-fecha_desde.day <= 7 and fecha_hasta.day-fecha_desde.day >= 0 )
            if(fecha_hasta.day == fecha_desde.day and fecha_desde.month==fecha_hasta.month 
                      and fecha_desde.year == fecha_hasta.year and fecha_desde.hour == fecha_hasta.hour):
                try:
                    assert(fecha_hasta.minutes - fecha_desde.minutes >= 15)
                except:
                    print('el tiempo minimo para un servicio es de 15 min')
            break
        
        except:
            print('el tiempo maximo para un servicio es de 7 dias')
            
    return(fecha_desde,fecha_hasta)

def tiempoServicio(fecha_desde: date, fecha_hasta: date) -> int:
    tiempoTotal = (fecha_hasta.day-fecha_desde.day)* 24
    tiempoMinSeg = (fecha_hasta.hour + (fecha_hasta.minute/60) + ((fecha_hasta.second/60)/60))- (fecha_desde.hour+ (fecha_desde.minute/60)+ ((fecha_desde.second/60)/60)) 
    tiempoTotal = tiempoTotal + tiempoMinSeg
    return(tiempoTotal)

if __name__ == '__main__':
    
    (fecha_desde, fecha_hasta) = introDatos()
    diaI = datetime.weekday(fecha_desde)
    diaF = datetime.weekday(fecha_hasta)
    