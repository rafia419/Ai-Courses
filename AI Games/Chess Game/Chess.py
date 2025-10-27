import tkinter as tk
from tkinter import messagebox
import chess  # python-chess library for board, moves, rules
import threading
import math
import random

# ========== CONFIGURATION ==========
AI_DEPTH = 3           # AI search depth (higher = stronger but slower)
SQUARE_SIZE = 75       # Size of each chessboard square in pixels
LIGHT_COLOR = "#F0D9B5"   # Light square color
DARK_COLOR = "#B58863"    # Dark square color
HIGHLIGHT_COLOR = "#FFEB3B"  # Highlight selected piece
MOVE_COLOR = "#77DD77"       # Highlight possible move squares

# ========== PIECE SETUP ==========
# Unicode symbols for displaying pieces
PIECE_SYMBOLS = {
    'P': "♙", 'N': "♘", 'B': "♗", 'R': "♖", 'Q': "♕", 'K': "♔",
    'p': "♟", 'n': "♞", 'b': "♝", 'r': "♜", 'q': "♛", 'k': "♚"
}

# Piece values for AI evaluation
PIECE_VALUES = {
    chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330,
    chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 20000
}

# ========== AI EVALUATION ==========
def evaluate_board(board):
    """
    Evaluate the board position for AI:
    Positive = White advantage
    Negative = Black advantage
    """
    # Checkmate
    if board.is_checkmate():
        return -99999 if board.turn else 99999
    # Draw conditions
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = PIECE_VALUES[piece.piece_type]
            score += value if piece.color == chess.WHITE else -value
    return score

def minimax(board, depth, alpha, beta, maximizing):
    """
    Minimax algorithm with alpha-beta pruning
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    moves = list(board.legal_moves)

    if maximizing:
        max_eval = -math.inf
        for move in moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def get_ai_move(board):
    """
    Get the AI's move using minimax
    """
    _, move = minimax(board, AI_DEPTH, -math.inf, math.inf, board.turn == chess.WHITE)
    return move

# ========== GUI CLASS ==========
class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Chess AI")
        self.board = chess.Board()  # chess board object
        self.selected_square = None
        self.legal_moves = []

        # Canvas to draw the chessboard
        self.canvas = tk.Canvas(root, width=8 * SQUARE_SIZE, height=8 * SQUARE_SIZE)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)  # click events

        # Status label to show turn or check/checkmate
        self.status = tk.Label(root, text="White to move", font=("Arial", 12))
        self.status.pack(pady=5)

        # Buttons: Undo and New Game
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        tk.Button(btn_frame, text="Undo", command=self.undo).pack(side="left", padx=5)
        tk.Button(btn_frame, text="New Game", command=self.new_game).pack(side="left", padx=5)

        self.draw_board()

    # Draw the chessboard and pieces
    def draw_board(self):
        self.canvas.delete("all")  # clear previous drawings
        for row in range(8):
            for column in range(8):
                color = LIGHT_COLOR if (row + column) % 2 == 0 else DARK_COLOR
                x1, y1 = column * SQUARE_SIZE, row * SQUARE_SIZE
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

        # Highlight selected square
        if self.selected_square is not None:
            f, r = chess.square_file(self.selected_square), 7 - chess.square_rank(self.selected_square)
            self.canvas.create_rectangle(f*SQUARE_SIZE, r*SQUARE_SIZE,
                                         (f+1)*SQUARE_SIZE, (r+1)*SQUARE_SIZE,
                                         outline=HIGHLIGHT_COLOR, width=3)
            # Highlight legal moves
            for target in self.legal_moves:
                tf, tr = chess.square_file(target), 7 - chess.square_rank(target)
                self.canvas.create_oval(tf*SQUARE_SIZE+30, tr*SQUARE_SIZE+30,
                                        tf*SQUARE_SIZE+50, tr*SQUARE_SIZE+50,
                                        fill=MOVE_COLOR)

        # Draw pieces
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                f, r = chess.square_file(square), 7 - chess.square_rank(square)
                symbol = PIECE_SYMBOLS[piece.symbol()]
                self.canvas.create_text(f*SQUARE_SIZE+40, r*SQUARE_SIZE+40,
                                        text=symbol, font=("Arial", 40))

        # Update status label
        if self.board.is_checkmate():
            self.status.config(text="Checkmate! " + ("Black wins" if self.board.turn else "White wins"))
        elif self.board.is_stalemate():
            self.status.config(text="Draw (Stalemate)")
        elif self.board.is_check():
            self.status.config(text=("White" if self.board.turn else "Black") + " in check!")
        else:
            self.status.config(text=("White" if self.board.turn else "Black") + " to move")

    # Handle clicks on the board
    def on_click(self, event):
        if self.board.is_game_over():
            return
        file = event.x // SQUARE_SIZE
        rank = 7 - (event.y // SQUARE_SIZE)
        square = chess.square(file, rank)

        piece = self.board.piece_at(square)
        if self.selected_square is None:
            # Select a piece of the correct color
            if piece and piece.color == self.board.turn:
                self.selected_square = square
                self.legal_moves = [m.to_square for m in self.board.legal_moves if m.from_square == square]
        else:
            # Attempt to move selected piece
            move = chess.Move(self.selected_square, square)
            # Handle pawn promotion
            if move in self.board.legal_moves or chess.Move(self.selected_square, square, promotion=chess.QUEEN) in self.board.legal_moves:
                if self.board.piece_at(self.selected_square).piece_type == chess.PAWN and (rank == 0 or rank == 7):
                    move = chess.Move(self.selected_square, square, promotion=chess.QUEEN)
                self.board.push(move)
                self.selected_square = None
                self.legal_moves = []
                self.draw_board()
                # Let AI play after player move
                self.root.after(500, self.ai_move)
                return
            else:
                self.selected_square = None
                self.legal_moves = []

        self.draw_board()

    # AI makes a move (in separate thread to prevent GUI freeze)
    def ai_move(self):
        if self.board.is_game_over():
            return

        def think():
            move = get_ai_move(self.board)
            if move:
                self.board.push(move)
            self.draw_board()

        t = threading.Thread(target=think)
        t.start()

    # Undo last player + AI moves
    def undo(self):
        if len(self.board.move_stack) > 0:
            self.board.pop()
        if len(self.board.move_stack) > 0:
            self.board.pop()  # undo AI move as well
        self.draw_board()

    # Start a new game
    def new_game(self):
        self.board.reset()
        self.selected_square = None
        self.legal_moves = []
        self.draw_board()


# ========== RUN THE GAME ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = ChessGUI(root)
    root.mainloop()
