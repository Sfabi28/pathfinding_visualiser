import pygame
import random

def get_neighbors(node, grid, rows, offset):

    neighbors = []
    coordinates = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    r, c = node.row, node.col
    
    limit_y = rows - offset - 1

    for dr, dc in coordinates:

        new_r = r + dr
        new_c = c + dc

        if 0 < new_r < rows - 1 and 0 < new_c < limit_y:
            neighbor = grid[new_r][new_c]
            
            if neighbor.is_barrier():
                neighbors.append(neighbor)
                
    return neighbors

def generate_maze(draw, grid, rows, offset):

    for col in grid:
        for cell in col[:rows - offset]:
            cell.make_barrier()
    
    start_node = grid[1][1]
    start_node.reset()

    stack = [start_node]

    draw()

    while len(stack) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, None
            
        current = stack[-1]

        neighbors = get_neighbors(current, grid, rows, offset)

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

    start_node.make_start()

    end_x = rows - 2
    end_y = rows - offset - 1
    
    if end_y % 2 == 0:
        end_y -= 1

    end_node = grid[end_x][end_y]
    end_node.make_end()
    
    draw()

    return start_node, end_node