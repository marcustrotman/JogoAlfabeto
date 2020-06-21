'''import funcao
import pygame
numero = 10
tempo = 0

while True:
    tela = pygame.display.set_mode((945, 600))
    funcao.mostrartela(tela, funcao.carregarimagem(f'numeros/{numero}.png'), 870, 455)
    pygame.display.update()

    tempo += 0.1
    if tempo >= 3:
        numero -= 1
        tempo=0
        if numero < 1:
            numero = 10
    clock = pygame.time.Clock()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()'''

'''import pygame, funcao
from random import randint
frutas = ['cereja', 'pessego', 'pera']

indice = randint(0, len(frutas)-1)
fruta = frutas[indice]
while True:
    tela = pygame.display.set_mode((945, 600))
    funcao.mostrartela(tela, funcao.carregarimagem(f'frutas/{fruta}.png'), 700, 350)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def sortearfruta():
    frutas = ['cereja', 'pessego', 'pera']
    indice = randint(0, len(frutas) - 1)
    fruta = frutas[indice]
    return fruta'''

