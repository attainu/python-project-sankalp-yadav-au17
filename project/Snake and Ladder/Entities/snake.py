import pygame
class Snake:
    # snake
    def snakes(x,con2):
        pygame.mixer.music.load("Snake and Ladder/Assets/sound/snake_sound.wav")
        snake_sound = pygame.mixer.Sound("Snake and Ladder/Assets/sound/snake_sound.wav")
        
        if x == 17:
            snake_sound.play()
            return 7, True
        elif x == 54:
            snake_sound.play()
            return 34, True
        elif x == 62:
            snake_sound.play()
            return 19, True
        elif x == 64:
            snake_sound.play()
            return 60, True
        elif x == 87:
            snake_sound.play()
            return 36, True
        elif x == 93:
            snake_sound.play()
            return 73, True
        elif x == 95:
            snake_sound.play()
            return 75, True
        elif x == 98:
            snake_sound.play()
            return 79, True
        else:
            return x, False