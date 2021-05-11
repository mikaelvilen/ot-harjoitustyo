import sys
import pygame
from db import get_scores, set_new_score


class Gameloop:
    def __init__(self, screen, py_display, player, computer, ball):
        self.screen = screen
        self.player = player
        self.computer = computer
        self.ball = ball
        self.score = 0
        self.game_active = False
        self.py_display = py_display

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not self.game_active:
                    self.game_active = True
                    self.ball.velocity = [10, 10]
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
            self.ball.velocity[0] *= 1.01
            self.ball.velocity[1] *= 1.01
        if self.ball.check_collision_walls(self.screen.size) == 1:
            self.ball.center_ball(self.screen.size)
            if self.score > get_scores()[4][1]:
                self._input_new_high_score(self.score)
            self.score = 0
            self._show_high_scores()
            self.game_active = False
        if self.ball.check_collision_walls(self.screen.size) == 2:
            self.ball.velocity[1] *= -1
        if self.ball.check_collision_walls(self.screen.size) == 3:
            self.score += 1000
            self.ball.center_ball(self.screen.size)
            self.game_active = False

    def _input_new_high_score(self, score):
        input_name = ''
        self.py_display.blit(
                    self.screen.font.render(
                        'NEW HIGH SCORE! ENTER YOUR NAME', 1, (255, 255, 255)
                    ), (140, 120)
                )
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        set_new_score(input_name, score)
                        return
                    input_name += event.unicode
                    self.py_display.blit(
                        self.screen.font.render(
                            input_name, 1, (255, 255, 255)
                        ), (235, 240)
                    )
                    pygame.display.flip()

    def _show_high_scores(self):
        top_5 = get_scores()
        positions = [50, 70, 90, 110, 130]
        self.py_display.blit(
            self.screen.font_2.render(
                'HIGH SCORES', 1, (255, 255, 255)
            ), (450, 10)
        )
        i = 0
        for score in top_5:
            self.py_display.blit(
                self.screen.font_2.render(
                    score[0] + ': ' + str(score[1]), 1 , (255, 255, 255)
                ), (450, positions[i])
            )
            i += 1

    def _draw_screen(self):
        self.py_display.fill(self.screen.color)
        pygame.draw.line(self.py_display, (255, 255, 255), ((
            self.screen.size[0] / 2) - 1, 0), (
                (self.screen.size[0] / 2) - 1, self.screen.size[1]), 2)
        score_label = self.screen.font.render(
            'Score ' + str(self.score), 1, (255, 255, 255))
        if not self.game_active:
            self._show_high_scores()
            new_game_label = self.screen.font.render(
            'Press any key to play ', 1, (255, 255, 255))
            self.py_display.blit(new_game_label, (235, 240))
        self.py_display.blit(score_label, (100, 10))
        self.py_display.blit(self.ball.image, self.ball.rect)
        self.py_display.blit(self.player.image, self.player.rect)
        self.py_display.blit(self.computer.image, self.computer.rect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    def start(self):
        """Starts the game
        """
        while True:
            self._draw_screen()
            if self.game_active:
                self.score += 1
            self._handle_events()
            self._handle_collisions()
            self.computer.rect.y = self.ball.rect.y - self.computer.height / 2
            self.ball.update()
            self.player.update(self.screen.size)
            self.computer.update(self.screen.size)
