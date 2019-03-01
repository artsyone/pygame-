# Imports
import pygame
import math
import random

# Initia lize game engine
pygame.mixer.pre_init()
pygame.init()


# Window
SIZE = (800, 500)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


  
# Timer
clock = pygame.time.Clock()
refresh_rate = 60
 

# Colors
RED = (250, 24, 31)
REDL = (255, 159, 163)
GREEN = (0, 255, 0)
BLUE = (33, 65, 103)
BLUE1 = (33,65,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
GREY = (196, 196, 196)
DAGREY = (58, 59, 61)
DARKERG = (29, 29, 30)
LGREY = (162, 169, 179)
YELLOW =(255,125,0) # not really yellow
FGREEN =(34,139,34)
DBLUE = (0,57,89)


# Sound Effects
tv = pygame.mixer.music.load("sounds/tv.ogg")
laugh = pygame.mixer.music.load("sounds/friends.ogg")
birds = pygame.mixer.music.load("sounds/birds.ogg")
friends = pygame.image.load("friends.jpg")
guide = pygame.image.load("guide3.png")
shoe = pygame.image.load("shoe2.png")
man1= pygame.image.load("man1.png")
man2= pygame.image.load("man2.png")
music1= pygame.image.load("music1.png")
music2= pygame.image.load("music2.png")
sun = pygame.image.load("sun.png")
bbox= pygame.image.load("bbox1.png")
glasses = pygame.image.load("manglass.png")
ad = pygame.image.load("ad3.jpg")

num_clouds = 1
clouds = []
for i in range(num_clouds):
    x = random.randrange(379, 380)
    y = random.randrange(250, 270)
    loc = [x, y]
    clouds.append(loc)

        
colors = [RED,REDL,ORANGE,YELLOW]
xgoes =[300,310,320,330,340,350,369,370,380,390,400]
ygoes =[315,320,325,330,335]
postions = [489, 250, 489,264],[475, 264, 489,264],[489, 277, 489,264],[502, 264,489,264]
knobp = [489, 328,489,314],[475, 314, 489,314],[489, 300, 489,314],[502, 314,489,314]




c = colors[random.randint(0,len(colors)-1)]
xa = xgoes[random.randint(0,len(xgoes)-1)]
ya = ygoes[random.randint(0,len(ygoes)-1)]

xb = xgoes[random.randint(0,len(xgoes)-1)]
yb = ygoes[random.randint(0,len(ygoes)-1)]

xc = xgoes[random.randint(0,len(xgoes)-1)]
yc = ygoes[random.randint(0,len(ygoes)-1)]

b = [(pygame.draw.line(screen, GREEN, [489, 328], [489,314], 3)),(pygame.draw.line(screen, GREEN, [475, 314], [489,314], 3)),(pygame.draw.line(screen,WHITE, [489, 300], [489,314], 3)),(pygame.draw.line(screen,GREEN, [502, 314], [489,314], 3))]
def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, WHITE, [x +10, y + 20, 20 , 20])
    pygame.draw.ellipse(screen, WHITE, [x + 50, y + 20, 20 , 20])
    pygame.draw.ellipse(screen, WHITE, [x + 25, y + 10, 15, 15])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 30, 30])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 40, 20])


def draw_flower(xa,ya,c):
    
    
    pygame.draw.ellipse(screen, c, [xa +0, ya + 14, 10 , 10])
    pygame.draw.ellipse(screen, c, [xa +5, ya + 20, 10 , 10])
    pygame.draw.ellipse(screen, c, [xa +0, ya + 25, 10 , 10])

    pygame.draw.ellipse(screen, c, [xa - 5, ya +20, 10 , 10])
    pygame.draw.ellipse(screen, BLACK, [xa + 3, ya + 22, 7.5 , 7.5])


def draw_flower1(xb,yb,c):
    
    
    pygame.draw.ellipse(screen, c, [xb +0, yb + 14, 10 , 10])
    pygame.draw.ellipse(screen, c, [xb +5, yb + 20, 10 , 10])
    pygame.draw.ellipse(screen, c, [xb +0, yb + 25, 10 , 10])

    pygame.draw.ellipse(screen, c, [xb - 5, yb +20, 10 , 10])
    pygame.draw.ellipse(screen, BLACK, [xb + 3, yb + 22, 7.5 , 7.5])


