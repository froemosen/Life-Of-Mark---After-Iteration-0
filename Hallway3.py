import pygame as pg
import pygame.mixer
import time
import random as r
import Classes
from saveFile1 import *
import Variabler

x = 1920
y = 1080
fps = 60
#Er der for settings

if scene == 2 or scene == 1:
    smark = Classes.smark(1075, 725)
    smark.walkUp = True
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

def start():
    import Menu
    import Hallway2
    bgLocation = -3364
    inventory = Classes.inventory()
    pg.mixer.music.set_volume(0.07)
    eatingAllowed = False
    def drawWorld():
        win.blit(bgScene3, (0,bgLocation))
        if smark.hitbool:
            smark.attack(win)
        else:
            smark.draw(win)
        #allPlayerText.tekst(win)
        inventory.draw(win)
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
        if smark.x < 890:
            if bgLocation > -3290 and bgLocation < -2190: #mur1
                walkAllowed_A = False
            elif bgLocation > -1540 and bgLocation < -970: #mur2
                walkAllowed_A = False
            elif bgLocation > -685 and bgLocation < -90: #mur3
                walkAllowed_A = False
            elif smark.x < 790 and bgLocation > -84: #murSlut
                walkAllowed_A = False
            else:
                walkAllowed_A = True
            
        else:
            walkAllowed_A = True

        if smark.x < 870:
            if bgLocation > -2255 and bgLocation < -2184: #mur1
                walkAllowed_S = False
            elif bgLocation > -1100 and bgLocation < -964: #mur2
                walkAllowed_S = False
            elif bgLocation > -120 and bgLocation < -84: #mur3    
                walkAllowed_S = False
            else:
                walkAllowed_S = True
        else: 
            walkAllowed_S = True

        if smark.x < 870:
            if bgLocation > -3295 and bgLocation < -3200: #mur1
                walkAllowed_W = False
            elif bgLocation > -1545 and bgLocation < -1450: #mur2
                walkAllowed_W = False
            elif bgLocation > -725 and bgLocation < -680: #mur3
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
        if keys[pg.K_a] and smark.x > 510 and walkAllowed_A == True:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
            walking = True

        elif keys[pg.K_d] and smark.x < 1280 and walkAllowed_D == True:
            smark.x += smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = True
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_s] and smark.y < 695 and walkAllowed_S == True:
            smark.y += smark.vel
            smark.walkDown = True
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_w] and smark.y > 35 and walkAllowed_W == True:
            smark.y -= smark.vel
            smark.walkDown = False
            smark.walkUp = True
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_SPACE] and smark.allow:
                smark.hitbool = True
                smark.allow = False

        elif keys[pg.K_p]:
            Variabler.pizza += 1

        elif keys[pg.K_e] and Variabler.pizza >= 1:
            Variabler.pizza -= 1
            Variabler.health += 100
            if Variabler.health > 1000:
                Variabler.health = 1000

        elif keys[pg.K_1]:
            if eatingAllowed:    
                eatingAllowed = False
                if Variabler.pizza > 0:
                        Variabler.pizza -= 1
                        Variabler.health += 100
                        if Variabler.health > 1000:
                            Variabler.health = 1000
                        else: pass
                else: pass
            else: pass

        elif keys[pg.K_2]:
            if eatingAllowed:
                eatingAllowed = False
                if Variabler.burger > 0:
                    Variabler.burger -= 1
                    Variabler.health += 300
                    if Variabler.health > 1000:
                        Variabler.health = 1000
                    else: pass
                else: pass
            else: pass
            
        elif keys[pg.K_3] and eatingAllowed:
            if eatingAllowed:
                eatingAllowed = False
                if Variabler.kaffe > 0:
                    Variabler.kaffe -= 1
                    Variabler.health += 300
                    if Variabler.health > 1000:
                        Variabler.health = 1000
                    else: pass
                else: pass
            else: pass

        elif keys[pg.K_4] and eatingAllowed:
            if eatingAllowed:
                eatingAllowed = False
                if Variabler.energidrik > 0:
                    Variabler.energidrik -= 1
                    Variabler.health += 1000
                    if Variabler.health > 1000:
                        Variabler.health = 1000
                    else: pass
                else: pass
            else: pass

        else:
            smark.stand = True
            smark.walkCount = 0
            walking = False
            eatingAllowed = True

        if keys[pg.K_ESCAPE]:
            pg.mouse.set_visible(True)
            Menu.pygameMenuStart()

    

        if keys[pg.K_l]:
            f = open("saveFile1.py", "w")
            f.write("import Classes" + "\n")
            f.write("import Variabler" + "\n")
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
            f.write("Variabler.health = " + str(Variabler.health) + "\n")
            #inventory
            f.write("pizza = " + str(Variabler.pizza) + "\n")
            f.write("burger = " + str(Variabler.burger) + "\n")
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

        if smark.x > 1020 and smark.x < 1260 and smark.y > 690 and smark.y < 730: #Sceneskift
            Hallway2.start()

        if smark.y < 295 and bgLocation < 0: #Stopper baggrund fra at rykke sig i enden
            bgLocation += smark.vel
            smark.y = 295
        
        if smark.y > 300 and bgLocation > -3364: #Stopper baggrund fra at rykke sig i enden
            bgLocation -= smark.vel
            smark.y = 295

        print(mx) #mouse x pos
        print(my) #mouse y pos

        print("SmarkX", smark.x) #main sprite x pos
        print("SmarkY", smark.y) #main sprite y pos

        print("BaggrundY: ", bgLocation)
        drawWorld() #"Tegner" verden
        smark.hitbool = False
        smark.allow = True
    pg.quit()
