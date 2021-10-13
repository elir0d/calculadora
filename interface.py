from abc import ABC, abstractmethod, abstractclassmethod
class ICalc(ABC):
    '''Interface responsável por implementar as classes/metodos concretos'''
    @abstractmethod
    def calcular(self, n1, n2):
        pass
