import pygame
from pygame.locals import * 

from config import *
from grid import *


# Initialisation de l'écran et de la grille
pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))


# Boucle infinie
while True:
    in_lobby, in_game = 1, 1

    grid = Grid(cell_size, cell_count_x, cell_count_y)
    # Ecran d'accueil
    while in_lobby:
        for event in pygame.event.get():
        
            # Fermeture de l'app
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()
        
            # Switch l'état d'une cell lors d'un clic
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                grid.switch_cell(*event.pos)

            # Fermeture du lobby et lancement du jeu
            if event.type == KEYDOWN and event.key == K_RETURN:
                in_lobby = 0

        grid.show(screen)
        pygame.display.flip()


    # Déroulement du jeu 
    while in_game:
        pygame.time.Clock().tick(frame_rate)
        pause = 0

        for event in pygame.event.get():       
            # Fermeture de l'app
            if event.type == QUIT: 
                pygame.quit()
                quit()            
            # Retour accueil
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                in_game = 0
            # Pause
            if event.type == KEYDOWN and event.key == K_SPACE:
                pause = 1

        grid.evolve()
        grid.show(screen)
        pygame.display.flip()

        # Pause screen
        while pause:
            for event in pygame.event.get():        
                # Fermeture de l'app
                if event.type == QUIT: 
                    pygame.quit()
                    quit()           
                # Retour accueil
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

