import tkinter as tk
from tkinter import messagebox
import math
import random

# --- Game Logic Functions ---

# ✅ Function to check winner of the game
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None  # No winner yet

# ✅ Check if the board is full (draw condition)
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# ✅ Minimax algorithm for hard difficulty (AI optimal play)
def minimax(board, depth, is_maximizing, ai_symbol, player_symbol):
    winner = check_winner(board)
    # Base conditions: winner or draw
    if winner == ai_symbol:
        return 1
    elif winner == player_symbol:
        return -1
    elif is_full(board):
        return 0

    # AI’s turn (maximize score)
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai_symbol
                    score = minimax(board, depth+1, False, ai_symbol, player_symbol)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    # Player’s turn (minimize score)
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player_symbol
                    score = minimax(board, depth+1, True, ai_symbol, player_symbol)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# ✅ AI move logic for all difficulty levels
def ai_move():
    # Easy → Random move
    if difficulty.get() == "Easy":
        empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        return random.choice(empty)

    # Medium → Try to win/block, else random
    elif difficulty.get() == "Medium":
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    # Try to win
                    board[i][j] = ai_symbol
                    if check_winner(board) == ai_symbol:
                        return (i, j)
                    board[i][j] = " "
                    # Try to block player
                    board[i][j] = player_symbol
                    if check_winner(board) == player_symbol:
                        board[i][j] = ai_symbol
                        return (i, j)
                    board[i][j] = " "
        # Else random
        empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        return random.choice(empty)

    # Hard → Use minimax algorithm
    else:
        best_score = -math.inf
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai_symbol
                    score = minimax(board, 0, False, ai_symbol, player_symbol)
                    board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

# --- GUI Functions ---

# ✅ Player button click event
def on_click(r, c):
    # Only allow click if cell empty and game not over
    if board[r][c] == " " and not check_winner(board):
        board[r][c] = player_symbol
        buttons[r][c].config(text=player_symbol, state="disabled", disabledforeground="black")
        winner = check_winner(board)
        if winner:
            update_score(winner)
            return
        elif is_full(board):
            update_score("Draw")
            return
        ai_turn()  # AI makes move

# ✅ AI plays its turn
def ai_turn():
    if is_full(board) or check_winner(board):
        return
    ai_r, ai_c = ai_move()
    board[ai_r][ai_c] = ai_symbol
    buttons[ai_r][ai_c].config(text=ai_symbol, state="disabled", disabledforeground="green")
    winner = check_winner(board)
    if winner:
        update_score(winner)
    elif is_full(board):
        update_score("Draw")

# ✅ Update scores and show result
def update_score(winner):
    global player_wins, ai_wins, draws
    if winner == player_symbol:
        player_wins += 1
        messagebox.showinfo("Game Over", "🏆 You win!")
    elif winner == ai_symbol:
        ai_wins += 1
        messagebox.showinfo("Game Over", "💻 AI wins!")
    else:
        draws += 1
        messagebox.showinfo("Game Over", "🤝 It's a draw!")
    # Update scoreboard label
    score_label.config(text=f"📊 Player: {player_wins} | AI: {ai_wins} | Draws: {draws}")

# ✅ Start a new game with selected settings
def new_game():
    global player_symbol, ai_symbol
    player_symbol = symbol_var.get()
    ai_symbol = "O" if player_symbol == "X" else "X"
    reset_board(ai_first=(start_first.get() == "AI"))

# ✅ Reset the board for a new round
def reset_board(ai_first=False):
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")
    if ai_first:
        ai_turn()

# --- GUI Setup ---

root = tk.Tk()
root.title("Tic Tac Toe AI Game")
root.geometry("620x650")
root.config(bg="#9b9bf3")

# Initialize game state
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
player_wins = 0
ai_wins = 0
draws = 0

# --- Symbol Selection (Player chooses X or O) ---
symbol_frame = tk.Frame(root)
symbol_frame.pack(pady=5)
tk.Label(symbol_frame, text="Choose your symbol:", font=("times new roman", 12)).pack(side="left")
symbol_var = tk.StringVar(value="X")
tk.Radiobutton(symbol_frame, text="X", variable=symbol_var, value="X").pack(side="left", padx=5)
tk.Radiobutton(symbol_frame, text="O", variable=symbol_var, value="O").pack(side="left", padx=5)

player_symbol = symbol_var.get()
ai_symbol = "O" if player_symbol == "X" else "X"

# --- Difficulty Selection (Easy / Medium / Hard) ---
difficulty_frame = tk.Frame(root)
difficulty_frame.pack(pady=5)
tk.Label(difficulty_frame, text="Select AI Difficulty:", font=("Arial", 12)).pack(side="left")
difficulty = tk.StringVar(value="Hard")
tk.Radiobutton(difficulty_frame, text="Easy", variable=difficulty, value="Easy").pack(side="left", padx=5)
tk.Radiobutton(difficulty_frame, text="Medium", variable=difficulty, value="Medium").pack(side="left", padx=5)
tk.Radiobutton(difficulty_frame, text="Hard", variable=difficulty, value="Hard").pack(side="left", padx=5)

# --- Who Starts First (Player or AI) ---
first_frame = tk.Frame(root)
first_frame.pack(pady=5)
tk.Label(first_frame, text="Who starts first?", font=("Arial", 12)).pack(side="left")
start_first = tk.StringVar(value="Player")
tk.Radiobutton(first_frame, text="Player", variable=start_first, value="Player").pack(side="left", padx=5)
tk.Radiobutton(first_frame, text="AI", variable=start_first, value="AI").pack(side="left", padx=5)

# --- New Game Button ---
tk.Button(root, text="🎮 New Game", font=("Helvetica", 12), command=new_game).pack(pady=5)

# --- Game Board (3x3 Buttons) ---
frame = tk.Frame(root, bg="black")
frame.pack(padx=10, pady=10)
for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text=" ", font=("Helvetica", 32, "bold"), width=4, height=2,
                        bg="white", command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=2, pady=2)
        buttons[i][j] = btn

# --- Score Display ---
score_label = tk.Label(root, text="📊 Player: 0 | AI: 0 | Draws: 0", font=("Arial", 12))
score_label.pack(pady=5)

# --- AI makes first move if selected ---
if start_first.get() == "AI":
    ai_turn()

# --- Run the Game ---
root.mainloop()
