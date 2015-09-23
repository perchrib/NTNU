import Tkinter as tk
from math import sqrt


class Vertex:
	def __init__(self,index,x,y):
		self.index = index
		self.x = x
		self.y = y
		self.neighbour = []
		self.guiX = None
		self.guiY = None




class Draw(tk.Tk):
	def __init__(self,allVertex):
		tk.Tk.__init__(self)
		#node_size = (self.winfo_screenheight()-50)/board.Ydim 
		scale = 0.01 #Scaling
		r = 5 #radius
		i = 5 #Indent

		#0 0 5
		#1 3 3
		#2 3 7

		self.width = self.winfo_screenwidth()
		self.height = self.winfo_screenheight()
		self.canvas = tk.Canvas(self, width= self.width,height=self.height)
		self.canvas.pack()
		index = 0
		for vertex in allVertex:
			
			x = (vertex.x + i) * scale
			y = (vertex.y + i) * scale
			vertex.guiX = x
			vertex.guiY = y
			
			print "Current: ", x,y

			
			
			
				
			for neighbour in vertex.neighbour:
				print "Current x:%d y:%d" %(x,y)
				#print "neighbour x:%d y%d" %(neighbour.x,neighbour.y)
				t = r / 2.0
				print "TTTT: ",t
				neighbourX = (neighbour.x+i)*scale
				neighbourY = (neighbour.y+i)*scale
				self.canvas.create_line(x+t,y+t,neighbourX+t,neighbourY+t)
		
		for vertex in allVertex:
			color = ['red','blue','green']
			tag = vertex.index
			if index == 3:
				index = 0

			self.canvas.create_oval(vertex.guiX,vertex.guiY,vertex.guiX+r,vertex.guiY+r,fill=color[index],tag=vertex.index)
			index += 1



				
def delegateData(data):
	initData = data.pop(0)
	vertex = [] 
	for d in data:
		if len(d) == 3:

			tempVertex = Vertex(int(d[0]),d[1],d[2])
			vertex.append(tempVertex)
		else:
			vertex[int(d[0])].neighbour.append(vertex[int(d[1])])
			vertex[int(d[1])].neighbour.append(vertex[int(d[0])])


	return initData, vertex



def readFile(f):
	data = map(lambda x: x.strip(), open(f,'r'))
	data = map(lambda x: x.split(),data)
	data = map(lambda row: map(float, row), data)
	print data
	return data

if __name__ == "__main__":
	f = "graphs/graph_6.txt"
	init, allvertex = delegateData(readFile(f))
	gui = Draw(allvertex)
	gui.mainloop()

	
