import unittest
import fxcalculator as fx


class TestFXApp(unittest.TestCase):

    def test_unity(self):
        unity1 = fx.UnityInstance("AUD","AUD",100)
        self.assertEqual(unity1.calculate_converted_amt(),100.00)
        unity2 = fx.UnityInstance("JPY","JPY",100)
        self.assertEqual(unity2.calculate_converted_amt(),100.00)

    def test_non_cross(self):
        direct = fx.NonCrossInstance("AUD","USD",100)
        self.assertEqual(direct.calculate_converted_amt(),83.71)
        inverted = fx.NonCrossInstance("USD","NZD",100)
        self.assertEqual(inverted.calculate_converted_amt(),129.03)

    def test_cross_usd(self):
        cross_usd = fx.CrossUsdInstance("AUD","DKK",100)
        self.assertEqual(cross_usd.calculate_converted_amt(),505.75)

    def test_cross_eur(self):  
        cross_eur = fx.CrossEurInstance("CZK","NOK",100)
        self.assertEqual(cross_eur.calculate_converted_amt(),31.37)


if __name__ == "__main__":
    unittest.main()