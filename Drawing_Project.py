import pygame
import math
import random

pygame.mixer.pre_init()
pygame.init()


# Window
SIZE = (800, 500)
TITLE = "AP_COMP_FINAL"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60
 

# Colors
RED = (250, 24, 31)
GREEN = (0, 255, 0)
BLUE = (33, 65, 103)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
GREY = (196, 196, 196)



#images
paint_stroke = pygame.image.load("img/paint_stroke.png")

def stroke():
    num_strokes = 1
    stroke = []
    for i in range(num_strokes):
        x = 100
        y = random.randrange(150, 270)
    #loc = [x, y]
    #stroke.append(loc)
        
    screen.blit(paint_stroke,(y,x))

    
    
    
        
left_click = False
right_click = False  
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                left_click = True 
                print("left_click")
            elif event.button == 2:
                print("mid_click")
            else:
                right_click = True
                print("right_click")
                      

                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
           
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_LEFT:
                
                pass
            elif event.key == pygame.K_RIGHT:
                pass
                
                # Game logic (Check for collisions, update points, etc.)
                


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    # Drawing code


    

    
    screen.fill(BLACK)

    mouse_pos = pygame.mouse.get_pos()
    player1 = [mouse_pos[0], mouse_pos[1], 50, 50]
    pygame.draw.rect(screen, RED, player1)

    if left_click == True:
        strokes = []
        get_pos = pygame.mouse.get_pos()
        loc = [get_pos[0], get_pos[1]]
        strokes.append(loc)

        
        pygame.draw.rect(screen, WHITE, [strokes , 50, 50])
        
 

    

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()




