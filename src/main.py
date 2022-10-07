"""A tic-tac-toe game built with Python and Tkinter."""
from board import Board
from game import Game


def main():
    """Create the game's board and run its main loop."""
    game = Game()
    board = Board(game)
    board.mainloop()


if __name__ == "__main__":
    main()
