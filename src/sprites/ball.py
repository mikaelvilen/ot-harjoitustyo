import pygame


class Ball(pygame.sprite.Sprite):
    """Class defines ball sprite

    Attributes:
        image: pygame surface, Needed for drawing object on the screen
        rect: x and y coordinates for the ball
        radius: radius of the ball
        velocity: speed of the ball,
        x and y values which define the offset how much the ball will move on the screen
    """
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
        """Moves the ball on the screen
        """
        self.rect = self.rect.move(self.velocity)

    def center_ball(self, screen_size):
        """Puts the ball back in starting position in the center of the screen
        Args:
            screen_size: tuple, width and height of the screen to calculate the center of the screen
        """
        self.rect.x = screen_size[0] / 2 - (self.radius / 2)
        self.rect.y = screen_size[1] / 2 - (self.radius / 2)
        self.velocity = [0, 0]

    def check_collision_pad(self, player_rect, computer_rect):
        """Checks if a collision between the ball and a Pad-object has happened

        Args:
            player_rect: x and y coordinates of the Pad-object
            computer_rect: x and y coordinates of the Pad-object

        Returns:
            True, if a collision has happened, otherwise False
        """
        return pygame.Rect.colliderect(self.rect, player_rect) or pygame.Rect.colliderect(
            self.rect, computer_rect)

    def check_collision_walls(self, screen_size):
        """Checks if a collision between the ball and a wall has happened

        Args:
            screen_size: tuple, width and height of the screen

        Returns:
            int: 2 if collision with top or bottom,
            1 if collision with left and 3 if collision with right wall
        """
        if self.rect.y <= 0 or self.rect.y >= screen_size[1]:
            return 2
        if self.rect.x < 0:
            return 1
        if self.rect.x > screen_size[0]:
            return 3
        return 0
