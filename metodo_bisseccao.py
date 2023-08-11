import re

def resFunc(func, n):
    func = re.split(r'\s*([-+*/])\s*', func.replace('x', '*'+str(n)))

    for i in range(0, len(func)):
        if func[i] == '':
            func[i] = '1'

        if func[i].find('^') != -1:
            exp = func[i].split('^')
            func[i] = f'{float(exp[0])**int(exp[1])}'

    return eval(''.join(map(str,func)))

def rcbPrec():
    prec = input('Precisão: ')
    nums = prec.split('^')
    prec = float(int(nums[0])**int(nums[1]))
    return prec

func = input('Função: ').replace(' ', '')
a = float(input('Intervalo a: '))
b = float(input('Intervalo b: '))
prec = rcbPrec()

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
            x = (a+b)/2
            break

        cont+=1
else:
    x = a

print(f'\nx = {x:.9f} em {cont} iterações.')
