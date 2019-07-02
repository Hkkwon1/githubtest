import pygame
import sys
from time import sleep

BLACK = {0, 0, 0}
padWidth = 500
padHeigt = 500

def initGame():
    global gamepad,clodck
    pygame.init()
    gamepad = pygame.display.set_mode((padWidth,padHeight))
    pygame.display.set_ception('pyshooting')
    clock = pygame.time.clock()

def runGame():
    global gamepad, clock

    ongame = False
    while not ongame: #각종 이벤트를 처리함
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        gamepad.fill(BLACK)

        pygame.display.update() #화면을 다시 한번 그려준다

        clock.tick(60) #초당 프레임수를 60으로 하겠다

    pygame.quit()


initGame() 
runGame()
        

       

        



        
                
                
            
