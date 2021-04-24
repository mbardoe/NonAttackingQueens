import copy
global_cache = {}

class TorusQueens:
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
			self.moves=x.moves
			self.subValues=x.subValues
			self.value=x.value
		else:
			self.moves=[[False for j in range(self.dimension)] for i in range(self.dimension)]
			for pos in positions:
				self.placeQueen(pos)
			self.subValues=[]
			self.calcSubValues()
			global_cache[self.__repr__()]=copy.deepcopy(self)
		
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
		for i in range(self.dimension):
			#Horizontal
			self.moves[down][(over+i)%self.dimension]=True
			#Vertical
			self.moves[(down+i)%self.dimension][over]=True
			#Diagonal Pos
			self.moves[(down+i)%self.dimension][(over+i)%self.dimension]=True
			#Diagonal Neg
			if over-i<0:
				pos=over-i+self.dimension
			else:
				pos=over-i
			self.moves[(down+i)%self.dimension][(pos)%self.dimension]=True

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
					newGame=TorusQueens(self.dimension, positions=newPos)
					self.subValues[y].append(newGame.value)
				else:
					self.subValues[y].append("X")
		if len(self.subValues)==0:
			self.value=0
		else:
			self.value=self.mex(sum(self.subValues,[]))

if __name__ == "__main__":
	#pos=[(0,0)]
	pos=[]
	game=TorusQueens(10,positions=pos)
	print(game.positions)
	print(game)
	print(game.value)
	while True:
		x=int(input("row:"))
		y=int(input("column:"))
		pos.append((x,y))
		print(pos)
		game=TorusQueens(10,positions=pos)
		print(game)
		print(game.value)
