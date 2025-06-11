from collections import deque

start_state = (3, 3, 1)
goal_state = (0, 0, 0)

moves = [(1,0), (0,1), (1,1), (2,0), (0,2)]

def is_valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
           (m == 0 or m >= c) and
           ((3 - m) == 0 or (3 - m) >= (3 - c)))

def bfs():
    queue = deque()
    visited = set()

    queue.append((start_state, [start_state]))

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal_state:
            return path

        for move in moves:
            dm, dc = move

            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            if is_valid(*new_state[:2]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

solution = bfs()
if solution:
    print("Solution found:")
    for step in solution:
        print(f"Missionaries: {step[0]}, Cannibals: {step[1]}, Boat on {'left' if step[2]==1 else 'right'}")
else:
    print("No solution found.")
