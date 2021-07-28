import pygame
import time 
import random

pygame.init()

screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Snake and Ladder Wala Game")

# background
snk_lddr_img=pygame.image.load("images/Snakes_ladders_big_image.png")
bckimg=pygame.image.load("images/introduction_image2.jpg")
playbutton = pygame.image.load("images/playbutton.png")
playbutton = pygame.transform.scale(playbutton, (40,40))
button = pygame.Rect(50,200,40,40)

def bck():
    screen.blit(bckimg,(0,0))
    screen.blit(snk_lddr_img,(433,134))
    screen.blit(playbutton,(50,200))

# players
font1 = pygame.font.SysFont("comicsansms",30)
font2 = pygame.font.SysFont("comicsansms",25)

red=pygame.image.load("images/red_c.png")
blue=pygame.image.load("images/blue_c.png")
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

# board
def board(x):
    brd=[[434,584],[484,584],[534,584],[584,584],[634,584],[684,584],[734,584],[784,584],[834,584],[884,584]
    ,[884,534],[834,534],[784,534],[734,534],[684,534],[634,534],[584,534],[534,534],[489,534],[434,534]
    ,[434,484],[484,484],[534,484],[584,484],[634,484],[684,484],[734,484],[784,484],[834,484],[884,484]
    ,[884,434],[834,434],[784,434],[734,434],[684,434],[634,434],[584,434],[534,434],[489,434],[434,434]
    ,[434,384],[484,384],[534,384],[584,384],[634,384],[684,384],[734,384],[784,384],[834,384],[884,384]
    ,[884,334],[834,334],[784,334],[734,334],[684,334],[634,334],[584,334],[534,334],[489,334],[434,334]
    ,[434,284],[484,284],[534,284],[584,284],[634,284],[684,284],[734,284],[784,284],[834,284],[884,284]
    ,[884,234],[834,234],[784,234],[734,234],[684,234],[634,234],[584,234],[534,234],[489,234],[434,234]
    ,[434,184],[484,184],[534,184],[584,184],[634,184],[684,184],[734,184],[784,184],[834,184],[884,184]
    ,[884,134],[834,134],[784,134],[734,134],[684,134],[634,134],[584,134],[534,134],[489,134],[434,134]]

    return brd[x]

# snake
def snake(x,con2):
    if x == 17:
        return 7, True
    elif x == 54:
        return 34, True
    elif x == 62:
        return 19, True
    elif x == 64:
        return 60, True
    elif x == 87:
        return 36, True
    elif x == 93:
        return 73, True
    elif x == 95:
        return 75, True
    elif x == 98:
        return 79, True
    else:
        return x, False
    
# ladder
def ladder(x,con1):
    if x == 1:
        return 38 , True
    elif x == 4:
        return 14 , True
    elif x == 9: 
        return 31 , True
    elif x == 21:
        return 42 , True
    elif x == 28:
        return 84 , True
    elif x == 72:
        return 91 , True
    elif x == 51:
        return 67 , True
    elif x == 80:
        return 99 , True
    else:
        return x , False

# dice
def goti_number():
    diceroll = random.randint(1,6)
    if diceroll == 1:
        dice = pygame.image.load("images/dice_image1.png")
    elif diceroll == 2:
        dice = pygame.image.load("images/dice_image2.png")
    elif diceroll == 3:
        dice = pygame.image.load("images/dice_image3.png")
    elif diceroll == 4:
        dice = pygame.image.load("images/dice_image4.png")
    elif diceroll == 5:
        dice = pygame.image.load("images/dice_image5.png")
    elif diceroll == 6:
        dice = pygame.image.load("images/dice_image6.png")
    return (dice, diceroll)
    
    
