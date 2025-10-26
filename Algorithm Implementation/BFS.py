graph = {} 
n = int(input("\nEnter the number of nodes: "))
print()

# we take user input 
for i in range(n):
    node = input(f"Enter the name of node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node}: ").split()
    graph[node] = neighbors

# Graph print
print("\nGraph:", graph)

def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph[node])

start = input("\nStart node: ")
print("\nVisited Node: ")
bfs(start)
