import pygame as pg

def rotate_img(win, img, top_left, angle):
    rotated_img = pg.transform.rotate(img,angle)
    new_rec = rotated_img.get_rect(
        center = img.get_rect(topleft= top_left).center)
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
