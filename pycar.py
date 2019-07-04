import pygame
import random
from time import sleep

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

class car:
    image_car = ['RacingCar01.png','RacingCar02.png','RacingCar03.png','RacingCar04.png','RacingCar05.png','racingCar06.png',\
                 'RacingCar07.png','RacingCar08.png','RacingCar09.png','RacingCar10.png','RacingCar11.png','racingCar12.png',\
                 'RacingCar13.png','RacingCar14.png','RacingCar15.png','RacingCar16.png','RacingCar17.png','racingCar18.png',\
                 'RacingCar19.png','RacingCar20.png']

    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image =
        self.x = x
        self.y = y 
        self.dx = dx
        self.dy = dy

    def load_image(self):
        self.image = pygame.image.load(random.choice(self.image_car))#이미지를 랜덤으로 불러 오겠다
        self.width = self.image.get_rect().size[0]  #불러온 이미지에 대한 폭 높이
        self.height = self.image.get_rect().size[1]


    def draw_image(self):
        screen.blit(self.image, [self.x, self.y]) #x,y위치에 이미지를 그려준다


    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self): #게임을 만들때 항상 화면 밖으로 나가지 않게 설정 해준다
        if.self.x+self.width > WINDOW_WIDTH or self.x<0:
            self.x -= self.dx

    def check_crash(slef, car):
        if (self.x+self.width > car.x) and (self.x < car.x+car.width) and (self.y <car.y+car.height) and (self.y +car.height>car.y):
            return True

        else:
            return False





if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #게임화면에 대한 설정
    pygame.display.set_ception('Pycar')
    clock = pygame.time.clock()

    pygame.mixer.music.load('race.wav')
    sound_crash = pygame.mixer.sound('crash.wav')
    sound_engine = pygame. mixer.sound('engine.wav')

    player = car((WINDOW_WIDTH / 2), (WINDOW_HEIGHT - 150), 0, 0)
    player.load_image()

    cars = []
    car_count *4
    for i in range(car_count):
        x = random.randrange(0, WINDOW_WIDTH-55)
        y = random.randrange(-150,-50)
        car = car(x, y, 0, random.randint(5,10)) #장애물 자동차의 속도를 5에서 10사이에서 오게끔하는것
        car.load_image()
        cars.append(car) #car라는 객체를 추가해주어야 한다.

    lanes = []
    lane_width= 10
    lane_height= 80
    lane_margin = 20
    lane_count = 20
    lane_x = (WINDOW_WIDTH - lane_width)/2
    lane_y = -10
    for i in range(lane_count):
        lanes.append([lane_x,lane_y])
        lane_y += lane_height + lane_margin
        

     score = 0
     crash = True
     game_on = True
     while game_on:
         for event in pygame.event.get():
             if evnet,type == pygame.QUIT:
                 game_on = False

             if crash:
                 if event.tpye == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                     crash = False
                     for i in range(car_count):
                         cars[i].x = random.randrange(0, WINDOW_WIDTH-cars[i].width)
                         cars[i].y = random.randrange(-150,-50)
                         cars[i].load_image()

                     player.load_image()
                     player.x =
                     player.dx = 0
                     score = 0
                     pygame.mouse.set_visible(False)
                     sound.engine.play()
                     sleep(5)
                     pygame.mixer.music.play(-1)#반복해서 음악틀어준다

            if not crash:
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RIGHT:
                        player.dx = 4

                    elif event.type == pygame.K_LEFT:
                        player.dy = -4

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player.dx= 0

                    if event.type == pygame.K_LEFT:
                        player.dx = 0


        screen.fill(GRAY)

        if not crash: # 중앙선이 반복해서 표시해준다
            for i in range(lane_count):
                pygame.draw.rect(screen, WHITE, [lanes[i][0], lanes[i][1], lane_width, lane_height])
                lanes[i][1] += 10
                
    
    
            
