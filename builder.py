import pygame
import random

def get_neighbors(node, grid, rows):

    neighbors = []
    coordinates = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    r, c = node.row, node.col

    for dr, dc in coordinates:

        new_r = r + dr
        new_c = c + dc

        if 0 < new_r < rows - 1 and 0 < new_c < rows - 1:
            neighbor = grid[new_r][new_c]
            
            if neighbor.is_barrier():
                neighbors.append(neighbor)
                
    return neighbors

def generate_maze(draw, grid, rows):

    for row in grid:
        for cell in row:
            cell.make_barrier()
    
    start = grid[1][1]
    start.reset()

    stack = [start]

    draw()

    while len(stack) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        current = stack[-1]

        neighbors = get_neighbors(current, grid, rows)

        if len(neighbors) > 0:

            random_neighbor = random.choice(neighbors)

            wall_r = (current.row + random_neighbor.row) // 2
            wall_c = (current.col + random_neighbor.col) // 2

            grid[wall_r][wall_c].reset()
            random_neighbor.reset()

            stack.append(random_neighbor)

            draw()

        else:

            stack.pop()
            
        

