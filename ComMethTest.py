import unittest
import OperacionesComplejos as CoMe
import math

class TestCplxMethods(unittest.TestCase):
    def test_suma(self):
        c1 = (5.6, -8.9)
        c2 = (-3.4, 6.2)
        self.assertAlmostEqual(CoMe.sumCom(c1, c2)[0], 2.2)
        self.assertAlmostEqual(CoMe.sumCom(c1, c2)[1], -2.7)

    def test_suma2(self):
        c1 = (3, -9)
        c2 = (24, 8)
        self.assertAlmostEqual(CoMe.sumCom(c1, c2)[0], 27)
        self.assertAlmostEqual(CoMe.sumCom(c1, c2)[1], -1)

    def test_producto(self):
        c1 = (5, -5)
        c2 = (9, 7)
        self.assertAlmostEqual(CoMe.prodCom(c1, c2)[0], 80)
        self.assertAlmostEqual(CoMe.prodCom(c1, c2)[1], -10)

    def test_producto2(self):
        c1 = (-3, -5)
        c2 = (-7, 9)
        self.assertAlmostEqual(CoMe.prodCom(c1, c2)[0], 66)
        self.assertAlmostEqual(CoMe.prodCom(c1, c2)[1], 8)

    def test_sustraccion(self):
        c1 = (14.15, 3/4)
        c2 = (-54.9587, 9)
        self.assertAlmostEqual(CoMe.sustCom(c1, c2)[0], 69.1087)
        self.assertAlmostEqual(CoMe.sustCom(c1, c2)[1], (-33/4))

    def test_sustraccion2(self):
        c1 = (-6, 1)
        c2 = (-12, 88)
        self.assertAlmostEqual(CoMe.sustCom(c1, c2)[0], 6)
        self.assertAlmostEqual(CoMe.sustCom(c1, c2)[1], -87)

    def test_modulo(self):
        c = (4/(math.sqrt(2)), -5/(math.sqrt(2)))
        self.assertAlmostEqual(CoMe.modCom(c), math.sqrt(41/2))

    def test_modulo2(self):
        c = (14, -900)
        self.assertAlmostEqual(CoMe.modCom(c), math.sqrt(810196))

    def test_division(self):
        c1 = (-4, 5)
        c2 = (8, -2)
        self.assertAlmostEqual(CoMe.divCom(c1, c2)[0], -21/34)
        self.assertAlmostEqual(CoMe.divCom(c1, c2)[1], 8/17)

    def test_division2(self):
        c1 = (-3, -5)
        c2 = (-1, 2)
        self.assertAlmostEqual(CoMe.divCom(c1, c2)[0], -7/5)
        self.assertAlmostEqual(CoMe.divCom(c1, c2)[1], 11/5)

    def test_conjugado(self):
        c = (0, -12343.3544)
        self.assertAlmostEqual(CoMe.conjCom(c)[0], 0)
        self.assertAlmostEqual(CoMe.conjCom(c)[1], 12343.3544)

    def test_conjugado2(self):
        c = (76, 10000)
        self.assertAlmostEqual(CoMe.conjCom(c)[0], 76)
        self.assertAlmostEqual(CoMe.conjCom(c)[1], -10000)

    def test_conversion_cartpol(self):
        c = (0, -15)
        self.assertAlmostEqual(CoMe.convCartPol(c)[0], 15)
        self.assertAlmostEqual(CoMe.convCartPol(c)[1], (3*math.pi)/2)

    def test_conversion_cartpol2(self):
        c = (5, 6)
        self.assertAlmostEqual(CoMe.convCartPol(c)[0], math.sqrt(61))
        self.assertAlmostEqual(CoMe.convCartPol(c)[1], math.atan(6/5))

    def test_conversion_polcart(self):
        c = (100, math.pi/4)
        self.assertAlmostEqual(CoMe.convPolCart(c)[0], 50*math.sqrt(2))
        self.assertAlmostEqual(CoMe.convPolCart(c)[1], 50*math.sqrt(2))

    def test_conversion_polcart2(self):
        c = (49, math.pi)
        self.assertAlmostEqual(CoMe.convPolCart(c)[0], -49)
        self.assertAlmostEqual(CoMe.convPolCart(c)[1], 0)

    def test_fase(self):
        c = (15, 16)
        self.assertAlmostEqual(CoMe.faseCom(c), math.atan(16/15))

    def test_fase2(self):
        c = (765, 4324.67887)
        self.assertAlmostEqual(CoMe.faseCom(c), math.atan(4324.67887/765))


if __name__ == '__main__':
    unittest.main()