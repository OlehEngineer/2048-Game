import pygame
import sys,random
import numpy as np
from logic import *

'''**************************************************************'''
BLOCKS = 4
SIZE = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE + (BLOCKS+1) * MARGIN
HEIGHT = WIDTH + 110
TITLE = pygame.Rect((0,0),(WIDTH,110))
WHITE = (255,255,255)
BLACK = (1,1,1)
GREEN = (0,181,26)  # RAL 6038 - color for WINNER message
RED = (255,42,27)    #RAL 3026 - color for lose massage
WIN = pygame.Rect((0,0),(200,100))
LOSE = pygame.Rect((0,0),(200,100))
winner_value = 2048
'''**************************************************************'''

current_grid = np.zeros((4,4))                                          # creating of empty matrix (zero matrix)

current_grid = grid_new_value(current_grid)                             # filling of the matrix with one random value 2 or 4

pygame.init()                                                           # initiation of PYGAME

screen = pygame.display.set_mode((WIDTH,HEIGHT))                        # create the main game window

pygame.display.set_caption("2048")                                      # create title of the game window

font = pygame.font.SysFont('arial', 48,bold=False,italic=False)         # creating a font in PYGAME for score infor

font_grid_cell = pygame.font.SysFont('arial', 56,bold=True,italic=False)# creating a font for cell's value




running = True

while running:                                                          #cycle which check if palyer close the window
    for even in pygame.event.get():
        
        if even.type == pygame.QUIT:
            pygame.quit
            sys.exit(0)


            
        '''creating a rectangle of cell and add appropriate value from the Grid matrix'''

        for row in range(BLOCKS):

            for colomn in range(BLOCKS):

                w = colomn * SIZE + (colomn + 1) * MARGIN
                h = row * SIZE + (row + 1) * MARGIN + 110

                cell_color = grid_cell_color(current_grid[row][colomn]) # choice a color for ppropriate cell depends of cell's value
                
                pygame.draw.rect(screen,cell_color,(w,h,110,110))       # draw the appropriate cell
                
                grid_value = font_grid_cell.render(str(current_grid[row][colomn]),True,BLACK,cell_color)    # create a text for appropriate cell
                
                grid_value_rect = grid_value.get_rect(center = ((w + 55), (h + 55)))    # aligment of text in a cell. 55 means half of the grid width and height
                screen.blit(grid_value,grid_value_rect)                 # join cell background with cell's value
                
                '''creating of TITLE screen of the game'''
                
                score_color = grid_cell_color(grid_score(current_grid)) # score fild color depends of color of max value in the current_grid
                
                pygame.draw.rect(screen,score_color,TITLE)              # 
                
                score = font.render('Score: '+ str(grid_score(current_grid)), True, BLACK,score_color)
                
                screen.blit(score, (10,25))
           

        pygame.display.update()

        if even.type == pygame.KEYDOWN:
            if even.key == pygame.K_ESCAPE:
                pygame.quit
                sys.exit(0)
        
            if even.key == pygame.K_DOWN:
                current_grid = sum_down(current_grid)

            if even.key == pygame.K_UP:
                current_grid = sum_up(current_grid)

            if even.key == pygame.K_LEFT:
                current_grid = sum_left(current_grid)

            if even.key == pygame.K_RIGHT:
                current_grid = sum_right(current_grid)
            
            current_grid = grid_new_value(current_grid)
            
            pygame.display.update()
            '*********************************************'
    '''check is there empty cell (with zero) in the matrix. In case no, player lose'''
    status = is_empty_cell(current_grid)
    if status == "STOP":
        pygame.draw.rect(screen,RED,LOSE)

        lose_bunner = font.render("YOU ARE LOSE!!!", True, BLACK, RED)

        screen.blit(lose_bunner,(75,300))
        pygame.draw.rect(screen,score_color,TITLE)              # 
                
        score = font.render('Score: '+ str(grid_score(current_grid)), True, BLACK,score_color)
                
        screen.blit(score, (10,25))
    elif status == "GO":
        pass
    
    pygame.display.update()

    '''check the WIN status. In case of any cell has value 2048 you win and game stopped'''
    actual_score = int(grid_score(current_grid))
    if actual_score == winner_value:

        pygame.draw.rect(screen,GREEN,WIN)

        win_bunner = font.render("YOU ARE WINNER!!!", True, BLACK, GREEN)

        screen.blit(win_bunner,(50,300))
        
        pygame.draw.rect(screen,score_color,TITLE)              # 
                
        score = font.render('Score: '+ str(grid_score(current_grid)), True, BLACK,score_color)
                
        screen.blit(score, (10,25))

    else:
        pass
    pygame.display.update()
        