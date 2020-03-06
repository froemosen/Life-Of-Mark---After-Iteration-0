import Tekst
import pygame as pg
import time
import random as r
x = 1920
y = 1080
pg.mixer.init(frequency=44100, size=-16, channels=6, buffer=4096)
clock = pg.time.Clock()
tick = pg.time.get_ticks()
bg = pg.image.load("Baggrund.png")
bg1 = pg.image.load("baggrund1.png")
win = pg.display.set_mode((x,y), pg.FULLSCREEN)
pg.display.set_caption("Life of Mark episode 1 - The List")
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)
select = pg.mixer.Sound("selectMenu.wav")
startButton = pg.image.load("startButton.png")
startButton1 = pg.image.load("startButton1.png")
settingButton = pg.image.load("settingButton.png")
settingButton1 = pg.image.load("settingButton1.png")
quitButton = pg.image.load("quitButton.png")
quitButton1 = pg.image.load("quitButton1.png")
picOfClosedScroll = pg.image.load("closedScroll.png")
openScrolls = [pg.image.load("openScrollCpp.png"), pg.image.load("openScrollCsharp.png"), pg.image.load("openScrollCss.png"), pg.image.load("openScrollHTML.png"), pg.image.load("openScrollJs.png"), pg.image.load("openScrollPython.png")]

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
        mx, my = pg.mouse.get_pos()
        win.blit(bg, (0,0))
        buttons.drawStart()
        buttons.drawSetting()
        buttons.drawQuit()
        closedScroll.drawClosedScroll1()
        closedScroll.drawClosedScroll2()
        closedScroll.drawClosedScroll3()
        if mx > 850 and mx < 1070 and my > 520 and my < 560:
            win.blit(bg, (0,0))
            closedScroll.drawClosedScroll2()
            closedScroll.drawClosedScroll3()
            buttons.drawStart()
            buttons.drawSetting()
            buttons.drawQuit()

        if mx > 785 and mx < 1150 and my > 720 and my < 765:
            win.blit(bg, (0,0))
            closedScroll.drawClosedScroll1()
            closedScroll.drawClosedScroll3()
            buttons.drawStart()
            buttons.drawSetting()
            buttons.drawQuit()

        if mx > 880 and mx < 1035 and my > 930 and my < 965:
            win.blit(bg, (0,0))
            closedScroll.drawClosedScroll1()
            closedScroll.drawClosedScroll2()
            buttons.drawStart()
            buttons.drawSetting()
            buttons.drawQuit()

        if mx > 850 and mx < 1070 and my > 520 and my < 560:
            scrolls.drawMouseOverStart()
            win.blit(icon, (783, 480))
            win.blit(startButton1, (720, 440))
            if pg.mixer.Channel(1).get_busy() == False:
                pg.mixer.Channel(1).play(select)

        if mx > 785 and mx < 1150 and my > 720 and my < 765:
            scrolls.drawMouseOverSetting()
            win.blit(settingButton1, (710, 640))
            if pg.mixer.Channel(2).get_busy() == False:
                pg.mixer.Channel(2).play(select)
                
        if mx > 880 and mx < 1035 and my > 930 and my < 965:
            scrolls.drawMouseOverQuit()
            win.blit(quitButton1, (700, 840))
            if pg.mixer.Channel(3).get_busy() == False:
                pg.mixer.Channel(3).play(select)




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
    pg.mixer.music.load("MainMenuMusic.mp3")
    pg.mixer.music.set_volume(0.3)
    pg.mixer.music.play(-1)
    run = True
    while run:
        mx, my = pg.mouse.get_pos()
        clock.tick(40)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if mx > 850 and mx < 1070 and my > 520 and my < 560:
                    pg.mixer.music.fadeout(1500)
                    Game.start()
                if mx > 785 and mx < 1150 and my > 720 and my < 765:
                    startSettings()
                if mx > 880 and mx < 1035 and my > 930 and my < 965:
                    run = False
                    pg.quit()
        drawWorld()
        pg.display.update()
scrolls = scrolls(750, 490, 1075, 490, 690, 690, 1140, 690, 785, 890, 1035, 890)
closedScroll = closedScroll(750, 490, 1080, 490, 685, 690, 1150, 690, 770, 890, 1045, 890)
buttons = buttons(720, 440, 710, 640, 700, 840, 900, 900)
pygameMenuStart()