import pygame

class Obstacle:
    def __init__(self):
        self.image = pygame.image.load("assets/obstacle1.png")
        self.rect = self.image.get_rect(midbottom=(800, 450))
        self.passed = False

    def update(self, speed):
        self.rect.x -= speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)