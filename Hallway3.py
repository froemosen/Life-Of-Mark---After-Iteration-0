import pygame as pg
import pygame.mixer
import time
import random as r
import Classes
from saveFile1 import *
import Variabler
import Tekst

x = 1920
y = 1080
fps = 60
#Er der for settings

if scene == 2 or scene == 1:
    smark = Classes.smark(1075, 715)
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
eatSound = pg.mixer.Sound("assets/lyd/eatSound.wav") #lyd når burger eller pizza spises
drinkSound = pg.mixer.Sound("assets/lyd/drinkSound.wav") #lyd når kaffe eller energidrik drikkes
failureToConsume = pg.mixer.Sound("assets/lyd/failureToEat.wav") #Lyd når der ikke er mere mad af den type man vil spise
#Alle backgorund og sprites skal sorteres
def start():
    tick = 0
    import Menu
    import Hallway2
    bgLocation = -3364
    inventory = Classes.inventory()
    broByggerCoolDown = 0
    bb1 = Classes.broBygger(650, bgLocation+2100)
    bb2 = Classes.broBygger(1100, bgLocation+2100)
    bb3 = Classes.broBygger(1100, bgLocation+3000)
    brobyggere = [bb1, bb2, bb3]
    jiji = Classes.jiji(1200, bgLocation+200)
    pg.mixer.music.set_volume(0.07)
    eatingAllowed = False
    def drawWorld():
        win.blit(bgScene3, (0, bgLocation))
        try:
            pizza1.draw(win)
        except:
            pass
        try:
            burger1.draw(win)
        except:
            pass
        try:
            kaffe1.draw(win)
        except:
            pass
        try:
            energidrik1.draw(win)
        except:
            pass
        for brobygger in brobyggere:
            brobygger.draw(win)
        jiji.draw(win)
        if smark.hitbool:
            smark.attack(win)
        else:
            smark.draw(win)
        if jijiTalk:
            allPlayerText.tekst(win)
            Tekst.jijitalk0()
        elif jijiTalk1:
            allPlayerText.tekst(win)
            Tekst.jijitalk1()
        elif jijiTalk2:
            allPlayerText.tekst(win)
            Tekst.jijitalk2()
        elif jijiTalk3:
            allPlayerText.tekst(win)
            Tekst.jijitalk3()
        elif jijiTalk4:
            allPlayerText.tekst(win)
            Tekst.jijitalk4()            
        #allPlayerText.tekst(win)
        inventory.draw(win)
        pg.display.update()
    run = True
    walking = False
    dialogStart = False #Bruge til at starte dialog()
    musicCooldown = r.randint(1, 800)
    timeToTalk = 0
    jijiTalk = False #Bruges så jiji kan snakke
    jijiTalk1 = False #Til jiji's anden dialog
    jijiTalk2 = False
    jijiTalk3 = False
    jijiTalk4 = False
    timerToTalk = 0
    while run:
        timerToTalk = 0
        walkAllowed_A = True
        walkAllowed_S = True
        walkAllowed_D = True
        walkAllowed_W = True
        dropchoice = r.randint(1, 4)
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
            Variabler.kaffe += 1

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

        if keys[pg.K_ESCAPE]:
            pg.mouse.set_visible(True)
            Menu.pygameMenuStart()

        if smark.x > 1150 and smark.x < 1255 and (bgLocation - smark.y) > -500:
            allPlayerText = Classes.allPlayerText(200, 740) #Grafikken kommer det placering for "textbox
            if timeToTalk < 100:
                jijiTalk = True
            elif timeToTalk > 100 and timeToTalk < 200:
                jijiTalk = False
                jijiTalk1 = True
            elif timerToTalk > 200 and timeToTalk < 300:
                jijiTalk1 = False
                jijiTalk2 = True
            elif timerToTalk > 300 and timeToTalk < 400:
                jijiTalk2 = False
                jijiTalk3 = True
            elif timerToTalk > 400 and timeToTalk < 500:
                jijiTalk3 = False
                jijiTalk4 = True
            else:
                walkAllowed_A = True
                walkAllowed_D = True
                walkAllowed_S = True
                walkAllowed_W = True
            timeToTalk += 1
        if keys[pg.K_l]:
            f = open("saveFile1.py", "w")
            f.write("import Classes" + "\n")
            f.write("import Variabler" + "\n")
            f.write("x = " + str(smark.x) + "\n")
            f.write("y = " + str(smark.y) + "\n")
            f.write("bgLocation = " + str(bgLocation) + "\n")
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

        if smark.x > 1020 and smark.x < 1260 and smark.y > 690 and smark.y < 730: #Sceneskift
            Hallway2.start()

        if smark.y < 295 and bgLocation < 0: #Rykker baggrund, for at smark ikke går ud af skærmen
            bgLocation += smark.vel
            for brobygger in brobyggere:
                brobygger.y += smark.vel
            smark.y = 295
            try:
                pizza1.y += smark.vel
            except:
                pass
            try:
                burger1.y += smark.vel
            except:
                pass
            try:
                kaffe1.y += smark.vel
            except:
                pass
            try:
                energidrik1.y += smark.vel
            except:
                pass
            jiji.y += smark.vel
        
        if smark.y > 300 and bgLocation > -3364: #Rykker baggrund, for at smark ikke går ud af skærmen
            bgLocation -= smark.vel
            for brobygger in brobyggere:
                brobygger.y -= smark.vel
            smark.y = 295
            try:
                pizza1.y -= smark.vel
            except:
                pass
            try:
                burger1.y -= smark.vel
            except:
                pass
            try:
                kaffe1.y -= smark.vel
            except:
                pass
            try:
                energidrik1.y -= smark.vel
            except:
                pass
            jiji.y -= smark.vel


        
        for brobygger in brobyggere:
            #BOT MOVEMENT, COLLISION OG ANGREB FOR SCENE
            distanceX = abs(brobygger.x-smark.x)
            distanceY = abs(brobygger.y-(smark.y+65))
            if distanceX < 400 and distanceY < 400:
                    if distanceX > distanceY:
                        if brobygger.x <= smark.x:
                            brobygger.x += brobygger.vel
                            brobygger.left = False
                            brobygger.right = True
                            brobygger.up = False
                            brobygger.down = False
                            brobygger.stand = False

                        elif brobygger.x > smark.x:
                            brobygger.x -= brobygger.vel
                            brobygger.left = True
                            brobygger.right = False
                            brobygger.up = False
                            brobygger.down = False
                            brobygger.stand = False

                    elif distanceX < distanceY:
                        if brobygger.y <= smark.y+50:
                            brobygger.y += brobygger.vel
                            brobygger.left = False
                            brobygger.right = False
                            brobygger.up = False
                            brobygger.down = True
                            brobygger.stand = False

                        elif brobygger.y > smark.y+50:
                            brobygger.y -= brobygger.vel
                            brobygger.left = False
                            brobygger.right = False
                            brobygger.up = True
                            brobygger.down = False
                            brobygger.stand = False
                    else:
                        brobygger.movement()
                    
                    if distanceX < 80 and distanceY < 80:
                        smark.attacked()
            
            else:
                if brobygger.x > 925 and brobygger.x < 1235 and bgLocation-brobygger.y < -2500 and bgLocation-brobygger.y > -3649 or brobygger.x > 505 and brobygger.x < 1225 and bgLocation-brobygger.y > -2539 and bgLocation-brobygger.y < -2000:
                    brobygger.movement()
                else: 
                    if brobygger.x > 1200:
                        brobygger.x -= 3
                        brobygger.y -= 1
                        brobygger.movementChoice = 2
                    elif brobygger.x < 1000:
                        brobygger.x += 3
                        brobygger.y += 1
                        brobygger.movementChoice = 1
                    elif bgLocation-brobygger.y > -3649:
                        brobygger.y -= 3
                        brobygger.x -= 1
                        brobygger.movementChoice = 4
                    elif bgLocation-brobygger.y < -2000:
                        brobygger.y += 3
                        brobygger.x += 1
                        brobygger.movementChoice = 3
            

            #Smark.attack:
            if smark.attackingRight and brobygger.x-smark.x > -10 and distanceX < 200 and distanceY < 80 and smark.generalAttack:
                brobygger.health -= 80
                brobygger.vel = 0
                brobygger.stand = True
                brobygger.left = False
                brobygger.right = False
                brobygger.up = False
                brobygger.down = False
                brobygger.movementChoice = 5
                broByggerCoolDown = tick
                pg.mixer.Channel(4).play(Hallway2.bbDamagedSound) #afspilning af lyd
            
            elif smark.attackingLeft and brobygger.x-smark.x < 10 and distanceX < 200 and distanceY < 80 and smark.generalAttack:
                brobygger.health -= 80
                brobygger.vel = 0
                brobygger.stand = True
                brobygger.left = False
                brobygger.right = False
                brobygger.up = False
                brobygger.down = False
                brobygger.movementChoice = 5
                broByggerCoolDown = tick
                pg.mixer.Channel(4).play(Hallway2.bbDamagedSound) #afspilning af lyd

            elif smark.attackingDown and brobygger.y-smark.y > -10 and distanceY < 200 and distanceX < 80 and smark.generalAttack:
                brobygger.health -= 80
                brobygger.vel = 0
                brobygger.stand = True
                brobygger.left = False
                brobygger.right = False
                brobygger.up = False
                brobygger.down = False
                brobygger.movementChoice = 5
                broByggerCoolDown = tick
                pg.mixer.Channel(4).play(Hallway2.bbDamagedSound) #afspilning af lyd
            
            elif smark.attackingUp and brobygger.y-smark.y < 10 and distanceY < 200 and distanceX < 80 and smark.generalAttack:
                brobygger.health -= 80
                brobygger.vel = 0
                brobygger.stand = True
                brobygger.left = False
                brobygger.right = False
                brobygger.up = False
                brobygger.down = False
                brobygger.movementChoice = 5
                broByggerCoolDown = tick
                pg.mixer.Channel(4).play(Hallway2.bbDamagedSound) #afspilning af lyd

            if brobygger.health < 0:
                if dropchoice == 1:
                    pizza1 = Classes.droppedItems(brobygger.x+15, brobygger.y+50, Classes.pizzaSprite)
                elif dropchoice == 2:
                    burger1 = Classes.droppedItems(brobygger.x, brobygger.y, Classes.burgerSprite)
                elif dropchoice == 3:
                    kaffe1 = Classes.droppedItems(brobygger.x, brobygger.y, Classes.kaffeSprite)
                elif dropchoice == 4:
                    energidrik1 = Classes.droppedItems(brobygger.x, brobygger.y, Classes.energidrikSprite)
                brobygger.x = -10000
                brobygger.health = 0

            if tick-broByggerCoolDown > 50 and brobygger.vel == 0:
                brobygger.vel = 5
            #collision og angreb slut

        #Tjek om Smark er tæt nok på mad til at samle det op.
        try:
            if abs(smark.x+45-pizza1.x) < 80 and abs(smark.y+80-pizza1.y) < 80:
                del(pizza1)
                pg.mixer.Channel(3).play(Hallway2.pizzaPickup, loops=0)
                Variabler.pizza += 1
        except:
            pass
        try:
            if abs(smark.x+45-burger1.x) < 80 and abs(smark.y+80-burger1.y) < 80:
                del(burger1)
                pg.mixer.Channel(3).play(Hallway2.pizzaPickup, loops=0)
                Variabler.burger += 1
        except:
            pass
        try:
            if abs(smark.x+45-kaffe1.x) < 80 and abs(smark.y+80-kaffe1.y) < 80:
                del(kaffe1)
                pg.mixer.Channel(3).play(Hallway2.pizzaPickup, loops=0)
                Variabler.kaffe += 1
        except:
            pass
        try:
            if abs(smark.x+45-energidrik1.x) < 80 and abs(smark.y+80-energidrik1.y) < 80:
                del(energidrik1)
                pg.mixer.Channel(3).play(Hallway2.pizzaPickup, loops=0)
                Variabler.energidrik += 1
        except:
            pass
        tick += 1

        #Tjek om mark er død
        if Variabler.health < 1:
            smark.x = 1075
            smark.y = 715
            Variabler.health = 1000
            Hallway2.respawn()

        #print(mx) #mouse x pos
        #print(my) #mouse y pos

        print("SmarkX", smark.x) #main sprite x pos
        print("SmarkY - bgLocation", bgLocation-smark.y) #main sprite y pos
        print(timeToTalk)
        #print("BaggrundY: ", bgLocation)
        drawWorld() #"Tegner" verden
        smark.hitbool = False
        smark.allow = True


    pg.quit()

def respawn():
    smark.y += 20
    start()
