import somar, subtrair, dividir, multiplicar

'''Contexto que define qual operacão a interface irá utilizar'''

operacao = {
    '+': somar.Somar.soma_dois_numeros,
    '-': subtrair.Subtrair.subtrai_dois_numeros,
    '*': multiplicar.Multiplicar.multiplica_dois_numeros,
    '/': dividir.Dividir.divide_dois_numeros,
}