# game loop
def main():
    turn = "blue"
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
        bck()

        if turn == "red":
            red_msg()
        elif turn == "blue":
            blue_msg()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button.collidepoint(mouse_pos):
                    goti_number()
                    dice,diceroll = goti_number()
                    screen.blit(dice,(100,170))
                    print(diceroll)
                # for changing the turn 
                if goti_number() and turn == "red":
                    turn = "blue"
                    # for red goti
                    if diceroll == 1 and rx == 370 and ry ==300 and cnt1==None:
                        rx = 300
                        ry = 584
                        cnt1=0
                    elif cnt1 !=None and (cnt1 + diceroll) == 100:
                        cnt1 += diceroll
                        a = board(cnt1 - 1)
                        rx = a[0]
                        ry = a[1]
                        return "Red"
                        
                    elif cnt1 != None and (cnt1 + diceroll) > 100:
                        continue
                    elif cnt1 !=None and diceroll == 1 :
                        cnt1 += diceroll
                        lddr,condition1 = ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        rx = a[0]
                        ry = a[1] 
                    elif cnt1 !=None and diceroll == 2:
                        cnt1 += diceroll
                        lddr,condition1 = ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    elif cnt1 !=None and diceroll == 3:
                        cnt1 += diceroll
                        lddr,condition1 = ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    elif cnt1 !=None and diceroll == 4:
                        cnt1 += diceroll
                        lddr,condition1 = ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    elif cnt1 !=None and diceroll == 5:
                        cnt1 += diceroll
                        lddr,condition1 = ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    elif cnt1 !=None and diceroll == 6:
                        cnt1 += diceroll
                        lddr,condition1 = ladder(cnt1,con1)
                        if condition1 == True:
                            cnt1 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt1 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        rx = a[0]
                        ry = a[1]
                    
                # for blue goti
                elif goti_number() and turn == "blue":
                    turn = "red"
                    if diceroll == 1 and bx == 370 and by ==450 and cnt2==None:
                        bx = 351
                        by = 584
                        cnt2=0
                    elif cnt2 !=None and (cnt2 + diceroll) == 100:
                        cnt2 += diceroll
                        a = board(cnt2 - 1)
                        bx = a[0]
                        by = a[1]
                        return "Blue"
                    elif cnt2 != None and (cnt2 + diceroll) > 100 :
                        continue
                    elif cnt2 !=None and diceroll == 1 :
                        cnt2 += diceroll
                        lddr,condition1 = ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        bx = a[0]
                        by = a[1]
                    elif cnt2 !=None and diceroll == 2 :
                        cnt2 += diceroll
                        lddr,condition1 = ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        bx = a[0]
                        by = a[1] 
                    elif cnt2 !=None and diceroll == 3 :
                        cnt2 += diceroll
                        lddr,condition1 = ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        bx = a[0]
                        by = a[1]
                    elif cnt2 !=None and diceroll == 4 :
                        cnt2 += diceroll
                        lddr,condition1 = ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        bx = a[0]
                        by = a[1]
                    elif cnt2 !=None and diceroll == 5 :
                        cnt2 += diceroll
                        lddr,condition1 = ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        bx = a[0]
                        by = a[1]
                    elif cnt2 !=None and diceroll == 6 :
                        cnt2 += diceroll
                        lddr,condition1 = ladder(cnt2,con1)
                        if condition1 == True:
                            cnt2 = lddr
                            con1,condition1 = False, False
                        snk,condition2 = snake(lddr,con2)
                        if condition2 == True:
                            cnt2 = snk
                            con2,condition2 = False, False
                        a = board(snk-1)
                        bx = a[0]
                        by = a[1]
                        
                


        red_player(rx,ry)
        blue_player(bx,by)
        pygame.display.update()
        time.sleep(1.3)
win = main()
if win == "Red":
    msg = font1.render("Red successfully crossed the hurdle",True, (255,0,0))
    screen.blit(msg,(409,50))
    pygame.display.update()
else:
    msg = font1.render("Blue successfully crossed the hurdle",True, (255,0,0))
    screen.blit(msg,(409,50))
    pygame.display.update()
time.sleep (10)
pygame.quit()
quit()