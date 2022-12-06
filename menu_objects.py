import pygame as pg
from gameview import screen

class selector:
    def __init__(self, left,right, key_l, key_r):
        self.left = left 
        self.right = right
        self.key_left = key_l
        self.key_right = key_r
    def change(self, keys, idx):
        if keys[self.key_left]:
            idx-=1
        elif keys[self.key_right]:
            idx+=1
        if idx>self.right:
            idx=self.left
        if idx < self.left: 
            idx=self.right
        return idx
       
    
class button:
    def __init__(self, location, img):
        self.img = img
        self.locrec= location
        self.corner1 = (location[0],location[1])
        self.corner2= (location[0]+location[2], location[1]+location[3])

    def check_hover(self, mousepos, disp):
        if self.corner1[0] <= mousepos[0] <=  self.corner2[0] and self.corner1[1] <= mousepos[1] <= self.corner2[1]:
            disp.blit(self.img,(0,0))
            return False
        return True


    def check_clicked(self, ev, mousepos):
        if ev.type == pg.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the
            # button the game is terminated
            if self.corner1[0] <= mousepos[0] <=  self.corner2[0] and self.corner1[1] <= mousepos[1] <= self.corner2[1]:
                return True

        return False

