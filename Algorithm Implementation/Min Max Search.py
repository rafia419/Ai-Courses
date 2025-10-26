# ---------------------------------------
# 🧭 MIN MAX SEARCH
# ---------------------------------------

# ----  Take graph input and utilities input from user ----
tree = {}        
utilities = {}   

n = int(input("\nNumber of nodes in the game tree: "))
print()

for i in range(n):
    node = input(f"Node name {i+1}: ")
    children = input(f"Children of {node}: ").split()
    if children:
        tree[node] = children
    else:
        user_input = input(f"Utility values of leaf node {node}: ")
        parts = user_input.split()      
        vals = []

        for p in parts:
            vals.append(int(p))         # ["3","5","7"] → [3,5,7]

        utilities[node] = vals
 
# Min-max implementation---
def minimax(node, depth, path):
    if node in utilities:
        if depth % 2 == 0:   
            chosen = max(utilities[node])
        else:                
            chosen = min(utilities[node])
        return chosen, path + [f"{node}({chosen})"]

    if depth % 2 == 0:
        best_val = -999999
        best_path = []
        for child in tree.get(node, []):
            new_path_input = path + [node]
            result = minimax(child, depth + 1, new_path_input)
            val = result[0]        
            new_path = result[1]    
            if val > best_val:
                best_val = val
                best_path = new_path
        return best_val, best_path

    else:
        best_val = 999999
        best_path = []
        for child in tree.get(node, []):
            new_path_input = path + [node]
            result = minimax(child, depth + 1, new_path_input)
            val = result[0]        
            new_path = result[1] 
            if val < best_val:
                best_val = val
                best_path = new_path
        return best_val, best_path

# ---we take root node from user---
root = input("\nEnter root node of the game tree: ")
result = minimax(root, 0, [])
value = result[0]           
decision_path = result[1]
print(f"\nOptimal value at root '{root}': {value}")
print("Decision path:", " → ".join(decision_path))