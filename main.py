import pygame as pg

import time , random
from ingame_objects import PlayerVehicle, Track, banana, booster, Finish
from menu_objects import button, selector

from gameview import screen, obstacle_setup

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

finish1img = pg.image.load('imgs/finish.png')
finish2img =  pg.image.load('imgs/finish2.png')



menuback = pg.image.load('imgs/Goofy Racing.png')

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

track1 = Track(track1img, border1,(80,120),track1obstacle_locations,(100,160),(120,160) )
track2 = Track(track2img, border2,(20,220),track2obstacle_locations,(30,260),(60,260) )

finish1 = Finish(finish1img)
finish2 = Finish(finish2img)
finishes = [finish1,finish2]

tracks = [track1, track2]

w , h = track1.img.get_width(), track1.img.get_height()



disp = pg.display.set_mode((w,h))

pg.display.set_caption('Goofy Racing')

running = True

ck = pg.time.Clock()#setup a clock to make game run at a constant rate

fps = 120


car_select = [green_car,purple_car,blue_car,pink_car,teal_car,yellow_car]
i = 0 
j = 1







p1buttonMask = pg.mask.from_surface(p1buttonimg)
p2buttonMask = pg.mask.from_surface(p2buttonimg)


p1button = button([w/2-200,h/2-175,400,75],p1buttonimg)
p2button = button([w/2-200,h/2-70,400,75],p2buttonimg)
game = False

car_selector = selector(0,5,pg.K_LEFT,pg.K_RIGHT)
car_selector2 = selector(0,5,pg.K_a,pg.K_d)
obs_selector = selector(0,8,pg.K_z,pg.K_x)
track_selector = selector(0,1,pg.K_1,pg.K_2)
track_num = 1

banana = banana(bananaimg)
booster = booster(boostimg)


obsnum = 0

while running:
    menuimgs = [(menuback,(0,0)),(car_select[i], (w/2+175,h/2+130)),(car_select[j], (w/2+175,h/2+230)), (numbers[obsnum],(w/2+150,h/2+310)), (track_num_lst[track_num],(w/2+100,h/2+30))]
    # ADD A LIST OF TEXT VALUEs FOR 0 - 10 FOR OBSTACLE SELECTOR USING INDEX OBSNUM
    
    mousepos = pg.mouse.get_pos()
    

    
    
    time.sleep(.15)
    keys = pg.key.get_pressed()
    i = car_selector.change(keys,i)
    j = car_selector2.change(keys,j)
    obsnum = obs_selector.change(keys,obsnum)
    track_num = track_selector.change(keys, track_num)

    for event in pg.event.get():
        if event.type == pg.QUIT: #close game if the x is clicked
            running = False
            break
        if p1button.check_clicked(event,mousepos):
            players =1
            track = tracks[track_num]
            finish = finishes[track_num]
            player1_car = PlayerVehicle(4,5,0.15,0.3,car_select[i], 1,track.p1_start, track.p2_start)
            cars = [player1_car]
            obstacles = obstacle_setup(obsnum,track.obstacle_locations,banana,booster)
            imgs= [(cyber,(0,0)),(track.img,(0,0)),(finish.img,track.finish_loc),(track.borderimg,(0,0))]

            game=True
        if p2button.check_clicked(event,mousepos):
            players =2 
            track = tracks[track_num]
            finish = finishes[track_num]
            player1_car = PlayerVehicle(4,5,0.15,0.3,car_select[i], 1, track.p1_start, track.p2_start)
            player2_car = PlayerVehicle(4,5,0.15, 0.3,car_select[j],2, track.p1_start, track.p2_start)
            cars = [player1_car,player2_car]
            obstacles = obstacle_setup(obsnum,track.obstacle_locations,banana,booster)
            imgs= [(cyber,(0,0)),(track.img,(0,0)),(finish.img,track.finish_loc),(track.borderimg,(0,0))]
        
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
        player1_car.control(keys,1)
        if players ==2:
            player2_car.control(keys,2)
        


        for player_car in cars:
            if player_car.collision(track.border) != None:
                player_car.recoil()
            
            if player_car.collision(finish.border,track.finish_loc)!= None:
                print('finish')

            for o in obstacles:
                if o[0].type == 'banana':
                    if player_car.collision(o[0].get_mask(),o[1])!= None:
                        banana.spin(player_car)
                    else:
                        player_car.spin = False
                if o[0].type == 'booster':
                    if player_car.collision(o[0].get_mask(),o[1])!= None:
                        booster.boost(player_car)
                    


pg.quit()