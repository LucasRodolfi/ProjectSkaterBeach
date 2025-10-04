import pygame

import pygame

class ScoreManager:
    def __init__(self):
        self.points = 0
        self.font = pygame.font.Font(None, 36)

    def add(self, value):
        self.points += value

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.points}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
