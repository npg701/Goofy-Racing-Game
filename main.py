import pygame as pg

import time 
from ingame_objects import PlayerVehicle, Track, banana, booster, Checkpoint
from menu_objects import button, selector

from gameview import screen, obstacle_setup, start_game, display_text

#Load all images
purple_car = pg.image.load('imgs/Purple_car.png')
green_car = pg.image.load('imgs/Green_car.png')
blue_car = pg.image.load('imgs/Blue_car.png')
pink_car = pg.image.load('imgs/Pink_car.png')
teal_car = pg.image.load('imgs/Teal_car.png')
yellow_car = pg.image.load('imgs/Yellow_car.png')
#tracks and borders
track1img = pg.image.load('imgs/trk1.png')
border1 = pg.image.load('imgs/trk1border.png')
track2img = pg.image.load('imgs/trk2.png')
border2 = pg.image.load('imgs/trk2border.png')
#finish lines adn checkpoints
finish2img = pg.image.load('imgs/finish.png')
finish1img =  pg.image.load('imgs/finish2.png')
check2img = pg.image.load('imgs/trk1check.png')
check1img =  pg.image.load('imgs/trk2check.png')


#menu backgrounds
menuback = pg.image.load('imgs/Goofy Racing.png')
p1winback = pg.image.load('imgs/Goofy p1 Win.png')
p2winback = pg.image.load('imgs/Goofy p2 Win.png')
solowinback = pg.image.load('imgs/Goofy solo Win.png')
cyber = pg.image.load('imgs/cyber.png')

wins2p = [p1winback,p2winback]

p1buttonimg = pg.image.load('imgs/1pbutton.png')
p2buttonimg = pg.image.load('imgs/2pbutton.png')
bananaimg = pg.image.load('imgs/banana.png')
boostimg = pg.image.load('imgs/boost.png')

zero= pg.image.load('imgs/0.png')
one= pg.image.load('imgs/1.png')
two= pg.image.load('imgs/2.png')
three= pg.image.load('imgs/3.png')
four= pg.image.load('imgs/4.png')
five= pg.image.load('imgs/5.png')
six= pg.image.load('imgs/6.png')
seven= pg.image.load('imgs/7.png')
eight= pg.image.load('imgs/8.png')
numbers = [zero,one,two,three,four,five,six,seven,eight]
track_num_lst = [one,two]

pg.init()

pg.mixer.init()

pg.mixer.music.load('synth.mp3')

pg.mixer.music.set_volume(1)

pg.mixer.music.play()


track1obstacle_locations = [(93, 91) ,(141, 78) ,(186, 58) ,(185, 144) ,(235, 162) ,(289, 190) ,(299, 126) ,(258, 88) ,(298, 39) ,(352, 91) ,(399, 87) ,(497, 176) ,(478, 235) ,(514, 271) ,(497, 351) ,(478, 439) ,(500, 485) ,(448, 531) ,(415, 601) ,(362, 608) ,(294, 660) ,(230, 628) ,(166, 662) ,(149, 624) ,(128, 577) ,(148, 511) ,(203, 499) ,(243, 532) ,(274, 500) ,(328, 521) ,(383, 471) ,(430, 455) ,(391, 371) ,(431, 328) ,(407, 266) ,(348, 258) ,(313, 284) ,(273, 259) ,(248, 293) ,(198, 264) ,(217, 325) ,(195, 355) ,(247, 366) ,(271, 334) ,(336, 382) ,(293, 411) ,(226, 448) ,(195, 417) ,(130, 407) ,(123, 336) ,(90, 293) ,(125, 255) ,(94, 221)]
track2obstacle_locations = [(71, 321), (29, 371), (72, 445),(48, 536), (93, 645),(117, 609), (257, 612) ,(202, 574) ,(217, 500) ,(134, 486) ,(161, 396) ,(225, 409) ,(311, 361) ,(357, 443) ,(415, 479) ,(385, 609), (457, 641) ,(469, 592) ,(545, 529) ,(495, 476) ,(541, 399) ,(494, 356) ,(456, 254) ,(406, 301) ,(368, 255) ,(260, 258) ,(183, 221) ,(171, 159) ,(191, 294) ,(250, 148),(324, 196) ,(431, 152) , (487, 182) ,(497, 113) ,(396, 38), (199, 46),(213, 86) ,(131, 69) ,(104, 150), (69, 139)]  

track2 = Track(track1img, border1,(80,120),track1obstacle_locations,(100,160),(120,160) )
track1 = Track(track2img, border2,(20,220),track2obstacle_locations,(30,260),(60,260) )

finish1 = Checkpoint(finish1img)
finish2 = Checkpoint(finish2img)
check1 = Checkpoint(check1img)
check2 = Checkpoint(check2img)
finishes = [finish1,finish2]
checks = [check1,check2]

tracks = [track1, track2]

w , h = track1.img.get_width(), track1.img.get_height() # both tracks were created to be the exact same dimensions in the window so this would work



disp = pg.display.set_mode((w,h))

pg.display.set_caption('Goofy Racing')

ck = pg.time.Clock()#setup a clock to make game run at a constant rate by ticking at a framerate

fps = 120


car_select = [green_car,purple_car,blue_car,pink_car,teal_car,yellow_car]
i = 0 
j = 1






#gets masks for button on menu
p1buttonMask = pg.mask.from_surface(p1buttonimg)
p2buttonMask = pg.mask.from_surface(p2buttonimg)

#initialize buttons
p1button = button([w/2-200,h/2-175,400,75],p1buttonimg)
p2button = button([w/2-200,h/2-70,400,75],p2buttonimg)

