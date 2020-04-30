# Header settings
title = "Conway's Game of Life"
icon = "images/icon.jpg"

# Screen settings
frame_rate = 8
cell_size = 20
cell_count_x = 62
cell_count_y = 44
screen_size_x = cell_count_x * cell_size
screen_size_y = cell_count_y * cell_size

# Colors settings
black = (0,0,0)
white = (255,255,255)
gray = (220,220,220)
red = (255,0,0)
blue = (0,0,255)

cell_colors = {
    True: black,  # Living cell
    False: white  # Dead cell
}
grid_color = gray
