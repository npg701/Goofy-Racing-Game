import pygame as pg
from gameview import rotate_img
import math
class Vehicle:
    
    def __init__(self, maxv, maxav, accel, img,ang_accel):
        self.img = img
        self.maxv = maxv #max velocity of vehicle
        self.maxangvel = maxav # angular velocity of vehicle
        self.v = 0
        self.av = 0
        self.angle = 0 #current angle and vel
        self.x, self.y = self.start_position
        self.accel = accel
        self.ang_accel= ang_accel
        self.spin = False
    
    def rotate(self,l=False, r=False):
        self.av += self.ang_accel
        if self.av >= self.maxangvel:
            self.av = self.maxangvel
        if self.spin:
            self.angle -= 8*self.maxangvel
            
        elif l:
            self.angle += self.av
        elif r:
            self.angle -= self.av
        

    def angreset(self):
        self.av = 0
    
    def print(self, disp):

        rotate_img(disp,self.img,(self.x,self.y), self.angle)
    
    def forward(self, boost = False):
        self.v += self.accel
        if boost:
            self.v = 3*self.maxv
        elif ((3/2)*self.maxv > self.v) and  (self.v> self.maxv):
            self.v = self.maxv
        self.move()
    
    def slow(self):
        if self.v>.2:
            self.v -= self.accel*(3/4)
        if self.v<-.2:
            self.v += self.accel*(3/4)
        if ((self.v<.2) and (self.v>-.2)):
            self.v = 0
        self.move()
    
    def reverse(self):
        self.v -= self.accel
        if self.v <= (-self.maxv*(3/4)):
            self.v = (-self.maxv*(3/4))
        self.move()


    def move(self):
        radians = math.radians(self.angle)
        self.x -= self.v*math.sin(radians)
        self.y -= self.v*math.cos(radians)

    def collision (self, mask ,pos= (0,0)):
        vehicleMask = pg.mask.from_surface(self.img)
        offset = (int(self.x - int(pos[0])), int(self.y - int(pos[1])))
        overlap = mask.overlap(vehicleMask,offset)
        return overlap

    def recoil(self):
        self.v = -self.v*(9/10)

class PlayerVehicle(Vehicle):
    
    def __init__(self, maxv, av, accel,ang_accel, img,player,p1start, p2start):
        if player ==1:
            self.start_position = p1start
        if player ==2:
            self.start_position = p2start
        super().__init__(maxv, av,accel, img,ang_accel)

    def control(self,keys,player):
        
        if player == 1:       
            if keys[pg.K_LEFT]:
                super().rotate(True)
            elif keys[pg.K_RIGHT]:
                super().rotate(False,True)
            elif not self.spin:
                super().angreset()

            if keys[pg.K_UP]:
                super().forward()
            elif keys[pg.K_DOWN]:
                super().reverse()
            else:
                super().slow()
        if player == 2:
            if keys[pg.K_a]:
                super().rotate(True)
            elif keys[pg.K_d]:
                super().rotate(False,True)
            elif not self.spin:
                super().angreset()

            if keys[pg.K_w]:
                super().forward()
            elif keys[pg.K_s]:
                super().reverse()
            else:
                super().slow()
        

class Opponent(Vehicle):
    def __init__(self, maxv, maxav, accel, img):
        super().__init__(maxv, maxav, accel, img)

class obstacle:
    def __init__(self,img) -> None:
        self.img = img 
    def insert(self,disp, loc):
        disp.blit(self.img, loc)
    def get_mask(self):
        return pg.mask.from_surface(self.img)



        
    ## position and mask
class banana(obstacle):
    def __init__(self, img) -> None:
        super().__init__(img)
        self.type = 'banana'
    def spin(self, vehicle):
        vehicle.spin = True
        vehicle.rotate()
    def insert(self, disp,loc):
        super().insert(disp,loc)
        
    
class booster(obstacle):
    def __init__(self, img) -> None:
        super().__init__(img)
        self.type= 'booster'
    def boost(self, vehicle):
        vehicle.v = vehicle.maxv * 3
        vehicle.forward(boost = True)
    def insert(self, disp,loc):
        super().insert(disp,loc)

class Track:
    def __init__(self, img, borderimg,finish_loc,obstacle_locations, p1_start_pos, p2_start_pos )-> None:
        self.img = img
        self.borderimg = borderimg
        self.border = pg.mask.from_surface(borderimg)
        self.finish_loc = finish_loc 
        self.obstacle_locations = obstacle_locations
        self.p1_start = p1_start_pos
        self.p2_start = p2_start_pos