import contexto
from abc import ABC, abstractmethod, abstractclassmethod


class InterfaceCalculadora(ABC):
    '''Interface responsável por implementar as classes/metodos concretos'''
    @abstractmethod
    def calcular(self, n1, n2):
        return contexto.operacao[self](0, n1, n2)
