import pygame
import math
from node import *
from algorithm import algorithm
from buttons import *

pygame.font.init()

WIDTH = 612
UI_OFFSET = 10
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Visualizer")

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            if j >= rows - UI_OFFSET:
                node.make_barrier()
            grid[i].append(node)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    limit_rows = rows - UI_OFFSET
    limit_pixel = limit_rows * gap

    for i in range(limit_rows + 1): 
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        
    for j in range(rows):
        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, limit_pixel))

def draw(win, grid, rows, width, buttons, current_brush):
    win.fill(WHITE)
    for row in grid:
        for node in row[:rows - UI_OFFSET]: 
            node.draw(win)
    draw_grid(win, rows, width)
    
    for button in buttons:
        selected = False
        if button.text == "Wall" and current_brush == "barrier":
            selected = True
        elif button.text == "Water" and current_brush == "water":
            selected = True
        elif button.text == "Mud" and current_brush == "mud":
            selected = True

        button.draw(win, selected)

    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos
    row = x // gap
    col = y // gap
    return row, col

def run_simulation(grid, ROWS, start, end, win, width):
    reset(grid, ROWS, start, end)
    for row in grid:
        for node in row:
            node.update_neighbors(grid)
    
    return algorithm(lambda: draw(win, grid, ROWS, width, [], None), grid, start, end)

def reset(grid, ROWS, start, end):
    for row in grid:
        for node in row[:ROWS - UI_OFFSET]:
            if node.is_barrier() or node == start or node == end:
                continue
            
            if node.weight > 1:
                node.color = node.base_color
            else:
                node.reset()

def main(win, width):
    ROWS = 51
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    
    current_brush = "barrier" 

    gap = width // ROWS
    ui_start_y = (ROWS - UI_OFFSET) * gap
    
    btn_y = ui_start_y + 15
    btn_width = 90
    btn_height = 30
    
    clear_btn = Button(20, btn_y, btn_width, btn_height, "Clear (D)")
    reset_btn = Button(20, btn_y + 40, btn_width, btn_height, "Reset (R)")
    
    wall_btn = Button(140, btn_y, btn_width, btn_height, "Wall", WALL, WALL_HOVER)
    water_btn = Button(140 + 100, btn_y, btn_width, btn_height, "Water", WATER, WATER_HOVER)
    mud_btn = Button(140 + 200, btn_y, btn_width, btn_height, "Mud", MUD, MUD_HOVER)
    
    buttons = [clear_btn, reset_btn, wall_btn, water_btn, mud_btn]

    while run:
        draw(win, grid, ROWS, width, buttons, current_brush)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                
                if col < ROWS - UI_OFFSET: 
                    spot = grid[row][col]
                    
                    if not start and spot != end:
                        start = spot
                        start.make_start()
                    elif not end and spot != start:
                        end = spot
                        end.make_end()
                    elif spot != end and spot != start:
                        if current_brush == "barrier":
                            spot.make_barrier()
                        elif current_brush == "mud":
                            spot.make_mud()
                        elif current_brush == "water":
                            spot.make_water()
                
                else:
                    if clear_btn.is_clicked(pos):
                        start = None
                        end = None
                        grid = make_grid(ROWS, width)
                        current_brush = "barrier"
                    
                    elif reset_btn.is_clicked(pos):
                        reset(grid, ROWS, start, end)

                    elif wall_btn.is_clicked(pos):
                        current_brush = "barrier"
                    
                    elif water_btn.is_clicked(pos):
                        current_brush = "water"

                    elif mud_btn.is_clicked(pos):
                        current_brush = "mud"

            elif pygame.mouse.get_pressed()[2]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                
                if col < ROWS - UI_OFFSET:
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    current_brush = "barrier"

                if event.key == pygame.K_r:
                    reset(grid, ROWS, start, end)
                
                elif event.key == pygame.K_SPACE and start and end:
                    ret = run_simulation(grid, ROWS, start, end, win, width)
                    if ret == 2:
                        pygame.quit()
                        return

    pygame.quit()

if __name__ == "__main__":
    main(WIN, WIDTH)