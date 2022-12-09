import pygame as pg
import random
import time
def rotate_img(win, img, top_left, angle):
    rotated_img = pg.transform.rotate(img,angle)
    new_rec = rotated_img.get_rect(center = img.get_rect(topleft= top_left).center)
    win.blit(rotated_img, new_rec.topleft)

def screen(disp, imgs, player_car=False, obstacles=False):
    for img, pos in imgs:
        disp.blit(img, pos)
    if player_car:
        for car in player_car:
            car.print(disp)
    if obstacles:
        for o in obstacles:
            o[0].insert(disp,o[1])
    pg.display.update()

def obstacle_setup(obsnum,obstacle_locations,banana,booster):
    obstacles = []
    obst_loc_nums = []
    for i in range (obsnum):
        i = random.randint(0,len(obstacle_locations)-1)
        obst_loc_nums.append(i)
            
    for x in obst_loc_nums:
        obs = random.randint(0,1)
        if obs == 0:
            obstacles.append((banana,obstacle_locations[x]))
        if obs == 1:
            obstacles.append((booster,obstacle_locations[x]))
    return obstacles

def start_game(disp,imgs,numbers,w,h,cars,obstacles):
    imgs.append((numbers[3],(w/2,h/2)))
    screen(disp,imgs,cars,obstacles)
    imgs.remove((numbers[3],(w/2,h/2)))
    time.sleep(1)
    imgs.append((numbers[2],(w/2,h/2)))
    screen(disp,imgs,cars,obstacles)
    imgs.remove((numbers[2],(w/2,h/2)))
    time.sleep(1)
    imgs.append((numbers[1],(w/2,h/2)))
    screen(disp,imgs,cars,obstacles)
    imgs.remove((numbers[1],(w/2,h/2)))
    time.sleep(1)

def display_text(disp, text , w, h):
    font = pg.font.Font('freesansbold.ttf', 32)
    Text = font.render(text, True,(0, 0, 128))
    textRect = Text.get_rect()
    textRect.center = (w / 2, h / 2 + 125)
    disp.blit(Text, textRect)
