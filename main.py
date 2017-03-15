import pygame, sys, ball, block


# game globals
screen_width = 640
screen_height = 480

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():

    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode([screen_width, screen_height])

    background = pygame.Surface(screen.get_size())
    background.fill(BLACK)
    screen.blit(background, (0, 0))

    # instantiate ball and block objects
    gameBall = ball.Ball(RED, (screen_width/2 , 200), 10)
    gameBlock = block.Block(GREEN, 60, 5, (screen_width/2, 400))

    # sprite groups make updating and drawing to the screen easy
    spriteList = pygame.sprite.Group()

    spriteList.add(gameBall)
    spriteList.add(gameBlock)

    # hide the mouse
    pygame.mouse.set_visible(False)

    # used for framerate
    clock = pygame.time.Clock()

    done = False

    while not done:

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # if the ball collides with the block, reverse its direction
        if pygame.sprite.collide_rect(gameBall, gameBlock):
            gameBall.velocity = -.90*gameBall.velocity

        # draw and update
        spriteList.clear(screen, background)
        spriteList.update()
        spriteList.draw(screen)

        pygame.display.update()

main()
