import heapq

ROWS=4
COLS=6
START= (2,1)
GOAL= (2,4)

OBSTACLES= {
    ((1,1), (1,2)),
    ((2,1), (2,2)),
    ((3,1), (3,2)),
    ((0,5), (1,5)),
    ((0,4), (1,4))
}

MOVES= [(-1,0), (1,0), (0,-1), (0,1)]

def isValidMove(curr, next):
    r, c= next

    if not(0<=r<ROWS and 0<=c<COLS):
        return False
    edge= tuple(sorted([curr,next]))
    
    if edge in OBSTACLES:
        return False

    return True

def heuristic(a,b):
    return abs(a[0]-b[0])+ abs(a[1]-b[1])

def a_star_search(start, goal):
    visited= set()
    priority_queue= [(0, start, [start])]

    while priority_queue:
        curr_cost, curr_node, curr_path= heapq.heappop(priority_queue)

        if curr_node in visited:
            continue

        visited.add(curr_node)

        if curr_node== goal:
            return curr_path
        
        for move in MOVES:
            neighbor= (curr_node[0]+ move[0], curr_node[1]+ move[1])

            if isValidMove(curr_node, neighbor):
                new_cost= curr_cost+1
                f= new_cost+ heuristic(neighbor, goal)
                new_path= curr_path+ [neighbor]
                heapq.heappush(priority_queue, (f, neighbor, new_path))
    
    return []

path= a_star_search(START, GOAL)

if path:
    print("The path is :", path)
else:
    print("No path")
