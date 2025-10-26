# ---------------------------------------
# 🧭 Bidirectional BFS Path Finder
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

# ---- Step 2: Take start and goal nodes ----
start = input("\nEnter the START node: ")
goal = input("Enter the GOAL node: ")

# ---- Step 3: Bi-directional BFS implementation ----
def b_bfs(graph, start, goal):
    if start == goal:
        print(f"\nShortest path: {start}")
        return [start]

    # Queues for both searches
    qstart = [start]
    qgoal = [goal]

    # Parent tracking dictionaries
    tstart = {start: None}
    tgoal = {goal: None}

    # Continue until one side runs out
    while qstart and qgoal:

        # ---------- Expand from START side ----------
        current = qstart.pop(0)
        for neigh in graph.get(current, []):
            if neigh not in tstart:
                tstart[neigh] = current
                qstart.append(neigh)

                # ✅ Check if both searches met
                if neigh in tgoal:
                    return build_path(neigh, tstart, tgoal)

        # ---------- Expand from GOAL side ----------
        current = qgoal.pop(0)
        for neigh in graph.get(current, []):
            if neigh not in tgoal:
                tgoal[neigh] = current
                qgoal.append(neigh)

                # ✅ Check if both searches met
                if neigh in tstart:
                    return build_path(neigh, tstart, tgoal)

    print("\nNo path found!")
    return None


# ---- Step 4: Function to build the full path ----
def build_path(meet, tstart, tgoal):
    # Path from START to meeting node
    path_left = []
    node = meet
    while node is not None:
        path_left.append(node)
        node = tstart[node]
    path_left.reverse()

    # Path from meeting node to GOAL
    path_right = []
    node = tgoal[meet]
    while node is not None:
        path_right.append(node)
        node = tgoal[node]

    # Combine both paths
    full_path = path_left + path_right
    print("\n✅ Shortest Path:", " → ".join(full_path))
    print()
    return full_path


# ---- Step 5: Run the Bidirectional BFS ----
b_bfs(graph, start, goal)
