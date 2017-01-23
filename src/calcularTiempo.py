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
            break
        
        except:
            print('el tiempo maximo para un servicio es de 7 dias')
            
        
    return(fecha_desde,fecha_hasta)
 

if __name__ == '__main__':
    
    (fecha_desde, fecha_hasta) = introDatos()
    diaI = datetime.weekday(fecha_desde)
    diaF = datetime.weekday(fecha_hasta)
    
    print("fecha1: ", diaI)
    print("fecha1: ", diaF)