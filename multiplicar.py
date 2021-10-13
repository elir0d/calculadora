from interface import ICalc

'''Classe concreta'''
class Multiplicar():
    def calcular(self, numero1: int, numero2: int) -> int:
        return numero1 * numero2