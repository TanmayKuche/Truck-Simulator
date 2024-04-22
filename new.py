import pygame 
from pygame.locals import*
from pygame import mixer 
import time
import random
pygame.init()

gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=800
display_height=600



            
gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("TRUCK GAME")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.png')
backgroundpic=pygame.image.load("grass.jpeg")
yellow_strip=pygame.image.load("yellow_strip.jpg")
strip=pygame.image.load("strip.jpeg")
intro_background=pygame.image.load("background.jpg")
# movie=pygame.movie.Movie("movie.mp4")
instruction_background=pygame.image.load("bk.png")
pause_background=pygame.image.load("background.jpg")
car_width=50
mixer.music.load("intro.mp3")
mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
pause=False

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()      
        gamedisplays.blit(intro_background,(0,0))
        button("START",150,480,100,50,green,bright_green,"play")
        button("CONTACT US",0,0,150,50,150,50,"contact")
        button("QUIT",550,480,100,50,red,bright_red,"quit")
        button("INSTRUCTION",300,480,200,50,blue,bright_blue,"intro")
     
        pygame.display.update()
        clock.tick(50)



def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()
            elif action=="horn":
                horn()
            elif action=="contact":
                contact()
    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)

def contact():
    contact=True
    while contact:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))
        mediumtext=pygame.font.Font('freesansbold.ttf',25)
        largetext=pygame.font.Font('freesansbold.ttf',75)
        textSurf,textRect=text_objects("MAIL ME :tanmaykuche15@gmail.com",mediumtext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("CONTACT",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()

def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        atextSurf,atextRect=text_objects("ARROW UP : ACCELERATOR",smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_objects("ARROW DOWN: BRAKE ",smalltext)
        rtextRect.center=((150),(550))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        sTextSurf,sTextRect=text_objects("HORNS : key_0, key_1, key_2, key_3, key_4, key_5",smalltext)
        sTextRect.center=((270),(350))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            mixer.init()
            mixer.music.load("intro.mp3")
            mixer.music.play(-1)
            pygame.mixer.music.set_volume(1)
            gamedisplays.blit(pause_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/3))
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            button("HORN",0,0,100,50,100,50,"horn")
            pygame.display.update()
            clock.tick(30)

def unpaused():
            mixer.init()
            start=mixer.Sound('start.wav')
            start.play()
            start.set_volume(0.6)
            mixer.music.load("background.mp3")
            mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.8)
            global pause
            pause=False


def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,600))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,200))
    gamedisplays.blit(carimg,(x,y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))

 



def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            mixer.init() 
            mixer.music.load("countdown2.mp3")
            mixer.music.play()
            pygame.mixer.music.set_volume(0.7)       
  

            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',80)
            TextSurf,TextRect=text_objects("JAI BHAWANI!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()

            mixer.init()
            start=mixer.Sound('start.wav')
            start.play()
            start.set_volume(0.6)
            mixer.music.load("background.mp3")
            mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.8)
            clock.tick(1)
            game_loop()

def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("8.jpeg")
    elif obs==1:
        obs_pic=pygame.image.load("2.jpeg")
    elif obs==2:
        obs_pic=pygame.image.load("3.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("7.jpg")
    elif obs==5:
       mixer.init()
       po=mixer.Sound('police.mp3')
       po.play()
       po.set_volume(0.1)
       obs_pic=pygame.image.load("4.png")
    elif obs==8:
       mixer.init()
       amb=mixer.Sound('amb.mp3')
       amb.play()
       amb.set_volume(0.2)
       obs_pic=pygame.image.load("5.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("2.jpeg")
    elif obs==7:
        obs_pic=pygame.image.load("10.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("7.jpg")
    elif obs==9:
        obs_pic=pygame.image.load("9.jpg")
    else:
       obs==10
       obs_pic=pygame.image.load("6.jpg")

    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))
    

def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed"+str(passed),True,black)
    score=font.render("Score"+str(score),True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))


def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

#sound
def horn():
  mixer.init()
  h1=mixer.Sound('h1.mp3')
  h1.play()

#song
def song1():
    h0=mixer.Sound('h0.mp3')
    h0.play()
def song2():
  h2=mixer.Sound('h2.mp3')
  h2.play()
def song3():
  h3=mixer.Sound('h3.mp3')
  h3.play()
def song4():
  h4=mixer.Sound('h4.mp3')
  h4.play()
def song5():
    h5=mixer.Sound("h5.mpeg")
    h5.play()


def crash():
    crash=mixer.Sound("crash.mp3")
    crash.play()
    message_display("HUG DIYA")



def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))


def car(x,y):
    gamedisplays.blit(carimg,(x,y))

def game_loop():
    global pause
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=10
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=54
    obs_height=133
    passed=0
    level=0
    score=0
    y2=7
    fps=120
    




    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_UP:
                    obstacle_speed+=2
                    ab =  mixer.Sound("engine.mp3")
                    ab.play()
                if event.key==pygame.K_DOWN:
                    obstacle_speed-=2
                    bk=mixer.Sound("bk.mp3")
                    bk.play()
                if event.key==pygame.K_0:
                    horn()
                if event.key==pygame.K_1:
                    song1()
                if event.key==pygame.K_2:
                   song2()
                if event.key==pygame.K_3:
                   song3()
                if event.key==pygame.K_4:
                   song4()
                if event.key==pygame.K_5:
                   song5()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.fill(gray)

        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(700,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

        y2+=obstacle_speed




        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>690-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,10)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)


        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        button("HORN",0,0,100,50,100,50,"horn")
        pygame.display.update()
        clock.tick(60)
          
intro_loop()
game_loop()
pygame.quit()
quit()