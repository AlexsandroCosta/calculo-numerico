def exibiMatriz(matriz, b):
    print()
    for ind, linha in enumerate(matriz):
        for indc, elemento in enumerate(linha):
            if indc == 0:
                print(f'{elemento:.0f}', end="")
            else:
                print(f'{elemento:4.0f}', end="")
        print(f' |{b[ind]:4.0f}', end="")
        print()
    print()

def resolucao(matriz, b, n):
    x = [0]*n

    for k in range(n-1, -1, -1):
        s = 0

        for j in range(k+1, n):
            s += matriz[k][j]*x[j]

        x[k] = (b[k]-s)/matriz[k][k]
            
    print("\nSolução para as variáveis x:")
    for i in range(n):
        print(f"x{i + 1} = {x[i]}")

def elimicacao(matriz, b, n):
    for k in range(n-1):
        for i in range(k+1, n):
            m = matriz[i][k]/matriz[k][k]

            print(f'M[{i+1}][{k+1}] = {m}')

            matriz[i][k] = 0

            for j in range(k+1, n):
                matriz[i][j] -= m * matriz[k][j]

            b[i] -= m*b[k]

        exibiMatriz(matriz, b)
    
    resolucao(matriz, b, n)

def main():
    n = int(input('Número de linhas e colunas: '))

    matriz = []
    b = []

    print('Matriz estendida:')
    for i in range(n):
        while True:
            linha = [int(n) for n in input().split()]
            b.append(linha.pop())

            if len(linha) == n:
                break

            b.pop()
            print(f'Uma linha deve conter {n} colunas')

        matriz.append(linha)

    elimicacao(matriz, b, n)

info = ''''
-> Quando passar a matriz estendida precione ENTER ao final de cada linha 
   e um espaço entre cada número.
'''
main()

