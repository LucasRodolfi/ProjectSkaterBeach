import pygame

from code.factory import ObstacleFactory
from code.mediator import GameMediator
from code.player import Player
from code.score import ScoreManager


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.bg_static = pygame.image.load("assets/background.png")
        self.bg_dynamic = pygame.image.load("assets/background2.png")
        self.bg_dynamic_x = 0

        self.speed = 5
        self.player = Player()
        self.factory = ObstacleFactory()
        self.obstacles = []
        self.score = ScoreManager()
        self.mediator = GameMediator(self.player, self.obstacles, self.score)
        self.font = pygame.font.Font(None, 48)
        self.game_over = False

    def run(self):
        while True:
            self.screen.blit(self.bg_static, (0, 0))
            self.screen.blit(self.bg_dynamic, (self.bg_dynamic_x, 0))
            self.screen.blit(self.bg_dynamic, (self.bg_dynamic_x + 800, 0))
            self.bg_dynamic_x -= self.speed
            if self.bg_dynamic_x <= -800:
                self.bg_dynamic_x = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if not self.game_over:
                    self.player.handle_event(event)

            if not self.game_over:
                self.player.update()
                self.player.draw(self.screen)

                if pygame.time.get_ticks() % 1500 < 20:
                    self.obstacles.append(self.factory.create_obstacle())

                for obstacle in self.obstacles[:]:
                    obstacle.update(self.speed)
                    obstacle.draw(self.screen)
                    if obstacle.rect.colliderect(self.player.rect):
                        self.mediator.notify("collision")
                        self.game_over = True
                        self.screen.blit(self.font.render("GAME OVER", True, (255, 0, 0)), (300, 180))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        return

                    elif obstacle.rect.right < self.player.rect.left and not obstacle.passed:
                        obstacle.passed = True
                        self.score.add(10)
                    if obstacle.rect.x < -50:
                        self.obstacles.remove(obstacle)

                self.score.draw(self.screen)
            else:
                text = self.font.render("GAME OVER", True, (255, 0, 0))
                self.screen.blit(text, (300, 180))

            pygame.display.update()
            self.clock.tick(60)