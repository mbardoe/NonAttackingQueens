from graphics import *
from Cell import *
from BoardQueens import *

class Board:
	
	def __init__(self, winWidth, dimension, positions=[]):
		self.dimension=dimension
		self.width=winWidth
		self.window=GraphWin("Board Queens", self.width, self.width+200)
		self.cellSize=int(winWidth/dimension)
		self.cells=[]
		for i in range(self.dimension):
			for j in range(self.dimension):
				newCell=Cell(self.window, j*self.cellSize, i*self.cellSize, self.cellSize)
				self.cells.append(newCell)
		self.positions=positions
		self.solution=BoardQueens(self.dimension, positions=self.positions)
		self.createRestart()

	def restart(self):
		self.positions=[]
		self.solution=BoardQueens(self.dimension, positions=self.positions)
		self.boardUpdate()
		
	def createRestart(self):
		#print("Here")
		p1=Point(100, self.width+50)
		p2=Point(200, self.width+100)
		self.restartrect=Rectangle(p1,p2)
		self.restartrect.setWidth(4)
		self.restartrect.setFill("black")
		self.restartrect.setOutline("white")
		restarttext=Text(Point(150,self.width+75), "RESTART")
		restarttext.setSize(int(14))
		restarttext.setTextColor("red")
		self.restartrect.draw(self.window)
		restarttext.draw(self.window)

	def getCellByLabel(self, i, j):
		return self.cells[j*self.dimension+i]

	def getCoordByPoint(self, point):
		x=point.getX()
		y=point.getY()
		return (int(y/self.cellSize),int(x/self.cellSize))

	def assignCellValue(self, cell, value):
		
		#print(value)
		if value=="X":
			cell.activate()
		else:
			cell.deactivate()
			cell.setText(str(value))

	def show(self):
		#for cell in self.cells:
		for i in range(self.dimension):
			for j in range(self.dimension):
				cell=self.cells[i*self.dimension+j]
				value=self.solution.subValues[j][i]
				self.assignCellValue(cell, value)
				cell.show()

	def boardUpdate(self):
		for i in range(self.dimension):
			for j in range(self.dimension):
				cell=self.cells[i*self.dimension+j]
				value=self.solution.subValues[j][i]
				self.assignCellValue(cell, value)
				#cell.cellUpdate();
		update()

	def run(self):
		self.show()
		while True:
			clickPoint=self.window.getMouse()
			#print(clickPoint)
			#print(self.restartrect.getP2())
			#print(self.restartrect.getP1())
			if (clickPoint.getY()<self.restartrect.getP2().getY() and 
				clickPoint.getY()>self.restartrect.getP1().getY() and
				clickPoint.getX()<self.restartrect.getP2().getX() and
				clickPoint.getX()>self.restartrect.getP1().getX()):
				#print("RESTART")
				self.restart()
			elif clickPoint.getY()<self.width:

				#print(clickPoint)
				coords=self.getCoordByPoint(clickPoint)
				#print(coords)
				self.positions.append(coords)

				self.solution=BoardQueens(self.dimension, positions=self.positions)
				#print(self.solution)
				self.boardUpdate()



			

if __name__ == "__main__":
	bd=Board(600, 7,[(0,0)])
	bd.run()
	