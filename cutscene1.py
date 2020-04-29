import pygame as pg
import pygame.mixer
import time
import random as r
import Classes #Alle classes er inde i den fil
import Tekst
import Game

x = 1920
y = 1080
fps = 60
#Er der for settings
pg.init()
pg.font.init()
smark = Classes.smark(1450, 6) #Marks placering se i classes under smarks klassen
mads = Classes.Mads(758, 320) #Mads placering se i classes under Mads klassen
Lac = Classes.Lac(500, 320) #Lac placering se i classes under lac klassen
hod = Classes.hodyah(946, 315) #Hodyah placering se i classes under hodyah klassen
kris = Classes.kristian(1214, 315) #kristian placering se i classes under kristian klassen
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
        win.blit(table1, (56,500))
        win.blit(table1, (287,500))
        win.blit(table1, (518,500))
        win.blit(table1, (749,500))
        win.blit(table1, (980,500))

        if tick > 6 and tick < 8:
            allPlayerText.tekst(win)
            Tekst.TextMark()
        elif tick > 8 and tick < 12:
            allPlayerText.tekst(win)
            Tekst.TextMark1()
        elif tick > 12 and tick < 16:
            allPlayerText.tekst(win)
            Tekst.TextMark2()
        elif tick > 16 and tick < 20:
            allPlayerText.tekst(win)
            Tekst.TextElev()
        elif tick > 20 and tick < 23:
            allPlayerText.tekst(win)
            Tekst.TextElev1()
        elif tick > 23 and tick < 26:
            allPlayerText.tekst(win)
            Tekst.TextElev2()
        elif tick > 26 and tick < 28:
            allPlayerText.tekst(win)
            Tekst.TextElev3()
        elif tick > 42 and tick < 44:
            allPlayerText.tekst(win)
            Tekst.TextMark3()
        smark.draw(win)
        mads.movementMads(win)
        kris.draw(win)
        hod.draw(win)
        Lac.draw(win)
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
            #mark movement
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False

        if tick > 0 and tick < 3.3:
            #Mads movements
            mads.x -= mads.vel
            mads.down = False
            mads.up = False
            mads.right = False
            mads.left = True
            mads.stand = False

            #Lac movement
            Lac.x -= Lac.vel
            Lac.down = False
            Lac.up = False
            Lac.right = False
            Lac.left = True
            Lac.stand = False

            #hod movement
            hod.x -= hod.vel
            hod.down = False
            hod.up = False
            hod.right = False
            hod.left = True
            hod.stand = False

            #kris movement
            kris.x -= kris.vel
            kris.down = False
            kris.up = False
            kris.right = False
            kris.left = True
            kris.stand = False
        
        if tick > 3.5 and tick < 6:

            #hod movement
            hod.down = False
            hod.up = True
            hod.right = False
            hod.left = False
            hod.stand = True

            #kris movement
            kris.down = False
            kris.up = True
            kris.right = False
            kris.left = False
            kris.stand = True

            #Mads movements
            mads.down = False
            mads.up = True
            mads.right = False
            mads.left = False
            mads.stand = True

            #Lac movement
            Lac.down = False
            Lac.up = True
            Lac.right = False
            Lac.left = False
            Lac.stand = True


        if tick > 6 and tick < 28:
            #mark movement
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = True
        
        if tick > 28 and tick < 50:
            if tick > 28 and tick < 33:
                #Mads movements
                mads.x += mads.vel
                mads.down = False
                mads.up = False
                mads.right = True
                mads.left = False
                mads.stand = False
            elif tick > 33 and tick < 42:
                #Mads movements
                mads.y -= mads.vel
                mads.down = False
                mads.up = True
                mads.right = False
                mads.left = False
                mads.stand = False
            if tick > 28 and tick < 34:
                #Lac movement
                Lac.x += Lac.vel
                Lac.down = False
                Lac.up = False
                Lac.right = True
                Lac.left = False
                Lac.stand = False
            elif tick > 35 and tick < 40:
                #Lac movement
                Lac.y -= Lac.vel
                Lac.down = False
                Lac.up = True
                Lac.right = False
                Lac.left = False
                Lac.stand = False
            if tick > 28 and tick < 32:
                hod.x += hod.vel
                hod.down = False
                hod.up = False
                hod.right = False
                hod.left = True
                hod.stand = False
            elif tick > 32 and tick < 40:
                hod.y -= hod.vel
                hod.down = True
                hod.up = False
                hod.right = False
                hod.left = False
                hod.stand = False
            if tick > 28 and tick < 31:
                kris.x += kris.vel
                kris.down = False
                kris.up = False
                kris.right = True
                kris.left = False
                kris.stand = False
            elif tick > 31 and tick < 40:
                kris.y -= kris.vel
                kris.down = False
                kris.up = True
                kris.right = False
                kris.left = False
                kris.stand = False
        if tick > 50:
            Game.start()
        drawWorld() #"tegner" hele spillet
    pg.quit()
pygame.mouse.set_visible(False)
start()