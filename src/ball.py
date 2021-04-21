import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, radius, velocity_x, velocity_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radius, radius])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.radius = radius
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocity = [velocity_x, velocity_y]

    def update(self):
        self.rect = self.rect.move(self.velocity)
    
    def center_ball(self, screen_size):
        self.rect.x = screen_size[0] / 2 - (self.radius / 2)
        self.rect.y = screen_size[1] / 2 - (self.radius / 2)
        self.velocity = [0, 0]

    def check_collision_pad(self, player_rect, computer_rect):
        return pygame.Rect.colliderect(self.rect, player_rect) or pygame.Rect.colliderect(self.rect, computer_rect)

    def check_collision_walls(self, screen_size):
        if self.rect.y <= 0 or self.rect.y >= screen_size[1]:
            return 2
        if self.rect.x < 0:
            return 1
        if self.rect.x > screen_size[0]:
            return 3
        else:
            return 0
