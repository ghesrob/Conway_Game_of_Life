import pygame
from pygame.locals import * 
import numpy as np

from config import *


class Grid:

    def __init__(self, cell_size, cell_count_x, cell_count_y):
        """Initialize a grid of the game."""
        self.cell_size = cell_size
        self.cell_count_x = cell_count_x
        self.cell_count_y = cell_count_y
        self.iter = 0
        self.structure = np.full(shape = (cell_count_y, cell_count_x), fill_value = False)


    def switch_cell(self, coord_x, coord_y):
        """Switch the state (alive/dead) of a cell."""
        cell_x = coord_x // cell_size
        cell_y = coord_y // cell_size
        self.structure[cell_y, cell_x] = not(self.structure[cell_y, cell_x])

   
    def evolve(self):
        """Evolve the grid for one turn.
        At turn n+1, a cell will be alive if 3 neighbours or 2 neighbours and already alive.
        """
        X = self.structure.copy().astype(int)
        neigh = np.zeros(X.shape)
        neigh[1:-1,1:-1] = (X[:-2,:-2]  + X[:-2,1:-1] + X[:-2,2:] + 
                            X[1:-1,:-2] +                X[1:-1,2:]  + 
                            X[2:,:-2]   + X[2:,1:-1]  + X[2:,2:])
        self.structure = np.logical_or(neigh==3,np.logical_and(X==1,neigh==2))


    def show(self, screen):
        """Print the grid on PyGame screen"""      
        for x in range(cell_count_x):
            for y in range(cell_count_y):
                coord_x, coord_y = x * cell_size, y * cell_size
                cell_color = cell_colors.get(self.structure[y,x])
                rect = pygame.Rect(coord_x, coord_y, cell_size, cell_size)
                screen.fill(cell_color, rect)
                pygame.draw.rect(screen, gray, rect, 1)


