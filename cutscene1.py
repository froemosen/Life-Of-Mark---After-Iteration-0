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
walkAllowed_A = True
walkAllowed_S = True
walkAllowed_D = True
walkAllowed_W = True
smark = Classes.smark(100, 600) #Marks placering se i classes under smarks klassen
allPlayerText = Classes.allPlayerText(100, 920) #Grafikken kommer det placering for "textbox"
bg = pg.image.load("assets/maps/Classroom(1.0).png") #Loader baggrunden
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
clock = pg.time.Clock() 
table1 = pg.image.load("assets/maps/table1.png") #loader grafikken til bordene
walkSound = pg.mixer.Sound("assets/lyd/walksound.wav") #Loader lyd til når mark går
pg.mixer.music.set_volume(0.03)

    def drawWorld():
        win.blit(bg, (0,0))
        #Bord er 231 pixels langt
        win.blit(table1, (56,250))
        win.blit(table1, (287,250))
        win.blit(table1, (518,250))
        win.blit(table1, (749,250))
        win.blit(table1, (980,250))
        borde.drawBorde()
        smark.draw(win)
        pg.display.update()

    run = True
    walking = False
    musicCooldown = r.randint(1, 800)
    borde = Classes.borde(152, 255, 1156, 115)
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

        #Sceneskift
        if smark.x > 1350 and smark.x < 1560 and smark.y > -35 and smark.y < -29:
            import Hallway2
            Hallway2.start()

        #print("mx", mx) #mouse x pos
        #print("my", my) #mouse y pos

        print("mark xpos", smark.x) #main sprite x pos
        print("mark ypos", smark.y) #main sprite y pos

        print("Table xpos: ", borde.x) #Table x pos
        print("Table ypos: ", borde.y) #Table y pos

        drawWorld() #"tegner" hele spillet
    pg.quit()
start()