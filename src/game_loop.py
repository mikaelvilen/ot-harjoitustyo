import pygame
import sys

class Gameloop:
    def __init__(self, screen, screen_size, screen_color, player, computer, ball):
        self.screen = screen
        self.screen_size = screen_size
        self.screen_color = screen_color
        self.player = player
        self.computer = computer
        self.ball = ball
        self.font = pygame.font.Font('src/assets/8bitOperatorPlus-Regular.ttf', 30)
        self.score = 0
        self.game_active = False

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not self.game_active:
                    self.game_active = True
                    self.ball.velocity = [5, 5]
                if event.key == pygame.K_UP:
                    self.player.velocity = -10
                if event.key == pygame.K_DOWN:
                    self.player.velocity = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player.velocity = 0
                if event.key == pygame.K_DOWN:
                    self.player.velocity = 0

    def _handle_collisions(self):
        if self.ball.check_collision_pad(self.player.rect, self.computer.rect):
                self.ball.velocity[0] *= -1
        if self.ball.check_collision_walls(self.screen_size) == 1:
            self.ball.rect.x = self.screen_size[0] / 2 - (self.ball.radius / 2)
            self.ball.rect.y = self.screen_size[1] / 2 - (self.ball.radius / 2)
            self.ball.velocity = [0, 0]
            self.score = 0
            self.game_active = False
        if self.ball.check_collision_walls(self.screen_size) == 2:
            self.ball.velocity[1] *= -1
        if self.ball.check_collision_walls(self.screen_size) == 3:
            self.score += 1000

    def _draw_screen(self):
        self.screen.fill(self.screen_color)
        pygame.draw.line(self.screen, (255, 255, 255), ((self.screen_size[0] / 2) - 1, 0), ((self.screen_size[0] / 2) - 1, self.screen_size[1]), 2)
        score_label = self.font.render('Score ' + str(self.score), 1, (255, 255, 255))
        self.screen.blit(score_label, (50, 10))
        self.screen.blit(self.ball.image, self.ball.rect)
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.computer.image, self.computer.rect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    def start(self):
        while True:
            self._handle_events()
            self._handle_collisions()
            self.computer.rect.y = self.ball.rect.y
            self.ball.update()
            self.player.update(self.screen_size)
            self.computer.update(self.screen_size)
            if self.game_active:
                self.score += 1
            self._draw_screen()