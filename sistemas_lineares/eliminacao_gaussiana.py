matriz = []
b = []
n = 0 

def construirMatriz():
    print('Digite as equações: ')
    while True:
        equa = input()

        if not equa:
            break

        aux = []
        ult = ''

        #remove o número que vem depois de x
        for i in equa.replace(' ', '0'):
            if ult != 'x':
                aux.append(i)
            ult = i
        
        equa = ''.join(aux)
        aux = []
        ult = '0'

        if equa[0] == 'x':
            aux.append('1')
        
        #adicona 1 onde tem apenas o x
        for v in equa.replace('x', ''):
            if v in '+-=' and ult in '+-':
                aux.append('1')

            aux.append(v)
            ult = v
        
        equa = ''.join(aux)
        linha = []
    
        if equa[0].isdigit():
            linha.append(int(equa[0]))

        for i, v in enumerate(equa):
            if v == '-':
                linha.append(int(equa[i+1])*-1)
            elif v == '+':
                linha.append(int(equa[i+1]))
            elif v == '=':
                matriz.append(linha)
                if equa[i+1] == '-':
                    b.append(int(equa[i+2])*-1)
                else:
                    b.append(int(equa[i+1]))
                break

    print('Matriz extendida:')
    exibiMatriz()

def exibiMatriz():
    tmax = max(max(max(len(f'{j}') for j in i)for i in matriz), max(len(f'{i}') for i in b))
    if tmax > 6:
        tmax = 6

    for ind, linha in enumerate(matriz):
        for elemento in linha:
            if len(str(elemento).split("."))==2 and str(elemento).split(".")[1] == '0':
                print(f'{elemento:{tmax+2}.0f}', end="")
            else:
                if len(f'{elemento}') > 6:
                    print(f'{elemento:{tmax+2}.4f}', end="")
                else:
                    print(f'{elemento:{tmax+2}}', end="")

        if len(str(b[ind]).split("."))==2 and str(b[ind]).split(".")[1] == '0':
            print(f' |{b[ind]:{tmax+2}.0f}', end="")
        else:
            if len(f'{b[ind]}') > 6:
                print(f' |{b[ind]:{tmax+2}.4f}', end="")
            else:
                print(f' |{b[ind]:{tmax+2}}', end="")
        print()
    print()

def pivoteamento(k):
    index = k
    for i in range(k+1, n):
        if abs(matriz[i][k]) > abs(matriz[index][k]):
            index = i

    matriz[k], matriz[index] = matriz[index], matriz[k]
    b[k], b[index] = b[index], b[k]

def resolucao():
    x = [0]*n

    for k in range(n-1, -1, -1):
        s = 0

        for j in range(k+1, n):
            s += matriz[k][j]*x[j]

        x[k] = (b[k]-s)/matriz[k][k]
            
    print("\nSolução para as variáveis x:")
    for i in range(n):
        print(f"x{i + 1} = {x[i]:.4f}")

def elimicacao(pivotea=False):
    for k in range(n-1):
        if pivotea:
            pivoteamento(k)

        for i in range(k+1, n):
            m = matriz[i][k]/matriz[k][k]

            print(f'M[{i+1}][{k+1}] = {m}')

            matriz[i][k] = 0

            for j in range(k+1, n):
                matriz[i][j] -= m * matriz[k][j]

            b[i] -= m*b[k]

        exibiMatriz()
    
    resolucao()

def main():
    global matriz, b, n

    construirMatriz()

    if input('Pivoteamento parcial (s/n)? ').lower() == 's':
        elimicacao(pivotea=True)
    else:
        elimicacao()

info = ''''
-> Quando digitar todas equações precissone ENTER para finalizar.
'''

main()

