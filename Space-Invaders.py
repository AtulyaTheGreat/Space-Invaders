"""
This is a space invaders game
Hope you enjoy this game!

Developed By-
AtulyaTheGreat


"""



import pygame
import random
import math


from pygame import mixer



pygame.init( )


screen = pygame.display.set_mode((800, 600))

#caption
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('bg.jpg')

#music
mixer.music.load('background.wav')
mixer.music.play(-1)

#player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480 
playerX_change = 0

#enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num = 6 

for i in range(num):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.8)
    enemyY_change.append(40)


#bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0 
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score 
score = 0
font = pygame.font.Font('04B_19.TTF', 30)

textX = 10
textY = 10

#Game over
over = pygame.font.Font('04B_19.TTF', 64)

def show_score(x,y):
    score_value = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(score_value,(x,y)) 

def game_over():
    over_end = over.render("GAME OVER " , True, (0,0,0))
    screen.blit(over_end,(200,250))

def Player(x,y):
    screen.blit(playerimg,(x,y))


def Enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def Fire_bullet(x,y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletimg,(x + 16,y + 10))



def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2))))
    if distance < 27:
        return True
    else:
        return False


#game loop

run = True
while run:
    screen.fill((0,0,0))
    #bg image
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            
            elif event.key == pygame.K_RIGHT:
                playerX_change = 2
            
            elif event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    Fire_bullet(playerX, bulletY)
       
       
        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                playerX_change = 0

 
       
    # eg x = 5
    # 5 +(-0.1) = 5 - 0.1
    playerX += playerX_change 
    enemyX += enemyX_change

    #boundary
    if playerX <=0:
        playerX = 736
    elif playerX>= 736:
        playerX = 0 
    #enemy movement
    for i in range(num):
        #Game Over
        if enemyY[i] >  535:
            for j in range(num):  
                enemyY[j] = 2000
                game_over()
                break
            

  

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 0.8
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.8
            enemyY[i] += enemyY_change[i]

        #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 10
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)
        
        Enemy(enemyX[i], enemyY[i], i)

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    elif bullet_state is "fired":
        Fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change 




    Player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()   


# code ends here
