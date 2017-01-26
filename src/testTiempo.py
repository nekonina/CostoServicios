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
       self.tarifa = 2.0
       self.horas = 2
       self.tarifa =(2, 1)

    def tearDown(self):
        pass

    def testDiaManana(self):
        M = obtenerManana(self.dia)
        self.failUnlessEqual(M, datetime(2017,10,14))

    def test_calcularCosto(self):
        A = calcularCosto(self.tarifa,self.horas)
        self.failUnlessEqual(A, self.tarifa*self.horas)
        
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
        dia2 = date(2017,10,12)
        r = validarDiferencia(self.dia, dia2)
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
        r = round(tiempoServicio(inicio,fin),2)
        self.failUnlessEqual(r, 0.42)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDato']
    unittest.main()