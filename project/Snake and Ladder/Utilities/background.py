import pygame
from Utilities.screen_size import Size

class Background:
    # background
    def __init__(self):
        self.snk_lddr_img=pygame.image.load("Snake and Ladder/Assets/images/Snakes_ladders_big_image.png")
        self.bckimg=pygame.image.load("Snake and Ladder/Assets/images/introduction_image2.jpg")
        self.playbutton = pygame.image.load("Snake and Ladder/Assets/images/playbutton.png")
        self.playbutton = pygame.transform.scale(self.playbutton, (40,40))
        self.button = pygame.Rect(50,200,40,40)
        self.screen = pygame.display.set_mode((Size.width,Size.heigth))


    def bck(self):
        self.screen.blit(self.bckimg,(0,0))
        self.screen.blit(self.snk_lddr_img,(433,134))
        self.screen.blit(self.playbutton,(50,200))