#initialize selectors
car_selector = selector(0,5,pg.K_LEFT,pg.K_RIGHT)
car_selector2 = selector(0,5,pg.K_a,pg.K_d)
obs_selector = selector(0,8,pg.K_z,pg.K_x)
track_selector = selector(0,1,pg.K_1,pg.K_2)
lap_selector = selector(1,8,pg.K_c,pg.K_v)

track_num = 0
lap_goal = 2
banana = banana(bananaimg)
booster = booster(boostimg)
obsnum = 0

def check_lap(car, finish, track , check):
    if (car.collision(finish.border,track.finish_loc)!= None) and car.check:
        car.laps += 1 #if the car has passed the checkpoint and hits the finish line, count the lap
        car.check = False #reset checpoint
        return True

    if car.collision(check.border):
        car.check = True  #checkpoint
    return False

def check_win(car,lap_goal):
    if car.laps == lap_goal:
        car.win = True #marks which car won
        return car.player

lap_times = [] # empty list to hold laptimes


winner = int
game = False
running = True #run game but only the menu
winScreen= False
while running:
    menuimgs = [(menuback,(0,0)),(car_select[i], (w/2+175,h/2+130)),(car_select[j], (w/2+175,h/2+230)), (numbers[obsnum],(w/2+150,h/2+310)), (track_num_lst[track_num],(w/2+220,h/2+27)),(numbers[lap_goal],(w/2-60,h/2+27))]
    #list of aall the menu images to print them to the screen
    
    mousepos = pg.mouse.get_pos()
    

    #pause so the selectors have a short dead period
    time.sleep(.15)
    keys = pg.key.get_pressed()
    i = car_selector.change(keys,i)
    j = car_selector2.change(keys,j)
    obsnum = obs_selector.change(keys,obsnum)
    track_num = track_selector.change(keys, track_num)
    lap_goal = lap_selector.change(keys, lap_goal)
    #chang all of the selectors 

    for event in pg.event.get():
        if event.type == pg.QUIT: #close game if the x is clicked
            running = False
            break
        if p1button.check_clicked(event,mousepos):
            players = 1 #set up game for 1 player if the button is pressed
            track = tracks[track_num]
            finish = finishes[track_num]
            check = checks[track_num]
            player1_car = PlayerVehicle(5,6,0.25,0.4,car_select[i], 1,track.p1_start)
            cars = [player1_car]
            obstacles = obstacle_setup(obsnum,track.obstacle_locations,banana,booster)
            imgs= [(cyber,(0,0)),(check.img,(0,0)),(track.img,(0,0)),(finish.img,track.finish_loc),(track.borderimg,(0,0))]
            start_game(disp, imgs, numbers,w,h,cars,obstacles) #countdown
            lasttime = time.time()
            game=True
        if p2button.check_clicked(event,mousepos):
            players = 2 #set up game for 2 players if the button is pressed 
            track = tracks[track_num]
            finish = finishes[track_num]
            check = checks[track_num]
            player1_car = PlayerVehicle(5,6,0.25,0.4,car_select[i], 1, track.p1_start)
            player2_car = PlayerVehicle(5,6,0.25, 0.4,car_select[j],2, track.p2_start)
            cars = [player1_car,player2_car]
            obstacles = obstacle_setup(obsnum,track.obstacle_locations,banana,booster)
            imgs= [(cyber,(0,0)),(check.img,(0,0)),(track.img,(0,0)),(finish.img,track.finish_loc),(track.borderimg,(0,0))]
            start_game(disp, imgs, numbers,w,h,cars,obstacles) #countdown
            lasttime = time.time()
            game=True

    
    if p1button.check_hover(mousepos,disp) and p2button.check_hover(mousepos,disp):
        screen(disp,menuimgs) #draw the screen wihtout the buttons if they are not being hovered over.

    pg.display.update() #update the display






    while game:

        ck.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT: #close game if the x is clicked
                game = False
                running = False
                break
        screen(disp,imgs,cars, obstacles)
        keys = pg.key.get_pressed()
        
        for car in cars: #iterate through the cars and check laps, wins, and collision with obstacles/ the wall after controlling them
            car.control(keys)

            if car.collision(track.border) != None:
                car.recoil() #recoil the car if a border is touched
            if check_lap(car, finish , track, check) and (players==1):
                laptime=round((time.time() - lasttime), 2) #reset the laptime if a lap was completed and add the last to the list
                lasttime = time.time()
                lap_times.append(laptime)
            
            if check_win(car, lap_goal):
                winner = int (check_win(car, lap_goal))
                winScreen = True #if a player won, send game to end screen
                running= False
                game = False
                
            for o in obstacles:
                if o[0].type == 'banana':
                    if car.collision(o[0].get_mask(),o[1])!= None:
                        banana.spin(car) #spin the car if a banana is touched
                    else:
                        car.spin = False
                if (o[0].type == 'booster') and (car.collision(o[0].get_mask(),o[1])!= None):
                    booster.boost(car) #boost car if a booster is touched


while winScreen:
    if players ==2:
        winimg = wins2p[winner-1] # display image corresponding to who won
        winimgs = [(winimg,(0,0))]
        screen (disp,winimgs)
    if players ==1:
        winimgs = [(solowinback,(0,0))]
        best_lap = min(lap_times) # get best lap time
        text = 'Best lap: ' + str(best_lap)
        screen (disp,winimgs) #print win screen with lap time
        display_text(disp, text, w,h)
        pg.display.update()
        time.sleep(1) # pause so the text flickers less
        
    
    for event in pg.event.get():
        if event.type == pg.QUIT: #close game if the x is clicked
            winScreen = False # need this block so game can be closed
            break
    

pg.quit() 