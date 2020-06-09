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

textColor = (238, 238, 238)

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

def TextMark():
    Text = "Mark: Hey Guys"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def TextMark1():
    Text = "Mark: I'm gonna run protocol!"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def TextMark2():
    Text = "Mark: Wait where is my computer???"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def TextElev():
    Text= "Emil: Haha you can't run protocol!"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def TextElev1():
    Text= "Emil: Hey everyone!!! We can just go!!!"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def TextElev2():
    Text= "Emil: Haha loser!!!"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def TextElev3():
    Text= "Everyone: HAHAHHAHAHA!"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def TextMark3():
    Text = "Mark: Ohhh..."
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def jijitalk0():
    Text = "Jiji: Ohh hi Mark!"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def jijitalk1():
    Text = "Jiji: Normally this would be the"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 920)
    win.blit(textSetting, textRect)

def jijitalk11():
    Text = "the beginning of an amazing adventure"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 1000)
    win.blit(textSetting, textRect)

def jijitalk2():
    Text = "Jiji: I would give you a quest that"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 920)
    win.blit(textSetting, textRect)

def jijitalk21():
    Text = "would lead to hours of amazing gameplay"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 1000)
    win.blit(textSetting, textRect)

def jijitalk3():
    Text = "Jiji: But this is the end of the demo"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 960)
    win.blit(textSetting, textRect)

def jijitalk4():
    Text = "Jiji: Well done! "
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 920)
    win.blit(textSetting, textRect)

def jijitalk41():
    Text = "See you in the full release!"
    textSetting = font.render(Text, run, black1, textColor)
    textRect = textSetting.get_rect()
    textRect.center = (960, 1000)
    win.blit(textSetting, textRect)