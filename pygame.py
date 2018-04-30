import pygame,random,time,sys

check_error=pygame.init()
if check_error[1]>0:
    print("(!) Had {0} initializing errors , exiting ...".format(checck_error[1]))
    sys.exit(-1)
else:
    print("(+) Pygame succesfully initialized ! ")
# Play surface
plysrfce=pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake")

# Colours
r=pygame.Color(255,0,0) # Game over
g=pygame.Color(0,255,0) # Snake
b=pygame.Color(0,0,0) # Score
w=pygame.Color(255,255,255) #background
bwn=pygame.Color(165,42,42) #food

# Fps controller
fps=pygame.time.Clock()

# snake info
snstrt=[100,50]
snakebody=[[100,50],[90,50],[80,50]]

#Food
foodpos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodspawn=True

# Direction 
direction='RIGHT'
changeto=direction
global score
score=0
def shwscr(choice=1):
    
    fnt=pygame.font.SysFont('manoca',24)
    ssrf=fnt.render('Score : {0}'.format(score),True,(0,0,0))
    srct=ssrf.get_rect()
    if choice==1:
        srct.midtop=(60,10)
    else:
        srct.midtop=(360,120)
    
    plysrfce.blit(ssrf,srct)    
# Gameover func
def gameover():
    fnt=pygame.font.SysFont('monaco',72)
    srf=fnt.render('Game Over !',True,(255,0,0))
    rct=srf.get_rect()
    rct.midtop=(360,15)
    plysrfce.blit(srf,rct)
    pygame.display.flip()
    shwscr(634)
    time.sleep(2)
    pygame.quit()
    sys.exit()
# main logic
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit
            sys.exit
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or  event.key==ord('d'):
                changeto='RIGHT'
            if event.key==pygame.K_LEFT or  event.key==ord('a'):
                changeto='LEFT'
            if event.key==pygame.K_UP or  event.key==ord('w'):
                changeto='DOWN'
            if event.key==pygame.K_DOWN or  event.key==ord('s'):
                changeto='UP'
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Directions validations
    if changeto=='RIGHT' and not direction =='LEFT':
        direction='RIGHT'
    if changeto=='LEFT' and not direction =='RIGHT':
        direction='LEFT'
    if changeto=='UP' and not direction =='DOWN':
        direction='UP'
    if changeto=='DOWN' and not direction =='UP':
        direction='DOWN'
        
    #  Directions 
    if direction =='RIGHT':
        snstrt[0] += 10
    if direction =='LEFT':
        snstrt[0] -= 10
    if direction =='DOWN':
        snstrt[1] -= 10
    if direction =='UP':
        snstrt[1] += 10

    # Snake Mech
    snakebody.insert(0,list(snstrt))
    if snstrt[0] == foodpos[0] and snstrt[1] == foodpos[1]:
        score +=1
        foodspawn=False
    else:
        snakebody.pop()
    if foodspawn==False:
        foodpos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
        foodspawn=True
    plysrfce.fill((255,255,255))
    # SNAKE MOVEMENT 
    for pos in snakebody:
        pygame.draw.rect(plysrfce,(0,255,0),
                         pygame.Rect(pos[0],pos[1],10,10))
        pygame.draw.rect(plysrfce,(255,0,0),
                         pygame.Rect(foodpos[0],foodpos[1],10,10))
        if snstrt[0] > 710 or snstrt[0]<0:
            gameover()
        if snstrt[1] > 440 or snstrt[1]<0:
            gameover()
        for blc in snakebody[1:]:
            if blc[0]==snstrt[0] and blc[1]==snstrt[1]:
                gameover()
    shwscr()
    pygame.display.flip()
    fps.tick(25) 
   
           
            
