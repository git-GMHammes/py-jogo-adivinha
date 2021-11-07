# Listas em Python
# append, insert, pop, del, clear, externd
"""
valorBoleano = True
valorInteiro = 10
valorFloat = 10.5
valorString1 = 'Textos'
variáveis = ('')
lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4, 'Gustavo Hammes', True, 10.3]  # Pode colocar funções e Classes!
print(lista2[4])
print(lista2)
print(lista2[1:4])
print(lista2[:3])
print(lista2[3:])
print(lista2[::2])
#
lista3 = ['A', 'B', 'C', 'D', 'E']
print(lista3[4])
valorString2 = 'ABCDE'
print(valorString2[2])
#
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = ['@', '#', '$']
print(l1 + l3 + l2)
l3.extend(l1)  # Atenção que tem que exibir a l3
print(l3)
#
l1.extend('a')  # Atenção que tem que exibir a l3
print(l1)
#
l2.append('alegria')
print(l2)
#
print(l3)
l3.insert(2, 'rato')
print(l3)
l3.pop(-3)
print(l3)
#
l3 = [1, 2, 3, 4, 5, "A", "B", "C", "D", "E"]
l2 = [1, 2, 3, 4, 5, 6, 7]
print(l3)
del (l3[:2])
print(l3)
#
print(max(l2))
print(min(l2))
#
import random
l5 = list(range(1, 10))
r5 = random.random()
print(r5)
#
l4 = list(range(1, 10))
print(l4)
print(max(l4))
print(min(l4))
#
l6 = list(range(0, 71, 7))
print(l6)
for valor in l6:
    print(valor)
#
misto = ["String", True, 10, -1.5]
for b in misto:
    print(f'"{b}" é {type(b)}')
"""
# Jogo de adivinhação
secreto = "Malandro"
digitadas = []
chances = 5
while True:  # Laço infinito com True
    print()
    if chances <= 0:  # conta os erros até 3 vezes!
        print('Você perdeu!!!')
        print()
        break
    else:
        print(f'Você ainda têm: {chances} tentativas!')  # apresemta as chances restantes
    letra = input('Digite uma letra: ')  # Input que recebe as letras
    if len(letra) > 1:  # Teste de apenas uma letra
        print('Somente uma letra!!')
        continue
    digitadas.append(letra)  # Append na variável digitadas
    if letra in secreto:  # decisão e encontrando a letra digitada na palavra secreta
        print(f'Acertou Mizeravi. Letra: {letra}')
    else:
        print(f'Erroooooouuuu! Letra: {letra}')
        digitadas.pop()  # retira, caso a ultima letra não seja a correta
        chances -= 1
    tempG = ''  # Variável temporária para montar a palavra
    #
    # FOR para montar a palavra
    #
    for letraSecreta in secreto:  # montar a palavra secreta com a lista que foi digitada
        if letraSecreta in digitadas:  # se letra secreta estiver dentro da lista digiadas
            tempG += letraSecreta  # Variável temporária recebe letra secreta
        else:
            tempG += '*'  # Se não coloque um asterisco no lugar da letra
    #
    # fim do FOR que monta a palavra
    #
    if tempG == secreto:  # se a variável temporária for igual a palavra secreta
        print()
        print(f'VC venceu!!!. Palara Secreta: {secreto}')
        break  # Pare o laço de repetição
    else:  # Se não
        print(tempG)  # Exiba a variável temporária

print(f'Quais foram as letras que vc acertou:')
print(digitadas)
