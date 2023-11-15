matriz = []
b = []
n = 0
p = []


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
        num = ''
        for j in equa[i+1:]:
          if j in '+-=':
            break
          num += j
        linha.append(int(num) * -1)
          
      elif v == '+':
        num = ''
        for j in equa[i+1:]:
          if j in '+-=':
            break
          num += j
        linha.append(int(num))

      elif v == '=':
        matriz.append(linha)
        if equa[i + 1] == '-':
          b.append(int(''.join(equa[i + 2:])) * -1)
        else:
          b.append(int(''.join(equa[i + 1:])))
        break

  print('Matriz extendida:')
  exibiMatriz()


def exibiMatriz(fatoracao=False):
  tmax = max(max(max(len(f'{j}') for j in i) for i in matriz),
             max(len(f'{i}') for i in b))
  if tmax > 6:
    tmax = 6

  for ind, linha in enumerate(matriz):
    for elemento in linha:
      if len(str(elemento).split(".")) == 2 and str(elemento).split(
          ".")[1] == '0':
        print(f'{elemento:{tmax+2}.0f}', end="")
      else:
        if len(f'{elemento}') > 6:
          print(f'{elemento:{tmax+2}.4f}', end="")
        else:
          print(f'{elemento:{tmax+2}}', end="")
    if not fatoracao:
      if len(str(b[ind]).split(".")) == 2 and str(b[ind]).split(".")[1] == '0':
        print(f' |{b[ind]:{tmax+2}.0f}', end="")
      else:
        if len(f'{b[ind]}') > 6:
          print(f' |{b[ind]:{tmax+2}.4f}', end="")
        else:
          print(f' |{b[ind]:{tmax+2}}', end="")
    print()
  print()


def pivoteamento(k,fatoracao=False):
  
  index = k
  for i in range(k + 1, n):
    if abs(matriz[i][k]) > abs(matriz[index][k]):
      index = i

  matriz[k], matriz[index] = matriz[index], matriz[k]
  
  if not fatoracao:
    b[k], b[index] = b[index], b[k]
  else:
    po=[[1 if j==i else 0 for j in range(n)] for i in range(n)]
    po[k], po[index] = po[index], po[k]
    p.append(po)
    
    
def fatoracaoLu(pivotea=False):
  if pivotea:      
    pzao = p[-1]
    #multiplica as matrizes pra descobrir o pzão
    for i in range(len(p)-2, -1, -1):
      a = p[i]
      linha = []
      for j in range(n):
        aux = []
        for k in range(n):
          soma = 0
          for l in range(n):
            soma += pzao[j][l]*a[l][k]
          aux.append(soma)
        linha.append(aux)
      pzao = linha

    #muda a linha dos resltados das equações    
    aux = []
    for i in range(n):
      soma = 0
      for j in range(n):
        soma += pzao[i][j]*b[j]
      aux.append(soma)

    for i in range(n):
      b[i] = aux[i]
  
  l = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
  
  #constroi a matriz L
  for i, var1 in enumerate(matriz):
    for j, var2 in enumerate(var1):
      if i > j:
        l[i][j] = var2
        matriz[i][j] = 0

  resolucao(l, y=True)


def resolucao(matriz=matriz, y=False):
  x = [0] * n

  if y:
    for k in range(0, n):
      s = 0

      for j in range(0, n):
        s += matriz[k][j] * x[j]

      x[k] = (b[k] - s) / matriz[k][k]

    for i in range(n):
      b[i] = x[i]
    
  else:
    for k in range(n - 1, -1, -1):
      s = 0

      for j in range(k + 1, n):
        s += matriz[k][j] * x[j]

      x[k] = (b[k] - s) / matriz[k][k]
    else:
      print("\nSolução para as variáveis x:")
      for i in range(n):
        print(f"x{i + 1} = {x[i]}")


def eliminacao(pivotea, fatoracao):
  for k in range(n - 1):
    if pivotea:
      pivoteamento(k,fatoracao)

    for i in range(k + 1, n):

      m = matriz[i][k] / matriz[k][k]

      print(f'M[{i+1}][{k+1}] = {m}')

      if fatoracao:
        matriz[i][k] = m
      else:
        matriz[i][k] = 0

      for j in range(k + 1, n):
        matriz[i][j] -= m * matriz[k][j]

      if not fatoracao:
        b[i] -= m * b[k]

    exibiMatriz(fatoracao)
   
  if fatoracao:
    fatoracaoLu(pivotea)

  resolucao()


def main():
  global matriz, b, n, p
  pivotea = fatoracao = False
  
  construirMatriz()

  n = len(matriz[0])

  if input('Fatoração LU (s/n)? ').lower() == 's':
    fatoracao = True

  if input('Pivoteamento parcial (s/n)? ').lower() == 's':
    pivotea = True

  eliminacao(pivotea, fatoracao)


info = ''''
Gaussiana sem pivotemaente (pode fazer com)
x1+x2+ +3x3=4
2x1+x2-x3+x4=1
3x1-x2-x3+2x4=-3
-x1+2x2+3x3-x4=4

com pivoteamento
2x1+4x2+3x3=1
x1+2x2-2x3=11
4x1+4x2+3x3=3

2x1+2x2+x3+x4=7
x1-x2+2x3-x4=1
3x1+2x2-3x3-2x4=4
4x1+3x2+2x3+x4=12

LU Sem pivoteamento
3x1+2x2+4x3=1
x1+x2+2x3=2
4x1+3x2+2x3=3

LU Com pivoteamento
3x1-4x2+x3=9
x1+2x2+2x3=3
4x1+ -3x3=-2

LU Sem pivoteamento
x1+x2+x3=-2
2x1+x2-x3=1
2x1-x2+x3=3

1,-2,-1

-> Digitar todas as equações e precissone ENTER para finalizar.
-> Deixe um espaço onde não houver 'x'. Exemplo: x1+x2+ +3x4=4
'''

main()