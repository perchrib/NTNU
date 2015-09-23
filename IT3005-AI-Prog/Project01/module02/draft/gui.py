import Tkinter as tk

class Vertex:
	def __init__(self,index,x,y):
		self.index = index
		self.x = x
		self.y = y
		self.neighbour = []
		self.guiX = None
		self.guiY = None

class Draw(tk.Tk):
	def __init__(self,allVertex,min_max):
		tk.Tk.__init__(self)
		self.xmin = min_max[0]
		self.xmax = min_max[1]
		self.ymin = min_max[2]
		self.ymax = min_max[3]
		self.xAxis = 0
		self.yAxis = 0
		self.scaleX = 0
		self.scaleY = 0
		self.lineshift_x = 0
		self.lineshift_y = 0
		self.width = self.winfo_screenwidth()
		self.height = self.winfo_screenheight()
		self.padding = 50
		self.calculateScaling()
		r = 10 #radius
		
		self.canvas = tk.Canvas(self, width= self.width,height=self.height)
		self.canvas.pack(fill='both',expand='yes')
		index = 0

		for vertex in allVertex:
			for neighbour in vertex.neighbour:
				m = r / 2.0 
				nx = neighbour.x
				ny = neighbour.y
				self.canvas.create_line(self.plotFitScreenX(vertex.x)+m,self.plotFitScreenY(vertex.y)+m,self.plotFitScreenX(nx)+m,self.plotFitScreenY(ny)+m)
		
		for vertex in allVertex:
			color = ['red','blue','green']
			tag = vertex.index
			if index == 3:
				index = 0

			self.canvas.create_oval(self.plotFitScreenX(vertex.x),self.plotFitScreenY(vertex.y),self.plotFitScreenX(vertex.x)+r,self.plotFitScreenY(vertex.y)+r,fill=color[index],tag=vertex.index)
			index += 1

	def calculateScaling(self):
		print "xmin: ", self.xmin, " xmax: ",self.xmax, " ymin: ", self.ymin," ymax: ",self.ymax
		self.xAxis = abs(self.xmax) + abs(self.xmin)
		self.yAxis = abs(self.ymax) + abs(self.ymin)
		padding = 100
		self.scaleX = (self.width-padding) / self.xAxis
		self.scaleY = (self.height-padding) / self.yAxis

		if self.xmin < 0:
			self.lineshift_x = abs(self.xmin)
		if self.ymin < 0:  
			self.lineshift_y = abs(self.ymin) 
		print "scaleX: ",self.scaleX, " scaleY: ",self.scaleY

	def plotFitScreenX(self,x):
		s = (self.lineshift_x + x) * self.scaleX
		return s + self.padding/2

	def plotFitScreenY(self,y):
		s = (self.lineshift_y + y) * self.scaleY
		return s + (self.padding/2)

def initiateData(data):
	initData = data.pop(0)
	numVertex = int(initData[0])
	numEdges = int(initData[1])
	Allvertex = []
	vertexData = data[:numVertex]
	edgesData = data[numVertex:] 
	for d in vertexData:
		tempVertex = Vertex(int(d[0]),d[1],d[2])
		Allvertex.append(tempVertex)
	
	for d in edgesData:
		Allvertex[int(d[0])].neighbour.append(Allvertex[int(d[1])])
		Allvertex[int(d[1])].neighbour.append(Allvertex[int(d[0])])

	xmin = min(x[1] for x in vertexData)
	xmax = max(x[1] for x in vertexData)
	ymin = min(y[2] for y in vertexData)
	ymax = max(y[2] for y in vertexData)
	print "Vertexes: " ,numVertex
	return (numVertex,numEdges), Allvertex,(xmin,xmax,ymin,ymax)



def readFile(f):
	data = map(lambda x: x.strip(), open(f,'r'))
	data = map(lambda x: x.split(),data)
	data = map(lambda row: map(float, row), data)
	return data

if __name__ == "__main__":
	f = "graphs/graph_1.txt"
	init, allvertex,min_max = initiateData(readFile(f))
	gui = Draw(allvertex,min_max)
	gui.mainloop()

	
