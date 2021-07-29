import pygame
import time 
import random
import sys 
from Entities.matrix import Board
from Utilities.screen_size import Size
from Entities.snake import Snake
from Entities.ladder import Ladders
from Entities.dice import Dice
from Utilities.background import Background


pygame.init()

screen = pygame.display.set_mode((Size.width,Size.heigth))
pygame.display.set_caption("Snake and Ladder Wala Game")

# # background
# snk_lddr_img=pygame.image.load("Snake and Ladder/Assets/images/Snakes_ladders_big_image.png")
# bckimg=pygame.image.load("Snake and Ladder/Assets/images/introduction_image2.jpg")
# playbutton = pygame.image.load("Snake and Ladder/Assets/images/playbutton.png")
# playbutton = pygame.transform.scale(playbutton, (40,40))
# button = pygame.Rect(50,200,40,40)

# def bck():
#     screen.blit(bckimg,(0,0))
#     screen.blit(snk_lddr_img,(433,134))
#     screen.blit(playbutton,(50,200))

# players
font1 = pygame.font.SysFont("comicsansms",30)
font2 = pygame.font.SysFont("comicsansms",25)

red=pygame.image.load("Snake and Ladder/Assets/images/red_c.png")
blue=pygame.image.load("Snake and Ladder/Assets/images/blue_c.png")
# player name and dice

def red_player(rx,ry):
    msg1 = font1.render("Player 1",True,(255,0,0))
    screen.blit(msg1,(250,303))
    screen.blit(red,(rx,ry))
   
def blue_player(bx,by):
    msg1 = font1.render("Player 2",True,(0,0,255))
    screen.blit(msg1,(250,453))
    screen.blit(blue,(bx,by))
# player turn message
def red_msg():
    msg1=font2.render("Your Turn!!!",True,(0,0,0))
    screen.blit(msg1,(255,355))
def blue_msg():
    msg1=font2.render("Your Turn!!!",True,(0,0,0))
    screen.blit(msg1,(255,504))

    
# game loop
def main(turn):
    # turn = "blue"
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
        Background.bck()

        if turn == "red":
            red_msg()
        elif turn == "blue":
            blue_msg()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # game = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if Background.button.collidepoint(mouse_pos):
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
                        
                


        red_player(rx,ry)
        blue_player(bx,by)
        pygame.display.update()
        time.sleep(1.3)
turn = "blue"
win = main(turn)
if win == "Red":
    msg = font1.render("Red successfully crossed the hurdle",True, (255,0,0))
    screen.blit(msg,(409,50))
    pygame.display.update()
    time.sleep (10)
else:
    msg = font1.render("Blue successfully crossed the hurdle",True, (255,0,0))
    screen.blit(msg,(409,50))
    pygame.display.update()
    time.sleep (10)
pygame.quit()
quit()