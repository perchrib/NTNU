import Tkinter as tk


class Draw(tk.Tk):
	def __init__(self,dimension):
		tk.Tk.__init__(self)
		node_size = (self.winfo_screenheight()-100)/dimension
		self.width = self.winfo_screenheight()
		self.height = self.winfo_screenheight()
		self.canvas = tk.Canvas(self, width= self.width,height=self.height)
		self.canvas.pack()

		
		for x in range(dimension):
			for y in range(dimension):
				gridx = node_size*y+3
				gridy = node_size*x+3
				gridx2 = gridx + node_size -2
				gridy2 = gridy + node_size -2
				gx2 = gridx + (node_size -2)/2
				gy2 = gridy + (node_size -2)/2
				"""c for color, i for integer"""
				coltag = 'c'+ str(x)+"-"+ str(y)
				inttag = 'i'+ str(x)+"-"+ str(y)
				self.canvas.create_rectangle(gridx,gridy, gridx2, gridy2, fill="mint cream",tags=coltag)
				self.canvas.create_text(gx2,gy2,text="",font=("Helvetica",70),tags=inttag)

def log_2(number):
	if number == 1:
		return 0
	else:
		return log_2(number/2) + 1



def setColor(tile_num):
	key = log_2(tile_num)
	colors = {1:'light sky blue',2:'dodger blue',3:'coral',4:'dark orange',5:'IndianRed1',6:'red',7:'khaki',8:'yellow',9:'olivedrab2',10:'green',11:'hot pink',12:'deep pink'}#,13:,14:,15:,}
	return colors[key]

def main():
	gui = Draw(4)
	gui.canvas.itemconfig('i0-0',text='2')
	gui.canvas.itemconfig('c0-0',fill='light sky blue')
	gui.canvas.itemconfig('c0-1',fill='dodger blue')
	gui.canvas.itemconfig('i0-1',text='4')
	gui.canvas.itemconfig('c0-2',fill='coral')
	gui.canvas.itemconfig('i0-2',text='8')
	gui.canvas.itemconfig('c0-3',fill='dark orange')
	gui.canvas.itemconfig('i0-3',text='16')
	gui.canvas.itemconfig('c1-0',fill='IndianRed1')
	gui.canvas.itemconfig('i1-0',text='32')
	gui.canvas.itemconfig('c1-1',fill='red')
	gui.canvas.itemconfig('i1-1',text='64')
	gui.canvas.itemconfig('c1-2',fill='khaki')
	gui.canvas.itemconfig('i1-2',text='128')
	gui.canvas.itemconfig('c1-3',fill='yellow')
	gui.canvas.itemconfig('i1-3',text='256')
	gui.canvas.itemconfig('c2-0',fill='olivedrab2')
	gui.canvas.itemconfig('i2-0',text='512')
	gui.canvas.itemconfig('c2-1',fill='green')
	gui.canvas.itemconfig('i2-1',text='1024')
	gui.canvas.itemconfig('c2-2',fill='hot pink')
	gui.canvas.itemconfig('i2-2',text='2048')
	gui.canvas.itemconfig('c2-3',fill='deep pink')
	gui.canvas.itemconfig('i2-3',text='4096')
	gui.mainloop()
main()