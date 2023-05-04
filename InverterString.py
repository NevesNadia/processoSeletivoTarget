
palavra = input('Digite uma palavra ou frase para ser invertida: ')

cont = len(palavra)
palavraInversa = ""

for letra in palavra:
   cont-=1
   palavraInversa += palavra[cont]

print(palavraInversa)