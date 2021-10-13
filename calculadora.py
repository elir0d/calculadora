import os
import somar
import interface as ICalc

'''Classe Calculadora que contém o programa principal'''
class Calculadora():

    def main():
        os.system('clear')
        numero1  = input('digite o primeiro numero: ')
        os.system('clear')
        numero2  = input('digite o segundo numero: ')
        os.system('clear')
        operador = input('Digite o operador: ')
        os.system('clear')
        
        contexto = operador
        calcular = ICalc.InterfaceCalculadora.calcular(operador, int(numero1), int(numero2))

        print(f'{numero1} {operador} {numero2} =', calcular, end=' ')
        
if __name__ == '__main__':
    calc = Calculadora
    calc.main()