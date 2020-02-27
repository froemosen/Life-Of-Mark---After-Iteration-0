import Tekst
import pygame as pg
import time
x = 1920
y = 1080
clock = pg.time.Clock()
tick = pg.time.get_ticks()
bg = pg.image.load("Baggrund.png")
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
startButton = pg.image.load("startButton.png")
settingButton = pg.image.load("settingButton.png")
quitButton = pg.image.load("quitButton.png")

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

def drawWorld():
        win.blit(bg, (0,0))
        buttons.drawStart()
        buttons.drawSetting()
        buttons.drawQuit()

def startSettings():
    run = True
    while run:
        keys = pg.key.get_pressed()
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run = False

def pygameMenuStart():
    import Game
    pg.init()
    run = True
    point = 1
    while run:
        mx, my = pg.mouse.get_pos()
        clock.tick(40)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if mx > 850 and mx < 1070 and my > 520 and my < 560:
                    Game.start()
                if mx > 785 and mx < 1150 and my > 720 and my < 765:
                    startSettings()
                if mx > 880 and mx < 1035 and my > 930 and my < 965:
                    pg.quit()
        if mx > 850 and mx < 1070 and my > 520 and my < 560:
            pass #Animations der indikerer at bruger er over feltet
        if mx > 785 and mx < 1150 and my > 720 and my < 765:
            pass #Animations der indikerer at bruger er over feltet
        if mx > 880 and mx < 1035 and my > 930 and my < 965:
            pass #Animations der indikerer at bruger er over feltet
        drawWorld()
        pg.display.update()
buttons = buttons(720, 440, 710, 640, 700, 840, 900, 900)
pygameMenuStart()