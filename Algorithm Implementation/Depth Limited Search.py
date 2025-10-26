# ----- Create an empty dictionary to store the graph -----
graph = {} 

# ----- Take user input for the graph -----
n = int(input("\nEnter the number of nodes: "))
print()

# Input nodes and their neighbors
for i in range(n):
    node = input(f"Enter the name of node {i+1}: ")  # Example: A
    neighbors = input(f"Enter neighbors of {node}: ").split()  # Example: B C
    graph[node] = neighbors  # Store adjacency list (connections)

# Print the entire graph to verify input
print("\nGraph:", graph)

# ----- Take input for start node, goal node, and depth limit -----
start = input("\nEnter the START node: ")
goal = input("Enter the GOAL node: ")
limit = int(input("Enter the Limit: "))

# ----- Depth Limited Search (DLS) function -----
def dls(start, limit, goal):
    visited = []                 # Keeps track of visited nodes
    stack = [(start, 0)]         # Stack holds (node, depth) pairs

    # Continue until the stack becomes empty
    while stack:
        node, depth = stack.pop()   # Pop the top node (LIFO behavior)

        # If the node is not yet visited
        if node not in visited:
            print(node, end=" ")    # Print the current node being explored
            visited.append(node)    # Mark node as visited

            # If goal is found, stop the search
            if node == goal:
                print("\nGoal found!")
                return

            # If current depth is less than the limit, explore deeper
            if depth < limit:
                # Add neighbors in reverse order to maintain correct DFS order
                for neighbor in reversed(graph[node]):
                    stack.append((neighbor, depth + 1))

# ----- Run the DLS algorithm -----
print("\nDepth Limited Search: ")
dls(start, limit, goal)
