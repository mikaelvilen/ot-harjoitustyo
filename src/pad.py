import pygame

class Pad(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 100])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity