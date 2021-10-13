from abc import ABC, abstractmethod, abstractclassmethod
class ICalc(ABC):
    '''Interface responsável por implementar as classes/metodos concretos'''
    @abstractmethod
    def calcular(self, numero1: int, numero2: int) -> int:
        pass
