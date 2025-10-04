import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect(midbottom=(100, 450))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound("assets/jump.mp3")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.rect.bottom >= 450:
                self.gravity = -25
                self.jump_sound.play()

    def update(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 450:
            self.rect.bottom = 450
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def crash(self):
        pygame.mixer.Sound("assets/crash.mp3").play()