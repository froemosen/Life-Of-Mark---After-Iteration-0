import Tekst
import pygame as pg
import time
import random as r
import Classes
import Game
from saveFile1 import *
import Hallway2, Hallway3
import cutscene1

x = 1920
y = 1080
#For settings

pg.mixer.init(frequency=44100, size=-16, channels=6, buffer=4096) #nobet lyd

clock = pg.time.Clock()
tick = pg.time.get_ticks()

bg = pg.image.load("assets/menu/Baggrund.png") #loader grafik til baggrund
bg1 = pg.image.load("assets/menu/baggrund1.png") #loader grafik til anden baggrund

win = pg.display.set_mode((x,y), pg.FULLSCREEN)
pg.display.set_caption("Life of Mark episode 1 - The List") #window title

icon = pg.image.load("assets/icon.png") #Loader window billede
pg.display.set_icon(icon) #ligger window bilede oppe i hjørnet
select = pg.mixer.Sound("assets/lyd/selectMenu.wav") #loader lyd
scrolls = Classes.scrolls(750, 490, 1075, 490, 690, 690, 1140, 690, 785, 890, 1035, 890) #Alle opne scrolls x og y pos
closedScroll = Classes.closedScroll(750, 490, 1080, 490, 685, 690, 1150, 690, 770, 890, 1045, 890) #Alle lukket scrolls x og y pos
buttons = Classes.buttons(720, 440, 710, 640, 700, 840, 900, 900) #Alle knappers x og y pos
startButton1 = Classes.startButton1 #"import" af startButton1
settingButton1 = Classes.settingButton1 #"import" af settingsButton1
quitButton1 = Classes.quitButton1 #"import" af quitButton1

def drawWorld(baggrundValg):
        mx, my = pg.mouse.get_pos()
        if  baggrundValg >= 1 and baggrundValg <= 20:
            win.blit(bg1, (0,0))
        elif baggrundValg >= 31 and baggrundValg <= 60:
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
    pg.mouse.set_visible(True)
    pg.init()
    pg.mixer.music.load("assets/lyd/MainMenuMusic.mp3") #loader mainMenuMusic
    pg.mixer.music.set_volume(0.3) #lydstyrken
    pg.mixer.music.play(-1) #hvor mange gange musikken skal spille (-1 = bliver ved)
    baggrundValg = 21 #Startvariabel for tilfældig baggrunds-valg
    run = True
    while run:
        mx, my = pg.mouse.get_pos()
        clock.tick(60)
        baggrundValg += 1

        if baggrundValg > 61:
            baggrundValg = r.randint(1, 40)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if mx > 850 and mx < 1070 and my > 520 and my < 560:
                    pg.mixer.music.fadeout(1500)
                    if scene == 0:
                        cutscene1.start()
                    elif scene == 1:
                        pg.mouse.set_visible(False)
                        Game.start()
                    elif scene == 2:
                        pg.mouse.set_visible(False)
                        Hallway2.start()
                    elif scene == 3:
                        pg.mouse.set_visible(False)
                        Hallway3.start()
                if mx > 785 and mx < 1150 and my > 720 and my < 765:
                    startSettings()
                if mx > 880 and mx < 1035 and my > 930 and my < 965:
                    run = False
                    pg.quit()
        drawWorld(baggrundValg) #Tegner verden
        pg.display.update()