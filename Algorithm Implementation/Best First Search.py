# Create empty dictionaries for graph structure and heuristic values
graph = {}
heuristic = {}

# ----- Input graph and heuristic values -----
n = int(input("\nNumber of nodes: "))
print()

for i in range(n):
    node = input(f"Node name {i+1}: ")  # Example: A
    neighbors = input(f"Neighbors of {node}: ").split()  # Example: B C
    graph[node] = neighbors  # Store adjacency list (graph connections)
    h = int(input(f"Heuristic value for {node}: "))  # Example: 5
    heuristic[node] = h  # Store heuristic value for each node

# ----- Best First Search Algorithm -----
def best_first_search(start, goal):
    visited = set()  # To keep track of visited nodes
    queue = [(heuristic[start], start)]  # Priority queue (sorted by heuristic value)

    while queue:
        queue.sort()  # Sort queue based on heuristic value (lowest first)
        current_h, current = queue.pop(0)  # Pop the node with smallest heuristic

        if current in visited:
            continue  # Skip if already visited

        print(current, end=" ")  # Print current node being explored
        visited.add(current)  # Mark node as visited

        if current == goal:
            print("\nGoal reached!")  # Stop when goal is found
            return

        # Explore all neighbors of the current node
        for neighbor in graph[current]:
            if neighbor not in visited:
                # Add neighbor with its heuristic value into queue
                queue.append((heuristic[neighbor], neighbor))

    # If goal not found after exploring all nodes
    print("\nGoal not reachable.")

# ----- Take start and goal input from user -----
start = input("\nStart node: ")
goal = input("Goal node: ")

# ----- Run the Best First Search -----
best_first_search(start, goal)

