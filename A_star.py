import heapq
from collections import deque
graph = {
    0: [(1, 2), (2, 1)],
    1: [(0, 2),(2,5),(3,11),(4,3)],
    2: [(0,1),(1,5),(4,1),(5,15)],
    3: [(1,11),(4,2),(6,1)],
    4: [(1,3),(2,1),(3,2),(5,4),(6,5)],
    5: [(2,15),(4,4),(6,1)],
    6:[(3,1),(4,5),(5,1)]
}

heuristics ={
    0:1,
    1:3,
    2:15,
    3:2,
    4:1,
    5:float('inf'),
    6:0
}

def a_star_search(graph,heuristics,start,goal):
    nodes_gen=0
    vis=set()
    pq=[(0,start,[])]
    nodes_gen=nodes_gen+1
    while pq:
        curr_cost, curr_node, curr_path = heapq.heappop(pq)
        if curr_node in vis:
            continue
        vis.add(curr_node)
        curr_path.append(curr_node)

        if curr_node == goal:
            return curr_path, nodes_gen
        
        for neighbor, weight in graph[curr_node]:
            if neighbor not in vis:
                tentative_cost = curr_cost + weight
                heuristic = heuristics[neighbor]
                f = tentative_cost + heuristic
                nodes_gen=nodes_gen+1
                heapq.heappush(pq, (f, neighbor, curr_path))
            
    return [], nodes_gen

def uniform_cost_search(graph,start,goal):
    pq=[(0,start)]
    nodes_gen=1
    visited=set()
    parent={start:None}
    while pq:
        cost, node=heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            path=[]
            while node:
                path.append(node)
                node=parent[node]
            return cost, path[::-1], nodes_gen
        
        for neighbor, weight in graph.get(node,[]):
            if neighbor not in visited:
                nodes_gen=nodes_gen+1
                heapq.heappush(pq,(cost+weight,neighbor))
                parent[neighbor]=node
    
    return float('inf'), [], nodes_gen

def dfs(graph, start_node, result=None, vis=None, nodes_gen=0):
    if result is None:
        result = []
    if vis is None:
        vis = set()
    
    result.append(start_node)
    vis.add(start_node)
    nodes_gen += 1  

    for neighbor, _ in graph.get(start_node, []):  
        if neighbor not in vis:
            nodes_gen = dfs(graph, neighbor, result, vis, nodes_gen)[1]  
    
    return result, nodes_gen

def bfs(graph,start_node):
    q=deque([start_node])
    result=[]
    vis=set()
    nodes_gen=1
    while q:
        curr=q.popleft()
        if curr not in vis:
            result.append(curr)
            vis.add(curr)
        for neigh, _ in graph.get(curr, []): 
            if neigh not in vis:
                q.append(neigh)
                nodes_gen += 1 
          
    
    return result, nodes_gen

def main():
    start_node = int(input("Enter the start node: "))
    goal_node = int(input("Enter the goal node: ")) 
    a_star_path, a_star_nodes_gen = a_star_search(graph, heuristics, start_node, goal_node)
    a_star_cost = 0
    for i in range(len(a_star_path)-1):
        current_node = a_star_path[i]
        next_node = a_star_path[i+1]
        
        for neighbor, weight in graph[current_node]:
            if neighbor == next_node:
                a_star_cost += weight
                break
    print(f"A* search found the optimal path with cost {a_star_cost} and path: {a_star_path}")

    print("Comparing with DFS, BFS, UCS based on number of nodes generated: ")

    dfs_nodes_gen = dfs(graph, start_node)[1]
    bfs_nodes_gen = bfs(graph, start_node)[1]
    ucs_nodes_gen = uniform_cost_search(graph, start_node, goal_node)[2]

    print(f"No. of nodes generated for DFS: {dfs_nodes_gen}")
    print(f"No. of nodes generated for BFS: {bfs_nodes_gen}")
    print(f"No. of nodes generated for UCS: {ucs_nodes_gen}")
    print(f"No. of nodes generated for A*: {a_star_nodes_gen}")

if __name__ == "__main__":
    main()