import heapq

graph = {
    'S': [('d', 3), ('e', 9), ('p', 1)],
    'b': [('a', 2)],
    'a': [],
    'd': [('b', 1), ('c', 8), ('e', 2)],
    'c': [('a', float('inf'))],
    'e': [('h', 8), ('r', 2)],
    'h': [('p', float('inf')), ('q', float('inf'))],
    'f': [('G', 2), ('c', float('inf'))],
    'r': [('f', 1)],
    'G': [],
    'p': [('q', 15)],
    'q': []
}

def ucs(graph, start, goal):
    pq = [(0, start, [])]  
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        if node == goal:
            return cost, path

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

    return float('inf'), []

cost, path = ucs(graph, 'S', 'G')
print(f"Minimum Cost: {cost}")
print(f"Optimal Path: {' -> '.join(path)}")
