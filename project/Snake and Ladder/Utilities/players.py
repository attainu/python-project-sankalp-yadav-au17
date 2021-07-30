import pygame
from Utilities.screen_size import Size


class Players:
    def __init__(self):
        self.font1 = pygame.font.SysFont("comicsansms", 30)
        self.font2 = pygame.font.SysFont("comicsansms", 25)
        self.red = pygame.image.load("Snake and Ladder/Assets/images/red_c.png")
        self.blue = pygame.image.load("Snake and Ladder/Assets/images/blue_c.png")
        self.screen = pygame.display.set_mode((Size.width, Size.heigth))
    
    def red_player(self, rx, ry):
        msg1 = self.font1.render("Player 1", True, (255, 0, 0))
        self.screen.blit(msg1, (250, 303))
        self.screen.blit(self.red, (rx, ry))
    
    def blue_player(self, bx, by):
        msg1 = self.font1.render("Player 2", True, (0, 0, 255))
        self.screen.blit(msg1, (250, 453))
        self.screen.blit(self.blue, (bx, by))

    def red_msg(self):
        msg1 = self.font2.render("Your Turn!!!", True, (0, 0, 0))
        self.screen.blit(msg1, (255, 355))
    
    def blue_msg(self):
        msg1 = self.font2.render("Your Turn!!!", True, (0, 0, 0))
        self.screen.blit(msg1, (255, 504))