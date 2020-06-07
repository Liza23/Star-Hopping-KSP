import pygame, sys
from random import randrange
from pygame.locals import *
from ctypes import c_int, WINFUNCTYPE, windll
from ctypes.wintypes import HWND, LPCSTR, UINT

def MessageBox(title, text, style):
    return windll.user32.MessageBoxW(0, text, title, style)

pygame.init()
screen_x = 500
screen_y = 500

win = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Minesweeper")
surfObj = pygame.display.set_mode((170, 200))

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

#image_load
block = pygame.image.load("sprites/block.png")
one = pygame.image.load("sprites/one.png")
two = pygame.image.load("sprites/two.png")
three = pygame.image.load("sprites/three.png")
four = pygame.image.load("sprites/four.png")
five = pygame.image.load("sprites/five.png")
six = pygame.image.load("sprites/six.png")
seven = pygame.image.load("sprites/seven.png")
eight = pygame.image.load("sprites/eight.png")
empty = pygame.image.load("sprites/empty.png")
flag = pygame.image.load("sprites/flagged.png")
mine = pygame.image.load("sprites/mine.png")

boxes = []
numBombs = 0

class box():
	#flag = -3 # -3 = NO FLAG; -2 = FLAGGED; -1 = ?; 0 = BLANK; 1-8 = WARN; 9 = Exploded
	isbomb = False
	index = 0
	x = 0 
	y = 0
	def __init__(self, boxPos):
		self.box_P = boxPos
		self.flag = -3

refBlock = box((Rect(-100, -100, 0, 0)))
refBlock.x = -10
refBlock.y = -10
selBlock = refBlock

def drawBox():
	pygame.draw.line(surfObj, black, (10, 10), (160, 10))
	pygame.draw.line(surfObj, black, (160, 10), (160, 160))
	pygame.draw.line(surfObj, black, (160, 160), (10, 160))
	pygame.draw.line(surfObj, black, (10, 160), (10, 10))


drawBox()

def drawBoxesInit():
	for x in range(0, 9):
		for y in range(0, 9):
			bo = box(Rect(x*17+10, y*17+10, 17, 17))
			bo.index = len(boxes)
			print(bo.index)
			bo.x = x
			bo.y = y
			boxes.append(bo)
			surfObj.blit(block, (x*17 + 10, y*17 + 10))

drawBoxesInit()
