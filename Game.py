import Classes #Alle classes er inde i den fil
import pygame as pg
import pygame.mixer
import time
import random as r
import Hallway2
from saveFile1 import *
import Variabler

if scene >= 2:
    smark = Classes.smark(1400, -27)
else:
    smark = Classes.smark(smark.x, smark.y) #Marks placering se i classes under smarks klassen
scene = 1 #var som bruges som en slags ID til forskellige scener i spillet
x = 1920
y = 1080
fps = 60
#Er der for settings
pg.init()
pg.font.init()
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


eatSound = pg.mixer.Sound("assets/lyd/eatSound.wav") #lyd når burger eller pizza spises
drinkSound = pg.mixer.Sound("assets/lyd/drinkSound.wav") #lyd når kaffe eller energidrik drikkes
failureToConsume = pg.mixer.Sound("assets/lyd/failureToEat.wav") #Lyd når der ikke er mere mad af den type man vil spise
#Alle backgorund og sprites skal sorteres

def start():
    import Menu
    pg.mixer.music.set_volume(0.07)
    inventory = Classes.inventory()
    eatingAllowed = False
    def drawWorld():
        win.blit(bg, (0,0))
        #Bord er 231 pixels langt
        win.blit(table1, (56,250))
        win.blit(table1, (287,250))
        win.blit(table1, (518,250))
        win.blit(table1, (749,250))
        win.blit(table1, (980,250))
        if smark.hitbool:
            smark.attack(win)
        else:
            smark.draw(win)
        inventory.draw(win)
        pg.display.update()

    run = True
    walking = False
    musicCooldown = r.randint(1, 800)
    x1 = 0
    while run:
        mx, my = pg.mouse.get_pos()
        keys = pg.key.get_pressed()
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                Menu.pygameMenuStart()
        
        #Kollision til borde - start
        if smark.x < 1280:
            if smark.y > 55 and smark.y < 240:
                walkAllowed_A = False
            else:
                walkAllowed_A = True
        else:
            walkAllowed_A = True

        if smark.x < 1260:
            if smark.y > 45 and smark.y < 240:
                walkAllowed_S = False
            else:
                walkAllowed_S = True
        else: 
            walkAllowed_S = True

        if smark.x < 1260:
            if smark.y > 55 and smark.y < 250:
                walkAllowed_W = False
            else:
                walkAllowed_W = True
        else: 
            walkAllowed_W = True
        #Kollision til borde - slut

        if walking:
                if pg.mixer.Channel(5).get_busy() == False:
                    pg.mixer.Channel(5).play(walkSound)
                else:
                    pass
        #if smark.y > 350 and smark.y < 250 and smark.x < 1210:
        if keys[pg.K_a] and smark.x > 130 and walkAllowed_A == True: #and smark.x + 77 > borde.x + borde.height and smark.y + 65 > borde.y:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
            walking = True

        elif keys[pg.K_d] and smark.x < 1660 and walkAllowed_D == True:
            smark.x += smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = True
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_s] and smark.y < 750 and walkAllowed_S == True:
            smark.y += smark.vel
            smark.walkDown = True
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_w] and smark.y > -0 and walkAllowed_W == True:
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


        elif keys[pg.K_1]:
            if eatingAllowed:    
                eatingAllowed = False
                if Variabler.pizza > 0:
                        Variabler.pizza -= 1
                        Variabler.health += 100
                        pg.mixer.Channel(2).play(eatSound)
                        if Variabler.health > 1000:
                            Variabler.health = 1000
                        else: pass
                else: 
                    pg.mixer.Channel(2).play(failureToConsume)
            else: pass

        elif keys[pg.K_2]:
            if eatingAllowed:
                eatingAllowed = False
                if Variabler.burger > 0:
                    Variabler.burger -= 1
                    Variabler.health += 300
                    pg.mixer.Channel(2).play(eatSound)
                    if Variabler.health > 1000:
                        Variabler.health = 1000
                    else: pass
                else: 
                    pg.mixer.Channel(2).play(failureToConsume)
            else: pass
            
        elif keys[pg.K_3]:
            if eatingAllowed:
                eatingAllowed = False
                if Variabler.kaffe > 0:
                    Variabler.kaffe -= 1
                    Variabler.health += 200
                    pg.mixer.Channel(2).play(drinkSound)
                    if Variabler.health > 1000:
                        Variabler.health = 1000
                    else: pass
                else: 
                    pg.mixer.Channel(2).play(failureToConsume)
            else: pass

        elif keys[pg.K_4]:
            if eatingAllowed:
                eatingAllowed = False
                if Variabler.energidrik > 0:
                    Variabler.energidrik -= 1
                    Variabler.health += 1000
                    pg.mixer.Channel(2).play(drinkSound)
                    if Variabler.health > 1000:
                        Variabler.health = 1000
                    else: pass
                else: 
                    pg.mixer.Channel(2).play(failureToConsume)
            else: pass

        else:
            smark.stand = True
            smark.walkCount = 0
            walking = False
            eatingAllowed = True


        #Sceneskift
        if smark.x > 1400 and smark.x < 1620 and smark.y > -15 and smark.y <= 0:
            Hallway2.start()

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
            f.write("Variabler.pizza = " + str(Variabler.pizza) + "\n")
            f.write("Variabler.burger = " + str(Variabler.burger) + "\n")
            f.write("Variabler.kaffe = " + str(Variabler.kaffe) + "\n")
            f.write("Variabler.energidrik = " + str(Variabler.energidrik) + "\n")
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
        #print("mx", mx) #mouse x pos
        #print("my", my) #mouse y pos

        #print("mark xpos", smark.x) #main sprite x pos
        #print("mark ypos", smark.y) #main sprite y pos

        #print("Table xpos: ", borde.x) #Table x pos
        #print("Table ypos: ", borde.y) #Table y pos
        drawWorld() #"tegner" hele spillet
        print("smarkX:",smark.x)
        print("smarky:",smark.y)
        smark.hitbool = False
        smark.allow = True
    pg.quit()
    
#start() # "#" kan fjernes under tests


def respawn():
    smark.y += 20
    start()