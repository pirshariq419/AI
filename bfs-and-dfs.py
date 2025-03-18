n = int(input("Enter the number of nodes: "))
adj = [[] for _ in range(n)]

for i in range(n):
    num= int(input(f"Enter number of neighbours for node {i}  "))
    neighbours = []
    for j in range(num):
        neighbours.append(int(input()))
    adj[i] = neighbours
src= int(input("Enter the source node: "))

visited = [0] * n

def dfs(adj, src, visited):
    visited[src] = 1
    print(src, end=" ")
    for i in adj[src]:
        if visited[i] == 0:
            dfs(adj, i, visited)
print("DFS\n")
dfs(adj, src, visited)
visited = [0] * n

def bfs(adj, src, visited):
    visited[src] = 1
    queue = [src]
    while queue:
        curr = queue.pop(0)
        print(curr, end=" ")
        for i in adj[curr]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
print("\nBFS\n")
bfs(adj, src, visited)