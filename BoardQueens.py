import copy
from BoardData import *
global_cache = {}

class BoardQueens:
	def __init__(self, dim, positions=[]):
		global global_cache
		#print(positions)

		self.dimension = dim
		self.positions=positions
		self.positions.sort()
		if self.__repr__() in global_cache:
			#print("Found it")
			x=global_cache[self.__repr__()]
			#print(x)
			self.moves=[[False for j in range(self.dimension)] for i in range(self.dimension)]
			for pos in self.positions:
				self.placeQueen(pos)
			self.subValues=x.subValues
			self.value=x.value
		else:
			self.moves=[[False for j in range(self.dimension)] for i in range(self.dimension)]
			for pos in positions:
				self.placeQueen(pos)
			self.subValues=[]
			self.calcSubValues()
			x=BoardData(self.subValues, self.value)
			global_cache[self.__repr__()]=copy.deepcopy(x)
		
	def __repr__(self):
		#self.positions.sort()
		## Change the positions so that we are always putting first
		## position at (0,0)
		##if len(self.positions)>1:
		##	startingPos=self.positions[0]
		##	xoffset=startingPos[0]
		##	yoffset=startingPos[1]
		##	alteredPos=[(0,0)]


		return str(self.dimension)+str(self.positions)

	def placeQueen(self, pos):	
		#print(pos)	
		over=int(pos[0]);
		down=int(pos[1]);
		positiveDiagonalOffset=over-down
		negativeDiagonalOffset=over+down
		for i in range(self.dimension):
			#Horizontal
			self.moves[down][i]=True
			#Vertical
			self.moves[i][over]=True
			#Diagonal Pos
			if (positiveDiagonalOffset+i)>=0 and (positiveDiagonalOffset+i)<self.dimension:
				self.moves[i][positiveDiagonalOffset+i]=True
			#Diagonal Neg
			if (negativeDiagonalOffset-i)>=0 and (negativeDiagonalOffset-i)<self.dimension:
				self.moves[i][negativeDiagonalOffset-i]=True

	def mex(self, mylist):

		if len(mylist)==0:
			return 0
		else:
			for i in range(len(mylist)):
				if i not in mylist:
					return i
		return len(mylist)
	
	def __str__(self):
		ans=""
		for y in range(self.dimension):
			for x in range(self.dimension):
				if self.moves[y][x]:
					ans+="X\t"
				else:
					ans+=str(self.subValues[y][x])+"\t"
			ans+="\n"
		return ans

	def calcSubValues(self):
		flag=False
		for y in range(self.dimension):
			self.subValues.append([])
			for x in range(self.dimension):
				if not self.moves[y][x]:

					newPos=self.positions+[tuple((x,y))]
					#print(newPos)
					newGame=BoardQueens(self.dimension, positions=newPos)
					self.subValues[y].append(newGame.value)
				else:
					self.subValues[y].append("X")
		if len(self.subValues)==0:
			self.value=0
		else:
			self.value=self.mex(sum(self.subValues,[]))

if __name__ == "__main__":
	pos=[(0,0)]
	#pos=[]
	size=5
	game=BoardQueens(size,positions=pos)
	print(game.positions)
	print(game)
	print(game.value)
	while True:
		x=int(input("row:"))
		y=int(input("column:"))
		pos.append((x,y))
		print(pos)

		game=BoardQueens(size,positions=pos)
		print(game)
		print(game.value)
