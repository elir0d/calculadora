from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod
import somar, subtrair, multiplicar, dividir

'''Fábrica de operadores'''

class IOperadores(ABC):

    @abstractstaticmethod
    def cria_operador(self):
        pass


class soma(IOperadores):
    def cria_operador(self):
        return somar.Somar

class diminui(IOperadores):
    def cria_operador(self):
        return subtrair.Subtrair

class multiplica(IOperadores):
    def cria_operador(self):
        return multiplicar.Multiplicar

class divide(IOperadores):
    def cria_operador(self):
        return dividir.Dividir

class FabricarOperador(object):

    @staticmethod
    def define_operador(tipo):
        try:
            if tipo == '+': return soma().cria_operador()
            elif tipo == '-': return diminui().cria_operador()
            elif tipo == '*': return multiplica().cria_operador()
            elif tipo == '/': return divide().cria_operador()
            raise AssertionError('Operador inválido')
        except AssertionError as err:
            print(err)

fab = FabricarOperador