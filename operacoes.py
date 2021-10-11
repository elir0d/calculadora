import calculadora as calc

class Operacoes():

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