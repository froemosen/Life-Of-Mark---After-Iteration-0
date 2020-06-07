import pygame as pg
import random as r
import Variabler
x = 1920
y = 1080
pg.mixer.init()
win = pg.display.set_mode((x,y), pg.FULLSCREEN)

#MARK ANIME
markStandLeft = pg.image.load("assets/sprites/mark/gåVenstre1.png")
markStandRight = pg.image.load("assets/sprites/mark/gåHøjre1.png")
markStandUp = pg.image.load("assets/sprites/mark/gåOp3.png")
markStandDown = pg.image.load("assets/sprites/mark/gåNed1.png")
markStand = pg.image.load("assets/sprites/mark/gåNed1.png")
markWalkUp = [pg.image.load("assets/sprites/mark/gåOp3.png"), pg.image.load("assets/sprites/mark/gåOp2.png"), pg.image.load("assets/sprites/mark/gåOp3.png"), pg.image.load("assets/sprites/mark/gåOp4.png"), pg.image.load("assets/sprites/mark/gåOp3.png"), pg.image.load("assets/sprites/mark/gåOp2.png"), pg.image.load("assets/sprites/mark/gåOp3.png"), pg.image.load("assets/sprites/mark/gåOp4.png"), pg.image.load("assets/sprites/mark/gåOp3.png"), pg.image.load("assets/sprites/mark/gåOp2.png"), pg.image.load("assets/sprites/mark/gåOp3.png"), pg.image.load("assets/sprites/mark/gåOp4.png")]
markWalkLeft = [pg.image.load("assets/sprites/mark/gåVenstre1.png"), pg.image.load("assets/sprites/mark/gåVenstre2.png"), pg.image.load("assets/sprites/mark/gåVenstre3.png"), pg.image.load("assets/sprites/mark/gåVenstre4.png"), pg.image.load("assets/sprites/mark/gåVenstre1.png"), pg.image.load("assets/sprites/mark/gåVenstre2.png"), pg.image.load("assets/sprites/mark/gåVenstre3.png"), pg.image.load("assets/sprites/mark/gåVenstre4.png"), pg.image.load("assets/sprites/mark/gåVenstre1.png"), pg.image.load("assets/sprites/mark/gåVenstre2.png"), pg.image.load("assets/sprites/mark/gåVenstre3.png"), pg.image.load("assets/sprites/mark/gåVenstre4.png")]
markWalkRight = [pg.image.load("assets/sprites/mark/gåHøjre1.png"), pg.image.load("assets/sprites/mark/gåHøjre2.png"), pg.image.load("assets/sprites/mark/gåHøjre3.png"), pg.image.load("assets/sprites/mark/gåHøjre4.png"), pg.image.load("assets/sprites/mark/gåHøjre1.png"), pg.image.load("assets/sprites/mark/gåHøjre2.png"), pg.image.load("assets/sprites/mark/gåHøjre3.png"), pg.image.load("assets/sprites/mark/gåHøjre4.png"), pg.image.load("assets/sprites/mark/gåHøjre1.png"), pg.image.load("assets/sprites/mark/gåHøjre2.png"), pg.image.load("assets/sprites/mark/gåHøjre3.png"), pg.image.load("assets/sprites/mark/gåHøjre4.png")]
markWalkDown = [pg.image.load("assets/sprites/mark/gåNed1.png"), pg.image.load("assets/sprites/mark/gåNed2.png"), pg.image.load("assets/sprites/mark/gåNed3.png"), pg.image.load("assets/sprites/mark/gåNed4.png"), pg.image.load("assets/sprites/mark/gåNed1.png"), pg.image.load("assets/sprites/mark/gåNed2.png"), pg.image.load("assets/sprites/mark/gåNed3.png"), pg.image.load("assets/sprites/mark/gåNed4.png"), pg.image.load("assets/sprites/mark/gåNed1.png"), pg.image.load("assets/sprites/mark/gåNed2.png"), pg.image.load("assets/sprites/mark/gåNed3.png"), pg.image.load("assets/sprites/mark/gåNed4.png")]
markAttackUp = [pg.image.load("assets/sprites/mark/hitUp1.png"),  pg.image.load("assets/sprites/mark/hitUp3.png"), pg.image.load("assets/sprites/mark/hitUp2.png"), pg.image.load("assets/sprites/mark/hitUp4.png"), pg.image.load("assets/sprites/mark/hitUp2.png"),pg.image.load("assets/sprites/mark/hitUp1.png"), pg.image.load("assets/sprites/mark/hitUp3.png"),  pg.image.load("assets/sprites/mark/hitUp2.png"), pg.image.load("assets/sprites/mark/hitUp4.png"), pg.image.load("assets/sprites/mark/hitUp1.png"), pg.image.load("assets/sprites/mark/hitUp2.png"), pg.image.load("assets/sprites/mark/hitUp3.png"), pg.image.load("assets/sprites/mark/hitUp4.png")]
markAttackDown = [pg.image.load("assets/sprites/mark/hitDown1.png"), pg.image.load("assets/sprites/mark/hitDown2.png"), pg.image.load("assets/sprites/mark/hitDown3.png"), pg.image.load("assets/sprites/mark/hitDown4.png"), pg.image.load("assets/sprites/mark/hitDown1.png"), pg.image.load("assets/sprites/mark/hitDown2.png"), pg.image.load("assets/sprites/mark/hitDown3.png"), pg.image.load("assets/sprites/mark/hitDown4.png"), pg.image.load("assets/sprites/mark/hitDown1.png"), pg.image.load("assets/sprites/mark/hitDown2.png"), pg.image.load("assets/sprites/mark/hitDown3.png"), pg.image.load("assets/sprites/mark/hitDown4.png")]
markAttackLeft = [pg.image.load("assets/sprites/mark/hitLeft1.png"), pg.image.load("assets/sprites/mark/hitLeft2.png"), pg.image.load("assets/sprites/mark/hitLeft3.png"), pg.image.load("assets/sprites/mark/hitLeft4.png"), pg.image.load("assets/sprites/mark/hitLeft1.png"), pg.image.load("assets/sprites/mark/hitLeft2.png"), pg.image.load("assets/sprites/mark/hitLeft3.png"), pg.image.load("assets/sprites/mark/hitLeft4.png"), pg.image.load("assets/sprites/mark/hitLeft1.png"), pg.image.load("assets/sprites/mark/hitLeft2.png"), pg.image.load("assets/sprites/mark/hitLeft3.png"), pg.image.load("assets/sprites/mark/hitLeft4.png")]
markAttackRight = [pg.image.load("assets/sprites/mark/hitRight1.png"), pg.image.load("assets/sprites/mark/hitRight2.png"), pg.image.load("assets/sprites/mark/hitRight3.png"), pg.image.load("assets/sprites/mark/hitRight4.png"), pg.image.load("assets/sprites/mark/hitRight1.png"), pg.image.load("assets/sprites/mark/hitRight2.png"), pg.image.load("assets/sprites/mark/hitRight3.png"), pg.image.load("assets/sprites/mark/hitRight4.png"), pg.image.load("assets/sprites/mark/hitRight1.png"), pg.image.load("assets/sprites/mark/hitRight2.png"), pg.image.load("assets/sprites/mark/hitRight3.png"), pg.image.load("assets/sprites/mark/hitRight4.png")]
markAttackSound = pg.mixer.Sound("assets/lyd/smarkAttackSound.wav")
#Player
class smark(object):
    def  __init__(self, x, y,):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 100
        self.vel = 10
        self.walkCount = 1
        self.hitCount = 1
        self.playsound = 0
        self.stand = True
        self.walkDown = False
        self.walkUp = False
        self.walkRight = False
        self.walkLeft = False
        self.hitbool = False
        self.allow = True
        self.hitbox = (self.x, self.y, 170, 200)
        self.attackingRight = False
        self.attackingLeft = False
        self.attackingUp = False
        self.attackingDown = False
        self.generalAttack = False

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.stand):
            if self.walkDown:
                win.blit(markWalkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x, self.y, 170, 200)
            elif self.walkUp:
                win.blit(markWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x, self.y, 170, 200)
            elif self.walkRight:
                win.blit(markWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x, self.y, 160, 200)
            elif self.walkLeft:
                win.blit(markWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x, self.y, 160, 200)
        else:
            if self.walkDown:
                win.blit(markStandDown, (self.x, self.y))
                self.hitbox = (self.x, self.y, 170, 200)
            elif self.walkUp:
                win.blit(markStandUp, (self.x, self.y))
                self.hitbox = (self.x, self.y, 170, 200)
            elif self.walkRight:
                win.blit(markStandRight, (self.x, self.y))
                self.hitbox = (self.x, self.y, 160, 200)
            elif self.walkLeft:
                win.blit(markStandLeft, (self.x, self.y))
                self.hitbox = (self.x, self.y, 160, 200)
            else:
                win.blit(markStand, (self.x, self.y))
        self.healthBar()

    def attack(self, win):
        if self.hitCount + 1 >= 20:
            self.hitCount = 0

        if self.walkRight and self.hitbool:
            win.blit(markAttackRight[self.hitCount // 4], (self.x - 70, self.y - 50))
            self.hitCount += 1
            self.attackingRight = True
            self.attackingLeft = False
            self.attackingUp = False
            self.attackingDown = False
        elif self.walkLeft and self.hitbool:
            win.blit(markAttackLeft[self.hitCount // 4], (self.x - 70, self.y - 50))
            self.hitCount += 1
            self.attackingLeft = True
            self.attackingRight = False
            self.attackingUp = False
            self.attackingDown = False
        elif self.walkUp and self.hitbool:
            win.blit(markAttackUp[self.hitCount // 4], (self.x - 80, self.y - 70))
            self.hitCount += 1
            self.attackingUp = True
            self.attackingRight = False
            self.attackingLeft = False
            self.attackingDown = False
        elif self.walkDown and self.hitbool:
            win.blit(markAttackDown[self.hitCount // 4], (self.x, self.y))
            self.hitCount += 1
            self.attackingDown = True
            self.attackingRight = False
            self.attackingLeft = False
            self.attackingUp = False
        else:
            self.hitCount = 0
            self.attackingRight = False
            self.attackingLeft = False
            self.attackingUp = False
            self.attackingDown = False
        self.healthBar()
        
        if pg.mixer.Channel(1).get_busy() == False and self.hitCount == 2:
            pg.mixer.Channel(1).play(markAttackSound)

        if self.hitCount == 8:
            self.generalAttack = True
        else: 
            self.generalAttack = False

    
    def attacked(self):
        Variabler.health -= 3

    def healthBar(self):
        healthBarBack = (50, 1000, 250, 40)
        healthBarFront = (50, 1000, Variabler.health/4, 40)
        healthBarOutline = (50, 1000, 250, 40)
        pg.draw.rect(win, (255,0,0), healthBarBack, 0)
        pg.draw.rect(win, (0,255,0), healthBarFront, 0)
        pg.draw.rect(win, (0,255,0), healthBarFront, 2)
        pg.draw.rect(win, (0,0,0), healthBarOutline, 3)

"""
class borde(object): #Skal den BRUGES?!?!!?
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, self.height, self.width)
"""
#Player Text
#allPlayerTextBox
allPlayerTextBox = pg.image.load("assets/Textbox.png")
class allPlayerText(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def tekst(self, win):
        win.blit(allPlayerTextBox, (self.x, self.y))

#NPC
#Mads ANIME
madsWalkUp = [pg.image.load("assets/sprites/mads/madsUp1.png"), pg.image.load("assets/sprites/mads/madsUp2.png"), pg.image.load("assets/sprites/mads/madsUp3.png"), pg.image.load("assets/sprites/mads/madsUp4.png"), pg.image.load("assets/sprites/mads/madsUp1.png"), pg.image.load("assets/sprites/mads/madsUp2.png"), pg.image.load("assets/sprites/mads/madsUp3.png"), pg.image.load("assets/sprites/mads/madsUp4.png"), pg.image.load("assets/sprites/mads/madsUp1.png"), pg.image.load("assets/sprites/mads/madsUp2.png"), pg.image.load("assets/sprites/mads/madsUp3.png"), pg.image.load("assets/sprites/mads/madsUp4.png")]
madsWalkDown = [pg.image.load("assets/sprites/mads/madsDown1.png"), pg.image.load("assets/sprites/mads/madsDown2.png"), pg.image.load("assets/sprites/mads/madsDown3.png"), pg.image.load("assets/sprites/mads/madsDown4.png"), pg.image.load("assets/sprites/mads/madsDown1.png"), pg.image.load("assets/sprites/mads/madsDown2.png"), pg.image.load("assets/sprites/mads/madsDown3.png"), pg.image.load("assets/sprites/mads/madsDown4.png"), pg.image.load("assets/sprites/mads/madsDown1.png"), pg.image.load("assets/sprites/mads/madsDown2.png"), pg.image.load("assets/sprites/mads/madsDown3.png"), pg.image.load("assets/sprites/mads/madsDown4.png")]
madsWalkRight = [pg.image.load("assets/sprites/mads/madsRight1.png"), pg.image.load("assets/sprites/mads/madsRight2.png"), pg.image.load("assets/sprites/mads/madsRight3.png"), pg.image.load("assets/sprites/mads/madsRight4.png"), pg.image.load("assets/sprites/mads/madsRight1.png"), pg.image.load("assets/sprites/mads/madsRight2.png"), pg.image.load("assets/sprites/mads/madsRight3.png"), pg.image.load("assets/sprites/mads/madsRight4.png"), pg.image.load("assets/sprites/mads/madsRight1.png"), pg.image.load("assets/sprites/mads/madsRight2.png"), pg.image.load("assets/sprites/mads/madsRight3.png"), pg.image.load("assets/sprites/mads/madsRight4.png")]
madsWalkLeft = [pg.image.load("assets/sprites/mads/madsLeft1.png"), pg.image.load("assets/sprites/mads/madsLeft2.png"), pg.image.load("assets/sprites/mads/madsLeft3.png"), pg.image.load("assets/sprites/mads/madsLeft4.png"), pg.image.load("assets/sprites/mads/madsLeft1.png"), pg.image.load("assets/sprites/mads/madsLeft2.png"), pg.image.load("assets/sprites/mads/madsLeft3.png"), pg.image.load("assets/sprites/mads/madsLeft4.png"), pg.image.load("assets/sprites/mads/madsLeft1.png"), pg.image.load("assets/sprites/mads/madsLeft2.png"), pg.image.load("assets/sprites/mads/madsLeft3.png"), pg.image.load("assets/sprites/mads/madsLeft4.png"), pg.image.load("assets/sprites/mads/madsLeft1.png"), pg.image.load("assets/sprites/mads/madsLeft2.png"), pg.image.load("assets/sprites/mads/madsLeft3.png"), pg.image.load("assets/sprites/mads/madsLeft4.png")]
madsStandLeft = pg.image.load("assets/sprites/mads/madsLeft1.png")
madsStandRight = pg.image.load("assets/sprites/mads/madsRight1.png")
madsStandUp = pg.image.load("assets/sprites/mads/madsUp1.png")
madsStandDown = pg.image.load("assets/sprites/mads/madsDown1.png")
class Mads(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 1
        self.vel = 10
        self.stand = True

    def movementMads(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.stand):
            if self.down:
                win.blit(madsWalkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(madsWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(madsWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.left:
                win.blit(madsWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(madsStandDown, (self.x, self.y))
        else:
            if self.down:
                win.blit(madsStandDown, (self.x, self.y))
            elif self.up:
                win.blit(madsStandUp, (self.x, self.y))
            elif self.right:
                win.blit(madsStandRight, (self.x, self.y))
            elif self.left:
                win.blit(madsStandLeft, (self.x, self.y))
            else:
                win.blit(madsStandDown, (self.x, self.y))

#hodyah ANIME
hodWalkUp = [pg.image.load("assets/sprites/hodyah/hodUp1.png"), pg.image.load("assets/sprites/hodyah/hodUp2.png"), pg.image.load("assets/sprites/hodyah/hodUp3.png"), pg.image.load("assets/sprites/hodyah/hodUp4.png"), pg.image.load("assets/sprites/hodyah/hodUp1.png"), pg.image.load("assets/sprites/hodyah/hodUp2.png"), pg.image.load("assets/sprites/hodyah/hodUp3.png"), pg.image.load("assets/sprites/hodyah/hodUp4.png"), pg.image.load("assets/sprites/hodyah/hodUp1.png"), pg.image.load("assets/sprites/hodyah/hodUp2.png"), pg.image.load("assets/sprites/hodyah/hodUp3.png"), pg.image.load("assets/sprites/hodyah/hodUp4.png")]
hodWalkDown = [pg.image.load("assets/sprites/hodyah/hodDown1.png"), pg.image.load("assets/sprites/hodyah/hodDown2.png"), pg.image.load("assets/sprites/hodyah/hodDown3.png"), pg.image.load("assets/sprites/hodyah/hodDown4.png"), pg.image.load("assets/sprites/hodyah/hodDown1.png"), pg.image.load("assets/sprites/hodyah/hodDown2.png"), pg.image.load("assets/sprites/hodyah/hodDown3.png"), pg.image.load("assets/sprites/hodyah/hodDown4.png"), pg.image.load("assets/sprites/hodyah/hodDown1.png"), pg.image.load("assets/sprites/hodyah/hodDown2.png"), pg.image.load("assets/sprites/hodyah/hodDown3.png"), pg.image.load("assets/sprites/hodyah/hodDown4.png")]
hodWalkLeft = [pg.image.load("assets/sprites/hodyah/hodLeft1.png"), pg.image.load("assets/sprites/hodyah/hodLeft2.png"), pg.image.load("assets/sprites/hodyah/hodLeft3.png"), pg.image.load("assets/sprites/hodyah/hodLeft4.png"), pg.image.load("assets/sprites/hodyah/hodLeft1.png"), pg.image.load("assets/sprites/hodyah/hodLeft2.png"), pg.image.load("assets/sprites/hodyah/hodLeft3.png"), pg.image.load("assets/sprites/hodyah/hodLeft4.png"), pg.image.load("assets/sprites/hodyah/hodLeft1.png"), pg.image.load("assets/sprites/hodyah/hodLeft2.png"), pg.image.load("assets/sprites/hodyah/hodLeft3.png"), pg.image.load("assets/sprites/hodyah/hodLeft4.png")]
hodWalkRight = [pg.image.load("assets/sprites/hodyah/hodRight1.png"), pg.image.load("assets/sprites/hodyah/hodRight2.png"), pg.image.load("assets/sprites/hodyah/hodRight3.png"), pg.image.load("assets/sprites/hodyah/hodRight4.png"), pg.image.load("assets/sprites/hodyah/hodRight1.png"), pg.image.load("assets/sprites/hodyah/hodRight2.png"), pg.image.load("assets/sprites/hodyah/hodRight3.png"), pg.image.load("assets/sprites/hodyah/hodRight4.png"), pg.image.load("assets/sprites/hodyah/hodRight1.png"), pg.image.load("assets/sprites/hodyah/hodRight2.png"), pg.image.load("assets/sprites/hodyah/hodRight3.png"), pg.image.load("assets/sprites/hodyah/hodRight4.png")]
hodStandUp = pg.image.load("assets/sprites/hodyah/hodUp1.png")
hodStandDown = pg.image.load("assets/sprites/hodyah/hodDown1.png")
hodStandLeft = pg.image.load("assets/sprites/hodyah/hodLeft1.png")
hodStandRight = pg.image.load("assets/sprites/hodyah/hodRight1.png")

class hodyah(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 1
        self.stand = True
        self.movementAllowed = 0
    
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.stand):
            if self.up:
                win.blit(hodWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(hodWalkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(hodWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.left:
                win.blit(hodWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(hodStandDown[self.walkCount // 3], (self.x, self.y))
        else:
            if self.down:
                win.blit(hodStandDown, (self.x, self.y))
            elif self.up:
                win.blit(hodStandUp, (self.x, self.y))
            elif self.left:
                win.blit(hodStandLeft, (self.x, self.y))
            elif self.right:
                win.blit(hodStandRight, (self.x, self.y))
            else:
                win.blit(hodStandDown, (self.x, self.y))

#kristian ANIME
krisWalkUp = [pg.image.load("assets/sprites/kristian/krisUp1.png"), pg.image.load("assets/sprites/kristian/krisUp2.png"), pg.image.load("assets/sprites/kristian/krisUp3.png"), pg.image.load("assets/sprites/kristian/krisUp4.png"), pg.image.load("assets/sprites/kristian/krisUp1.png"), pg.image.load("assets/sprites/kristian/krisUp2.png"), pg.image.load("assets/sprites/kristian/krisUp3.png"), pg.image.load("assets/sprites/kristian/krisUp4.png"), pg.image.load("assets/sprites/kristian/krisUp1.png"), pg.image.load("assets/sprites/kristian/krisUp2.png"), pg.image.load("assets/sprites/kristian/krisUp3.png"), pg.image.load("assets/sprites/kristian/krisUp4.png")]
krisWalkDown = [pg.image.load("assets/sprites/kristian/krisDown1.png"), pg.image.load("assets/sprites/kristian/krisDown2.png"), pg.image.load("assets/sprites/kristian/krisDown3.png"), pg.image.load("assets/sprites/kristian/krisDown4.png"), pg.image.load("assets/sprites/kristian/krisDown1.png"), pg.image.load("assets/sprites/kristian/krisDown2.png"), pg.image.load("assets/sprites/kristian/krisDown3.png"), pg.image.load("assets/sprites/kristian/krisDown4.png"), pg.image.load("assets/sprites/kristian/krisDown1.png"), pg.image.load("assets/sprites/kristian/krisDown2.png"), pg.image.load("assets/sprites/kristian/krisDown3.png"), pg.image.load("assets/sprites/kristian/krisDown4.png")]
krisWalkLeft = [pg.image.load("assets/sprites/kristian/krisLeft1.png"), pg.image.load("assets/sprites/kristian/krisLeft2.png"), pg.image.load("assets/sprites/kristian/krisLeft3.png"), pg.image.load("assets/sprites/kristian/krisLeft4.png"), pg.image.load("assets/sprites/kristian/krisLeft1.png"), pg.image.load("assets/sprites/kristian/krisLeft2.png"), pg.image.load("assets/sprites/kristian/krisLeft3.png"), pg.image.load("assets/sprites/kristian/krisLeft4.png"), pg.image.load("assets/sprites/kristian/krisLeft1.png"), pg.image.load("assets/sprites/kristian/krisLeft2.png"), pg.image.load("assets/sprites/kristian/krisLeft3.png"), pg.image.load("assets/sprites/kristian/krisLeft4.png")]
krisWalkRight = [pg.image.load("assets/sprites/kristian/krisRight1.png"), pg.image.load("assets/sprites/kristian/krisRight2.png"), pg.image.load("assets/sprites/kristian/krisRight3.png"), pg.image.load("assets/sprites/kristian/krisRight4.png"), pg.image.load("assets/sprites/kristian/krisRight1.png"), pg.image.load("assets/sprites/kristian/krisRight2.png"), pg.image.load("assets/sprites/kristian/krisRight3.png"), pg.image.load("assets/sprites/kristian/krisRight4.png"), pg.image.load("assets/sprites/kristian/krisRight1.png"), pg.image.load("assets/sprites/kristian/krisRight2.png"), pg.image.load("assets/sprites/kristian/krisRight3.png"), pg.image.load("assets/sprites/kristian/krisRight4.png")]
krisStandUp = pg.image.load("assets/sprites/kristian/krisUp1.png")
krisStandDown = pg.image.load("assets/sprites/kristian/krisDown1.png")
krisStandLeft = pg.image.load("assets/sprites/kristian/krisLeft1.png")
krisStandRight = pg.image.load("assets/sprites/kristian/krisRight1.png")

class kristian(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 1
        self.stand = True
        self.movementAllowed = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.stand):
            if self.up:
                win.blit(krisWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(krisWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(krisWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.left:
                win.blit(krisWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(krisStandDown, (self.x, self.y))
        else:
            if self.up:
                win.blit(krisStandUp, (self.x, self.y))
            elif self.down:
                win.blit(krisStandDown, (self.x, self.y))
            elif self.left:
                win.blit(krisStandLeft, (self.x, self.y))
            elif self.right:
                win.blit(krisStandRight, (self.x, self.y))
            else:
                win.blit(krisStandDown, (self.x, self.y))
        

#Lac ANIME
lacWalkUp = [pg.image.load("assets/sprites/lac/lacUp1.png"), pg.image.load("assets/sprites/lac/lacUp2.png"), pg.image.load("assets/sprites/lac/lacUp3.png"), pg.image.load("assets/sprites/lac/lacUp4.png"), pg.image.load("assets/sprites/lac/lacUp1.png"), pg.image.load("assets/sprites/lac/lacUp2.png"), pg.image.load("assets/sprites/lac/lacUp3.png"), pg.image.load("assets/sprites/lac/lacUp4.png"), pg.image.load("assets/sprites/lac/lacUp1.png"), pg.image.load("assets/sprites/lac/lacUp2.png"), pg.image.load("assets/sprites/lac/lacUp3.png"), pg.image.load("assets/sprites/lac/lacUp4.png")]
lacWalkDown = [pg.image.load("assets/sprites/lac/lacDown1.png"), pg.image.load("assets/sprites/lac/lacDown2.png"), pg.image.load("assets/sprites/lac/lacDown3.png"), pg.image.load("assets/sprites/lac/lacDown4.png"), pg.image.load("assets/sprites/lac/lacDown1.png"), pg.image.load("assets/sprites/lac/lacDown2.png"), pg.image.load("assets/sprites/lac/lacDown3.png"), pg.image.load("assets/sprites/lac/lacDown4.png"), pg.image.load("assets/sprites/lac/lacDown1.png"), pg.image.load("assets/sprites/lac/lacDown2.png"), pg.image.load("assets/sprites/lac/lacDown3.png"), pg.image.load("assets/sprites/lac/lacDown4.png")]
lacWalkLeft = [pg.image.load("assets/sprites/lac/lacLeft1.png"), pg.image.load("assets/sprites/lac/lacLeft2.png"), pg.image.load("assets/sprites/lac/lacLeft3.png"), pg.image.load("assets/sprites/lac/lacLeft4.png"), pg.image.load("assets/sprites/lac/lacLeft1.png"), pg.image.load("assets/sprites/lac/lacLeft2.png"), pg.image.load("assets/sprites/lac/lacLeft3.png"), pg.image.load("assets/sprites/lac/lacLeft4.png"), pg.image.load("assets/sprites/lac/lacLeft1.png"), pg.image.load("assets/sprites/lac/lacLeft2.png"), pg.image.load("assets/sprites/lac/lacLeft3.png"), pg.image.load("assets/sprites/lac/lacLeft4.png")]
lacWalkRight = [pg.image.load("assets/sprites/lac/lacRight1.png"), pg.image.load("assets/sprites/lac/lacRight2.png"), pg.image.load("assets/sprites/lac/lacRight3.png"), pg.image.load("assets/sprites/lac/lacRight4.png"), pg.image.load("assets/sprites/lac/lacRight1.png"), pg.image.load("assets/sprites/lac/lacRight2.png"), pg.image.load("assets/sprites/lac/lacRight3.png"), pg.image.load("assets/sprites/lac/lacRight4.png"), pg.image.load("assets/sprites/lac/lacRight1.png"), pg.image.load("assets/sprites/lac/lacRight2.png"), pg.image.load("assets/sprites/lac/lacRight3.png"), pg.image.load("assets/sprites/lac/lacRight4.png")]
LacStandUp = pg.image.load("assets/sprites/lac/lacUp1.png")
LacStandDown = pg.image.load("assets/sprites/lac/lacDown1.png")
LacStandLeft = pg.image.load("assets/sprites/lac/lacLeft1.png")
LacStandRight = pg.image.load("assets/sprites/lac/lacRight1.png")

class Lac(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.walkCount = 1
        self.stand = True
    
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.stand):
            if self.up:
                win.blit(lacWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(lacWalkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.left:
                win.blit(lacWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(lacWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(madsStandDown, (self.x, self.y))
        else:
            if self.up:
                win.blit(LacStandUp, (self.x, self.y))
            elif self.down:
                win.blit(LacStandDown, (self.x, self.y))
            elif self.left:
                win.blit(LacStandLeft, (self.x, self.y))
            elif self.right:
                win.blit(LacStandRight, (self.x, self.y))

#EmilANIME
emilWalkUp = [pg.image.load("assets/sprites/emil/emilUp1.png"), pg.image.load("assets/sprites/emil/emilUp2.png"), pg.image.load("assets/sprites/emil/emilUp3.png"), pg.image.load("assets/sprites/emil/emilUp4.png"), pg.image.load("assets/sprites/emil/emilUp1.png"), pg.image.load("assets/sprites/emil/emilUp2.png"), pg.image.load("assets/sprites/emil/emilUp3.png"), pg.image.load("assets/sprites/emil/emilUp4.png"), pg.image.load("assets/sprites/emil/emilUp1.png"), pg.image.load("assets/sprites/emil/emilUp2.png"), pg.image.load("assets/sprites/emil/emilUp3.png"), pg.image.load("assets/sprites/emil/emilUp4.png")]
emilWalkDown = [pg.image.load("assets/sprites/emil/emilUp1.png"), pg.image.load("assets/sprites/emil/emilDown2.png"), pg.image.load("assets/sprites/emil/emilDown3.png"), pg.image.load("assets/sprites/emil/emilDown4.png"), pg.image.load("assets/sprites/emil/emilDown1.png"), pg.image.load("assets/sprites/emil/emilDown2.png"), pg.image.load("assets/sprites/emil/emilDown3.png"), pg.image.load("assets/sprites/emil/emilDown4.png"), pg.image.load("assets/sprites/emil/emilDown1.png"), pg.image.load("assets/sprites/emil/emilDown2.png"), pg.image.load("assets/sprites/emil/emilDown3.png"), pg.image.load("assets/sprites/emil/emilDown4.png")]
emilWalkRight = [pg.image.load("assets/sprites/emil/emilRight1.png"), pg.image.load("assets/sprites/emil/emilRight2.png"), pg.image.load("assets/sprites/emil/emilRight3.png"), pg.image.load("assets/sprites/emil/emilRight4.png"), pg.image.load("assets/sprites/emil/emilRight1.png"), pg.image.load("assets/sprites/emil/emilRight2.png"), pg.image.load("assets/sprites/emil/emilRight3.png"), pg.image.load("assets/sprites/emil/emilRight4.png"), pg.image.load("assets/sprites/emil/emilRight1.png"), pg.image.load("assets/sprites/emil/emilRight2.png"), pg.image.load("assets/sprites/emil/emilRight3.png"), pg.image.load("assets/sprites/emil/emilRight4.png")]
emilWalkLeft = [pg.image.load("assets/sprites/emil/emilLeft1.png"), pg.image.load("assets/sprites/emil/emilLeft2.png"), pg.image.load("assets/sprites/emil/emilLeft3.png"), pg.image.load("assets/sprites/emil/emilLeft4.png"), pg.image.load("assets/sprites/emil/emilLeft1.png"), pg.image.load("assets/sprites/emil/emilLeft2.png"), pg.image.load("assets/sprites/emil/emilLeft3.png"), pg.image.load("assets/sprites/emil/emilLeft4.png"), pg.image.load("assets/sprites/emil/emilLeft1.png"), pg.image.load("assets/sprites/emil/emilLeft2.png"), pg.image.load("assets/sprites/emil/emilLeft3.png"), pg.image.load("assets/sprites/emil/emilLeft4.png")]
emilStandUp = pg.image.load("assets/sprites/emil/emilUp1.png")
emilStandDown = pg.image.load("assets/sprites/emil/emilUp1.png")
emilStandRight = pg.image.load("assets/sprites/emil/emilRight1.png")
emilStandLeft = pg.image.load("assets/sprites/emil/emilLeft1.png")

class emil(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 1
        self.stand = True
        self.movementAllowed = 0
   
    def draw(self):  
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.stand):
            if self.up:
                win.blit(emilWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(emilWalkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(emilWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.left:
                win.blit(emilWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(emilStandDown, (self.x, self.y))
        else:
            if self.up:
                win.blit(emilStandUp, (self.x, self.y))
            elif self.down:
                win.blit(emilStandDown, (self.x, self.y))
            elif self.left:
                win.blit(emilStandLeft, (self.x, self.y))
            elif self.right:
                win.blit(emilStandRight, (self.x, self.y))

#broBygger ANIME
broByggerWalkUp = [pg.image.load("assets/sprites/brobygger/bbUp1.png"), pg.image.load("assets/sprites/brobygger/bbUp2.png"), pg.image.load("assets/sprites/brobygger/bbUp3.png"), pg.image.load("assets/sprites/brobygger/bbUp4.png"), pg.image.load("assets/sprites/brobygger/bbUp1.png"), pg.image.load("assets/sprites/brobygger/bbUp2.png"), pg.image.load("assets/sprites/brobygger/bbUp3.png"), pg.image.load("assets/sprites/brobygger/bbUp4.png"), pg.image.load("assets/sprites/brobygger/bbUp1.png"), pg.image.load("assets/sprites/brobygger/bbUp2.png"), pg.image.load("assets/sprites/brobygger/bbUp3.png"), pg.image.load("assets/sprites/brobygger/bbUp4.png")]
broByggerWalkDown = [pg.image.load("assets/sprites/brobygger/bbDown1.png"), pg.image.load("assets/sprites/brobygger/bbDown2.png"), pg.image.load("assets/sprites/brobygger/bbDown3.png"), pg.image.load("assets/sprites/brobygger/bbDown4.png"), pg.image.load("assets/sprites/brobygger/bbDown1.png"), pg.image.load("assets/sprites/brobygger/bbDown2.png"), pg.image.load("assets/sprites/brobygger/bbDown3.png"), pg.image.load("assets/sprites/brobygger/bbDown4.png"), pg.image.load("assets/sprites/brobygger/bbDown1.png"), pg.image.load("assets/sprites/brobygger/bbDown2.png"), pg.image.load("assets/sprites/brobygger/bbDown3.png"), pg.image.load("assets/sprites/brobygger/bbDown4.png")]
broByggerWalkLeft = [pg.image.load("assets/sprites/brobygger/bbLeft1.png"), pg.image.load("assets/sprites/brobygger/bbLeft2.png"), pg.image.load("assets/sprites/brobygger/bbLeft3.png"), pg.image.load("assets/sprites/brobygger/bbLeft4.png"), pg.image.load("assets/sprites/brobygger/bbLeft1.png"), pg.image.load("assets/sprites/brobygger/bbLeft2.png"), pg.image.load("assets/sprites/brobygger/bbLeft3.png"), pg.image.load("assets/sprites/brobygger/bbLeft4.png"), pg.image.load("assets/sprites/brobygger/bbLeft1.png"), pg.image.load("assets/sprites/brobygger/bbLeft2.png"), pg.image.load("assets/sprites/brobygger/bbLeft3.png"), pg.image.load("assets/sprites/brobygger/bbLeft4.png")]
broByggerWalkRight = [pg.image.load("assets/sprites/brobygger/bbRight1.png"), pg.image.load("assets/sprites/brobygger/bbRight2.png"), pg.image.load("assets/sprites/brobygger/bbRight3.png"), pg.image.load("assets/sprites/brobygger/bbRight4.png"), pg.image.load("assets/sprites/brobygger/bbRight1.png"), pg.image.load("assets/sprites/brobygger/bbRight2.png"), pg.image.load("assets/sprites/brobygger/bbRight3.png"), pg.image.load("assets/sprites/brobygger/bbRight4.png"), pg.image.load("assets/sprites/brobygger/bbRight1.png"), pg.image.load("assets/sprites/brobygger/bbRight2.png"), pg.image.load("assets/sprites/brobygger/bbRight3.png"), pg.image.load("assets/sprites/brobygger/bbRight4.png")]
broByggerStandUp = pg.image.load("assets/sprites/brobygger/bbUp1.png")
broByggerStandDown = pg.image.load("assets/sprites/brobygger/bbDown1.png")
broByggerStandLeft = pg.image.load("assets/sprites/brobygger/bbLeft1.png")
broByggerStandRight = pg.image.load("assets/sprites/brobygger/bbRight1.png")

class broBygger(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 1
        self.stand = True
        self.movementAllowed = 0
        self.health = 200

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.stand):
            if self.up:
                win.blit(broByggerWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(broByggerWalkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.left:
                win.blit(broByggerWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(broByggerWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(broByggerStandDown, (self.x, self.y))
        else:
            if self.up:
                win.blit(broByggerStandUp, (self.x, self.y))
            elif self.down:
                win.blit(broByggerStandDown, (self.x, self.y))
            elif self.left:
                win.blit(broByggerStandLeft, (self.x, self.y))
            elif self.right:
                win.blit(broByggerStandRight, (self.x, self.y))
            else:
                win.blit(broByggerStandDown, (self.x, self.y))
        self.healthbar()

    
    def movement(self):
        if self.movementAllowed < 9:
            self.movementChoice = r.randint(1,5)
        if self.movementAllowed > 10 and self.movementAllowed < 100:
            if self.movementChoice == 1:
                self.x += self.vel
                self.left = False
                self.right = True
                self.up = False
                self.down = False
                self.stand = False
            elif self.movementChoice == 2:
                self.x -= self.vel
                self.left = True
                self.right = False
                self.up = False
                self.down = False
                self.stand = False
            elif self.movementChoice == 3:
                self.y += self.vel
                self.left = False
                self.right = False
                self.up = False
                self.down = True
                self.stand = False
            elif self.movementChoice == 4:
                self.y -= self.vel
                self.left = False
                self.right = False
                self.up = True
                self.down = False
                self.stand = False
            elif self.movementChoice == 5:
                self.left = False
                self.right = False
                self.up = False
                self.down = False
                self.stand = True
        elif self.movementAllowed > 100:
            self.movementAllowed = 0
        self.movementAllowed += r.randint(1,7)

    def attack(self):
        #her kan eventuelt indsættes animationer til brobyggeren...
        pass

    def healthbar(self):
        healthBarBack = (self.x+40, self.y-5, 100, 5)
        healthBarFront = (self.x+40, self.y-5, self.health/2, 5)
        pg.draw.rect(win, (255,0,0), healthBarBack, 0)
        pg.draw.rect(win, (0,255,0), healthBarFront, 0)
        pg.draw.rect(win, (0,255,0), healthBarFront, 2)




#MENU
startButton = pg.image.load("assets/menu/startButton.png")
startButton1 = pg.image.load("assets/menu/startButton1.png")
settingButton = pg.image.load("assets/menu/settingButton.png")
settingButton1 = pg.image.load("assets/menu/settingButton1.png")
quitButton = pg.image.load("assets/menu/quitButton.png")
quitButton1 = pg.image.load("assets/menu/quitButton1.png")
picOfClosedScroll = pg.image.load("assets/menu/closedScroll.png")
openScrolls = [pg.image.load("assets/menu/openScrollCpp.png"), pg.image.load("assets/menu/openScrollCsharp.png"), pg.image.load("assets/menu/openScrollCss.png"), pg.image.load("assets/menu/openScrollHTML.png"), pg.image.load("assets/menu/openScrollJs.png"), pg.image.load("assets/menu/openScrollPython.png")]

#Closed Scrolls
class closedScroll(object):
    def __init__(self, closedscrollX1, closedscrollY1, closedscrollX2, closedscrollY2, closedscrollX3, closedscrollY3, closedscrollX4, closedscrollY4, closedscrollX5, closedscrollY5, closedscrollX6, closedscrollY6):
        self.closedscrollX1 = closedscrollX1
        self.closedscrollY1 = closedscrollY1
        self.closedscrollX2 = closedscrollX2
        self.closedscrollY2 = closedscrollY2
        self.closedscrollX3 = closedscrollX3
        self.closedscrollY3 = closedscrollY3
        self.closedscrollX4 = closedscrollX4
        self.closedscrollY4 = closedscrollY4
        self.closedscrollX5 = closedscrollX5
        self.closedscrollY5 = closedscrollY5
        self.closedscrollX6 = closedscrollX6
        self.closedscrollY6 = closedscrollY6

    def drawClosedScroll1(self):
        win.blit(picOfClosedScroll, (self.closedscrollX1, self.closedscrollY1))
        win.blit(picOfClosedScroll, (self.closedscrollX2, self.closedscrollY2))

    def drawClosedScroll2(self):
        win.blit(picOfClosedScroll, (self.closedscrollX3, self.closedscrollY3))
        win.blit(picOfClosedScroll, (self.closedscrollX4, self.closedscrollY4))

    def drawClosedScroll3(self):
        win.blit(picOfClosedScroll, (self.closedscrollX5, self.closedscrollY5))
        win.blit(picOfClosedScroll, (self.closedscrollX6, self.closedscrollY6))

#Opened Scrolls
class scrolls(object):
    def __init__(self, scrollX1, scrollY1, scrollX2, scrollY2, scrollX3, scrollY3, scrollX4, scrollY4, scrollX5, scrollY5, scrollX6, scrollY6):
        self.scrollX1 = scrollX1
        self.scrollY1 = scrollY1
        self.scrollX2 = scrollX2
        self.scrollY2 = scrollY2
        self.scrollX3 = scrollX3
        self.scrollY3 = scrollY3
        self.scrollX4 = scrollX4
        self.scrollY4 = scrollY4
        self.scrollX5 = scrollX5
        self.scrollY5 = scrollY5
        self.scrollX6 = scrollX6
        self.scrollY6 = scrollY6

    def drawMouseOverStart(self):
        win.blit(r.choice(openScrolls), (self.scrollX1, self.scrollY1))
        win.blit(r.choice(openScrolls), (self.scrollX2, self.scrollY2))

    def drawMouseOverSetting(self):
        win.blit(r.choice(openScrolls), (self.scrollX3, self.scrollY3))
        win.blit(r.choice(openScrolls), (self.scrollX4, self.scrollY4))

    def drawMouseOverQuit(self):
        win.blit(r.choice(openScrolls), (self.scrollX5, self.scrollY5))
        win.blit(r.choice(openScrolls), (self.scrollX6, self.scrollY6))

#Main Menu buttons
class buttons(object):
    def __init__(self, startX, startY, settingX, settingY, quitX, quitY, height, width):
        self.startX = startX
        self.startY = startY
        self.settingX = settingX
        self.settingY = settingY
        self.quitX = quitX
        self.quitY = quitY
        self.height = height
        self.width = width
    
    def drawStart(self):
        win.blit(startButton, (self.startX, self.startY))

    def drawSetting(self):
        win.blit(settingButton, (self.settingX, self.settingY))
    
    def drawQuit(self):
        win.blit(quitButton, (self.quitX, self.quitY))

class sangeListe():
    sange = ["assets/lyd/Violin_Background.mp3", "assets/lyd/kindahipandoldsong.mp3", "assets/lyd/EmotionalJegGuess.mp3"]


#items
pizzaSprite = pg.image.load("assets/items/pizza.png")
burgerSprite = pg.image.load("assets/items/burger.png")
kaffeSprite = pg.image.load("assets/items/kaffe.png")
energidrikSprite = pg.image.load("assets/items/energidrik.png")

class droppedItems(object):
    def __init__(self, x, y, item):
        self.x = x
        self.y = y
        self.item = item
        self.movementVar = 0

    def draw(self, win):
        win.blit(self.item, (self.x, self.y))



inventoryBackground = pg.image.load("assets/Inventory/Inventory.png")
inventoryPizza = pg.image.load("assets/Inventory/minipizza.png")
inventoryBurger = pg.image.load("assets/Inventory/miniburger.png")
inventoryKaffe = pg.image.load("assets/Inventory/kaffe.png")
inventoryEnergidrik = pg.image.load("assets/Inventory/energidrik.png")
class inventory(object):
    inventoryX = 1470
    inventoryY = 960

    def pizzaInvCount(self):
        import Tekst
        fontInventory = pg.font.Font("assets/invFont.ttf", 36)
        Text = str(Variabler.pizza)
        textSetting = fontInventory.render(Text, Tekst.run, Tekst.black1)
        textRect = textSetting.get_rect()
        textRect.center = (self.inventoryX+91, self.inventoryY+100)
        win.blit(textSetting, textRect)

    def burgerInvCount(self):
        import Tekst
        fontInventory = pg.font.Font("assets/invFont.ttf", 36)
        Text = str(Variabler.burger)
        textSetting = fontInventory.render(Text, Tekst.run, Tekst.black1)
        textRect = textSetting.get_rect()
        textRect.center = (self.inventoryX+204, self.inventoryY+100)
        win.blit(textSetting, textRect)

    def kaffeInvCount(self):
        import Tekst
        fontInventory = pg.font.Font("assets/invFont.ttf", 36)
        Text = str(Variabler.kaffe)
        textSetting = fontInventory.render(Text, Tekst.run, Tekst.black1)
        textRect = textSetting.get_rect()
        textRect.center = (self.inventoryX+318, self.inventoryY+100)
        win.blit(textSetting, textRect)

    def energidrikInvCount(self):
        import Tekst
        fontInventory = pg.font.Font("assets/invFont.ttf", 36)
        Text = str(Variabler.energidrik)
        textSetting = fontInventory.render(Text, Tekst.run, Tekst.black1)
        textRect = textSetting.get_rect()
        textRect.center = (self.inventoryX+427, self.inventoryY+100)
        win.blit(textSetting, textRect)

    def draw(self, win):
        win.blit(inventoryPizza, (self.inventoryX-2, self.inventoryY))
        win.blit(inventoryBurger, (self.inventoryX+115, self.inventoryY+13))
        win.blit(inventoryKaffe, (self.inventoryX+180, self.inventoryY-24))
        win.blit(inventoryEnergidrik, (self.inventoryX+291, self.inventoryY-35))
        win.blit(inventoryBackground, (self.inventoryX, self.inventoryY))

        self.pizzaInvCount()
        self.burgerInvCount()
        self.kaffeInvCount()
        self.energidrikInvCount()

jijiSprite1 = pg.image.load("assets/sprites/jiji/jiji1.png")
jijiSprite2 = pg.image.load("assets/sprites/jiji/jiji2.png")
questMark = pg.image.load("assets/quest.png")

class jiji(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.passiveMovement = 0
    def draw(self, win):
        if self.passiveMovement < 10:
            win.blit(jijiSprite1, (self.x, self.y))
        else:
            win.blit(jijiSprite2, (self.x, self.y))
            win.blit(questMark, (self.x+5, self.y-30))
        
        if self.passiveMovement > 15:
            self.passiveMovement = 0
        self.passiveMovement += 1


