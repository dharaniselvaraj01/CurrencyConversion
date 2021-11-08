import unittest
import fxcalculator as fx


class TestFXApp(unittest.TestCase):

    def test_unity(self):
        unity = fx.Unity("AUD","AUD")
        self.assertEqual(unity.calculate_conv_rate(),1)

    def test_non_cross(self):
        direct = fx.NonCross("AUD","USD")
        self.assertEqual(direct.calculate_conv_rate(),0.8371)
        inverted = fx.NonCross("USD","NZD")
        self.assertEqual(inverted.calculate_conv_rate(),1.2903)

    def test_cross_usd(self):
        cross_usd = fx.CrossUsd("AUD","DKK")
        self.assertEqual(cross_usd.calculate_conv_rate(),5.0575)

    def test_cross_eur(self):  
        cross_eur = fx.CrossEur("CZK","NOK")
        self.assertEqual(cross_eur.calculate_conv_rate(),0.3137)


    def test_convert_amt(self):
        converted_amt1 = fx.ConvertAmount(100,0.3137)
        self.assertEqual(converted_amt1.convert_amt(),31.37)
        converted_amt2 = fx.ConvertAmount(100,5.0575)
        self.assertEqual(converted_amt2.convert_amt(),505.75)

if __name__ == "__main__":
    unittest.main()