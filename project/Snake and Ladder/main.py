import pygame
import time 
import sys 
from Entities.matrix import Board
from Utilities.screen_size import Size
from Entities.snake import Snake
from Entities.ladder import Ladders
from Entities.dice import Dice
from Utilities.background import Background
from Utilities.players import Players


pygame.init()

screen = pygame.display.set_mode((Size.width,Size.heigth))
pygame.display.set_caption("Snake and Ladder Wala Game")

# object for background
bg = Background()
plyrs = Players()

    
# game loop
def main(turn):
    game = True
    # goti first place
    rx,bx=370, 370
    ry,by=300, 450
    cnt1=None
    cnt2=None
    con1 = False
    con2 = False

    while game:

        screen.fill((0,255,195))
        bg.bck()

        if turn == "red":
            plyrs.red_msg()
        elif turn == "blue":
            plyrs.blue_msg()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # game = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if bg.button.collidepoint(mouse_pos):
                    Dice.goti_number()
                    dice,diceroll = Dice.goti_number()
                    screen.blit(dice,(100,170))
                    print(diceroll)
                # for changing the turn 
                if Dice.goti_number() and turn == "red":
                    turn = "blue"
                    # for red goti
                    if diceroll == 1 and rx == 370 and ry ==300 and cnt1==None:
                        rx = 300
                        ry = 584
                        cnt1=0
                    elif cnt1 !=None and (cnt1 + diceroll) == 100:
                        cnt1 += diceroll
                        a = Board.board(cnt1 - 1)
                        rx = a[0]
                        ry = a[1]
                        return "Red"
                        
                    elif cnt1 != None and (cnt1 + diceroll) > 100:
                        continue
                    elif cnt1 !=None and diceroll == 1 :
                        cnt1 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        rx = a[0]
                        ry = a[1] 
                    elif cnt1 !=None and diceroll == 2:
                        cnt1 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    elif cnt1 !=None and diceroll == 3:
                        cnt1 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    elif cnt1 !=None and diceroll == 4:
                        cnt1 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    elif cnt1 !=None and diceroll == 5:
                        cnt1 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    elif cnt1 !=None and diceroll == 6:
                        cnt1 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    
                # for blue goti
                elif Dice.goti_number() and turn == "blue":
                    turn = "red"
                    if diceroll == 1 and bx == 370 and by ==450 and cnt2==None:
                        bx = 351
                        by = 584
                        cnt2=0
                    elif cnt2 !=None and (cnt2 + diceroll) == 100:
                        cnt2 += diceroll
                        a = Board.board(cnt2 - 1)
                        bx = a[0]
                        by = a[1]
                        return "Blue"
                    elif cnt2 != None and (cnt2 + diceroll) > 100 :
                        continue
                    elif cnt2 !=None and diceroll == 1 :
                        cnt2 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        bx = a[0]
                        by = a[1]
                    elif cnt2 !=None and diceroll == 2 :
                        cnt2 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        bx = a[0]
                        by = a[1] 
                    elif cnt2 !=None and diceroll == 3 :
                        cnt2 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        bx = a[0]
                        by = a[1]
                    elif cnt2 !=None and diceroll == 4 :
                        cnt2 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        bx = a[0]
                        by = a[1]
                    elif cnt2 !=None and diceroll == 5 :
                        cnt2 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        bx = a[0]
                        by = a[1]
                    elif cnt2 !=None and diceroll == 6 :
                        cnt2 += diceroll
                        lddr,condition1 = Ladders.ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = Snake.snakes(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = Board.board(snk-1)
                        bx = a[0]
                        by = a[1]
                        
                


        plyrs.red_player(rx,ry)
        plyrs.blue_player(bx,by)
        pygame.display.update()
        time.sleep(1.3)

turn = "blue"
win = main(turn)

# game over sound
pygame.mixer.music.load("Snake and Ladder/Assets/sound/game_over_sound.wav")
game_over_sound = pygame.mixer.Sound("Snake and Ladder/Assets/sound/game_over_sound.wav")

if win == "Red":
    game_over_sound.play()
    msg = plyrs.font1.render("Red successfully crossed the hurdle",True, (255,0,0))
    screen.blit(msg,(409,50))
    pygame.display.update()
    time.sleep (10)
else:
    game_over_sound.play()
    msg = plyrs.font1.render("Blue successfully crossed the hurdle",True, (0,0,255))
    screen.blit(msg,(409,50))
    pygame.display.update()
    time.sleep (10)
#  for event in pygame.event.get():    
#     if event.type == pygame.QUIT:
#         sys.exit()
#     else:
#         pygame.quit()
#         quit()