from PIL import Image, ImageFilter
import tkinter as tk
from tkinter import filedialog
import pytesseract
import numpy as np 
import cv2
import pygame
from functions import blank, congrats, green
from objects import number

def choose_file(screen, board):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg',), ("Image File", '.jpeg'), ("Image File", '.png')])

    txt = congrats.render("Wait ...", True, green)
    screen.fill((255, 255, 255))
    screen.blit(txt, ((800-txt.get_width())/2, (600-txt.get_height())/2))
    pygame.display.update()

    grid_detection(file_path, board)

def grid_detection(file_path, board):
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    edged = cv2.Canny(gray, 30, 200) 
    
    contours, hierarchy = cv2.findContours(edged,  
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    mx = contours[0]
    ar = -1
    for contour in contours:
        area = cv2.contourArea(contour)
        
        if area > ar:        
            ar = area
            mx = contour

    x, y, width, height = cv2.boundingRect(mx)
    roi = img[y:y+height, x:x+width]

    img = cv2.resize(roi, (800, 800))
    ret, grey = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    edge = cv2.Canny(grey, 50, 150, apertureSize = 3)

    lines = cv2.HoughLines(edge, 1, np.pi/180, 200)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho

        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*a)

        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*a)
        
        cv2.line(grey, (x1, y1), (x2, y2), (255, 255, 255), 5)

    img_height = grey.shape[1]
    h = int(img_height/9)

    img_width = grey.shape[0] 
    w = int(img_width/9)

    li = []

    beg = 0
    for i in range(9):
        li.append([])
        b = 0
        for j in range(9):
            im = grey[beg:beg+h, b:b+w]
            
            img = Image.fromarray(im)
            txt = pytesseract.image_to_string(img, lang='eng', \
                config='--psm 13 --oem 3 -c tessedit_char_whitelist=123456789 ')

            if(len(txt) > 1):
                li[i].append(int(txt)%10)
            elif(len(txt) == 0):
                li[i].append(0)
            else:
                li[i].append(int(txt))

            b += w

        beg += h
    
    write_grid(board, li)


def write_grid(board, li):
    wrong = []
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if(j != k and li[i][j] == li[i][k] and li[i][j] != 0):
                    wrong.append([i, j])
            for k in range(9):
                if(i != k and li[i][j] == li[k][j] and li[i][j] != 0):
                    wrong.append([i, j])
            r = int(i/3)*3
            c = int(j/3)*3

            for p in range(r, r+3):
                for q in range(c, c+3):
                    if not(p == i and q == j):
                        if(li[p][q] == li[i][j] and li[i][j] != 0):
                            wrong.append([i, j])

    for val in wrong:
        li[val[0]][val[1]] = 0

    blank(board)    

    for i in range(9):
        for j in range(9):
            board[i][j].value = li[i][j]
            if(li[i][j] != 0):
                board[i][j].fixed = "yes"