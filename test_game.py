import unittest

from board import Board
from game import DotsAndBoxes
from rules import valid_move


class DotsAndBoxesTests(unittest.TestCase):
    def test_valid_horizontal_and_vertical_moves(self):
        board = Board()
        self.assertTrue(valid_move(board, "H", 0, 0))
        board.add_line("H", 0, 0)
        self.assertTrue(valid_move(board, "V", 0, 0))

    def test_repeated_move_is_invalid_and_does_not_change_board(self):
        board = Board()
        board.add_line("H", 0, 0)
        with self.assertRaises(ValueError):
            board.add_line("H", 0, 0)
        self.assertEqual(sum(map(sum, board.horizontal)), 1)

    def test_completed_box_scores_and_keeps_turn(self):
        game = DotsAndBoxes()
        game.play_move("H", 0, 0)
        game.play_move("V", 0, 0)
        game.play_move("H", 1, 0)
        self.assertEqual(game.play_move("V", 0, 1), 1)
        self.assertEqual(game.scores, [0, 1])
        self.assertEqual(game.current, 1)
        self.assertEqual(game.board.owners[(0, 0)], "2")

    def test_end_of_game_and_moves_after_completion(self):
        game = DotsAndBoxes(rows=1, cols=1)
        for move in (("H", 0, 0), ("V", 0, 0), ("H", 1, 0), ("V", 0, 1)):
            game.play_move(*move)
        self.assertTrue(game.board.is_complete())
        with self.assertRaises(ValueError):
            game.play_move("H", 0, 0)


if __name__ == "__main__":
    unittest.main()