import argparse

from game import DotsAndBoxes


def parse_args():
    parser = argparse.ArgumentParser(description="Play Dots and Boxes")
    parser.add_argument("--rows", type=int, default=2, help="number of boxes vertically")
    parser.add_argument("--cols", type=int, default=2, help="number of boxes horizontally")
    parser.add_argument("--player1", default="P1", help="name of the first player")
    parser.add_argument("--player2", default="P2", help="name of the second player")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    try:
        DotsAndBoxes(args.rows, args.cols, (args.player1, args.player2)).run()
    except ValueError as error:
        raise SystemExit(f"Configuration error: {error}")
