import tkinter as tk
import random
from collections import defaultdict

# Possible moves
moves = ["rock", "paper", "scissors"]

# Scores
player_score = 0
ai_score = 0

# Store player move sequence patterns (Markov chain memory)
transition_counts = defaultdict(lambda: {"rock": 0, "paper": 0, "scissors": 0})

# Keep track of the last two moves
player_history = []

def predict_next_move():
    """Predict the next move based on the last 2 moves (Markov chain)"""
    if len(player_history) < 2:
        return random.choice(moves)
    
    last_two = tuple(player_history[-2:])
    possible_next = transition_counts[last_two]

    # Find the most likely next move
    if sum(possible_next.values()) == 0:
        return random.choice(moves)
    predicted = max(possible_next, key=possible_next.get)
    return predicted

def markov_ai_move():
    """AI counters the predicted next player move"""
    predicted_move = predict_next_move()

    # Counter move logic
    if predicted_move == "rock":
        return "paper"
    elif predicted_move == "paper":
        return "scissors"
    else:
        return "rock"

def get_winner(player, ai):
    """Determine winner"""
    if player == ai:
        return "draw"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "player"
    else:
        return "ai"

def play(player_move):
    """Main game logic"""
    global player_score, ai_score

    # Update Markov chain memory
    if len(player_history) >= 2:
        last_two = tuple(player_history[-2:])
        transition_counts[last_two][player_move] += 1

    player_history.append(player_move)

    ai_move = markov_ai_move()
    winner = get_winner(player_move, ai_move)

    # Update scores and show results
    if winner == "draw":
        result_label.config(text=f"🤝 Draw! Both chose {player_move}.", fg="blue")
    elif winner == "player":
        player_score += 1
        result_label.config(text=f"✅ You Win! AI chose {ai_move}.", fg="green")
    else:
        ai_score += 1
        result_label.config(text=f"💻 AI Wins! AI chose {ai_move}.", fg="red")

    score_label.config(text=f"📊 Score → You: {player_score} | AI: {ai_score}")

# ---------------- Tkinter UI ----------------

root = tk.Tk()
root.title("Rock Paper Scissors — Markov AI")
root.geometry("420x420")
root.config(bg="#48485a")

title_label = tk.Label(root, text="🎮 Rock Paper Scissors", font=("Arial", 16, "bold"), bg="#f4f4f9")
title_label.pack(pady=15)

instruction_label = tk.Label(root, text="Choose your move:", font=("Arial", 12), bg="#f4f4f9")
instruction_label.pack(pady=5)

# Buttons for moves
button_frame = tk.Frame(root, bg="#f4f4f9")
button_frame.pack(pady=15)

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 12), width=10, command=lambda: play("rock"))
paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12), width=10, command=lambda: play("paper"))
scissors_btn = tk.Button(button_frame, text="✂️Scissors", font=("Arial", 12), width=12, command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=3)

# Labels for result and score
result_label = tk.Label(root, text="", font=("Arial", 13, "bold"), bg="#f4f4f9")
result_label.pack(pady=20)

score_label = tk.Label(root, text="📊 Score → You: 0 | AI: 0", font=("Arial", 12), bg="#f4f4f9")
score_label.pack(pady=10)

# Exit button
exit_btn = tk.Button(root, text="❌ Quit", font=("Arial", 12), bg="#ff6666", fg="white", command=root.destroy)
exit_btn.pack(pady=15)

root.mainloop()
