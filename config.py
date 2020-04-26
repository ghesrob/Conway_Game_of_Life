# Screen
cell_size = 20
cell_count_x = 60
cell_count_y = 40
screen_size_x = cell_count_x * cell_size
screen_size_y = cell_count_y * cell_size

frame_rate = 8


# Colors
black = (0,0,0)
white = (255,255,255)
gray = (220,220,220)
red = (255,0,0)

cell_colors = {
    True: black,  #Color for an alive cell
    False: white  #Color for a dead cell
}
