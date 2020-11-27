from random import randint
from time import sleep

print('ÍMPAR OU PAR!!')
print('=' * 35)
print('''Escolha:
      Ímpar
      Par''')
print('=' * 35)

computador = randint(0,10)
jogador = input('Ímpar ou par? ')

print('=' * 35)
if jogador != 'impar' and jogador != 'par':
  print('Jogada inválida!')
  print('=' * 35)
else:
  print('Escolha um número de 0 a 10:')
  print('=' * 35)
  numero = int(input('Qual você joga? '))
  print('=' * 35)
  sleep(1)
  print('IIIMPARR')
  sleep(1)
  print('OUUUU')
  sleep(1)
  print('PAAR')
  print('=' * 35)
  if numero >= 0 and numero < 11:
    jog = numero
  else:
    print('Jogada inválida!')
    print('=' * 35)
  res = jog + computador
  if res %2 == 0:
    num = 'par'
  else:
    num = 'impar'
  if jogador == num:
    print('Jogador Venceu')
    print('=' * 35)
  else:
    print('A máquina venceu')
    print('=' * 35)
  print('A máquina jogou:',computador)
  print('Você jogou:',jog)
  print('=' * 35)
  print('Sua escolha foi:',jogador)