import pygame as pg
import pygame.mixer
import time
import random as r
import Classes

x = 1920
y = 1080
fps = 60
#Er der for settings

pg.init()
pg.font.init()

smark = Classes.smark(695, 650) #Mark x og y pos
allPlayerText = Classes.allPlayerText(100, 920) #allPlayerText x og y pos
bb = Classes.broBygger(100, 350)
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
        

        if walking == True:
                if pg.mixer.Channel(5).get_busy() == False:
                    pg.mixer.Channel(5).play(walkSound)
                else:
                    pass
        #if smark.y > 350 and smark.y < 250 and smark.x < 1210:
        if keys[pg.K_a] and smark.x > 40:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
            walking = True

        elif keys[pg.K_d] and smark.x < 1570:
            smark.x += smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = True
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_s] and smark.y < 700:
            smark.y += smark.vel
            smark.walkDown = True
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_w] and smark.y > -25:
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

        if smark.x > 1350 and smark.x < 1560 and smark.y > -35 and smark.y < -29:
            import Hallway3
            Hallway3.start()

        print(mx) #mouse x pos
        print(my) #mouse y pos

        print("SmarkX", smark.x) #main sprite x pos
        print("SmarkY", smark.y)#main sprite y pos
        bb.movement()
        drawWorld() #"Tegner" verden
    pg.quit()