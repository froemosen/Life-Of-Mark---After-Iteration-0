import pygame as pg
import random as r
x = 1920
y = 1080
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
markAttackUp = [pg.image.load("assets/sprites/mark/hitUp1.png"), pg.image.load("assets/sprites/mark/hitUp2.png"), pg.image.load("assets/sprites/mark/hitUp3.png"), pg.image.load("assets/sprites/mark/hitUp4.png"), pg.image.load("assets/sprites/mark/hitUp1.png"), pg.image.load("assets/sprites/mark/hitUp2.png"), pg.image.load("assets/sprites/mark/hitUp3.png"), pg.image.load("assets/sprites/mark/hitUp4.png"), pg.image.load("assets/sprites/mark/hitUp1.png"), pg.image.load("assets/sprites/mark/hitUp2.png"), pg.image.load("assets/sprites/mark/hitUp3.png"), pg.image.load("assets/sprites/mark/hitUp4.png")]
markAttackDown = [pg.image.load("assets/sprites/mark/hitDown1.png"), pg.image.load("assets/sprites/mark/hitDown2.png"), pg.image.load("assets/sprites/mark/hitDown3.png"), pg.image.load("assets/sprites/mark/hitDown4.png"), pg.image.load("assets/sprites/mark/hitDown1.png"), pg.image.load("assets/sprites/mark/hitDown2.png"), pg.image.load("assets/sprites/mark/hitDown3.png"), pg.image.load("assets/sprites/mark/hitDown4.png"), pg.image.load("assets/sprites/mark/hitDown1.png"), pg.image.load("assets/sprites/mark/hitDown2.png"), pg.image.load("assets/sprites/mark/hitDown3.png"), pg.image.load("assets/sprites/mark/hitDown4.png")]
markAttackLeft = [pg.image.load("assets/sprites/mark/hitLeft1.png"), pg.image.load("assets/sprites/mark/hitLeft2.png"), pg.image.load("assets/sprites/mark/hitLeft3.png"), pg.image.load("assets/sprites/mark/hitLeft4.png"), pg.image.load("assets/sprites/mark/hitLeft1.png"), pg.image.load("assets/sprites/mark/hitLeft2.png"), pg.image.load("assets/sprites/mark/hitLeft3.png"), pg.image.load("assets/sprites/mark/hitLeft4.png"), pg.image.load("assets/sprites/mark/hitLeft1.png"), pg.image.load("assets/sprites/mark/hitLeft2.png"), pg.image.load("assets/sprites/mark/hitLeft3.png"), pg.image.load("assets/sprites/mark/hitLeft4.png")]
markAttackRight = [pg.image.load("assets/sprites/mark/hitRight1.png"), pg.image.load("assets/sprites/mark/hitRight2.png"), pg.image.load("assets/sprites/mark/hitRight3.png"), pg.image.load("assets/sprites/mark/hitRight4.png"), pg.image.load("assets/sprites/mark/hitRight1.png"), pg.image.load("assets/sprites/mark/hitRight2.png"), pg.image.load("assets/sprites/mark/hitRight3.png"), pg.image.load("assets/sprites/mark/hitRight4.png"), pg.image.load("assets/sprites/mark/hitRight1.png"), pg.image.load("assets/sprites/mark/hitRight2.png"), pg.image.load("assets/sprites/mark/hitRight3.png"), pg.image.load("assets/sprites/mark/hitRight4.png")]

#Player
class smark(object):
    def  __init__(self, x, y):
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
        pg.draw.rect(win, (0,255,0), self.hitbox, 2)

    def attack(self, win):
        if self.hitCount + 1 >= 27:
            self.hitCount = 0

        if self.walkRight and self.hitbool:
            win.blit(markAttackRight[self.hitCount // 3], (self.x - 70, self.y - 50))
            self.hitCount += 1
        elif self.walkLeft and self.hitbool:
            win.blit(markAttackLeft[self.hitCount // 3], (self.x - 70, self.y - 50))
            self.hitCount += 1
        elif self.walkUp and self.hitbool:
            win.blit(markAttackUp[self.hitCount // 3], (self.x, self.y))
            self.hitCount += 1
        elif self.walkDown and self.hitbool:
            win.blit(markAttackDown[self.hitCount // 3], (self.x, self.y))
            self.hitCount += 1
        else:
            self.hitCount = 0

class borde(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, self.height, self.width)

    def drawBorde(self):
        pg.draw.rect(win, (0,255,0), self.hitbox, 2)

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

#Lac


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
        self.vel = 10
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.walkCount = 1
        self.stand = True
        self.movementAllowed = 0
        self.hitbox = (self.x + 20, self.y + 20 , 120, 175)


    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.stand):
            if self.up:
                win.blit(broByggerWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
            elif self.down:
                win.blit(broByggerWalkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
            elif self.left:
                win.blit(broByggerWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
            elif self.right:
                win.blit(broByggerWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
            else:
                win.blit(broByggerStandDown, (self.x, self.y))
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
        else:
            if self.up:
                win.blit(broByggerStandUp, (self.x, self.y))
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
            elif self.down:
                win.blit(broByggerStandDown, (self.x, self.y))
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
            elif self.left:
                win.blit(broByggerStandLeft, (self.x, self.y))
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
            elif self.right:
                win.blit(broByggerStandRight, (self.x, self.y))
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
            else:
                win.blit(broByggerStandDown, (self.x, self.y))
                self.hitbox = (self.x + 25, self.y + 20 , 95, 115)
        pg.draw.rect(win, (0,255,0), self.hitbox, 2)
    
    
    def movement(self):
        """
        if self.x >= 100 and self.x < 600:
            self.x += self.vel
            self.left = False
            self.right = True
            self.up = False
            self.down = False
            self.stand = False
        elif self.x >= 600:
            
            """
        if self.movementAllowed < 29:
            self.movementChoice = r.randint(1,5)
        if self.movementAllowed > 30 and self.movementAllowed < 200:
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
        elif self.movementAllowed > 200:
            self.movementAllowed = 0
        self.movementAllowed += r.randint(1,7)



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
