import somar, subtrair, dividir, multiplicar

'''Contexto que define qual operacão a interface irá utilizar'''

operacao = {
    '+': somar.Somar,
    '-': subtrair.Subtrair,
    '*': multiplicar.Multiplicar,
    '/': dividir.Dividir,
}