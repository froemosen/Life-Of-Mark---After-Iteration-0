import pygame as pg
import pygame.mixer
import time
import random as r
import Classes
from saveFile1 import *

x = 1920
y = 1080
fps = 60
#Er der for settings

if scene == 2:
    smark = Classes.smark(1040, 636)
else:
    smark = Classes.smark(smark.x, smark.y) #Marks x og y pos

scene = 3 #var som bruges som en slags ID til forskellige scener i spillet

pg.init()
pg.font.init()
allPlayerText = Classes.allPlayerText(100, 920) #allPlayerText x og y pos
pg.mixer.music.set_volume(0.03) #lydstyrke
bgScene3 = pg.image.load("assets/maps/Hallway3.png") #Loader grafikken til Hallway3
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
clock = pg.time.Clock()
walkSound = pg.mixer.Sound("assets/lyd/walksound.wav") #Loader lyd til når mark går
walkAllowed_A = True
walkAllowed_S = True
walkAllowed_D = True
walkAllowed_W = True
#Alle backgorund og sprites skal sorteres


"""
class borde(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, self.height, self.width)

    def drawBorde(self):
        pg.draw.rect(win, (0,255,0), self.hitbox, 2)
    """

def start():
    import Menu
    import Hallway2
    bgLocation = -3364
    def drawWorld():
        win.blit(bgScene3, (0,bgLocation))
        smark.draw(win)
        #allPlayerText.tekst(win)
        pg.display.update()

    run = True
    walking = False
    musicCooldown = r.randint(1, 800)
    while run:
        mx, my = pg.mouse.get_pos()
        keys = pg.key.get_pressed()
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                Menu.pygameMenuStart()
        
        #HVORDAN SKAL VI LAVE KOLLSION MED MURE I SIDEN????
         
        #Kollision til mure - start
        if smark.x < 825:
            if bgLocation > -3264 and bgLocation < -2134:
                walkAllowed_A = False
            else:
                walkAllowed_A = True
        else:
            walkAllowed_A = True

        if smark.x < 695:
            if bgLocation > -2255 and bgLocation < -2130:
                walkAllowed_S = False
            else:
                walkAllowed_S = True
        else: 
            walkAllowed_S = True

        if smark.x < 695:
            if bgLocation > -3265 and bgLocation < -3200:
                walkAllowed_W = False
            else:
                walkAllowed_W = True
        else: 
            walkAllowed_W = True
        #Kollision til mure - slut

        if walking == True:
                if pg.mixer.Channel(5).get_busy() == False:
                    pg.mixer.Channel(5).play(walkSound)
                else:
                    pass
        #if smark.y > 350 and smark.y < 250 and smark.x < 1210:
        if keys[pg.K_a] and smark.x > 405 and walkAllowed_A == True:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
            walking = True

        elif keys[pg.K_d] and smark.x < 1195 and walkAllowed_D == True:
            smark.x += smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = True
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_s] and smark.y < 650 and walkAllowed_S == True:
            smark.y += smark.vel
            smark.walkDown = True
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_w] and smark.y > -25 and walkAllowed_W == True:
            smark.y -= smark.vel
            smark.walkDown = False
            smark.walkUp = True
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
            walking = True

        else:
            smark.stand = True
            smark.walkCount = 0
            walking = False


        if keys[pg.K_ESCAPE]:
            Menu.pygameMenuStart()

        if keys[pg.K_l]:
            f = open("saveFile1.py", "w")
            f.write("import Classes" + "\n")
            f.write("x = " + str(smark.x) + "\n")
            f.write("y = " + str(smark.y) + "\n")
            f.write("smark = Classes.smark(x, y)" + "\n")            
            f.write("smark.walkDown = " + str(smark.walkDown) + "\n")
            f.write("smark.walkUp = " + str(smark.walkUp) + "\n")
            f.write("smark.walkRigth = " + str(smark.walkRight) + "\n")
            f.write("smark.walkLeft = " + str(smark.walkLeft) + "\n")
            f.write("smark.stand = " + str(smark.stand) + "\n")
            f.write("walking = " + str(walking) + "\n")
            f.write("scene = " + str(scene) + "\n")
            f.close()

        if pg.mixer.music.get_busy() == True:
            pass
        else:
            if musicCooldown == 1000:
                sangValg = (r.choice(Classes.sangeListe.sange))
                pg.mixer.music.load(sangValg)
                pg.mixer.music.play(0)
                musicCooldown = r.randint(1, 700)
            else:
                musicCooldown = musicCooldown +1

        if smark.x > 955 and smark.x < 1155 and smark.y > 640 and smark.y < 670:
            Hallway2.start()

        if smark.y < 295 and bgLocation < 0:
            bgLocation += smark.vel
            smark.y = 295
        
        if smark.y > 300 and bgLocation > -3364:
            bgLocation -= smark.vel
            smark.y = 295

        print(mx) #mouse x pos
        print(my) #mouse y pos

        print("SmarkX", smark.x) #main sprite x pos
        print("SmarkY", smark.y) #main sprite y pos

        print("BaggrundY: ", bgLocation)

        drawWorld() #"Tegner" verden
    pg.quit()
