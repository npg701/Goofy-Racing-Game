import pygame as pg
import random
import time
def rotate_img(disp, img, top_left, angle):
    ''' Will rotate an image  about the centersent into the function and print it to the screen
    :param 
    disp: display window  
    img : image to rotate 
    top_left: corner of img
    angle
    :return: none, but print rotated img
    '''
    rotated_img = pg.transform.rotate(img,angle) #rotate aroung top left
    new_rec = rotated_img.get_rect(center = img.get_rect(topleft= top_left).center) #move so that it was about center
    disp.blit(rotated_img, new_rec.topleft)

def screen(disp, imgs, player_car=False, obstacles=False):
    ''' Will print everything to the screen
    :param 
    disp: display window  
    imgs : list of imgs to be shown 
    player car : list of cars to be shown
    onstacles: list of obstacles to be shown
    :return: none, but display all of the images
    '''
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
    '''' Will randomize a bunch of obstacles
    :param 
    obsnum: number of obstacles to be added
    obstacle_locations : list of possible locations on the track
    banana: banana object
    booster: booster object
    :return: list of obstacles in tuples wiht their locations
    '''
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
    ''' Will print everything to the screen
    :param 
    disp: display window  
    imgs : list of imgs to be shown 
    numbers: list of number imgs
    w: width of the window
    h : height of the window
    cars : list of cars to be shown
    onstacles: list of obstacles to be shown
    :return: none, but display all of the images along with a countdown in the middle to start the game.
    '''
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
    ''' Will print everything to the screen
    :param 
    disp: display window  
    text : text that needs to be shown
    w: width of the window
    h : height of the window
    :return: none, but display the text
    '''
    font = pg.font.Font('freesansbold.ttf', 32)
    Text = font.render(text, True,(0, 0, 128))
    textRect = Text.get_rect()
    textRect.center = (w / 2, h / 2 + 125)
    disp.blit(Text, textRect)