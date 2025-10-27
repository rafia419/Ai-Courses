## 1️⃣ Breadth-First Search (BFS)

**How it works:**
BFS explores all the neighbor nodes at the current depth before moving on to the next level of nodes. It uses a queue data structure (FIFO). Starting from a source node, it visits all adjacent nodes, marks them visited, and continues level by level.

**Applications:**
- Finding the shortest path in an unweighted graph
- Web crawlers
- Peer-to-peer networks (e.g., BitTorrent)
- GPS navigation systems

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)
![BFS](<C:\Users\Lenovo\Desktop\AI Course\Algorithm Implementation\images\BFS output.png>)




## 2️⃣ Depth-First Search (DFS)

**How it works:**
DFS explores as far as possible along each branch before backtracking. It uses a stack. It starts at the root node and explores each path to its deepest node before moving to the next branch.

**Applications:**
- Topological sorting
- Detecting cycles in graphs
- Maze and puzzle solving
- Pathfinding in games

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)
![DFS](<Algorithm Implementation\images\DFS output.png>)




## 3️⃣ Bidirectional Search (for BFS and DFS)

**How it works:**
Bidirectional search runs two simultaneous searches — one forward from the start node and another backward from the goal node — and stops when both searches meet. This drastically reduces the search space.

**Applications:**
- Fast shortest path finding (e.g., in maps, navigation systems)
- AI-based game agents

**Time Complexity:** O(b^(d/2))
**Space Complexity:** O(b^(d/2))
(where b = branching factor, d = depth of solution)
![Bidirectional-Search](<Algorithm Implementation\images\Bidirectional Search Output.png>)



## 4️⃣ Depth-Limited Search (DLS)

**How it works:**
DLS is a variation of DFS where the search is limited to a specific depth level. If the goal is not found within that depth, the algorithm stops searching deeper.

**Applications:**
- Useful when the depth of the goal is known or limited
- Reduces risk of infinite loops in infinite search spaces

**Time Complexity:** O(b^l) (where l = depth limit)
**Space Complexity:** O(b * l)
![Depth-Limited-Search](<Algorithm Implementation\images\Depth Limited Search Output.png>)



## 5️⃣ Iterative Deepening Search (IDS)

**How it works:**
IDS repeatedly runs Depth-Limited Search (DLS) with increasing depth limits (1, 2, 3, ...), combining the space efficiency of DFS and the completeness of BFS.

**Applications:**
- Pathfinding in AI and games
- Solving puzzles like 8-puzzle or 15-puzzle

**Time Complexity:** O(b^d)
**Space Complexity:** O(b * d)
![Iterative-deppening-search](<Algorithm Implementation\images\Iterativ Deepening Search Output.png>)




## 6️⃣ Best-First Search

**How it works:**
This algorithm selects the next node to explore based on a heuristic function that estimates the “closeness” to the goal. It uses a priority queue, always expanding the most promising node.

**Applications:**
- Route planning
- Solving puzzles (like 8-puzzle)
- AI and robotics pathfinding

**Time Complexity:** O(b^m)
**Space Complexity:** O(b^m)
(where m = maximum depth of the search space)
![Best-First-Search](<Algorithm Implementation\images\Best_first_search_output.png>)




## 7️⃣ Beam Search

**How it works:**
Beam Search is a heuristic search that expands only the best k nodes at each level (where k is the beam width). It trades off completeness for speed and memory efficiency.

**Applications:**
- Natural Language Processing (e.g., machine translation, speech recognition)
- Game tree searches
- Optimization problems

**Time Complexity:** O(b * d) approximately (depends on beam width)
**Space Complexity:** O(b * d)
![Beam-Search](<Algorithm Implementation\images\Beam_search_Output.png>)




## 8️⃣ A* (A-star) Search Algorithm

**How it works:**
A* combines cost from the start (g) and estimated cost to goal (h) in the formula f(n) = g(n) + h(n). It expands nodes with the smallest f(n) value, ensuring optimal paths when h is admissible.

**Applications:**
- GPS and route planning
- AI games and robotics navigation
- Network optimization

**Time Complexity:** O(b^d) (depends on heuristic quality)
**Space Complexity:** O(b^d)
![A-Star-Search](<Algorithm Implementation\images\A_Star_Search_Output1.png>)
![A-Star-Search](<Algorithm Implementation\images\A_Star_Search_Output2.png>)




## 9️⃣ Min-Max Search Algorithm

**How it works:**
Used in two-player games, Min-Max assumes both players play optimally. The algorithm simulates all possible moves, assigning scores to terminal states, and backtracks to select the move that maximizes the player’s advantage while minimizing the opponent’s.

**Applications:**
- Turn-based games (chess, tic-tac-toe, checkers)
- Decision making in competitive AI

**Time Complexity:** O(b^m)
**Space Complexity:** O(b * m)
![Min-Max-Search](<Algorithm Implementation\images\Min-Max-Output.png>)



## 🔟 Alpha-Beta Pruning

**How it works:**
This is an optimization of Min-Max, which prunes branches that cannot possibly affect the final decision. It keeps track of two values, alpha and beta, to skip unnecessary computations. Uses **alpha (best for maximizer)** and **beta (best for minimizer)** values to prune.

**Applications:**
- AI in games (chess, checkers, tic-tac-toe)
- Any adversarial decision-making scenario

**Time Complexity:** O(b^(m/2)) (with perfect ordering)
**Space Complexity:** O(b * m)
![Alpha-Beta-Search-Algorithm](<Algorithm Implementation\images\Alpha-Beta-Output.png>)