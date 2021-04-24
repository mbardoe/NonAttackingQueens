from graphics import *
from Cell import *
from TorusQueens import *

class Board:
	
	def __init__(self, winWidth, dimension):
		self.dimension=dimension
		self.width=winWidth
		self.window=GraphWin("Torus Queens", self.width, self.width)
		self.cellSize=int(winWidth/dimension)
		self.cells=[]
		for i in range(self.dimension):
			for j in range(self.dimension):
				newCell=Cell(self.window, j*self.cellSize, i*self.cellSize, self.cellSize)
				self.cells.append(newCell)
		self.positions=[]
		self.solution=TorusQueens(self.dimension, positions=self.positions)

		

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
			coords=self.getCoordByPoint(clickPoint)
			#print(coords)
			self.positions.append(coords)

			self.solution=TorusQueens(self.dimension, positions=self.positions)
			print(self.solution)
			self.boardUpdate()


			

if __name__ == "__main__":
	bd=Board(600, 8)
	bd.run()
	