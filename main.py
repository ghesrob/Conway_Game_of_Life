import pygame
from pygame.locals import * 

from config import *
from grid import *


# Screen and grid initialization
pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
icon = pygame.image.load(icon).convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption(title)

text_font = pygame.font.SysFont("calibri", 30)

# Infinite loop
while True:
    in_lobby, in_game = 1, 1
    grid = Grid(cell_size, cell_count_x, cell_count_y)

    # Lobby 
    while in_lobby:
        grid.show(screen)
        # Title embedding
        text_title = text_font.render("Conway's Game of Life", True, blue)
        rect_title = pygame.Rect(6*cell_size, 0, screen_size_x - 12*cell_size, 4*cell_size)
        screen.fill(white, rect_title)
        pygame.draw.rect(screen, black, rect_title, 1)
        screen.blit(text_title, ((screen_size_x - text_title.get_rect().width) / 2, (4*cell_size - text_title.get_rect().height) / 2 ))
        # Foot instructions embedding
        text_foot = text_font.render("Select initial living cells and press RETURN to start", True, black)
        rect_foot = pygame.Rect(0, screen_size_y - 3*cell_size, screen_size_x, 3*cell_size)
        screen.fill(white, rect_foot)
        pygame.draw.rect(screen, grid_color, rect_foot, 1)
        screen.blit(text_foot, ((screen_size_x - text_foot.get_rect().width) / 2,  screen_size_y - (text_foot.get_rect().height + 3*cell_size) / 2))
        pygame.display.flip()

        # Events handling
        for event in pygame.event.get():       
            # Closing app
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()       
            # Switch cell state 
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                grid.switch_cell(*event.pos)
            # Closing lobby and starting game
            if event.type == KEYDOWN and event.key == K_RETURN:
                in_lobby = 0


    # In game
    while in_game:
        pygame.time.Clock().tick(frame_rate)
        pause = 0

        for event in pygame.event.get():       
            # Closing app
            if event.type == QUIT: 
                pygame.quit()
                quit()            
            # Back to lobby
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                in_game = 0
            # Pause
            if event.type == KEYDOWN and event.key == K_SPACE:
                pause = 1

        # Update grid
        grid.evolve()
        grid.show(screen)
        pygame.display.flip()

        # Pause screen
        while pause:
            for event in pygame.event.get():        
                # Closing app
                if event.type == QUIT: 
                    pygame.quit()
                    quit()           
                # Back to lobby
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    in_game, pause = 0, 0
                # Pause
                if event.type == KEYDOWN and event.key == K_SPACE:
                    pause = 0
                # Manually evolve grid
                if event.type == KEYDOWN and event.key == K_UP:
                    grid.evolve()
                    grid.show(screen)
                    pygame.display.flip() 

