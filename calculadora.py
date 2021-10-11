import os



class Calculadora():

    numero_atual = '0'
    primeiro_numero_digitado = None
    aguarda_proximo_numero = False
    operador = None

    def coletaNumeroDigitado(self, n):
        if self.aguarda_proximo_numero:
            self.numero_atual = n
            self.aguarda_proximo_numero = False
        else:
           self.numero_atual = n if self.numero_atual == '0' else n


    def adicionaPontoDecimal(self):
        if '.' not in self.numero_atual:
          self.numero_atual += '.'


    def operacoes(self, op, segundaOp):
            if op == '+':
                self.primeiro_numero_digitado += segundaOp
                return self.primeiro_numero_digitado
            if op == '-':
                self.primeiro_numero_digitado -= segundaOp
                return self.primeiro_numero_digitado
            if op == '*':
                self.primeiro_numero_digitado *= segundaOp
                return self.primeiro_numero_digitado
            if op == '/':
                self.primeiro_numero_digitado /= segundaOp
                return self.primeiro_numero_digitado
            if op == '=':
                return segundaOp

    def fazOperacao(self, op):
        if self.primeiro_numero_digitado == None:
            self.primeiro_numero_digitado = int(self.numero_atual)
        elif self.operador:
            resultado = self.operacoes(self.operador, int(self.numero_atual))
            self.numero_atual = str(resultado)
            self.primeiro_numero_digitado = resultado
        
        self.operador = op
        self.aguarda_proximo_numero = True

    def limpar(self):
        self.numero_atual = '0'
        self.primeiro_numero_digitado = None
        self.aguarda_proximo_numero = False
        self.operador = None

def main():
    calc = Calculadora()
    numero1 = input('digite o primeiro numero: ')
    calc.coletaNumeroDigitado(numero1)
    operador = input('digite um operador: ')
    calc.fazOperacao(operador)
    numero2 = input('digite o segundo numero: ')
    calc.coletaNumeroDigitado(numero2)

    print(f'{numero1} {operador} {numero2} =', end=' ')
    calc.fazOperacao(operador)
    print(calc.numero_atual)

if __name__ == '__main__':
    main()