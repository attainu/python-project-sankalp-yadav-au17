import pygame
class Ladders:
    # ladder
    def ladder(x,con1):
        pygame.mixer.music.load("Snake and Ladder/Assets/sound/ladder_laugh_sound.wav")
        ladder_laugh_sound = pygame.mixer.Sound("Snake and Ladder/Assets/sound/ladder_laugh_sound.wav")
        if x == 1:
            ladder_laugh_sound.play()
            return 38 , True
        elif x == 4:
            ladder_laugh_sound.play()
            return 14 , True
        elif x == 9: 
            ladder_laugh_sound.play()
            return 31 , True
        elif x == 21:
            ladder_laugh_sound.play()
            return 42 , True
        elif x == 28:
            ladder_laugh_sound.play()
            return 84 , True
        elif x == 72:
            ladder_laugh_sound.play()
            return 91 , True
        elif x == 51:
            ladder_laugh_sound.play()
            return 67 , True
        elif x == 80:
            ladder_laugh_sound.play()
            return 99 , True
        else:
            return x , False