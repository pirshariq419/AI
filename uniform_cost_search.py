import heapq

graph = {
    'S': [('d', 3), ('e', 9), ('p', 1)],
    'b': [('a', 2)],
    'a': [],
    'd': [('b', 1),('c', 8), ('e', 2)],
    'c': [('a', float('inf'))],
    'e': [('h', 8), ('r', 2)],
    'h': [('p', float('inf')), ('q', float('inf'))],
    'f': [('G', 2),('c',float('inf'))],
    'r': [('f',1)],
    'G': [],
    'p': [('q', 15)],
    'q': []
}

def ucs(graph,start,goal):
    pq=[(0,start)]
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
            return cost, path[::-1]
        
        for neighbor, weight in graph.get(node,[]):
            if neighbor not in visited:
                heapq.heappush(pq,(cost+weight,neighbor))
                parent[neighbor]=node
    
    return float('inf'), []

start_node='S'
goal_node='G'

cost, path=ucs(graph, start_node, goal_node)

print(f"Minimum Cost: {cost}")
print(f"Optimal Path: {' -> '.join(path)}")