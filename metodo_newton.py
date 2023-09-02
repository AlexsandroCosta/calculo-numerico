import math
import re
import sympy as sp

def precisao():
    prec1 = input('Precisão 1: ').replace(' ', '')
    prec2 = input('Precisão 2 (Enter se for igual a 1°): ').replace(' ', '')

    if prec2 == '':
        prec2 = prec1
    
    return eval(prec1.replace('^', '**')), eval(prec1.replace('^', '**'))

def sctl(func, v=0):
    lista = ['^','sen', 'sin','cos','tg','log','sqrt','e']

    if v:
        for i in lista:
            if i in func:
                if i == '^':
                    func = func.replace(i, '**')
                elif i == 'sen':
                    func = func.replace(i, 'sin')
                elif i == 'tg':
                    func = func.replace(i, 'tan')
                elif i == 'e':
                    func = func.replace(i, str(math.e))
    else:
        for i in lista:
            if i in func:
                if i == '^':
                    func = func.replace(i, '**')
                if i == 'sen' or i == 'sin':
                    func = func.replace(i, 'math.sin')
                elif i == 'tg':
                    func = func.replace(i, 'math.tan')
                elif i == 'e':
                    func = func.replace(i, str(math.e))
                else:
                    func = func.replace(i, f'math.{i}')

    return func

def resFunc(func, n=''):
    func = re.split(r'\s*([x])\s*', sctl(func))
    for i in range(0, len(func)):
        if i > 0 and func[i] == 'x':
            if func[i-1] != '' and func[i-1][-1].isnumeric():
                func[i] = func[i].replace('x', '*x')
    
    func = (''.join(func).replace('x', str(n))

    return eval(func)

def derivFunc(func, n):

    func = re.split(r'\s*([x])\s*', sctl(func, 1))
    for i in range(0, len(func)):
        if i > 0 and func[i] == 'x':
            if func[i-1] != '' and func[i-1][-1].isnumeric():
                func[i] = func[i].replace('x', '*x')

    func = ''.join(func)

    return str(sp.diff(sp.sympify(func), sp.symbols('x'))).replace('x', str(n))

def newton(func, inic, prec1, prec2):
    if abs(resFunc(func, inic)) >= prec1:
        cont=0
        
        print('\n{:^10}| {:^11} | {:^15}'.format('Iteração', 'x', 'f(x)'))

        while True:
            fx = resFunc(func, inic)

            print(f'{cont:^10}| {inic:.9f} | {fx:^15.8e}')

            dfx = resFunc(derivFunc(func, inic))
            x = inic - (fx/dfx)

            if abs(resFunc(func, x)) < prec1 or abs(x-inic) < prec2:
                inic=x
                fx = resFunc(func, inic)
                cont+=1
                print(f'{cont:^10}| {inic:.9f} | {fx:^15.8e}')
                break
            
            inic = x
            cont+=1

    print(f'\nAssim, x = {inic:.9f} e f(x) = {fx:^15.8e}.\n')
           

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
    inic = float(input('Aproximação inical: '))
    prec1, prec2 = precisao()

    newton(func, inic, prec1, prec2)

    if input('Digite 0 p/ encerrar ou 1 p/ continuar: ') == '0':
            break
