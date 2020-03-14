import pygame as pg
import random as r
x = 1920
y = 1080
win = pg.display.set_mode((x,y), pg.FULLSCREEN)

#MARK ANIME
markStandLeft = pg.image.load("gåVenstre1.png")
markStandRight = pg.image.load("gåHøjre1.png")
markStandUp = pg.image.load("gåOp3.png")
markStandDown = pg.image.load("gåNed1.png")
markStand = pg.image.load("gåNed1.png")
markWalkUp = [pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png")]
markWalkLeft = [pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png"), pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png"), pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png")]
markWalkRight = [pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png"), pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png"), pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png")]
markWalkDown = [pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png"), pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png"), pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png")]

#Player
class smark(object):
    def  __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50   
        self.width = 100
        self.vel = 10
        self.walkCount = 1
        self.playsound = 0
        self.stand = True
        self.walkDown = False
        self.walkUp = False
        self.walkRight = False
        self.walkLeft = False
        self.hitbox = (self.x + 77, self.y + 65, self.height + 102, self.width + 87)
    

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.stand):
            if self.walkDown:
                win.blit(markWalkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 77, self.y + 65, self.height + 102, self.width + 87)
            elif self.walkUp:
                win.blit(markWalkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 77, self.y + 65, self.height + 102, self.width + 87)
            elif self.walkRight:
                win.blit(markWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 88, self.y + 65, self.height + 102, self.width + 87)
            elif self.walkLeft:
                win.blit(markWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 79, self.y + 65, self.height + 102, self.width + 87)
        else:
            if self.walkDown:
                win.blit(markStandDown, (self.x, self.y))
                self.hitbox = (self.x + 77, self.y + 65, self.height + 102, self.width + 87)
            elif self.walkUp:
                win.blit(markStandUp, (self.x, self.y))
                self.hitbox = (self.x + 77, self.y + 65, self.height + 102, self.width + 87)
            elif self.walkRight:
                win.blit(markStandRight, (self.x, self.y))
                self.hitbox = (self.x + 88, self.y + 65, self.height + 102, self.width + 87)
            elif self.walkLeft:
                win.blit(markStandLeft, (self.x, self.y))
                self.hitbox = (self.x + 79, self.y + 65, self.height + 102, self.width + 87)
            else:
                win.blit(markStand, (self.x, self.y))
        pg.draw.rect(win, (0,255,0), self.hitbox, 2)

#Player Text
class allPlayerText(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def tekst(self, win):
        textBox = pg.image.load("textFrame.png")
        win.blit(textBox, (self.x, self.y))

#MENU
startButton = pg.image.load("startButton.png")
startButton1 = pg.image.load("startButton1.png")
settingButton = pg.image.load("settingButton.png")
settingButton1 = pg.image.load("settingButton1.png")
quitButton = pg.image.load("quitButton.png")
quitButton1 = pg.image.load("quitButton1.png")
picOfClosedScroll = pg.image.load("closedScroll.png")
openScrolls = [pg.image.load("openScrollCpp.png"), pg.image.load("openScrollCsharp.png"), pg.image.load("openScrollCss.png"), pg.image.load("openScrollHTML.png"), pg.image.load("openScrollJs.png"), pg.image.load("openScrollPython.png")]

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