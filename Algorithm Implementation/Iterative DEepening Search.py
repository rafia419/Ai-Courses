# ---------------------------------------
# 🧭 Iterative Deepening Search (IDS)
# ---------------------------------------

# ---- Step 1: Take graph input from user ----
graph = {}
n = int(input("\nEnter the number of nodes: "))
print()

for i in range(n):
    node = input(f"Enter the name of node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node}: ").split()
    graph[node] = neighbors

print("\nGraph:", graph)

# ---- Step 2: Take start, goal and depth limit ----
start_node = input("\nEnter the START node: ")
goal_node = input("Enter the GOAL node: ")
max_depth = int(input("Enter the maximum depth limit: "))

# ---- Step 3: Depth-Limited Search (DLS) ----
def dls(graph, start, goal, limit, visited_nodes):
    visited_nodes.append(start)

    if start == goal:
        return [start]

    if limit <= 0:
        return None

    for neighbor in graph.get(start, []):
        path = dls(graph, neighbor, goal, limit - 1, visited_nodes)
        if path:
            return [start] + path

    return None

# ---- Step 4: Iterative Deepening Search (IDS) ----
def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited_nodes = []
        print(f"\n🔎 Searching at depth {depth}...")
        path = dls(graph, start, goal, depth, visited_nodes)
        print(f"Visited nodes at depth {depth}: {visited_nodes}")
        if path:
            print(f"\n✅ Goal found at depth {depth}!")
            print("→ Path:", " → ".join(path))
            return path

    print("\n❌ Goal not found within the maximum depth limit.")
    return None

# ---- Step 5: Run IDS ----
ids(graph, start_node, goal_node, max_depth)
