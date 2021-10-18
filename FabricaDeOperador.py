from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod
import somar, subtrair, multiplicar, dividir

'''Fábrica de operadores'''
class IOperadores(ABC):

    @abstractstaticmethod
    def cria_operador(self):
        pass

'''Classes concretas'''
class soma(IOperadores):
    def __init__(self):
        self.operador = '+'
        self.operacao = somar.Somar

    def cria_operador(self):
        return {'operador':self.operador, 'operacao':self.operacao}

class diminui(IOperadores):
    def __init__(self):
        self.operador = '-'
        self.operacao = subtrair.Subtrair

    def cria_operador(self):
        return {'operador':self.operador, 'operacao':self.operacao}

class multiplica(IOperadores):
    def __init__(self):
        self.operador = '*'
        self.operacao = multiplicar.Multiplicar

    def cria_operador(self):
        return {'operador':self.operador, 'operacao':self.operacao}

class divide(IOperadores):
    def __init__(self):
        self.operador = '/'
        self.operacao = dividir.Dividir

    def cria_operador(self):
        return {'operador':self.operador, 'operacao':self.operacao}

'''Classe responsável por fabricar os operadores'''
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

if __name__ == '__main__':
    OPERADOR = FabricarOperador.define_operador('+')
    print(OPERADOR)