def draw_flower2(xc,yc,c):
    
    
    pygame.draw.ellipse(screen, c, [xc +0, yc + 14, 10 , 10])
    pygame.draw.ellipse(screen, c, [xc +5, yc + 20, 10 , 10])
    pygame.draw.ellipse(screen, c, [xc +0, yc + 25, 10 , 10])
 
    pygame.draw.ellipse(screen, c, [xc - 5, yc +20, 10 , 10])
    pygame.draw.ellipse(screen, BLACK, [xc + 3, yc + 22, 7.5 , 7.5])  

def draw_bush(x, y):
    pygame.draw.ellipse(screen, FGREEN, [x +10, y + 20, 20 , 20])
    pygame.draw.ellipse(screen, FGREEN, [x + 50, y + 20, 20 , 20])
    pygame.draw.ellipse(screen, FGREEN, [x + 25, y + 10, 15, 15])
    pygame.draw.ellipse(screen, FGREEN, [x + 35, y, 30, 30])
    pygame.draw.rect(screen, FGREEN, [x + 20, y + 20, 40, 20])
    pygame.draw.ellipse(screen, FGREEN, [x + 25, y, 30, 30])
    pygame.draw.ellipse(screen, FGREEN, [x + 15, y, 30, 30])


def draw_shoe(j):
    x = j[0]
    y = j[1]
    ((x + 274,y + 335))



daytime = True
tvbuzz = False
tvbuzz1 = False
dancer = True
dancerglass  = True
f = []
count = 0

count1 = 0


# Game loop
#pygame.mixer.music.play(-1)

