import unittest
import FabricaDeOperador as fab
import calculadora as calc

ef = calc.executaFabrica()
class Testes(unittest.TestCase):
    def test_deveria_somar_dois_numeros_e_retornar_4(self):
        operacao = ef.fabrica_operador('+')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 2, 2, operacao), 4)

    def test_deveria_subtrair_2_de_4_e_retornar_2(self):
        operacao = ef.fabrica_operador('-')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 4, 2, operacao), 2)

    def test_deveria_multiplicar_dois_numeros_e_retornar_6(self):
        operacao = ef.fabrica_operador('*')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 2, 3, operacao), 6)

    def test_deveria_dividir_dois_numeros_e_retornar_2(self):
        operacao = ef.fabrica_operador('/')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 10, 5, operacao), 2)

    def test_deveria_retornar_None_para_divisoes_por_0(self):
        operacao = ef.fabrica_operador('/')
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 0, 0, operacao), None)
        self.assertEqual(calc.executaCalculo.realiza_calculo(self, 2, 0, operacao), None)

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
    unittest.TextTestRunner(verbosity=2,failfast=False).run(suite)

if __name__ == '__main__':
    runTests()

