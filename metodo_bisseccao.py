import math
import re

def rcbPrec():
    prec = input('Precisão: ')

    if '^' in prec:
        x = prec.split('^')
        return float(float(x[0])**float(x[1]))
    
def resFunc(func, n):
    if 'log' in func:
        i = func.index('l')
        x = math.log10(n)
        
        if func[i-1] == 'x':
            func = func.replace('xlog(x)', str(n)+'*'+str(x))
        else:
            func = func.replace('log(x)', str(x))

    func = re.split(r'\s*([-+*/])\s*', func.replace('x', '*'+str(n)))

    for i in range(0, len(func)):
        if func[i] == '':
            func[i] = '1'

        if func[i].find('^') != -1:
            exp = func[i].split('^')
            func[i] = f'{float(exp[0])**int(exp[1])}'

    return eval(''.join(map(str,func)))

def bissec(func, a, b, prec):
    if (b-a) > prec:
        cont = 1
        m = resFunc(func, a)

        print('{:^10}| {:^11} | {:^15} | {:^15}'.format('Iteração', 'x', 'f(x)', 'b-a'))

        while True:
            x = (a+b)/2
            fx = resFunc(func, x)

            if (m*fx) > 0:
                a = x
            else:
                b = x

            print(f'{cont:^10}| {x:.9f} | {fx:^15.8e} | {(b-a):^15.8e}')

            if (b-a) < prec:
                break

            cont += 1
    else:
        print('Os limites devem ter sinais opostos.')
        exit(0)
    

func = input('Função: ').replace(' ', '')
a = float(input('Intervalo a: '))
b = float(input('Intervalo b: '))
prec = rcbPrec()

bissec(func, a, b, prec)

