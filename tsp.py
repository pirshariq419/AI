from collections import deque

def tsp_bfs(graph):
    n = len(graph) 
    startCity = 0       
    min_cost = float('inf')  
    opt_path = []        
    
    dq = deque([([startCity], 0)])  
    
    print("Path Traversal:")
    
    while dq:
        cur_path, cur_cost = dq.popleft()
        cur_city = cur_path[-1]
        
        print(f"Current Path: {cur_path}, Current Cost: {cur_cost}")
        
        if len(cur_path) == n and cur_path[0] == startCity:
            total_cost = cur_cost + graph[cur_city][startCity]
            if total_cost < min_cost:
                min_cost = total_cost
                opt_path = cur_path + [startCity]
            continue
        
        for next_city in range(n):
            if next_city not in cur_path:  
                new_path = cur_path + [next_city]
                new_cost = cur_cost + graph[cur_city][next_city]
                dq.append((new_path, new_cost))
    
    return min_cost, opt_path

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost, opt_path = tsp_bfs(graph)

print("\nOptimal Solution:")
print(f"Minimum cost: {min_cost}")
print(f"Optimal path: {opt_path}")