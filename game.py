import pygame
from objects import number
from constants import *
from functions import *
from gui import *

def main(screen, board):
    solved = [True]
    frames = [0]
    mode = [0]
    button = [True]
    intro(screen, board, solved, frames, mode, button)
    game_loop(screen, board, solved, frames, mode, button)

if __name__ == '__main__':
    pygame.init()
    screen_width = 800
    screen_height = 600
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    board_sudoku = board
    main(screen, board_sudoku)