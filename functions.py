import random
import pygame
import time

pygame.init()

green = (50, 175, 50)
congrats = pygame.font.Font('freesansbold.ttf', 40)
party = pygame.image.load('party.png')
party = pygame.transform.scale(party, (150, 150))


def draw_rect(screen, x, y, width, height, color):
   pygame.draw.rect(screen, color, [x, y, width, height])

def wish(screen, val, string):
    for i in range(2000):
        screen.fill((255, 255, 255))
        txt = congrats.render(string, True, (255, 0, 0))
        screen.blit(txt, ((800-txt.get_width())/2, 50))
        if(val):
            txt = congrats.render("New Best Time", True, (255, 0, 0))
            screen.blit(txt, ((800-txt.get_width())/2, 150))
        txt = congrats.render("! Congratulations !", True, green)
        screen.blit(txt, ((800-txt.get_width())/2, (600-txt.get_height())/2)) 
        screen.blit(party, (50, 225))
        screen.blit(party, (600, 225))

        pygame.display.update()

def get_wrong(mat):
    store = []
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if(j != k and mat[i][j].value == mat[i][k].value and mat[i][j].value != 0):
                    store.append([i, j])
            for k in range(9):
                if(i != k and mat[i][j].value == mat[k][j].value and mat[i][j].value != 0):
                    store.append([i, j])
            r = int(i/3)*3
            c = int(j/3)*3

            for p in range(r, r+3):
                for q in range(c, c+3):
                    if not(p == i and q == j):
                        if(mat[p][q].value == mat[i][j].value and mat[i][j].value != 0):
                            store.append([i, j])

    return store

def get_count(mat):
    count = 0
    for i in range(9):
        for j in range(9):
            if(mat[i][j].value != 0):
                count += 1

    return count

def find_pos(mat, l):
    for i in range(9):
        for j in range(9):
            if(mat[i][j].value == 0):
                l.append(i)
                l.append(j)
                return True
    
    return False

def check_avail(mat, l, x):
    r = l[0]
    c = l[1]

    for i in range(9):
        if(mat[r][i].value == x):
            return False

    for i in range(9):
        if(mat[i][c].value == x):
            return False
        
    row = int(r/3)*3
    col = int(c/3)*3
    
    for i in range(row, row+3):
        for j in range(col, col+3):
            if(mat[i][j].value == x):
                return False

    return True


def solve(mat):
    l = []
    if(not find_pos(mat, l)):
        return True
    
    for i in range(1, 10):
        if(check_avail(mat, l, i)):
            mat[l[0]][l[1]].value = i
            if(solve(mat)):
                return True
            
            mat[l[0]][l[1]].value = 0

    return False

def generate_grid(mat, boxes = 40):
    beg = 0

    for k in range(3):
        for i in range(beg, beg+3):
            for j in range(beg, beg+3):
                while True:
                    val = random.randint(1,9)
                    if(check_avail(mat, [i, j], val)):
                        mat[i][j].value = val
                        break
        beg += 3

    if(solve(mat)):
        for i in range(boxes):
            val = random.randint(0, 80)
            mat[int(val/9)][val%9].fixed = "yes"

    clear(mat)

def regenerate(mat, boxes = 40):
    blank(mat)
    
    generate_grid(mat, boxes)
    
    
def clear(mat):
    for i in range(9):
        for j in range(9):
            if(mat[i][j].fixed == "no"):
                mat[i][j].value = 0

def blank(mat):
    for i in range(9):
        for j in range(9):
            mat[i][j].value = 0
            mat[i][j].fixed = "no"