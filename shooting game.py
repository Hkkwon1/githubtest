import pygame
import sys
import random # 운석이 랜덤으로 떨어지게 하기 위해서
from time import sleep

BLACK = (0, 0, 0)
padWidth = 400
padHeight = 640
rockimage = ['rock01,png','rock02.png','rock03.png', 'rock04.png','rock05.png',\
             'rock06,png','rock07.png','rock08.png', 'rock09.png','rock10.png',\
             'rock11,png','rock12.png','rock13.png', 'rock14.png','rock15.png',\
             'rock16,png','rock17.png','rock18.png', 'rock19.png','rock20.png',\
             'rock21,png','rock22.png','rock23.png', 'rock24.png','rock25.png',\
             'rock26,png','rock27.png','rock28.png', 'rock29.png','rock30.png']


def drawObject(obj, x, y): #게임에 나오는 객체를 드로잉한다
    global gamePad
    gamePad.blit(obj, (x, y))
    




def initGame():
    global gamePad, clock, background,fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('pyshooting')
    background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    explosion = pygame.image.load('explosion.png')
    clock = pygame.time.Clock()


def runGame():
    global gamePad, clock, background,fighter,missile, explosion
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    isShot = False #전투기 미사일에 돌이 맞은 경우
    shotCount = 0
    rockpassd = 0

    x= padWidth * 0.45   #전투기 위치 표시
    y= padHeight*0.9
    fighterX = 0

    missileXY = [] #미사일이 여러개니까 리스트 형태로 저장한다

    #운석을 생성한다
    rock = pygame.image.load(random.choice(rockimage))
    rockSize = rock.get_rect().size #운석의 사이즈
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    #운석 초기 위치 설정
    rockX= random.randrange(0, padWidth-rockWidth)
    rockY= 0
    rockSpeed = 2

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit
                sys.exit()
            if event.type in [pygame.KEYDOWN]: #전투기 왼쪽으로 이동
                if event.key == pygame.K_LEFT:
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT: #전투기 오른쪽으로 이동
                    fighterX += 5
                elif event.key == pygame.K_SPACE:
                    missileX = x+ fighterWidth/2
                    missileY = y- fighterHeight
                    missileXY.append([missileX,missileY]) # missileXY = []라는 리스트에 좌표값을 저장해준다 
                
            if event.type in [pygame.KEYUP]:  #방향키를 때면 멈춤
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    fighterX = 0
                    


                
      

        drawObject(background, 0, 0) #배경화면 그리기

        x += fighterX #입력받은 전투기위치를 X에 반영시킨다
        if x < 0: #게임화면 왼쪽으로 벗어나게 되면 0으로 값을 지정해서 밖으로 못빠져나가게 한다
            x = 0
        elif x > padWidth-fighterWidth: #화면 오른쪽으로 완전히 벗어나지 못하게 한다
            x = padWidth-fighterWidth
        



        
        drawObject(fighter, x, y) #전투기를 그린다

        #미사일 발사하기
        if len(missileXY) !=0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1] #미사일이 -10씩이동하니까 리스트 값이 변화해야 한다

                #미사일이 운석을 맞춘경우

                if bxy[1] < rockY:
                    

                if bxy[1] <= 0: # 미사일이 화면을 벗어나면
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        rockY += rockSpeed
        if rockY > padHeight:
             rock = pygame.image.load(random.choice(rockimage))
             rockWidth = rockSize[0]
             rockHeight = rockSize[1]
             rockX = random.randrange(0, padWidth- rockWidth)
             rockY = 0
            
          

        drawObject(rock, rockX, rockY) 
                
                
        

        pygame.display.update() #게임화면을 다시그린다
        

        clock.tick(60)

    pygame.quit()

initGame()
runGame()
        

    

            
