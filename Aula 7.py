# Aula 007.
# EX 5: Faça um Programa que leia um número inteiro e mostre o antecessor e o sucessor deste número.
n1 = int(input('Digite um Número Inteiro qualquer:'))
A = (n1 - 1)
S = (n1 + 1)
print('O antecessor de {} é {} e o sucessor é {}!'.format( n1, A, S))
#  Nota Deiizz
# EX 6 : Crie um algorítimo que leia um número e mostre seu dobro, triplo e raiz quadrada.
n2 = int(input('Digite outro Número:'))
D = (n2 * 2)
T = (n2 * 3)
R = (n2 ** (1/2))
print('O Dobro de {} é {}, O Triplo é {} e a Raiz Quadrada do Número digitado é {}'.format( n2, D, T, R))
# Nota mew
# EX 7 : Desenvolva um Programa que leia as duas notas de um Aluno e depois calcule a média
N1 = int(input('Digite sua nota do Primeiro bimestre:'))
N2 = int(input('Digite sua nota do Segundo bimestre:'))
M = (N1 + N2)/2
print('Sua média final é {}'.format(M))
#acertô
# EX 8 :Escreva um programa que leia um valor em metros e converta ele para centímetro e depois em milímetros
Me = int(input('Digite um valor numérico:'))
cm = Me*100
mm = Me*1000
print('{} m em centímetros é {} cm e em milímetros é {} mm'.format(Me, cm, mm))
# Ex 9 :Faça um programa que monte uma tabuada a partir de um número inteiro
n3 = int(input('Digite um número qualquer para montar uma tabuada:'))
print('='*20)
print('{:3} x {:3} = {:3}'.format(n3, 1, n3*1))
print('{:3} x {:3} = {:3}'.format(n3, 2, n3*2))
print('{:3} x {:3} = {:3}'.format(n3, 3, n3*3))
print('{:3} x {:3} = {:3}'.format(n3, 4, n3*4))
print('{:3} x {:3} = {:3}'.format(n3, 5, n3*5))
print('{:3} x {:3} = {:3}'.format(n3, 6, n3*6))
print('{:3} x {:3} = {:3}'.format(n3, 7, n3*7))
print('{:3} x {:3} = {:3}'.format(n3, 8, n3*8))
print('{:3} x {:3} = {:3}'.format(n3, 9, n3*9))
print('{:3} x {:3} = {:3}'.format(n3, 10, n3*10))
print('='*20)
#EX 10: Crie um programa que converta um valor em real para dólares. dólar = 4.84
r = int(input('Digite um valor em Real'))
Do = r/4.84
print('Atualmete o Valor de {} em Dólares é {}'.format(r, Do))
#Ex 11: Faça um Programa que leia a largura e altura de uma parede em metros e cdepois disso calcule a área e a quantidade de tinta necessária para pintá-la 
#(Considerando que cada litro de tinta pinta 2m^2)
L = int(input('Qual é a largura da parede ? '))
H = int(input('Qual é a Altura? '))
Ar = L*H
l = Ar/2
print('A área a ser pintada é de {} m^2 e será necessário usar {} litros de tinta'.format(Ar, l))
# EX 12: Faça um algorítimo que leia um preço de um produto e mostre esse mesmo valor com 5% de desconto
P = int(input('Qual é o preço do produto ?'))
des = P*5/100
vp = P - des
print('O produto custa {} reais e com o desconto de 5% passará a custar {} reais'.format(P, vp))
#Ex 13: Construa um algorítimo que calcule um salário com 15% de aumento
P = int(input('Quanto é o seu salário ?'))
au = P*15/100
vs = P + au
print('O seu salário é {} reais e com o aumento de 15% passará a ser {} reais'.format(P, vs))