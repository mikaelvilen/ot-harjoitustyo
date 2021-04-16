import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, velocity_x, velocity_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radius, radius])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = [velocity_x, velocity_y]

    def update(self):
        self.rect = self.rect.move(self.velocity)
