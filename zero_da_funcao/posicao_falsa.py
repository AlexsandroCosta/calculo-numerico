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

def falsa(func, a, b, prec1, prec2):
    if (b-a) > prec1:
        cont = 1
        m = resFunc(func, a)

        print('\n{:^10}| {:^11} | {:^15} | {:^15}'.format('Iteração', 'x', 'f(x)', 'b-a'))

        while True:
            fa = resFunc(func, a)
            fb = resFunc(func, b)

            x = (a*fb-b*fa)/(fb-fa)
            
            fx = resFunc(func, x)

            print(f'{cont:^10}| {x:.9f} | {fx:^15.8e} | {(b-a):^15.8e}')
            
            if abs(fx) < prec2:
                break

            if (m*fx) > 0:
                a = x
            else:
                b = x

            if (b-a) < prec1:
                x = (a*fb-b*fa)/(fb-fa)
                break

            cont += 1
    else:
        x = (a*fb-b*fa)/(fb-fa)

    print(f'\nE portanto x = {x:.9f} e f(x) = {fx:^15.8e}.\n')
    
info = '''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-INFORMAÇÕES-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-
Funções:
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
    func = input('\nDigite a função: ').replace(' ', '')
    a = float(input('Intervalo a: '))
    b = float(input('Intervalo b: '))
    prec1, prec2 = rcbPrec()

    falsa(func, a, b, prec1, prec2)

    if input('Digite 0 p/ encerrar ou 1 p/ continuar: ') == '0':
        break
