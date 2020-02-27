import pygame as pg
win = pg.display.set_mode((0,0), pg.FULLSCREEN)
run = True
pg.init()
font = pg.font.Font("freesansbold.ttf", 64)
black1 = (0, 0, 0)
white1 = (255, 255, 255)
black2 = (0, 0, 0)
white2 = (255, 255, 255)
black3 = (0, 0, 0)
white3 = (255, 255, 255)
black4 = (0, 0, 0)
white4 = (255, 255, 255)
resTal = 1

def menuTekst1():
    font = pg.font.Font("freesansbold.ttf", 64)
    textMenu1 = font.render("Start", run, black1, white1)
    textRect = textMenu1.get_rect()
    textRect.center = (960, 540)
    win.blit(textMenu1, textRect)

def menuTekst2():
    black = (0, 0, 0)
    white = (255, 255, 255)
    font = pg.font.Font("freesansbold.ttf", 64)
    textMenu2 = font.render("Settings", run, black2, white2)
    textRect = textMenu2.get_rect()
    textRect.center = (960, 740)
    win.blit(textMenu2, textRect)

def menuTekst3():
    font = pg.font.Font("freesansbold.ttf", 64)
    textMenu3 = font.render("Quit", run, black3, white3)
    textRect = textMenu3.get_rect()
    textRect.center = (960, 940)
    win.blit(textMenu3, textRect)

def changeRes():
    textRes = "<= Resolution : 1920x1080"
    textSetting = font.render(textRes, run, black4, white4)
    textRect = textSetting.get_rect()
    textRect.center = (960, 540)
    win.blit(textSetting, textRect)

def changeRes1():
    textRes1 = "<= Resolution : 1600x900 =>"
    textSetting = font.render(textRes1, run, black4, white4)
    textRect = textSetting.get_rect()
    textRect.center = (960, 540)
    win.blit(textSetting, textRect)

def changeRes2():
    textRes2 = "<= Resolution : 1366x768 =>"
    textSetting = font.render(textRes2, run, black4, white4)
    textRect = textSetting.get_rect()
    textRect.center = (960, 540)
    win.blit(textSetting, textRect)

def changeRes3():
    textRes3 = "<= Resolution : 1280x720 =>"
    textSetting = font.render(textRes3, run, black4, white4)
    textRect = textSetting.get_rect()
    textRect.center = (960, 540)
    win.blit(textSetting, textRect)

def changeRes4():
    textRes4 = "Resolution : 1024x576 =>"
    textSetting = font.render(textRes4, run, black4, white4)
    textRect = textSetting.get_rect()
    textRect.center = (960, 540)
    win.blit(textSetting, textRect)