import pygame

from code.game import Game

pygame.init()
screen = pygame.display.set_mode((820, 540))
pygame.display.set_caption("Skater Beach Run")

game = Game(screen)
game.run()

pygame.quit()


