from board import Board


def test():
	b1 = Board(4)
	b1.print_board()
	b2 = [row[:] for row in b1.board] 
		
