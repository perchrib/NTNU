from tile import Tile
from board import Board
from gui import Draw
DIM = 4
def main():
	board = Board(DIM)
	gui = Draw(DIM,board)
	tile = Tile(None)
	tile.set_start_value()
	board.set_new_tile(tile)
	gui.update_board(5)
	gui.mainloop()

main()

"""TODO:
	Fixing cant move if no valid moves,
	score, delay on random tile on board"""

