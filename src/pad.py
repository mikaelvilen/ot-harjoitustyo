import pygame

class Pad(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.velocity = velocity

    def update(self, screen_size):
        if self.rect.y < 0:
            self.rect.y = 0
            self.velocity = 0
        if self.rect.y > screen_size[1] - self.height:
            self.rect.y = screen_size[1] - self.height
            self.velocity = 0
        self.rect = self.rect.move([0, self.velocity])
        