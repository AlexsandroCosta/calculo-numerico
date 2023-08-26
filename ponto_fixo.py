import math
import re

def rcbPrec():
    prec1 = input('Precisão 1: ').replace(' ', '')
    prec2 = input('Precisão 2 (Enter se for igual a 1º): ').replace(' ', '')

    if not prec2:
        prec2 = prec1

    prec1 = eval(prec1.replace('^', '**'))
    prec2 = eval(prec2.replace('^', '**'))

    return prec1, prec2
    
def lssc(func, n, op):
    if op in func:
        mod = False
        i = func.index(op[0])

        if func[i+len(op)+1] != 'x':
            n = float(func[func.index('(')+1])
            mod = True
        
        if op == 'log':
            x = math.log10(n)
        elif op == 'sqrt':
            x = math.sqrt(n)
        elif op == 'sen':
            x = math.sin(n)
        elif op == 'cos':
            x = math.cos(n)
        elif op == 'tg':
            x = math.tan(n)

        if func[i-1] not in '-+*/':
            if mod:
                return func.replace(f'{op}({func[i+len(op)+1]})', '*'+str(x))
            else:
                return func.replace(f'{op}(x)', '*'+str(x))
        else:
            if mod:
                return func.replace(f'{op}({func[i+len(op)+1]})', str(x))
            else:
                return func.replace(f'{op}(x)', str(x))

def resFunc(func, n):
    lista = ['log','sqrt','sen','cos', 'tg']

    for i in range(len(lista)):
        if lista[i] in func:
            func = lssc(func, n, lista[i])

    func = re.split(r'\s*([-+*/])\s*', func.replace('x', '*'+str(n)))

    for i in range(0, len(func)):
        if func[i] == '':
            func[i] = '1'
        elif func[i] == '(':
            func[i]= '(1'

        if func[i].find('^') != -1:
            exp = func[i].split('^')
            func[i] = f'{float(exp[0])**int(exp[1])}'

    return eval(''.join(map(str,func)))

def pontof(func, funci, inic, prec1, prec2):
    if abs(resFunc(func, inic)) > prec1:
        cont = 1

        print('\n{:^10}| {:^11} | {:^15}'.format('Iteração', 'x', 'f(x)'))

        while True:
            x = resFunc(funci, inic)
            
            fx = resFunc(func, x)

            print(f'{cont:^10}| {x:.9f} | {fx:^15.8e}')
            
            if abs(resFunc(func, x)) < prec1 or abs(x-inic) < prec2:
                break

            inic = x

            cont += 1
    else:
        x = inic

    print(f'\nE portanto x = {x:.9f} e f(x) = {fx:^15.8e}.\n')
    
info = '''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-INFORMAÇÕES-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-
Equações e Funções:
    Potenciação -> Use o (^) para elevar um número (Ex: x^3)
    Logaritmo -> Use log() para calcular o logaritmo na base 10 (Ex: log(x))
    Raiz quadrada -> sqrt() (Ex: sqrt(9))
    Seno -> sen() 
    Cosseno -> cos()
    Tangente -> tg()

Intervalos:
    Os intervalos podem incluir números inteiros ou decimais.
        Obs: Utilize o ponto (.) em vez da vírgula para representar números decimais (Ex: 2.5). 

Precisão:
    Use (*) em vez de (x) para multiplicação (Ex: 5*10^-7)       
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-
'''

print(info, end='')

while True:
    func = input('\nDigite a equação: ').replace(' ', '')
    funci = input('Digite a função de iteração: ').replace(' ', '')
    inic = float(input('Aproximação inicial: '))
    prec1, prec2 = rcbPrec()

    pontof(func, funci, inic, prec1, prec2)

    if input('Digite 0 p/ encerrar ou 1 p/ continuar: ') == '0':
        break