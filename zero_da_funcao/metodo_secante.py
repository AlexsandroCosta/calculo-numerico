import math
import re

def precisao():
    prec1 = input('Precisão 1: ').replace(' ', '')
    prec2 = input('Precisão 2 (Enter se for igual a 1°): ').replace(' ', '')

    if prec2 == '':
        prec2 = prec1
    
    return eval(prec1.replace('^', '**')), eval(prec1.replace('^', '**'))

def sctl(func):
    lista = ['^','sen','cos','tg','log','sqrt','e']

    for i in lista:
        if i in func:
            if i == '^':
                func = func.replace(i, '**')
            if i == 'sen':
                func = func.replace(i, 'math.sin')
            elif i == 'tg':
                func = func.replace(i, 'math.tan')
            elif i == 'e':
                func = func.replace(i, str(math.e))
            else:
                func = func.replace(i, f'math.{i}')

    return func

def resFunc(func, n):
    func = re.split(r'\s*([x])\s*', sctl(func))
    for i in range(0, len(func)):
        if i > 0 and func[i] == 'x':
            if func[i-1] != '' and func[i-1][-1].isnumeric():
                func[i] = func[i].replace('x', '*x')
    
    func = (''.join(func)).replace('x', str(n))

    return eval(func)

def secante(func, x0, x1, prec1, prec2):
    if abs(resFunc(func, x0)) >= prec1:
        if abs(resFunc(func, x1)) >= prec1 and abs(x1-x0) >= prec2:
            cont=0
            
            print('\n{:^10}| {:^11} | {:^15}'.format('Iteração', 'x', 'f(x)'))

            while cont <= 50:
                fx0 = resFunc(func, x0)
                fx1 = resFunc(func, x1)

                print(f'{cont:^10}| {x0:.9f} | {fx0:^15.8e}')

                x2 = x1 - (fx1/(fx1-fx0))*(x1-x0)

                if abs(resFunc(func, x2)) < prec1 or abs(x2-x1) < prec2:
                    x0 = x2
                    fx0 = resFunc(func, x0)
                    cont+=1
                    print(f'{cont:^10}| {x0:.9f} | {fx0:^15.8e}')
                    break

                x0 = x1
                x1 = x2
                cont+=1          

            if cont >= 50:
                print('\nMáximo de iterações atingido.')
        else:
            x0 = x1

    print(f'\nAssim, x = {x0:.9f} e f(x) = {fx0:^15.8e}.\n')
           

info = '''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-INFORMAÇÕES-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-
ATENÇÃO: Antes de executar o programa, é necessário instalar a biblioteca Sympy.

Funções:
    Potenciação -> Use o (^) para elevar um número (Ex: x^3)
    Logaritmo -> Use log(valor,base) para calcular o logaritmo (Ex: log(x,10))
    Raiz quadrada -> sqrt() (Ex: sqrt(9))
    Seno -> sen() 
    Cosseno -> cos()
    Tangente -> tg()

Precisão:
    Use (*) em vez de (x) para multiplicação (Ex: 5*10^-7)       
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-
'''

print(info, end='')

while True:
    func =  input('\nDigite a função: ').replace(' ', '')
    x0 = float(input('x0: '))
    x1 = float(input('x1: '))
    prec1, prec2 = precisao()

    secante(func, x0, x1, prec1, prec2)

    if input('Digite 0 p/ encerrar ou 1 p/ continuar: ') == '0':
            break
