
nColsultado = int(input("Digite um número inteiro para saber se ele pertence à sequencia de Fibonacci: "))

n1 = int(0)
n2 = int(1)
n3 = int(0)

while nColsultado > n3:
    n3 = n1 + n2
    n1 = n2
    n2 = n3

if nColsultado == 0 or nColsultado == 1:
    print ('O número digitado pertence à sequência de Fibonacci.')

elif nColsultado == n3:
    print ('O número digitado pertence à sequência de Fibonacci.')

else:
    print ('O número digitado não pertence à sequência de Fibonacci.')
