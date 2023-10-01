import pygame

pygame.init()

x=0
y=0
width=50
height=50
ve=0
ac=0 
mass=.1

#misc
run=True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1500,100))
pygame.display.set_caption("velocy test")
dedug=True
while run:
    screen.fill((0,0,0))
    square_rect = pygame.Rect(x,y,width,height)
    pygame.draw.rect(screen,(100,100,255),square_rect)

    #controlles
    key = pygame.key.get_pressed()

    if key[pygame.K_d] == True:
        ac += 1
    elif key[pygame.K_a] == True:
        ac -= 1
    
    else:
        if bool(ac == 0) == False:
            
            if ac >0:
                ac -=1
            if ac <0:
                ac += 1
        
    if key[pygame.K_SPACE]==True:
        x=0
        y=0
        ac = 0
    #movement
    ve = mass*ac
    x += ve

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
    pygame.display.update()
    pass
if dedug == True:
    print("acclertion:",ac)
    print("velocity:",ve)
    print("mass:",mass)