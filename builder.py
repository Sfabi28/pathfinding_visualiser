import pygame
import random

def generate_maze(draw, grid, rows):

    for row in range(grid):
        for cell in range(row):
            cell.make_barrier()
    
    start = grid[1][1]
    start.reset()

    stack = [start]

    draw()

    while len(stack) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

