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
if scene == 1:
    smark = Classes.smark(675, 699)
elif scene == 3:
    smark = Classes.smark(1350, -28)
else:
    smark = Classes.smark(smark.x, smark.y) #Mark x og y pos

scene = 2 #var som bruges som en slags ID til forskellige scener i spillet


pg.init()
pg.font.init()

allPlayerText = Classes.allPlayerText(100, 920) #allPlayerText x og y pos
bb = Classes.broBygger(800, 500)
pg.mixer.music.set_volume(0.03) #lydstyrke
bgScene = pg.image.load("assets/maps/Hallway2.png") #loader grafikken til Hallway2

win = pg.display.set_mode((x,y), pg.FULLSCREEN)
clock = pg.time.Clock()

walkSound = pg.mixer.Sound("assets/lyd/walksound.wav") #loader lyd til når mark går
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
    import Game
    walkAllowed_A = True
    walkAllowed_S = True
    walkAllowed_D = True
    walkAllowed_W = True

    def drawWorld():
        win.blit(bgScene, (0,0))
        smark.draw(win)
        bb.draw(win)
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
        
        #Kollision til mure - start
        
        if smark.x < 305:
            if smark.y > 489:
                walkAllowed_A = False
            else:
                walkAllowed_A = True    
        elif smark.x < 1055 and smark.x > 500:
            if smark.y < 195:
                walkAllowed_A = False
            else:
                walkAllowed_A = True
        else:
            walkAllowed_A = True
        
        if smark.x < 295:
            if smark.y > 480:
                walkAllowed_S = False
            else: 
                walkAllowed_S = True  
        else: 
            walkAllowed_S = True

        if smark.x < 1045 and smark.x > 345:
            if smark.y < 200: 
                walkAllowed_W = False
            else:
                walkAllowed_W = True
        elif smark.x < 345:
            if smark.y < 100:
                walkAllowed_W = False
            else:
                walkAllowed_W = True
        else: 
            walkAllowed_W = True

        if smark.x > 345 and smark.x < 900:
            if smark.y < 180:
                walkAllowed_D = False
            else:
                walkAllowed_D = True
        else:
            walkAllowed_D = True
        #Kollision til mure - slut

        if walking == True:
                if pg.mixer.Channel(5).get_busy() == False:
                    pg.mixer.Channel(5).play(walkSound)
                else:
                    pass
        #if smark.y > 350 and smark.y < 250 and smark.x < 1210:
        if keys[pg.K_a] and smark.x > 40 and walkAllowed_A:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
            walking = True

        elif keys[pg.K_d] and smark.x < 1570 and walkAllowed_D:
            smark.x += smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = True
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_s] and smark.y < 670 and walkAllowed_S:
            smark.y += smark.vel
            smark.walkDown = True
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_w] and smark.y > -25 and walkAllowed_W:
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

        if keys[pg.K_ESCAPE]:
            Menu.pygameMenuStart()

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

        if smark.x > 575 and smark.x < 775 and smark.y > 670 and smark.y < 700:
            Game.start()

        if smark.x > 1350 and smark.x < 1560 and smark.y > -35 and smark.y <= -28:
            import Hallway3
            Hallway3.start()

        print(mx) #mouse x pos
        print(my) #mouse y pos
        print(bb.movementAllowed)
        print("SmarkX", smark.x) #main sprite x pos
        print("SmarkY", smark.y)#main sprite y pos
        if bb.x > 100 and bb.x < 1700 and bb.y > 10 and bb.y < 800:
            bb.movement()
        else: 
            if bb.x > 1690:
                bb.x -= 6
            elif bb.x < 110:
                bb.x += 6
            elif bb.y > 790:
                bb.y -= 6
            elif bb.y < 20:
                bb.y += 6

        drawWorld() #"Tegner" verden
    pg.quit()