done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_UP:
                tvbuzz = not tvbuzz
                count += 1
            elif event.key == pygame.K_DOWN:
                tvbuzz1 = not tvbuzz1
                count1 += 1
            elif event.key == pygame.K_LEFT:
                dancer = not dancer

            elif event.key == pygame.K_RIGHT:
                dancerglass = not dancerglass
                
                # Game logic (Check for collisions, update points, etc.)

                
    for s in clouds:
        s[0] -= 1

        if s[0] < 245:
           s[0] = random.randrange(379, 380)
           s[1] = random.randrange(250, 270)

    
    ''' set sky color '''
    if daytime:
        f = BLUE1
    else:
        f = BLACK

    #for s in clouds:
        #draw_cloud(s)


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    # Drawing code
    screen.fill(WHITE)
    pygame.draw.rect(screen, DAGREY, [435, 245, 215, 215])
    pygame.draw.rect(screen, DARKERG, [435, 400, 215, 60])
    pygame.draw.rect(screen, BLACK, [235, 245, 300, 215])
    

    pygame.draw.line(screen, BLACK, [390, 190], [250,50], 5)
    pygame.draw.line(screen, BLACK, [400, 190], [520,50], 5)
    
    pygame.draw.rect(screen, RED, [340, 190, 100, 50])
    pygame.draw.rect(screen, REDL, [340, 198, 100, 50],1)
    pygame.draw.rect(screen, RED, [220, 200, 340, 240])
  
    pygame.draw.rect(screen, WHITE, [240, 220, 300, 200])
    pygame.draw.rect(screen, BLACK, [245, 225, 290, 190])
    pygame.draw.rect(screen, BLUE, [255, 235, 200, 170])
    
    pygame.draw.rect(screen, GREY, [255, 235, 200, 170])
    pygame.draw.rect(screen, BLACK, [270, 240, 170, 160])
    pygame.draw.rect(screen, BLUE, [275, 245, 160, 150])
    
    

    pygame.draw.rect(screen, GREY, [470, 235, 50, 170])
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 60],1)
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 0],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 50],1)
 
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 51],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 40],1)
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 41],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 30],1)
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 31],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 20],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 21],1)
    
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 10],1)
    pygame.draw.rect(screen, BLACK, [475, 340, 40, 11],1)



    pygame.draw.rect(screen, LGREY, [274, 253, 162, 130])
   

     
    pygame.draw.ellipse(screen, BLACK, [475, 250, 28, 28])
    pygame.draw.ellipse(screen, BLACK, [475, 300, 28, 28])


    pygame.draw.rect(screen, BLACK, [271, 245, 168, 154],6) 
    pygame.draw.rect(screen, GREY, [440, 235, 15, 169])
    pygame.draw.rect(screen, GREY, [255, 236, 15, 167])
    pygame.draw.rect(screen, f , [274, 248, 162, 147])    

    
    if f == BLUE1:
        ''' sun '''
        
        pygame.draw.ellipse(screen, YELLOW, [400, 260, 28, 28])
        ''' clouds '''

        for s in clouds:
            draw_cloud(s)

        ''' grass '''
        pygame.draw.rect(screen, GREEN, [275, 375, 163, 20])


        draw_bush(250,335)
        draw_bush(300,335)
        draw_bush(350,335)
        draw_bush(375,335)


        draw_flower(xa,ya,c)
        draw_flower1(xb,yb,c)
        draw_flower2(xc,yc,c)
        

        ''' fence '''
        y = 350
        for x in range(279, 431, 29):
            pygame.draw.polygon(screen,WHITE, [[x+5, y], [x+10, y+5],
                                                [x+10, y+40], [x, y+40],
                                                [x, y+5]])
        pygame.draw.line(screen, WHITE, [275, 370], [437, 370], 5)
        pygame.draw.line(screen, WHITE, [275, 380], [437, 380], 5)

                
    else:
        pygame.draw.rect(screen, BLACK, [271, 245, 168, 154],6) 

        
    
    if tvbuzz1:
        pygame.draw.line(screen, WHITE, [489, 250], [489,264],3)
        pygame.draw.line(screen, BLACK, [475, 264], [489,264],3)
        pygame.draw.line(screen, BLACK, [489, 277], [489,264],3)
        pygame.draw.line(screen, BLACK, [502, 264],[489,264] ,3)
        

    elif count == 1 :
        pygame.draw.line(screen, BLACK, [489, 250], [489,264],3)
        pygame.draw.line(screen, WHITE, [475, 264], [489,264],3)
        pygame.draw.line(screen, BLACK, [489, 277], [489,264],3)
        pygame.draw.line(screen, BLACK, [502, 264],[489,264] ,3)
        pygame.draw.rect(screen, DBLUE , [274, 248, 162, 147])
        if f == BLACK:    
                pygame.draw.rect(screen, f , [274, 248, 162, 147])

        else:
                pass
                #pygame.mixer.music.play(laugh,-1)
                #screen.blit(friends,(274,249))
                screen.blit(guide,(274,250))
                myfont = pygame.font.SysFont("comicsansms", 7)
                # render text
                label = myfont.render("TV Show", 1, (255,255,255))
                
                screen.blit(label,(305,324))
                
                

    elif count == 2:
        pygame.draw.line(screen, BLACK, [489, 250], [489,264],3)
        pygame.draw.line(screen, BLACK, [475, 264], [489,264],3)
        pygame.draw.line(screen, WHITE, [489, 277], [489,264],3)
        pygame.draw.line(screen, BLACK, [502, 264],[489,264] ,3)
        pygame.draw.rect(screen, BLACK , [274, 248, 162, 147])
        pygame.draw.rect(screen, BLUE , [274, 248, 162, 147])
        
        
        if f == BLACK:    
                pygame.draw.rect(screen, f , [274, 248, 162, 147])
        else:       
                static = []
          
                for i in range(200,400):
                    x = random.randrange(274,450)
                    y = random.randrange(260, 380)
                    r = random.randrange(1,5)
                    z = [ x,y,r,r]
                        
                    static.append(z)
                
                
                for z in static:
                        pygame.draw.ellipse(screen,GREEN,z)

                
            
    elif count == 3:
        
        pygame.draw.line(screen, BLACK, [489, 250], [489,264],3)
        pygame.draw.line(screen, BLACK, [475, 264], [489,264],3)
        pygame.draw.line(screen, BLACK, [489, 277], [489,264],3)
        pygame.draw.line(screen, WHITE, [502, 264],[489,264] ,3)
        pygame.draw.rect(screen, WHITE , [274, 248, 162, 147])
        screen.blit(ad,(274,249))
        
        if f == BLACK:    
                pygame.draw.rect(screen, f , [274, 248, 162, 147])

        else:
            x = 274
            y = 335
            count2 = 5 
            while count2 > 0:
                screen.blit(shoe,(x,y))
                x +=1
                count2 -= 1
        
        
          

    elif count == 4:
        pygame.draw.line(screen, WHITE, [489, 250], [489,264],3)
        pygame.draw.line(screen, BLACK, [475, 264], [489,264],3)
        pygame.draw.line(screen, BLACK, [489, 277], [489,264],3)
        pygame.draw.line(screen, BLACK, [502, 264],[489,264] ,3)
        count -= 4
    else:
        pygame.draw.line(screen, WHITE, [489, 250], [489,264],3)   
        
        
    if tvbuzz:
        pygame.draw.line(screen, WHITE, [489, 328],[489,314],3)
        pygame.draw.line(screen, BLACK, [475, 314], [489,314],3)
        pygame.draw.line(screen, BLACK, [489, 300], [489,314],3)
        pygame.draw.line(screen, BLACK, [502, 314],[489,314],3)

    elif count1 == 1 :
        pygame.draw.line(screen, BLACK, [489, 328],[489,314],3)
        pygame.draw.line(screen, WHITE, [475, 314], [489,314],3)
        pygame.draw.line(screen, BLACK, [489, 300], [489,314],3)
        pygame.draw.line(screen, BLACK, [502, 314],[489,314],3)
        pygame.draw.rect(screen, GREEN , [274, 248, 162, 147])



        if f == BLACK:    
                pygame.draw.rect(screen, f , [274, 248, 162, 147])
        else:

                text = 1
                font = []
                for i in range(text):
                    x = random.randrange(265, 380)
                    y = random.randrange(250, 270)
                    t = [x, y]
                    font.append(t)


                def draw_credits(t):
                    x = t[0]
                    y = t[1]
                    myfont = pygame.font.SysFont("monospace", 25)
                # render text
                    label = myfont.render("Some text!", 1, (0,0,0))
                    screen.blit(label,t)
                    

                for t in font:
                    t[0] -= 1
                    if t[0] < 200:
                       t[0] = random.randrange(274, 380)
                       t[1] = random.randrange(274, 380)
                    draw_credits(t)
                                  
             

    elif count1 == 2:
        pygame.draw.line(screen, BLACK, [489, 328],[489,314],3)
        pygame.draw.line(screen, BLACK, [475, 314], [489,314],3)
        pygame.draw.line(screen, WHITE, [489, 300], [489,314],3)
        pygame.draw.line(screen, BLACK, [502, 314],[489,314],3)
        
    elif count1 == 3:
        pygame.draw.line(screen, BLACK, [489, 328],[489,314],3)
        pygame.draw.line(screen, BLACK, [475, 314], [489,314],3)
        pygame.draw.line(screen, BLACK, [489, 300], [489,314],3)
        pygame.draw.line(screen, WHITE, [502, 314],[489,314],3)
        pygame.draw.rect(screen, WHITE , [274, 248, 162, 147])
       
        screen.blit(music1,(290,302))
        screen.blit(bbox,(274,332))

        if f == BLACK:    
                pygame.draw.rect(screen, f , [274, 248, 162, 147])

        else:

            if dancer:
                screen.blit(music1,(274,292))
                screen.blit(music2,(290,292))
                screen.blit(man1,(274,232))
                
            else:
                screen.blit(man2,(274,232))

            if dancerglass:
                screen.blit(glasses,(274,232))
                
            else:
                pass

       

      

    elif count1 == 4:
        pygame.draw.line(screen, WHITE, [489, 328],[489,314],3)
        pygame.draw.line(screen, BLACK, [475, 314], [489,314],3)
        pygame.draw.line(screen, BLACK, [489, 300], [489,314],3)
        pygame.draw.line(screen, BLACK, [502, 314],[489,314],3)
        pygame.draw.rect(screen, WHITE , [274, 248, 162, 147])
        count1 -= 4

        if f == BLACK:    
                pygame.draw.rect(screen, f , [274, 248, 162, 147])

        else:
            pass
    else:
        pygame.draw.line(screen, WHITE, [489, 250], [489,264],3)   
           
  
   
    
    pygame.draw.rect(screen, BLACK, [271, 245, 168, 154],6)
    pygame.draw.rect(screen, GREY, [440, 235, 15, 169])
    pygame.draw.rect(screen, GREY, [255, 236, 15, 167])
    #pygame.draw.polygon(screen, DAGREY, [[450, 500], [300,500], [500, 200]]) 
    #pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
   # pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)
   

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
