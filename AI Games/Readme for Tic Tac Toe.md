## 🧠 Tic Tac Toe (AI vs Player)

**🎯 Game Overview**
This is an AI-powered Tic Tac Toe game built using Python (Tkinter).
The game allows a player to compete with the AI on three difficulty levels:

**🟢 Easy** – AI plays random moves
**🟡 Medium** – AI tries to win or block
**🔴 Hard** – AI uses the Minimax Algorithm for optimal play


**⚙️ How to Run the Game**
-Make sure Python 3.x is installed on your system.
-Save this file as tic_tac_toe_ai.py.
-Open a terminal or command prompt and run:
 bash
   python tic_tac_toe_ai.py
-The game window will open automatically.


**🧩 Software / Library Requirements**
**✅ Pre-installed required libraries:**
-tkinter → comes pre-installed with Python
-math and random → built-in Python modules

No extra installation is required.



**🎮 How to Play**
-Choose your symbol (X or O).
-Select the AI difficulty level (Easy / Medium / Hard).
-Choose who starts first — Player or AI.
-Click on an empty cell to make your move.
-The AI will automatically respond based on the chosen difficulty level.
-The scoreboard updates after every round.
-Click 🎮 New Game to start a new round anytime.



**🧠 Algorithm Used**
## Minimax Algorithm (used in Hard mode)
-The AI evaluates all possible moves and selects the one that minimizes the player’s chances of winning.
-This ensures optimal play from the AI side.



**🖼️ Screenshots**

[Tic Tac Toe](images/Tic_Tac_Toe.png)


**📊 Features**

-Three difficulty levels: Easy, Medium, Hard
-Player vs AI gameplay
-AI move logic implemented using Minimax Algorithm
-Scoreboard to track wins, losses, and draws
-GUI made with Tkinter



**⏳ Algorithm Complexity**	            	         
**Minimax (Hard Mode):**  **Time Complexity** = O(b<sup>d</sup>) where b = branching factor, d = depth and **Space Complexity** = O(bd)
**Easy/Medium AI Move:**  **Time Complexity** = O(1) to O(9) and Space Complexity =	O(1)



**👩‍💻 Developed Using**

**Language:** Python
**Library:** Tkinter (for GUI)
**Algorithm:** Minimax