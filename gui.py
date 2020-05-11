import pygame
import csv
from functions import *
from objects import number
from constants import *
from image_processing import *
pygame.init()

clock = pygame.time.Clock()

def game_loop(screen, board, solved, frames, mode, button):
    active_X = 0
    active_Y = 0
    run = True
    fail = False
    intensity = 255
    gb = 0
    t = 0
    highest = 0
    store = []
    solved[0] = True
    frames[0] = 0
    button[0] = True
    click = pygame.mouse.get_pressed()
    while run:
        if(button[0]):
            frames[0] += 1
        screen.fill((0, 100, 150))
        prev_click = click
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()        
        button_X = 0
        button_Y = 0

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                
                if event.key == pygame.K_DOWN:
                    board[active_X][active_Y].type = "normal"
                    if(active_X < 8):
                        active_X += 1
                    else:
                        active_X = 0
                    board[active_X][active_Y].type = "active"
                    
                
                if event.key == pygame.K_UP:
                    board[active_X][active_Y].type = "normal"
                    if(active_X > 0):
                        active_X -= 1
                    else:
                        active_X = 8
                    board[active_X][active_Y].type = "active"
                
                if event.key == pygame.K_RIGHT:
                    board[active_X][active_Y].type = "normal"
                    if(active_Y < 8):
                        active_Y += 1
                    else:
                        active_Y = 0
                    board[active_X][active_Y].type = "active"
                
                if event.key == pygame.K_LEFT:
                    board[active_X][active_Y].type = "normal"
                    if(active_Y > 0):
                        active_Y -= 1
                    else:
                        active_Y = 8
                    board[active_X][active_Y].type = "active"

                if event.key == pygame.K_SPACE:
                    button[0] = not button[0]

                if event.key == pygame.K_0 or event.key == pygame.K_KP0 or event.key == pygame.K_DELETE:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 0
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    button[0] = True
                    if(board[active_X][active_Y].fixed == "no"):
                        board[active_X][active_Y].value = 9

                
        rel = get_wrong(board)
        for v in rel:
            i = v[0]
            j = v[1]
            X = start_X+(50+gap)*j+extra*int(j/3)
            Y = start_Y+(50+gap)*i+extra*int(i/3)
            draw_rect(screen, X-2, Y-2, 54, 54, red)  

        for i in range(9):
            for j in range(9):
                colour = white
                X = start_X+(50+gap)*j+extra*int(j/3)
                Y = start_Y+(50+gap)*i+extra*int(i/3)
                if(board[i][j].type == "active"):
                    colour = dark_grey
                elif(board[i][j].fixed == "yes"):
                    colour = grey
                draw_rect(screen, X, Y, 50, 50, colour)
                if(board[i][j].value != 0):
                    text = text_font.render(str(board[i][j].value), True, black)
                    text = pygame.transform.scale(text, (30, 40))
                    screen.blit(text, (X+10, Y+5))

        for i in range(9):
            for j in range(9):
                X = start_X+(50+gap)*j+extra*int(j/3)
                Y = start_Y+(50+gap)*i+extra*int(i/3)
                if(X < mouse[0] < X+50 and Y < mouse[1] < Y+50):
                    if(click[0] == 1):
                        board[active_X][active_Y].type = "normal"
                        active_X = i
                        active_Y = j
                        board[active_X][active_Y].type = "active"

        if(mode[0] < 4):
            mode_text = mode_font.render(modes[mode[0]], True, white)
            screen.blit(mode_text, ((800-mode_text.get_width())/2, 5))            

            button_X = (800+mode_text.get_width())/2+15
            button_Y = 5

            if(button_X-2.5 <= mouse[0] <= button_X+30 and button_Y-2.5 <= mouse[1] <= button_Y+30):
                draw_rect(screen, button_X-2.5, button_Y-2.5, 30, 30, white)
                if(click[0] == 1 and prev_click[0] == 0):
                    button[0] = not button[0]

            if(button[0]):
                screen.blit(play, (button_X, button_Y))
            else:
                screen.blit(pause, (button_X, button_Y))

            csvfile=open('scores.csv','r', newline='')
            obj=csv.reader(csvfile)
            for row in obj:
                store = row

            highest = int(store[mode[0]])

            best = highest
            hr = int(best/3600)
            best %= 3600
            mn = int(best/60)
            sec = int(best%60)
            string = "Best : "
            if(int(hr/10) == 0):
                string += "0"
            string = string + str(hr) + ":"
            if(int(mn/10) == 0):
                string += "0"
            string = string + str(mn) + ":"
            if(int(sec/10) == 0):
                string += "0"
            string = string + str(sec)

            text = mode_font.render(string, True, white)
            screen.blit(text, (5, 5))


            t = int(frames[0]/100)
            time = t
            hr = int(time/3600)
            time %= 3600
            mn = int(time/60)
            sec = int(time%60)
            string = "Time : "
            if(int(hr/10) == 0):
                string += "0"
            string = string + str(hr) + ":"
            if(int(mn/10) == 0):
                string += "0"
            string = string + str(mn) + ":"
            if(int(sec/10) == 0):
                string += "0"
            string = string + str(sec)

            if(solved[0] == True):
                text = mode_font.render(string, True, white)
                screen.blit(text, (800-text.get_width()-5, 5))
        

        if(580 < mouse[0] < 780 and 470 < mouse[1] < 570):
            draw_rect(screen, 580, 470, 200, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                exit()
        else:        
            draw_rect(screen, 580, 470, 200, 100, pink)
        text = large_font.render("Exit", True, black)
        screen.blit(text, (580+(200-text.get_width())/2, 470 + (100-text.get_height())/2))

        if(580 < mouse[0] < 780 and 330 < mouse[1] < 430):
            draw_rect(screen, 580, 330, 200, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                intro(screen, board, solved, frames, mode, button)
        else:
            draw_rect(screen, 580, 330, 200, 100, pink)
        text = large_font.render("New", True, black)
        screen.blit(text, (580+(200-text.get_width())/2, 330 + (100-text.get_height())/2))

        if(580 < mouse[0] < 780 and 50 < mouse[1] < 150):
            draw_rect(screen, 580, 50, 200, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                clear(board)
        else:                
            draw_rect(screen, 580, 50, 200, 100, pink)
        text = large_font.render("Clear", True, black)
        screen.blit(text, (580+(200-text.get_width())/2, 50 + (100-text.get_height())/2))

        if(580 < mouse[0] < 780 and 190 < mouse[1] < 290):
            draw_rect(screen, 580, 190, 200, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                if(len(rel) > 0):
                    fail = True
                elif(solve(board) == False):
                    fail = True
                else:
                    solved[0] = False
        else:
            draw_rect(screen, 580, 190, 200, 100, pink)
        text = large_font.render("Solve", True, black)
        screen.blit(text, (580+(200-text.get_width())/2, 190 + (100-text.get_height())/2))


        if(fail):
            screen.fill(white)
            text = large_font.render("Unsolvable at this moment", True, (intensity, gb, gb))
            screen.blit(text, ((800-text.get_width())/2, (600-text.get_height())/2-50))
            text = large_font.render("clear the board first", True, (intensity, gb, gb))
            screen.blit(text, ((800-text.get_width())/2, (600-text.get_height())/2+50))
            intensity -= 1
            if(intensity%5 == 0):
                gb += 3
            if(intensity < 100):
                intensity = 250
                gb = 0
                fail = False

        if(len(rel) == 0 and get_count(board) == 81):
            val = False
            if(solved[0] == True):
                if(mode[0] < 4):
                    if(t < highest):
                        val = True
                        store[mode[0]] = str(time)
                        csv_file = open('scores.csv', 'w', newline = '')
                        obj = csv.writer(csv_file)
                        obj.writerow(store)
                
                if(mode[0] >= 4):
                    string = ""
                wish(screen, val, string)
                intro(screen, board, solved, frames, mode, button)
                
        clock.tick(100)
        pygame.display.update()

def intro(screen, board, solved, frames, mode, button):
    solved[0] = True
    frames[0] = 0
    button[0] = True
    click = pygame.mouse.get_pressed()

    while True:
        screen.fill((0, 100, 150))
        mouse = pygame.mouse.get_pos()
        prev_click = click
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        if(50 < mouse[0] < 350 and 75 < mouse[1] < 175):
            draw_rect(screen, 50, 75, 300, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                regenerate(board, 80)
                mode[0] = 0
                return
        else:
            draw_rect(screen, 50, 75, 300, 100, pink)

        if(450 < mouse[0] < 750 and 75 < mouse[1] < 175):
            draw_rect(screen, 450, 75, 300, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                regenerate(board, 35)
                mode[0] = 1
                return
        else:
            draw_rect(screen, 450, 75, 300, 100, pink)

        if(50 < mouse[0] < 350 and 250 < mouse[1] < 350):
            draw_rect(screen, 50, 250, 300, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                regenerate(board, 25)
                mode[0] = 2
                return
        else:
            draw_rect(screen, 50, 250, 300, 100, pink)

        if(450 < mouse[0] < 750 and 250 < mouse[1] < 350):
            draw_rect(screen, 450, 250, 300, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                regenerate(board, 15)
                mode[0] = 3
                return
        else:
            draw_rect(screen, 450, 250, 300, 100, pink)

        if(50 < mouse[0] < 350 and 425 < mouse[1] < 525):
            draw_rect(screen, 50, 425, 300, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                blank(board)
                mode[0] = 4
                return
        else:
            draw_rect(screen, 50, 425, 300, 100, pink)

        if(450 < mouse[0] < 750 and 425 < mouse[1] < 525):
            draw_rect(screen, 450, 425, 300, 100, magenta)
            if(click[0] == 1 and prev_click[0] == 0):
                mode[0] = 5
                choose_file(screen, board)
                return
        else:
            draw_rect(screen, 450, 425, 300, 100, pink)

        text = large_font.render("Easy", True, black)
        screen.blit(text, (50 + (300-text.get_width())/2, 75 + (100-text.get_height())/2))
        text = large_font.render("Moderate", True, black)
        screen.blit(text, (450 + (300-text.get_width())/2, 75 + (100-text.get_height())/2))
        text = large_font.render("Hard", True, black)
        screen.blit(text, (50 + (300-text.get_width())/2, 250 + (100-text.get_height())/2))
        text = large_font.render("Expert", True, black)
        screen.blit(text, (450 + (300-text.get_width())/2, 250 + (100-text.get_height())/2))
        text = large_font.render("Custom", True, black)
        screen.blit(text, (50 + (300-text.get_width())/2, 425 + (100-text.get_height())/2))
        text = large_font.render("Image", True, black)
        screen.blit(text, (450 + (300-text.get_width())/2, 425 + (100-text.get_height())/2))
        
        pygame.display.update()
