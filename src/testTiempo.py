'''
Created on 23 ene. 2017

@author: iri_m_000
'''
import unittest
from datetime import*
from calcularTiempo import*

class Test(unittest.TestCase):


    def setUp(self):
       self.dia = date(2017,10,13)
       self.tarifa_e = 2.0
       self.horas = 2
       self.tarifa =(2, 1)

    def tearDown(self):
        pass

    def testDiaManana(self):
        M = obtenerManana(self.dia)
        self.failUnlessEqual(M, datetime(2017,10,14))

    def test_calcularCosto(self):
        A = calcularCosto(self.tarifa_e,self.horas)
        self.failUnlessEqual(A, self.tarifa_e*self.horas)
        
    def test_obtenerTarifaDia(self):
        caso1= obtenerTarifaDia(self.tarifa,1)
        caso2 = obtenerTarifaDia(self.tarifa,5)
        self.failUnlessEqual(caso1,2)
        self.failUnlessEqual(caso2,1)

    def test_validarMinutosMinimos(self):
        inicio = datetime(2017,10,14,15,20)
        fin = datetime(2017,10,14,15,30)
        res = validarMinutosMinimos(inicio, fin)
        self.failUnlessEqual(res, False)
        
        inicio = datetime(2017,10,14,15,20)
        fin = datetime(2017,10,14,15,35)
        res = validarMinutosMinimos(inicio, fin)
        self.failUnlessEqual(res, True)
        
    def test_validarDiferencia(self):
        dia2 = datetime(2017,10,12)
        dia1 = datetime(2017,10,14)
        r = validarDiferencia(dia1, dia2)
        self.failUnlessEqual(r, False)
        
        dia2 = date(2017,10,21)
        r = validarDiferencia(self.dia, dia2)
        self.failUnlessEqual(r, False)
        
        dia2 = date(2017,10,18)
        r = validarDiferencia(self.dia, dia2)
        self.failUnlessEqual(r, True)
        
    def test_tiempoServicio(self):
        inicio = datetime(2017,10,14,15,20)
        fin = datetime(2017,10,14,15,45)
        r = tiempoServicio(inicio,fin)
        self.failUnlessEqual(round(r,2), 0.42)
        
    def test_realidad(self):
        v1 = realidad(12.01)
        v2 = realidad(11.00)
        self.failUnlessEqual(v1,  13)
        self.failUnlessEqual(v2, 11)
        
    #prueba para intervalo que solo tiene tiempo de fin de semana
    def test_calcularParticionado(self):
        inicio = datetime(2017,1,14,15,20)
        fin = datetime(2017,1,15,23,45)
        r =  calcularParticionado(inicio,fin,self.tarifa)
        r1 = realidad(r)
        self.failUnlessEqual(r1, 33)
        
    #prueba para intervalo que solo tiene tiempo de dias de semana
    def test_calcularParticionado(self):
        inicio = datetime(2017,1,16,15,20)
        fin = datetime(2017,1,18,23,45)
        r =  calcularParticionado(inicio,fin,self.tarifa)
        r1 = realidad(r)
        self.failUnlessEqual(r1, 113)
        
    #prueba para intervalo que agarra un dia de semana y uno de fin de semana
    def test_calcularParticionado(self):
        inicio = datetime(2017,1,13,15,20)
        fin = datetime(2017,1,14,23,45)
        r =  calcularParticionado(inicio,fin,self.tarifa)
        r1 = realidad(r)
        self.failUnlessEqual(r1, 41)
        
    #prueba para intervalo que pasa de dia de semana a dia de semana pasando por el fin de semana
    def test_calcularParticionado(self):
        inicio = datetime(2017,1,12,15,20)
        fin = datetime(2017,1,16,23,45)
        r =  calcularParticionado(inicio,fin,self.tarifa)
        r1 = realidad(r)
        self.failUnlessEqual(r1, 161)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDato']
    unittest.main()