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
markStåV = pg.image.load("gåVenstre1.png")
markStåH = pg.image.load("gåHøjre1.png")
markStåO = pg.image.load("gåOp3.png")
markStåN = pg.image.load("gåNed1.png")
markStå = pg.image.load("gåNed1.png")
markGåOp = [pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp2.png"), pg.image.load("gåOp3.png"), pg.image.load("gåOp4.png")]
markGåVenstre = [pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png"), pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png"), pg.image.load("gåVenstre1.png"), pg.image.load("gåVenstre2.png"), pg.image.load("gåVenstre3.png"), pg.image.load("gåVenstre4.png")]
markGåHøjre = [pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png"), pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png"), pg.image.load("gåHøjre1.png"), pg.image.load("gåHøjre2.png"), pg.image.load("gåHøjre3.png"), pg.image.load("gåHøjre4.png")]
markGåNed = [pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png"), pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png"), pg.image.load("gåNed1.png"), pg.image.load("gåNed2.png"), pg.image.load("gåNed3.png"), pg.image.load("gåNed4.png")]
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
            self.gåtal = 1
            self.stå = True
            self.gåNed = False
            self.gåOp = False
            self.gåHøjre = False
            self.gåVenstre = False

        def draw(self, win):
            if self.gåtal + 1 >= 27:
                self.gåtal = 0

            if not(self.stå):
                if self.gåNed:
                    win.blit(markGåNed[self.gåtal // 3], (self.x, self.y))
                    self.gåtal += 1
                elif self.gåOp:
                    win.blit(markGåOp[self.gåtal // 3], (self.x, self.y))
                    self.gåtal += 1
                elif self.gåHøjre:
                    win.blit(markGåHøjre[self.gåtal // 3], (self.x, self.y))
                    self.gåtal += 1
                elif self.gåVenstre:
                    win.blit(markGåVenstre[self.gåtal // 3], (self.x, self.y))
                    self.gåtal += 1
            else:
                if self.gåNed:
                    win.blit(markStåN, (self.x, self.y))
                elif self.gåOp:
                    win.blit(markStåO, (self.x, self.y))
                elif self.gåHøjre:
                    win.blit(markStåH, (self.x, self.y))
                elif self.gåVenstre:
                    win.blit(markStåV, (self.x, self.y))
                else:
                    win.blit(markStåN, (self.x, self.y)) 

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
            smark.gåNed = False
            smark.gåOp = False
            smark.gåHøjre = False
            smark.gåVenstre = True
            smark.stå = False
        elif keys[pg.K_d]:
            smark.x += smark.vel
            smark.gåNed = False
            smark.gåOp = False
            smark.gåHøjre = True
            smark.gåVenstre = False
            smark.stå = False
        elif keys[pg.K_s]:
            smark.y += smark.vel
            smark.gåNed = True
            smark.gåOp = False
            smark.gåHøjre = False
            smark.gåVenstre = False
            smark.stå = False
        elif keys[pg.K_w]:
            smark.y -= smark.vel
            smark.gåNed = False
            smark.gåOp = True
            smark.gåHøjre = False
            smark.gåVenstre = False
            smark.stå = False
        else:
            smark.stå = True
            smark.gåtal = 0
        drawWorld()
    pg.quit()
start()
