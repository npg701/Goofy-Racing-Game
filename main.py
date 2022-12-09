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

track1img = pg.image.load('imgs/trk1.png')
border1 = pg.image.load('imgs/trk1border.png')
track2img = pg.image.load('imgs/trk2.png')
border2 = pg.image.load('imgs/trk2border.png')

finish2img = pg.image.load('imgs/finish.png')
finish1img =  pg.image.load('imgs/finish2.png')
check2img = pg.image.load('imgs/trk1check.png')
check1img =  pg.image.load('imgs/trk2check.png')



menuback = pg.image.load('imgs/Goofy Racing.png')
p1winback = pg.image.load('imgs/Goofy p1 Win.png')
p2winback = pg.image.load('imgs/Goofy p2 Win.png')
solowinback = pg.image.load('imgs/Goofy solo Win.png')

wins2p = [p1winback,p2winback]

p1buttonimg = pg.image.load('imgs/1pbutton.png')
p2buttonimg = pg.image.load('imgs/2pbutton.png')
cyber = pg.image.load('imgs/cyber.png')
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
#Load audio file
pg.mixer.music.load('synth.mp3')
#Set preferred volume
pg.mixer.music.set_volume(1)
#Play the music
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

w , h = track1.img.get_width(), track1.img.get_height()



disp = pg.display.set_mode((w,h))

pg.display.set_caption('Goofy Racing')

ck = pg.time.Clock()#setup a clock to make game run at a constant rate

fps = 120


car_select = [green_car,purple_car,blue_car,pink_car,teal_car,yellow_car]
i = 0 
j = 1







p1buttonMask = pg.mask.from_surface(p1buttonimg)
p2buttonMask = pg.mask.from_surface(p2buttonimg)


p1button = button([w/2-200,h/2-175,400,75],p1buttonimg)
p2button = button([w/2-200,h/2-70,400,75],p2buttonimg)


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

def check_lap(player_car, finish, track , check):
    if (player_car.collision(finish.border,track.finish_loc)!= None) and (player_car.prevfram == None) and player_car.check:
        player_car.laps += 1
        player_car.check = False
        return True
    player_car.prevfram = player_car.collision(finish.border,track.finish_loc)
    if player_car.collision(check.border):
        player_car.check = True
    return False

def check_win(player_car,lap_goal):
    if player_car.laps == lap_goal:
        player_car.win = True
        return player_car.player

lap_times = []


winner = int
game = False
running = True
winScreen= False
while running:
    menuimgs = [(menuback,(0,0)),(car_select[i], (w/2+175,h/2+130)),(car_select[j], (w/2+175,h/2+230)), (numbers[obsnum],(w/2+150,h/2+310)), (track_num_lst[track_num],(w/2+220,h/2+27)),(numbers[lap_goal],(w/2-60,h/2+27))]
    # ADD A LIST OF TEXT VALUEs FOR 0 - 10 FOR OBSTACLE SELECTOR USING INDEX OBSNUM
    
    mousepos = pg.mouse.get_pos()
    

    
    
    time.sleep(.15)
    keys = pg.key.get_pressed()
    i = car_selector.change(keys,i)
    j = car_selector2.change(keys,j)
    obsnum = obs_selector.change(keys,obsnum)
    track_num = track_selector.change(keys, track_num)
    lap_goal = lap_selector.change(keys, lap_goal)

    for event in pg.event.get():
        if event.type == pg.QUIT: #close game if the x is clicked
            running = False
            break
        if p1button.check_clicked(event,mousepos):
            players =1
            track = tracks[track_num]
            finish = finishes[track_num]
            check = checks[track_num]
            player1_car = PlayerVehicle(5,6,0.25,0.4,car_select[i], 1,track.p1_start)
            cars = [player1_car]
            obstacles = obstacle_setup(obsnum,track.obstacle_locations,banana,booster)
            imgs= [(cyber,(0,0)),(check.img,(0,0)),(track.img,(0,0)),(finish.img,track.finish_loc),(track.borderimg,(0,0))]
            start_game(disp, imgs, numbers,w,h,cars,obstacles)
            lasttime = time.time()
            game=True
        if p2button.check_clicked(event,mousepos):
            players =2 
            track = tracks[track_num]
            finish = finishes[track_num]
            check = checks[track_num]
            player1_car = PlayerVehicle(5,6,0.25,0.4,car_select[i], 1, track.p1_start)
            player2_car = PlayerVehicle(5,6,0.25, 0.4,car_select[j],2, track.p2_start)
            cars = [player1_car,player2_car]
            obstacles = obstacle_setup(obsnum,track.obstacle_locations,banana,booster)
            imgs= [(cyber,(0,0)),(check.img,(0,0)),(track.img,(0,0)),(finish.img,track.finish_loc),(track.borderimg,(0,0))]
            start_game(disp, imgs, numbers,w,h,cars,obstacles)
            lasttime = time.time()
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
            #if event.type == pg.MOUSEBUTTONDOWN:
                #print(mousepos, end = " ,") 
        screen(disp,imgs,cars, obstacles)
        keys = pg.key.get_pressed()
        
        

        for player_car in cars:
            player_car.control(keys)

            if player_car.collision(track.border) != None:
                player_car.recoil()
            if check_lap(player_car, finish , track, check) and (players==1):
                laptime=round((time.time() - lasttime), 2)
                lasttime = time.time()
                lap_times.append(laptime)
            
            if check_win(player_car, lap_goal):
                winner = int (check_win(player_car, lap_goal))
                winScreen = True
                running= False
                game = False
                
            for o in obstacles:
                if o[0].type == 'banana':
                    if player_car.collision(o[0].get_mask(),o[1])!= None:
                        banana.spin(player_car)
                    else:
                        player_car.spin = False
                if (o[0].type == 'booster') and (player_car.collision(o[0].get_mask(),o[1])!= None):
                    booster.boost(player_car)


while winScreen:
    if players ==2:
        winimg = wins2p[winner-1]
        winimgs = [(winimg,(0,0))]
        screen (disp,winimgs)
    if players ==1:
        winimgs = [(solowinback,(0,0))]
        best_lap = min(lap_times)
        text = 'Best lap: ' + str(best_lap)
        screen (disp,winimgs)
        display_text(disp, text, w,h)
        pg.display.update()
        time.sleep(1)
        ###lap time Leaderboard???
    
    for event in pg.event.get():
        if event.type == pg.QUIT: #close game if the x is clicked
            winScreen = False
            break
    

pg.quit()