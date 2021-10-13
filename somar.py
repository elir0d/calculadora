from interface import ICalc

'''Classe concreta'''
class Somar(ICalc):
    def calcular(self, numero1, numero2):
        return numero1 + numero2
