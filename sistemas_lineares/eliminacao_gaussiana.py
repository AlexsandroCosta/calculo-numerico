matriz = []
b = []
n = 0 

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

    n = int(input('Número de linhas e colunas: '))

    print('Matriz estendida:')
    for i in range(n):
        while True:
            linha = [float(n) for n in input().split()]
            b.append(linha.pop())

            if len(linha) == n:
                break

            b.pop()
            print(f'Uma linha deve conter {n} colunas')

        matriz.append(linha)

    if input('Pivoteamento parcial (s/n)? ').lower() == 's':
        elimicacao(pivotea=True)
    else:
        elimicacao()

info = ''''
-> Quando digitar a matriz estendida precione ENTER ao final de cada linha 
   e um espaço entre cada número.
'''

main()

