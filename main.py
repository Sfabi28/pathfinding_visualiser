import pygame
import math
from node import *
from algorithm import algorithm

WIDTH = 600
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

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row[:rows - UI_OFFSET]: 
            node.draw(win)
    draw_grid(win, rows, width)
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
    
    ret = algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
    return ret

def reset(grid, ROWS, start, end):
    for row in grid:
        for node in row[:ROWS - UI_OFFSET]:
            if not node.is_barrier() and node != end and node != start:
                node.reset()

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True

    while run:
        draw(win, grid, ROWS, width)
        
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
                        spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                
                if row < ROWS - UI_OFFSET:
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