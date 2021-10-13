import os
import interface
import contexto

from somar import Somar
from subtrair import Subtrair
from multiplicar import Multiplicar
from dividir import Dividir
'''Classe Calculadora que contém o programa principal'''
class Calculadora(object):

    def __init__(self, numero1, numero2):
        self.__numero1 = numero1
        self.__numero2 = numero2

    def get_numero1(self):
        return self.__numero1

    def get_numero2(self):
        return self.__numero2

'''Classe que obtem o Contexto'''
class executarCalculo(object):
    def realiza_calculo(self, numero1: int, numero2: int, icalc) -> int:
        operacao = icalc.calcular(self, numero1, numero2)
        return operacao

numero1  = None
numero2  = None
operacao = None
operador = ''

def main():

    global numero1, numero2, operador, operacao

    os.system('clear')
    numero1  = input('digite o primeiro numero: ')
    os.system('clear')
    numero2  = input('digite o segundo numero: ')
    os.system('clear')
    operador = input('Digite o operador: ')
    os.system('clear')

    operacao = contexto.operacao[operador]
                
if __name__ == '__main__':
    main()
    ec = executarCalculo()
    calc = Calculadora(numero1, numero2)
    resultado = ec.realiza_calculo(calc.get_numero1(), calc.get_numero2(), operacao)
    print(f'{numero1} {operador} {numero2} =', resultado, end=' ')
