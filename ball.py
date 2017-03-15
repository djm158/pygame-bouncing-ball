import pygame

class Ball(pygame.sprite.Sprite):
    """ 
        Ball class 
        attribute: velocity
        methods:   update
    """
        

    def __init__(self, color, position, radius):
        # call super class constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((radius*2, radius*2))
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.rect = self.image.get_rect()

        self.rect.center = position

        self.velocity = 3

    def update(self):
        self.velocity = self.velocity + .25
        self.rect.y += self.velocity
