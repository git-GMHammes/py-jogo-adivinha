print(f'\n Jogo de adivinhação')
#
secreto = "sucesso"
digitadas = []
chances = 5
while True:  # Laço infinito com True
    if chances <= 0:  # conta os erros até 3 vezes!
        print('\n Você perdeu!!!\n ')
        break
    else:
        # apresemta as chances restantes
        print(f'Você possui: {chances} tentativas!')
    letra = input('Digite uma letra: ')  # Input que recebe as letras
    if len(letra) > 1:  # Teste de apenas uma letra
        print('Somente uma letra!!')
        continue
    digitadas.append(letra)  # Append na variável digitadas
    if letra in secreto:  # decisão e encontrando a letra digitada na palavra secreta
        print(f'\n Acertou Mizeravi. Letra: {letra}\n ')
    else:
        print(f'\n Erroooooouuuu! Letra: {letra}\n ')
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
        print(f'\n VC venceu!!!. Palara Secreta: {secreto}')
        break  # Pare o laço de repetição
    else:  # Se não
        print(f'{tempG}\n')  # Exiba a variável temporária

print(f'\n Quais foram as letras que vc acertou: {digitadas}\n')
