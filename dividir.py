from interface import ICalc

'''Classe concreta'''
class Dividir():
    def calcular(self, numero1: int, numero2: int) -> int:
        try:
          return numero1 / numero2
        except ZeroDivisionError:
          return None
