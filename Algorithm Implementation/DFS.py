graph = {}
n = int(input("\nEnter the number of nodes: "))
print()

# Take user input for graph
for i in range(n):
    node = input(f"Enter the name of node {i+1}: ")   # Node name
    neighbors = input(f"Enter neighbors of {node}: ").split()
    graph[node] = neighbors

# Print Graph
print("\nGraph:", graph)

def dfs(start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            # ✅ Reverse to visit left (first neighbor) first
            stack.extend(reversed(graph[node]))

start = input("\nStart node: ")
print("\nVisited Node: ")
dfs(start)
