import pygame
from congkak.constant import *
from congkak.game import Game

pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Congkak')

def main():
    clock = pygame.time.Clock()
    run = True
    game = Game()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   run = False
            if not game.board.finish:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    game.select(game.get_pos(pos))

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        game.choose()
        game.update()
    pygame.quit()
main()