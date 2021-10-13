from interface import ICalc

'''Classe concreta'''
class Somar(ICalc):
    def calcular(self, numero1: int, numero2: int) -> int:
        return numero1 + numero2
