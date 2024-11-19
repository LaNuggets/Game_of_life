import generate_grid as gd
import display_grid as dg

frame = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]

def cell_state(grid):
    actual_grid = [row[:] for row in grid]
    live_cells = 0

    for i, value in enumerate(grid):
        for j,_ in enumerate(value):
            for x_frame, y_frame in frame:
                x_direction = i + x_frame
                y_direction = j + y_frame

                if 0 <= x_direction < len(grid) and 0 <= y_direction < len(grid[0]):
                    if grid[x_direction][y_direction] == 1:
                        live_cells += 1 

            if live_cells == 3:
                actual_grid[i][j] = 1
            elif live_cells == 2:
                continue
            else:
                actual_grid[i][j] = 0
            live_cells = 0

    return actual_grid