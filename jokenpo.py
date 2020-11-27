from random import randint
from time import sleep
import six

opcoes = ('Pedra', 'Papel','Tesoura')
pc = randint(0,2)


print('PEDRA, PAPEL OU TESOURA?!!')
print('=' * 35)
print('''Opções:
      [0] - Pedra
      [1] - Papel
      [2] - Tesoura''')
print('=' * 35)
escolha = (input('Qual você escolhe? '))
while(isinstance(escolha, six.string_types)):
    print('=' * 35)
    print('''APENAS ESTAS OPÇÕES:
      [0] - Pedra
      [1] - Papel
      [2] - Tesoura''')
    print('=' * 35)
    escolha = (input('Qual você escolhe? '))
    if(escolha == '0' or escolha == '1' or escolha == '2'):
        escolha = int (escolha)
print('=' * 35)
print('PEEDRA')
sleep(1)
print('PAPEEEL')
sleep(1)
print('TESOUUUURA')
print('=' * 35)
if pc == 0:
    if escolha == 0:
        print('Empate!')
        print('=' * 35)
    elif escolha == 1:
        print('Jogador Venceu -.-')
        print('=' * 35)
    elif escolha == 2:
        print('Venci otário KKKK!')
        print('=' * 35)
    else:
        print('Para de tentar achar erro, coisa chata >:(')
        print('=' * 35)
elif pc == 1:
    if escolha == 0:
        print('Venci otário KKKK!')
        print('=' * 35)
    elif escolha == 1:
        print('Empate!')
        print('=' * 35)
    elif escolha == 2:
        print('Jogador Venceu -.-')
        print('=' * 35)
    else:
        print('Para de tentar achar erro, coisa chata >:(')
        print('=' * 35)
elif pc == 2:
    if escolha == 0:
        print('Jogador venceu -.-')
        print('=' * 35)
    elif escolha == 1:
        print('Venci otário KKKK!')
        print('=' * 35)
    elif escolha == 2:
        print('Empate!')
        print('=' * 35)
    else:
        print('Para de tentar achar erro, coisa chata >:(')
        print('=' * 35)
if(escolha == '0' or escolha == '1' or escolha == '2'):
    print('Você escolheu',opcoes[escolha])
    print('O computador escolheu',opcoes[pc])