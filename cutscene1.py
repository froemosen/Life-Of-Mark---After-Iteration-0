import pygame as pg
import pygame.mixer
import time
import random as r
import Classes #Alle classes er inde i den fil
import Tekst

x = 1920
y = 1080
fps = 60
#Er der for settings
pg.init()
pg.font.init()
smark = Classes.smark(1450, 6) #Marks placering se i classes under smarks klassen
allPlayerText = Classes.allPlayerText(200, 740) #Grafikken kommer det placering for "textbox"
bg = pg.image.load("assets/maps/Classroom(1.0).png") #Loader baggrunden
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
clock = pg.time.Clock() 
table1 = pg.image.load("assets/maps/table1.png") #loader grafikken til bordene
walkSound = pg.mixer.Sound("assets/lyd/walksound.wav") #Loader lyd til når mark går

def start():
    import Menu
    pg.mixer.music.set_volume(0.03)
    def drawWorld():
        win.blit(bg, (0,0))
        #Bord er 231 pixels langt
        tick = pg.time.get_ticks() / 1000
        win.blit(table1, (56,250))
        win.blit(table1, (287,250))
        win.blit(table1, (518,250))
        win.blit(table1, (749,250))
        win.blit(table1, (980,250))
        smark.draw(win)
        if tick > 6 and tick < 1000:
            allPlayerText.tekst(win)
            Tekst.TextMark()
        pg.display.update()
    run = True
    walking = False
    musicCooldown = r.randint(1, 800)
    borde = Classes.borde(152, 255, 1156, 115)
    while run:
        keys = pg.key.get_pressed()
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                Menu.pygameMenuStart()

        if keys[pg.K_ESCAPE]:
            Menu.pygameMenuStart()
            
        tick = pg.time.get_ticks() / 1000
        print(tick)

        if tick > 0 and tick < 6:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
            walking = True
        if tick > 6 and tick < 1000:
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = True
            walking = True

        drawWorld() #"tegner" hele spillet
    pg.quit()
pygame.mouse.set_visible(False)
start()