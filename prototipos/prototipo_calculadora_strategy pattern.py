import abc

class Calculadora(object):

    def __init__(self, numero1, numero2):
        self.__numero1 = numero1
        self.__numero2 = numero2

    def get_numero1(self):
        return self.__numero1

    def get_numero2(self):
        return self.__numero2

class ICalc(metaclass=abc.ABCMeta):
    '''Interface responsável por implementar as classes/metodos concretos'''
    @abc.abstractmethod
    def calcular(self, n1, n2):
        pass

class Somar(ICalc):
    def calcular(self, numero1, numero2):
        return numero1 + numero2
    
class executarCalculo(object):
    def realiza_calculo(self, numero1, numero2, icalc):
        resultado = icalc.calcular(self, numero1, numero2)
        print(resultado)

ec = executarCalculo()
calc = Calculadora(1, 2)
ec.realiza_calculo(calc.get_numero1(), calc.get_numero2(), Somar)

