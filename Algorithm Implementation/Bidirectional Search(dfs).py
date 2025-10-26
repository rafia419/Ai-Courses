# ---- Take graph input from user ----
graph = {}
n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input(f"Enter the name of node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

print("\nGraph:", graph)

# ---- Take start and goal nodes ----
start = input("\nEnter the START node: ")
goal = input("Enter the GOAL node: ")

# ---- Bi-directional DFS implementation ----
def b_dfs(graph, start, goal):
    if start == goal:
        return [start]

    # We use stack for DFS
    sstart = [start]
    sgoal = [goal]

    tstart = {start: None}  
    tgoal = {goal: None}

    while sstart and sgoal:
        # expand from start side (DFS)
        current = sstart.pop()  # last element pop
        for neigh in graph.get(current, []):
            if neigh not in tstart:
                tstart[neigh] = current
                sstart.append(neigh)
                if neigh in tgoal:
                    return build_path(neigh, tstart, tgoal)

        # expand from goal side (DFS)
        current = sgoal.pop()
        for neigh in graph.get(current, []):
            if neigh not in tgoal:
                tgoal[neigh] = current
                sgoal.append(neigh)
                if neigh in tstart:
                    return build_path(neigh, tstart, tgoal)
        
    return None

def build_path(meet, tstart, tgoal):
    # path from start to meeting point
    path_left = []
    node = meet
    while node is not None:
        path_left.append(node)
        node = tstart[node]
        print(path_left)
    path_left.reverse()

    # path from meeting point to goal
    path_right = []
    node = tgoal[meet]
    while node is not None:
        path_right.append(node)
        node = tgoal[node]
        print(path_right)

    full_path = path_left + path_right
    print(" ".join(full_path))
    return full_path

# Run example
b_dfs(graph, start, goal)