from board import Board
from rules import valid_move, completed_boxes

class DotsAndBoxes:
    def __init__(self, rows=2, cols=2, player_names=None):
        self.board = Board(rows, cols)
        self.current = 0
        self.scores = [0, 0]
        self.player_names = list(player_names or ("P1", "P2"))
        if len(self.player_names) != 2 or any(not name.strip() for name in self.player_names):
            raise ValueError("exactly two non-empty player names are required")

    def play_move(self, orientation, row, col):
        """Apply one move and return the number of boxes claimed."""
        if self.board.is_complete():
            raise ValueError("the board is already complete")
        orientation = orientation.upper()
        if not valid_move(self.board, orientation, row, col):
            raise ValueError("invalid or already-used move")

        before = set(self.board.completed)
        self.board.add_line(orientation, row, col)
        newly_completed = completed_boxes(self.board, before)
        self.board.claim_boxes(str(self.current + 1))
        if newly_completed:
            self.scores[self.current] += newly_completed
        else:
            self.current = 1 - self.current
        return newly_completed

    def run(self):
        print("Dots and Boxes")
        print(f"{self.player_names[0]} vs {self.player_names[1]}")
        print("Enter moves as H row col or V row col.")
        print("Rows and columns start at 0.")
        print("Example: H 0 1")

        while not self.board.is_complete():
            self.board.display(self.scores, self.current)
            try:
                raw = input(f"{self.player_names[self.current]}, move: ").strip().upper()
            except EOFError:
                print("Input ended before the board was complete.")
                return
            parts = raw.split()

            if len(parts) != 3:
                print("Invalid format.")
                continue

            orientation, row, col = parts
            if not row.isdigit() or not col.isdigit():
                print("Row and column must be numbers.")
                continue

            row, col = int(row), int(col)
            try:
                newly_completed = self.play_move(orientation, row, col)
            except ValueError as error:
                print(f"Invalid move: {error}.")
                continue

            if newly_completed:
                print(f"{self.player_names[self.current]} completed {newly_completed} box(es) and plays again.")

        self.board.display(self.scores, self.current)
        print("Game over!")
        if self.scores[0] == self.scores[1]:
            print("The game is a draw.")
        else:
            winner = 1 if self.scores[0] > self.scores[1] else 2
            print(f"{self.player_names[winner - 1]} wins!")
