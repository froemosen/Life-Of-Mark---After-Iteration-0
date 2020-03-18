import pygame as pg
import pygame.mixer
import time
import random as r
import Classes #Alle classes er inde i den fil

x = 1920
y = 1080
fps = 60
#Er der for settings
pg.init()
pg.font.init()
smark = Classes.smark(1450, 15) #Marks placering se i classes under smarks klassen
allPlayerText = Classes.allPlayerText(100, 920) #Grafikken kommer det placering for "textbox"
bg = pg.image.load("assets/maps/Classroom(1.0).png") #Loader baggrunden
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
clock = pg.time.Clock() 
table1 = pg.image.load("assets/maps/table1.png") #loader grafikken til bordene
walkSound = pg.mixer.Sound("assets/lyd/walksound.wav") #Loader lyd til når mark går

def script():
    tick = pg.time.get_ticks() / 1000
    print(tick)

def start():
    import Menu
    pg.mixer.music.set_volume(0.03)
    def drawWorld():
        win.blit(bg, (0,0))
        #Bord er 231 pixels langt
        win.blit(table1, (56,250))
        win.blit(table1, (287,250))
        win.blit(table1, (518,250))
        win.blit(table1, (749,250))
        win.blit(table1, (980,250))
        smark.draw(win)
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
        script()
        drawWorld() #"tegner" hele spillet
    pg.quit()

"""
        if smark.hitbox[0] + 77 < borde.hitbox[0] or smark.hitbox[0] > borde.hitbox[1] + borde.hitbox[2]:
                smark.vel = 10
            else:
                smark.vel = 0

        if smark.y< borde.y or smark.y > borde.y + borde.width:
            if smark.x + 77 < borde.x or smark.x > borde.x + borde.height:
                smark.vel = 10
        else:
            smark.vel = 0
"""

start()