import pygame, random

class Block(pygame.sprite.Sprite):
    """ just a static block
    Returns: block object
    """

    def __init__(self, color, width, height, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.center = position
