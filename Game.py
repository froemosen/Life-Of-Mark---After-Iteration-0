import Tekst
import pygame as pg
from playsound import playsound
import pygame.mixer
x = 1920
y = 1080
fps = 60
#Er der for settings
pg.init()
pg.font.init()


bg = pg.image.load("Classroom(1.0).png")
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
clock = pg.time.Clock()
markStandLeft = pg.image.load("gåVenstre1.png")
markStandRight = pg.image.load("gåHøjre1.png")
markStandUp = pg.image.load("gåOp3.png")
markStandDown = pg.image.load("gåNed1.png")
markStand = pg.image.load("gåNed1.png")
markWalkUp = [pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png")]
markWalkLeft = [pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png"), pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png"), pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png")]
markWalkRight = [pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png"), pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png"), pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png")]
markWalkDown = [pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png"), pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png"), pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png")]
textBox = pg.image.load("textFrame.png")
table1 = pg.image.load("Table.png")
#Alle backgorund og sprites skal sorteres

def start():
    import Menu
    class smark(object):
        def  __init__(self, x, y, height, width):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.vel = 10
            self.walkCount = 1
            self.stand = True
            self.walkDown = False
            self.walkUp = False
            self.walkRight = False
            self.walkLeft = False
            self.walkSound = pg.mixer.Sound("walksound.wav")

        def draw(self, win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if not(self.stand):
                if self.walkDown:
                    win.blit(markWalkDown[self.walkCount // 3], (self.x, self.y))
                    #self.walkSound.play()
                    self.walkCount += 1
                elif self.walkUp:
                    win.blit(markWalkUp[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.walkRight:
                    win.blit(markWalkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.walkLeft:
                    win.blit(markWalkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.walkDown:
                    win.blit(markStandDown, (self.x, self.y))
                elif self.walkUp:
                    win.blit(markStandUp, (self.x, self.y))
                elif self.walkRight:
                    win.blit(markStandRight, (self.x, self.y))
                elif self.walkLeft:
                    win.blit(markStandLeft, (self.x, self.y))
                else:
                    win.blit(markStand, (self.x, self.y)) 
            
                


    class allPlayerText(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def tekst(self, win):
            win.blit(textBox, (self.x, self.y))
#Alle classes inde i en seperat fill...

    def drawWorld():
        win.blit(bg, (0,0))
        win.blit(table1, (56,250))
        smark.draw(win)
        allPlayerText.tekst(win)
        pg.display.update()

    run = True
    smark = smark(50, 780, 50, 50)
    allPlayerText = allPlayerText(100, 920)
    while run:
        keys = pg.key.get_pressed()
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                Menu.pygameMenuStart()
        
        if keys[pg.K_a]:
            smark.x -= smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = True
            smark.stand = False
        elif keys[pg.K_d]:
            smark.x += smark.vel
            smark.walkDown = False
            smark.walkUp = False
            smark.walkRight = True
            smark.walkLeft = False
            smark.stand = False
        elif keys[pg.K_s]:
            smark.y += smark.vel
            smark.walkDown = True
            smark.walkUp = False
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
        elif keys[pg.K_w]:
            smark.y -= smark.vel
            smark.walkDown = False
            smark.walkUp = True
            smark.walkRight = False
            smark.walkLeft = False
            smark.stand = False
        else:
            smark.stand = True
            smark.walkCount = 0
        if keys[pg.K_ESCAPE]:
            Menu.pygameMenuStart()
        drawWorld()
    pg.quit()
start()