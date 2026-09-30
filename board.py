class Board:
    def __init__(self, rows=2, cols=2):
        if not isinstance(rows, int) or not isinstance(cols, int) or rows < 1 or cols < 1:
            raise ValueError("rows and cols must be positive integers")

        self.rows = rows
        self.cols = cols
        self.horizontal = [[False] * cols for _ in range(rows + 1)]
        self.vertical = [[False] * (cols + 1) for _ in range(rows)]
        self.completed = set()
        self.owners = {}

    def add_line(self, orientation, row, col):
        if not self._line_is_available(orientation, row, col):
            raise ValueError("invalid or already-used line")

        if orientation == "H":
            self.horizontal[row][col] = True
        else:
            self.vertical[row][col] = True
        self._update_completed()

    def claim_boxes(self, player):
        new_boxes = [box for box in self.completed if box not in self.owners]
        for box in new_boxes:
            self.owners[box] = player
        return len(new_boxes)

    def _line_is_available(self, orientation, row, col):
        if orientation == "H":
            return 0 <= row <= self.rows and 0 <= col < self.cols and not self.horizontal[row][col]
        if orientation == "V":
            return 0 <= row < self.rows and 0 <= col <= self.cols and not self.vertical[row][col]
        return False

    def _update_completed(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (
                    self.horizontal[r][c]
                    and self.horizontal[r + 1][c]
                    and self.vertical[r][c]
                    and self.vertical[r][c + 1]
                ):
                    self.completed.add((r, c))

    def is_complete(self):
        total = self.rows * (self.cols + 1) + self.cols * (self.rows + 1)
        used = sum(map(sum, self.horizontal)) + sum(map(sum, self.vertical))
        return used == total

    def display(self, scores, current):
        print()
        print(f"Scores: P1={scores[0]}  P2={scores[1]} | Turn: P{current + 1}")

        for r in range(self.rows + 1):
            print(".".join("---" if self.horizontal[r][c] else "   " for c in range(self.cols)))
            if r < self.rows:
                middle = []
                for c in range(self.cols + 1):
                    wall = "|" if self.vertical[r][c] else " "
                    middle.append(wall)
                    if c < self.cols:
                        owner = self.owners.get((r, c))
                        middle.append(" " + (owner if owner else " ") + " ")
                print("".join(middle))
        print()
