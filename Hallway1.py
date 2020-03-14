import Game
import Tekst
import pygame as pg
import pygame.mixer
import time
import random as r

x = 1920 #ResX
y = 1080 #ResY
fps = 60 #Frames per second
volume = 0.03 #Lydstyrke
pg.init()
pg.font.init()
pg.mixer.music.set_volume(volume)
sange = ["Violin_Background.mp3", "kindahipandoldsong.mp3", "EmotionalJegGuess.mp3"]
bg = pg.image.load("")
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
table1 = pg.image.load("table1.png")
walkSound = pg.mixer.Sound("walksound.wav")

