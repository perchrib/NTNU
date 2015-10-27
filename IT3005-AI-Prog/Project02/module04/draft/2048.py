from tile import Tile
from board import Board
from gui import Draw
DIM = 4
def main():
	gui = Draw(DIM)
	gui.mainloop()

main()

"""TODO:
	AI implementation 
	-------------------------
	DONE!!!
	Fixing cant move if no valid moves, set new Tile fail when board is full and no more moves is possible
	, delay on random tile on board"""

