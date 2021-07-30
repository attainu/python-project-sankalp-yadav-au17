import pygame
import random

class Dice:
    # dice
    
    def goti_number():
        pygame.mixer.music.load("Snake and Ladder/Assets/sound/dice_roll_sound.wav")
        dice_sound = pygame.mixer.Sound("Snake and Ladder/Assets/sound/dice_roll_sound.wav")
        diceroll = random.randint(1,6)
        dice_sound.play()
        if diceroll == 1:
            dice = pygame.image.load("Snake and Ladder/Assets/images/dice_image1.png")
        elif diceroll == 2:
            dice = pygame.image.load("Snake and Ladder/Assets/images/dice_image2.png")
        elif diceroll == 3:
            dice = pygame.image.load("Snake and Ladder/Assets/images/dice_image3.png")
        elif diceroll == 4:
            dice = pygame.image.load("Snake and Ladder/Assets/images/dice_image4.png")
        elif diceroll == 5:
            dice = pygame.image.load("Snake and Ladder/Assets/images/dice_image5.png")
        elif diceroll == 6:
            dice = pygame.image.load("Snake and Ladder/Assets/images/dice_image6.png")
        return (dice, diceroll)