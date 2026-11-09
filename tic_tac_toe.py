"""TIC TAC TOE - 2 Player Game.

Plain Python, no dependencies. Player 1 claims slots with #, Player 2 with @.
Slots are numbered 1-9, left to right, top to bottom.
"""

import os
import sys

P1_MARK = "#"
P2_MARK = "@"
MARKS = (P1_MARK, P2_MARK)

WIN_GROUPS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
)


def clear_screen():
    """Clear the terminal on Windows and everything else."""
    os.system("cls" if os.name == "nt" else "clear")


def show_table(board, p1_name, p2_name, p1_wins, p2_wins):
    print("-----------------------------------------")
    print(f"SCORES: P1:{p1_wins} - P2:{p2_wins}")
    print("-----------------------------------------")
    print(f"[ {board[0]} ] [ {board[1]} ] [ {board[2]} ]")
    print(f"[ {board[3]} ] [ {board[4]} ] [ {board[5]} ]")
    print(f"[ {board[6]} ] [ {board[7]} ] [ {board[8]} ]")
    print(f"{p1_name}={P1_MARK}   {p2_name}={P2_MARK}")


def ask_move(board, player_name, marker):
    """Ask until the player gives a slot number that is still free."""
    while True:
        raw = input(f"{player_name} ({marker}) choose your slot: ").strip()

        if not raw.isdigit():
            print("Numbers only, 1 to 9. Try again.")
            continue

        choice = int(raw)
        if not 1 <= choice <= 9:
            print("That slot does not exist. Pick 1 to 9.")
            continue

        if board[choice - 1] in MARKS:
            print(f"Slot {choice} is already taken. Pick a free one.")
            continue

        board[choice - 1] = marker
        return


def has_winner(board, marker):
    return any(board[i] == board[j] == board[k] == marker for i, j, k in WIN_GROUPS)


def board_full(board):
    return all(cell in MARKS for cell in board)


def play_round(board, p1_name, p2_name, p1_wins, p2_wins):
    """Play one round. Returns '#', '@' or 'draw'."""
    while True:
        clear_screen()
        show_table(board, p1_name, p2_name, p1_wins, p2_wins)

        ask_move(board, p1_name, P1_MARK)
        if has_winner(board, P1_MARK):
            return P1_MARK
        if board_full(board):
            return "draw"

        clear_screen()
        show_table(board, p1_name, p2_name, p1_wins, p2_wins)

        ask_move(board, p2_name, P2_MARK)
        if has_winner(board, P2_MARK):
            return P2_MARK
        if board_full(board):
            return "draw"


def main():
    print("TIC TAC TOE - 2 Player Game")

    p1_name = input("Player 1 Name: ").strip() or "Player 1"
    p2_name = input("Player 2 Name: ").strip() or "Player 2"

    p1_wins = 0
    p2_wins = 0

    while True:
        board = [str(n) for n in range(1, 10)]
        result = play_round(board, p1_name, p2_name, p1_wins, p2_wins)

        if result == P1_MARK:
            p1_wins += 1
            headline = f"Player 1 WON! Congrats {p1_name}!"
        elif result == P2_MARK:
            p2_wins += 1
            headline = f"Player 2 WON! Congrats {p2_name}!"
        else:
            headline = "DRAW. Nobody wins, everybody survives."

        clear_screen()
        show_table(board, p1_name, p2_name, p1_wins, p2_wins)
        print(headline)

        if input("Play again (P) or quit (Q): ").strip().lower() == "q":
            print(f"Final score -> {p1_name}: {p1_wins}   {p2_name}: {p2_wins}")
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame closed.")
        sys.exit(0)
