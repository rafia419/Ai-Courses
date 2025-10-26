# Create empty dictionaries for graph and heuristic values
graph = {}
heuristic = {}

# ----- Input section -----
n = int(input("\nNumber of nodes: "))  # Total number of nodes in the graph
print()

for i in range(n):
    node = input(f"Node name {i+1}: ")  # Example: A
    graph[node] = input(f"Neighbors of {node}: ").split()  # Example: B C D → stored as ['B', 'C', 'D']
    h = int(input(f"Heuristic value for {node}: "))  # Example: 5
    heuristic[node] = h  # Store the heuristic value for the node

# ----- Beam Search Algorithm -----
def beam_search(start, goal, beam_width):
    # Each element in queue = (current_node, path_from_start_to_current)
    queue = [(start, [start])]
    visited = set()  # Keeps track of visited nodes

    # Continue until queue becomes empty
    while queue:
        # Show the nodes in the current beam (level)

        next_level = []  # Stores possible candidates for the next level

        # Explore each node in the current beam
        for node, path in queue:
            visited.add(node)  # Mark current node as visited

            # If goal is found → print path and stop
            if node == goal:
                print(f"\nGoal '{goal}' reached!")
                print("Path:", " → ".join(path))
                return

            # Explore neighbors of current node
            for neighbor in graph[node]:
                # Add neighbor if not visited and not already in next_level
                if neighbor not in visited and all(neighbor != n for n, _ in next_level):
                    next_level.append((neighbor, path + [neighbor]))  # Add neighbor with updated path

        # Sort next level nodes by heuristic value (lowest first)
        # Then keep only top 'beam_width' nodes → Beam pruning step
        next_level.sort(key=lambda x: heuristic.get(x[0], float('inf')))
        queue = next_level[:beam_width]

    # If goal not found after all possible expansions
    print("\nGoal not reachable.")

# ----- Input from user -----
start = input("\nStart node: ")
goal = input("Goal node: ")
beam_width = int(input("Beam width (k): "))  # Beam width decides how many nodes to keep per level

# ----- Run the Beam Search -----
beam_search(start, goal, beam_width)
