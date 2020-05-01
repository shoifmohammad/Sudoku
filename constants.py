import pygame
from objects import *

pygame.init()

# Basic Colours
black = (0, 0, 0)
white = (255, 255, 255)
grey = (200, 200, 200)
dark_grey = (100, 100, 100)
red = (255, 0, 0)
pink = (250, 50, 150)
magenta = (150, 0, 255)

modes = ["Easy", "Moderate", "Hard", "Expert"]
board = []
for i in range(9):
    board.append([])
    for j in range(9):
        num = number()
        board[i].append(num)

active_X = 0
active_Y = 0
board[active_X][active_Y].type = "active"
start_Y = 50
start_X = 30
gap = 7.5
extra = 7.5
text_font = pygame.font.Font('freesansbold.ttf', 50)
large_font = pygame.font.Font('freesansbold.ttf', 50)
mode_font = pygame.font.Font('freesansbold.ttf', 30)

play = pygame.image.load('pause.png')
play = pygame.transform.scale(play, (25, 25))
pause = pygame.image.load('play.png')
pause = pygame.transform.scale(pause, (25, 25))