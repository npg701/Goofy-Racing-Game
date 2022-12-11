import pygame as pg

class selector:
    '''
    Attributes
    ----------
    left: left boundary
    right: right boundary
    key_l:left selection key
    key_right: right selection key

    Methods
    -------
    change(keys,idx):
        change the index sent in based on teh keys pressed and return it
    '''
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
    '''
    Attributes
    ----------
    location list four values: top left x, top left y, bottom right x, bottom right y
    img: image of self

    Methods
    -------
    check_hover(mousepos, disp):
        checks if mouse is hovering over the button
    check clicked(event, mousepos):
        checks if the mouse was clicked on the button
    '''
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