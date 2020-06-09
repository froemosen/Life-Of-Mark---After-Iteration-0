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
if scene == 1:
    smark = Classes.smark(725, 650)
    smark.walkUp = True
    smark.walkDown = False
elif scene == 3:
    smark = Classes.smark(1350, -28)
else:
    smark = Classes.smark(725, 650) #Mark x og y pos

scene = 2 #var som bruges som en slags ID til forskellige scener i spillet


pg.init()
pg.font.init()

allPlayerText = Classes.allPlayerText(100, 920) #allPlayerText x og y pos
bb0 = Classes.broBygger(1500, 400)
pg.mixer.music.set_volume(0.03) #lydstyrke
bgScene = pg.image.load("assets/maps/Hallway2.png") #loader grafikken til Hallway2
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
clock = pg.time.Clock()
inventory = Classes.inventory()

walkSound = pg.mixer.Sound("assets/lyd/walksound.wav") #loader lyd til når mark går
#Alle backgorund og sprites skal sorteres
bbDamagedSound = pg.mixer.Sound("assets/lyd/BroByggerDamaged.wav") #lyd som afspilles når bb tager skade
pizzaPickup = pg.mixer.Sound("assets/lyd/PizzaPickup.wav") #lyd som afspilles når pizza tages op
eatSound = pg.mixer.Sound("assets/lyd/eatSound.wav") #lyd når burger eller pizza spises
drinkSound = pg.mixer.Sound("assets/lyd/drinkSound.wav") #lyd når kaffe eller energidrik drikkes
failureToConsume = pg.mixer.Sound("assets/lyd/failureToEat.wav") #Lyd når der ikke er mere mad af den type man vil spise
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
    walkAllowed_A = True
    walkAllowed_S = True
    walkAllowed_D = True
    walkAllowed_W = True
    eatingAllowed = False
    tick = 0
    broByggerCoolDown = 0
    pg.mixer.music.set_volume(0.07)

    def drawWorld():
        win.blit(bgScene, (0,0))
        try:
            pizza1.draw(win)
        except:
            pass
        if smark.hitbool:
            smark.attack(win)
        else:
            smark.draw(win)
        bb0.draw(win)
        inventory.draw(win)
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
        
        #Kollision til mure - start
        
        if smark.x < 385:
            if smark.y > 530:
                walkAllowed_A = False
            else:
                walkAllowed_A = True    
        elif smark.x < 1125 and smark.x > 515:
            if smark.y < 300:
                walkAllowed_A = False
            else:
                walkAllowed_A = True
        else:
            walkAllowed_A = True
        
        if smark.x < 370:
            if smark.y > 540:
                walkAllowed_S = False
            else: 
                walkAllowed_S = True  
        else: 
            walkAllowed_S = True

        if smark.x < 1120 and smark.x > 430:
            if smark.y < 245: 
                walkAllowed_W = False
            else:
                walkAllowed_W = True
        elif smark.x < 430:
            if smark.y < 120:
                walkAllowed_W = False
            else:
                walkAllowed_W = True
        else: 
            walkAllowed_W = True

        if smark.x > 415 and smark.x < 900:
            if smark.y < 230:
                walkAllowed_D = False
            else:
                walkAllowed_D = True
        else:
            walkAllowed_D = True
        #Kollision til mure - slut

        if walking == True:
                if pg.mixer.Channel(5).get_busy() == False:
                    pg.mixer.Channel(5).play(walkSound)
                else:
                    pass
        #if smark.y > 350 and smark.y < 250 and smark.x < 1210:
        if keys[pg.K_a] and smark.x > 150 and walkAllowed_A:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
            walking = True

        elif keys[pg.K_d] and smark.x < 1615 and walkAllowed_D:
            smark.x += smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = True
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_s] and smark.y < 720 and walkAllowed_S:
            smark.y += smark.vel
            smark.walkDown = True
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
            walking = True

        elif keys[pg.K_w] and smark.y > 0 and walkAllowed_W:
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

        #Bruges til test af inventory
        elif keys[pg.K_p]:
            Variabler.energidrik += 1

        #Spisning (1,2,3,4) - giver flere liv
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
            smark.hitCount = 0
            eatingAllowed = True


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

        if keys[pg.K_ESCAPE]:
            pg.mouse.set_visible(True)
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

        if smark.x > 665 and smark.x < 865 and smark.y > 715 and smark.y < 780:
            Game.start()

        if smark.x > 1425 and smark.x < 1635 and smark.y > -15 and smark.y <= 8:
            import Hallway3
            Hallway3.start()

        #BOT MOVEMENT, COLLISION OG ANGREB FOR SCENE
        distanceX = abs(bb0.x-smark.x)
        distanceY = abs(bb0.y-(smark.y+65))
        if distanceX < 400 and distanceY < 400:
                if distanceX > distanceY:
                    if bb0.x <= smark.x:
                        bb0.x += bb0.vel
                        bb0.left = False
                        bb0.right = True
                        bb0.up = False
                        bb0.down = False
                        bb0.stand = False

                    elif bb0.x > smark.x:
                        bb0.x -= bb0.vel
                        bb0.left = True
                        bb0.right = False
                        bb0.up = False
                        bb0.down = False
                        bb0.stand = False

                elif distanceX < distanceY:
                    if bb0.y <= smark.y+50:
                        bb0.y += bb0.vel
                        bb0.left = False
                        bb0.right = False
                        bb0.up = False
                        bb0.down = True
                        bb0.stand = False

                    elif bb0.y > smark.y+50:
                        bb0.y -= bb0.vel
                        bb0.left = False
                        bb0.right = False
                        bb0.up = True
                        bb0.down = False
                        bb0.stand = False
                else:
                    bb0.movement()
                
                if distanceX < 80 and distanceY < 80:
                    smark.attacked()
        else:
            if bb0.x > 1165 and bb0.x < 1615 and bb0.y > 100 and bb0.y < 780 or bb0.x > 415 and bb0.x < 1166 and bb0.y > 360 and bb0.y <  780:
                bb0.movement()
            else: 
                if bb0.x > 1614:
                    bb0.x -= 3
                    bb0.y -= 1
                    bb0.movementChoice = 2
                elif bb0.x < 416:
                    bb0.x += 3
                    bb0.y += 1
                    bb0.movementChoice = 1
                elif bb0.y > 779:
                    bb0.y -= 3
                    bb0.x -= 1
                    bb0.movementChoice = 4
                elif bb0.y < 101 or bb0.y < 380 and bb0.x < 1180:
                    bb0.y += 3
                    bb0.x += 1
                    bb0.movementChoice = 3


        #Smark.attack:
        if smark.attackingRight and bb0.x-smark.x > -10 and distanceX < 200 and distanceY < 80 and smark.generalAttack:
            bb0.health -= 80
            bb0.vel = 0
            bb0.stand = True
            bb0.left = False
            bb0.right = False
            bb0.up = False
            bb0.down = False
            bb0.movementChoice = 5
            broByggerCoolDown = tick
            pg.mixer.Channel(4).play(bbDamagedSound) #afspilning af lyd
        
        elif smark.attackingLeft and bb0.x-smark.x < 10 and distanceX < 200 and distanceY < 80 and smark.generalAttack:
            bb0.health -= 80
            bb0.vel = 0
            bb0.stand = True
            bb0.left = False
            bb0.right = False
            bb0.up = False
            bb0.down = False
            bb0.movementChoice = 5
            broByggerCoolDown = tick
            pg.mixer.Channel(4).play(bbDamagedSound) #afspilning af lyd

        elif smark.attackingDown and bb0.y-smark.y > -10 and distanceY < 200 and distanceX < 80 and smark.generalAttack:
            bb0.health -= 80
            bb0.vel = 0
            bb0.stand = True
            bb0.left = False
            bb0.right = False
            bb0.up = False
            bb0.down = False
            bb0.movementChoice = 5
            broByggerCoolDown = tick
            pg.mixer.Channel(4).play(bbDamagedSound) #afspilning af lyd
        
        elif smark.attackingUp and bb0.y-smark.y < 10 and distanceY < 200 and distanceX < 80 and smark.generalAttack:
            bb0.health -= 80
            bb0.vel = 0
            bb0.stand = True
            bb0.left = False
            bb0.right = False
            bb0.up = False
            bb0.down = False
            bb0.movementChoice = 5
            broByggerCoolDown = tick
            pg.mixer.Channel(4).play(bbDamagedSound) #afspilning af lyd

        if bb0.health < 0:
            pizza1 = Classes.droppedItems(bb0.x+15, bb0.y+50, Classes.pizzaSprite)
            bb0.x = -10000
            bb0.health = 0

        if tick-broByggerCoolDown > 50 and bb0.vel == 0:
            bb0.vel = 5

        #Tjek om Smark er tæt nok på pizza til at samle den op.
        try:
            if abs(smark.x+45-pizza1.x) < 80 and abs(smark.y+80-pizza1.y) < 80:
                del(pizza1)
                pg.mixer.Channel(3).play(pizzaPickup, loops=0)
                Variabler.pizza += 1
        except:
            pass
            
        #Tjek om mark er død
        if Variabler.health < 1:
            smark.x = 790
            smark.y = 650
            Variabler.health = 1000
            Game.respawn()

        tick += 1
        #print(mx) #mouse x pos
        #print(my) #mouse y pos
        #print(bb.movementAllowed)
        #print("SmarkX", smark.x) #main sprite x pos
        #print("SmarkY", smark.y)#main sprite y pos
        #print("DistanceX:", distanceX)
        #print("DistanceY:", distanceY)
        #print("Health:", Variabler.health)
        #print("BB.heatlh:", bb0.health)
        drawWorld() #"Tegner" verden
        smark.hitbool = False
        smark.allow = True
    pg.quit()


def respawn():
    smark.y += 20
    start()