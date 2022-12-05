import pygame as pg

import time , random
from objects import PlayerVehicle, Track, banana, booster
from menu import button, selector

from gameview import screen

#Load all images
border1 = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\trk1border.png")
border1Mask = pg.mask.from_surface(border1)

purple_car = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\Purple_car.png")
green_car = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\Green_car.png")
blue_car = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\Blue_car.png")
pink_car = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\Pink_car.png")
teal_car = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\Teal_car.png")
yellow_car = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\Yellow_car.png")

track1img = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\trk1.png")
finish = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\finish.png")

menuback = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\GOOFY RACING.png")

p1buttonimg = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\1pbutton.png")
p2buttonimg = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\2pbutton.png")
cyber = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\cyber.png")
bananaimg = pg.image.load("C:\\Users\\npg70\\OneDrive - Northeastern University\\Computing Fundamentals\\FINAL PROJECT GAME\\banana.png")

pg.init()

pg.mixer.init()
#Load audio file
pg.mixer.music.load('synth.mp3')
#Set preferred volume
pg.mixer.music.set_volume(1)
#Play the music
pg.mixer.music.play()

track1 = Track(track1img, border1Mask)
w , h = track1.img.get_width(), track1.img.get_height()



disp = pg.display.set_mode((w,h))

pg.display.set_caption('Goofy Racing')

running = True

ck = pg.time.Clock()#setup a clock to make game run at a constant rate

fps = 120


car_select = [green_car,purple_car,blue_car,pink_car,teal_car,yellow_car]
i = 0 
j = 1

imgs= [(cyber,(0,0)),(track1.img,(0,0)),(finish,(80,120)),(border1,(0,0))]




finishMask = pg.mask.from_surface(finish)
p1buttonMask = pg.mask.from_surface(p1buttonimg)
p2buttonMask = pg.mask.from_surface(p2buttonimg)


p1button = button([w/2-200,h/2-100,400,75],p1buttonimg)
p2button = button([w/2-200,h/2+30,400,75],p2buttonimg)
game = False

car_selector = selector(0,5,pg.K_LEFT,pg.K_RIGHT)
car_selector2 = selector(0,5,pg.K_a,pg.K_d)
obs_selector = selector(0,10,pg.K_z,pg.K_x)

bananamask = pg.mask.from_surface(bananaimg)
banana = banana(bananaimg,bananamask)

obstacle_locations = [(221, 131),(301, 119),(336, 45),(465, 191),(515, 352),(479, 439),(438, 588),(301, 631),(263, 670),(186, 634),(132, 582),(356, 532),(229, 505),(428, 464),(396, 345),(363, 259),(199, 271),(232, 341),(232, 419),(128, 340),(99, 276),(111, 230)]
obsnum = 0
obstacles = []
obst_loc_nums = []


while running:
    menuimgs = [(menuback,(0,0)),(car_select[i], (w/2+175,h/2+130)),(car_select[j], (w/2+175,h/2+230))]
    # ADD A LIST OF TEXT VALUEs FOR 0 - 10 FOR OBSTACLE SELECTOR USING INDEX OBSNUM
    
    mousepos = pg.mouse.get_pos()
    

    player1_car = PlayerVehicle(4,5,0.15,0.3,car_select[i], 1)
    player2_car = PlayerVehicle(4,5,0.15, 0.3,car_select[j],2)
    cars = [player1_car,player2_car]
    time.sleep(.05)
    keys = pg.key.get_pressed()
    i = car_selector.change(keys,i)
    j = car_selector2.change(keys,j)
    obsnum = obs_selector.change(keys,obsnum)

    for event in pg.event.get():
        if event.type == pg.QUIT: #close game if the x is clicked
            running = False
            break
        if p1button.check_clicked(event,mousepos):
            cars = [player1_car]
            for i in range (obsnum):
                i = random.randint(0,len(obstacle_locations)-1)
                obst_loc_nums.append(i)
            for x in obst_loc_nums:
                obstacles.append((banana,obstacle_locations[x]))
            
            game=True
        if p2button.check_clicked(event,mousepos):
            cars = [player1_car,player2_car]
            for i in range (obsnum):
                i = random.randint(0,len(obstacle_locations)-1)
                obst_loc_nums.append(i)
            for x in obst_loc_nums:
                obstacles.append((banana,obstacle_locations[x]))

            game=True

    
    if p1button.check_hover(mousepos,disp) and p2button.check_hover(mousepos,disp):
        screen(disp,menuimgs)

    pg.display.update()






    while game:
        
        
        ck.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT: #close game if the x is clicked
                game = False
                running = False
                break
            
                
        screen(disp,imgs,cars, obstacles)
        
        keys = pg.key.get_pressed()
        player1_car.control(keys,1)
        player2_car.control(keys,2)
        


        for player_car in cars:
            if player_car.collision(track1.border) != None:
                player_car.recoil()
            
            if player_car.collision(finishMask,(80,120))!= None:
                print('finish')


    
pg.quit()