import Classes #Alle classes er inde i den fil
from saveFile1 import *
import pygame as pg
import pygame.mixer
import time
import random as r

x = 1920
y = 1080
fps = 60
#Er der for settings
pg.init()
pg.font.init()
smark = Classes.smark(smark.x, smark.y) #Marks placering se i classes under smarks klassen
allPlayerText = Classes.allPlayerText(100, 920) #Grafikken kommer det placering for "textbox"
bg = pg.image.load("assets/maps/Classroom(1.0).png") #Loader baggrunden
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
clock = pg.time.Clock() 
table1 = pg.image.load("assets/maps/table1.png") #loader grafikken til bordene
walkSound = pg.mixer.Sound("assets/lyd/walksound.wav") #Loader lyd til når mark går
walkAllowed_A = True
walkAllowed_S = True
walkAllowed_D = True
walkAllowed_W = True

#Alle backgorund og sprites skal sorteres
 

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
        
        #Kollision til borde - start
        if smark.x < 1225:
            if smark.y > 15 and smark.y < 220:
                walkAllowed_A = False
            else:
                walkAllowed_A = True
        else:
            walkAllowed_A = True

        if smark.x < 1205:
            if smark.y > 5 and smark.y < 220:
                walkAllowed_S = False
            else:
                walkAllowed_S = True
        else: 
            walkAllowed_S = True

        if smark.x < 1215:
            if smark.y > 15 and smark.y < 230:
                walkAllowed_W = False
            else:
                walkAllowed_W = True
        else: 
            walkAllowed_W = True
        #Kollision til borde - slut

        if walking == True:
                if pg.mixer.Channel(5).get_busy() == False:
                    pg.mixer.Channel(5).play(walkSound)
                else:
                    pass
        #if smark.y > 350 and smark.y < 250 and smark.x < 1210:
        if keys[pg.K_a] and smark.x > 40 and walkAllowed_A == True: #and smark.x + 77 > borde.x + borde.height and smark.y + 65 > borde.y:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
            walking = True

        elif keys[pg.K_d] and smark.x < 1570 and walkAllowed_D == True:
            smark.x += smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = True
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_s] and smark.y < 700 and walkAllowed_S == True:
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
    
#start() # "#" kan fjernes under tests

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