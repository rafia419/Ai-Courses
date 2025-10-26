# ----- Alpha-Beta Pruning (Multiple Utilities + Full Prune Tracking) -----

tree = {}
utilities = {}

total_prunes = 0
total_pruned_nodes = 0

# ----- INPUT SECTION -----
n = int(input("\nNumber of nodes in the game tree: "))
print()
for i in range(n):
    node = input(f"Node name {i+1}: ")
    children = input(f"Children of {node}: ").split()

    if children:
        tree[node] = children
    else:
        user_input = input(f"Utility values of leaf node {node} (space-separated, can include negatives): ")
        vals = [int(x) for x in user_input.split()]
        utilities[node] = vals


# ----- FUNCTION: Count all nodes + utility values under a subtree -----
def count_subtree_nodes(node):
    count = 1  # include the node itself
    if node in tree:
        for child in tree[node]:
            count += count_subtree_nodes(child)
    elif node in utilities:
        count += len(utilities[node])  # count utility values
    return count


# ----- ALPHA-BETA FUNCTION -----
def alphabeta(node, depth, alpha, beta, maximizing):
    global total_prunes, total_pruned_nodes

    # Leaf node
    if node in utilities:
        val = max(utilities[node]) if maximizing else min(utilities[node])
        return val, [f"{node}({val})"]

    if maximizing:
        max_val = -999999
        best_path = []
        for i, child in enumerate(tree[node]):
            val, path = alphabeta(child, depth + 1, alpha, beta, False)

            if val > max_val:
                max_val = val
                best_path = [node] + path

            alpha = max(alpha, max_val)

            # Prune remaining children
            if beta <= alpha:
                total_prunes += 1
                remaining = tree[node][i + 1:]
                for r in remaining:
                    total_pruned_nodes += count_subtree_nodes(r)
                break
        return max_val, best_path

    else:
        min_val = 999999
        best_path = []
        for i, child in enumerate(tree[node]):
            val, path = alphabeta(child, depth + 1, alpha, beta, True)

            if val < min_val:
                min_val = val
                best_path = [node] + path

            beta = min(beta, min_val)

            # Prune remaining children
            if beta <= alpha:
                total_prunes += 1
                remaining = tree[node][i + 1:]
                for r in remaining:
                    total_pruned_nodes += count_subtree_nodes(r)
                break
        return min_val, best_path


# ----- RUN -----
root = input("\nEnter root node of the game tree: ")
value, path = alphabeta(root, 0, -999999, 999999, True)

# ----- OUTPUT -----
print("\n================ RESULT ================")
print(f"1️⃣ Optimal value at root '{root}': {value}")
print("2️⃣ Decision Path:", " → ".join(path))
print(f"3️⃣ Total prunes: {total_prunes}")
print(f"4️⃣ Total pruned node count (including utilities): {total_pruned_nodes}")
