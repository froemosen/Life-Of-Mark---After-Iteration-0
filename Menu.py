import Tekst
import pygame as pg
import time
x = 1920
y = 1080
clock = pg.time.Clock()
tick = pg.time.get_ticks()
bg = pg.image.load("Baggrund.png")
win = pg.display.set_mode((x,y), pg.FULLSCREEN)

def startSettings():
    run = True
    while run:
        points = Tekst.resTal
        tick = pg.time.get_ticks()
        win.blit(bg, (0,0))
        keys = pg.key.get_pressed()
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run = False
        
        if keys[pg.K_d] and Tekst.resTal >= 1:
            Tekst.resTal -= 1

        elif keys[pg.K_a] and Tekst.resTal <= 5:
            Tekst.resTal += 1

        if points == 1:
            Tekst.changeRes()

        elif points == 2:
            Tekst.changeRes1()

        elif points == 3:
            Tekst.changeRes2()
            
        elif points == 4:
            Tekst.changeRes3()

        elif points == 5:
            Tekst.changeRes4()

        elif keys[pg.K_ESCAPE]:
            pygameMenuStart()
        pg.display.update()

def pygameMenuStart():
    import Game
    pg.mouse.set_visible(False)
    pg.init()
    run = True
    point = 1
    while run:
        keys = pg.key.get_pressed()
        clock.tick(10)
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run = False
        win.blit(bg, (0,0))
        Tekst.menuTekst1()
        Tekst.menuTekst2()
        Tekst.menuTekst3()

        if keys[pg.K_w] and point >= 1:
            point -= 1

        if keys[pg.K_s] and point <= 3:

            point += 1

        if point == 1:
            Tekst.white1 = (255, 127, 80)
            Tekst.white2 = (255, 255, 255)
            Tekst.white3 = (255, 255, 255)
        elif point == 2:
            Tekst.white1 = (255, 255, 255)
            Tekst.white2 = (255, 127, 80)
            Tekst.white3 = (255, 255, 255)
        elif point == 3:
            Tekst.white1 = (255, 255, 255)
            Tekst.white2 = (255, 255, 255)
            Tekst.white3 = (255, 127, 80)

        if keys[pg.K_SPACE] and point == 1:
            Game.start()
        elif keys[pg.K_SPACE] and point == 2:
            startSettings()
        elif keys[pg.K_SPACE] and point == 3:
            run = False
            pg.quit()

        pg.display.update()
pygameMenuStart()

#HEJ MED DIG