import heapq

def heuristic(start_row, start_col, end_row, end_col):
    return abs(start_row - end_row) + abs(start_col - end_col)

def robo_path(start_row, start_col, end_row, end_col, matrix, directions_map, m, n):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start_row, start_col, end_row, end_col), 0, start_row, start_col))
    came_from = {}
    g_score = { (start_row, start_col): 0 }
    direction_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    while open_list:
        f, g, current_row, current_col = heapq.heappop(open_list)
        
        if (current_row, current_col) == (end_row, end_col):
            print("Path found!")
            path = []
            while (current_row, current_col) in came_from:
                path.append((current_row, current_col))
                current_row, current_col = came_from[(current_row, current_col)]
            path.append((start_row, start_col))
            path.reverse()
            for (r, c) in path:
                print(f"({r}, {c})")
            return
        
        valid_directions = directions_map[(current_row, current_col)]
        for direction in valid_directions:
            delta_row, delta_col = direction_map[direction]
            neighbor_row = current_row + delta_row
            neighbor_col = current_col + delta_col
            
            if 0 <= neighbor_row < m and 0 <= neighbor_col < n and matrix[neighbor_row][neighbor_col] != 1:
                tentative_g = g + 1
                
                if (neighbor_row, neighbor_col) not in g_score or tentative_g < g_score[(neighbor_row, neighbor_col)]:
                    g_score[(neighbor_row, neighbor_col)] = tentative_g
                    f = tentative_g + heuristic(neighbor_row, neighbor_col, end_row, end_col)
                    heapq.heappush(open_list, (f, tentative_g, neighbor_row, neighbor_col))
                    came_from[(neighbor_row, neighbor_col)] = (current_row, current_col)
    
    print("Path not found.")

def main():
    m = int(input("Enter the number of rows:\n"))
    n = int(input("Enter the number of columns:\n"))
    print("Enter the elements of the matrix:")
    matrix = [[0 for j in range(n)] for i in range(m)]
    directions_map = {}
    print("Enter valid directions for each cell (U for up, D for down, L for left, R for right):")
    for i in range(m):
        for j in range(n):
            directions = input(f"Enter directions for cell ({i}, {j}): ").upper().split()
            directions_map[(i, j)] = directions
    start_row = int(input("Enter the start row:\n"))
    start_col = int(input("Enter the start column:\n"))
    goal_row = int(input("Enter the goal row:\n"))
    goal_col = int(input("Enter the goal column:\n"))
    robo_path(start_row, start_col, goal_row, goal_col, matrix, directions_map, m, n)

if __name__ == '__main__':
    main()
