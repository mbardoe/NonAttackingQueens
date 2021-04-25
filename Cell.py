from graphics import *


class Cell:
	#grey=color_rgb(125, 125, 125)

	def __init__(self,window,x,y,size):
		self.window=window
		self.activated=False
		self.text=""
		#self.position=tuple(x,y)
		self.size=size
		self.pt=Point(x,y)
		self.pt2=Point(x+size, y+size)
		self.rect=Rectangle(self.pt, self.pt2)
		self.rect.setWidth(4)
		self.rect.setOutline("white")
		text="A"
		textPos=self.pt.clone()
		textPos.move(self.size/2, self.size/2)
		self.text=Text(textPos, text)
		self.text.setSize(int(self.size/4))
		self.text.setTextColor("red")
		

	

	def activate(self):
		#print("activated")
		self.rect.setFill("grey")
		self.activated=True
		self.text.setText("")
		

	def setText(self, text):
		self.text.setText(str(text))
	

	def deactivate(self):
		self.rect.setFill("black")
		self.activated=False

	

	def show(self):
		#strokeWeight(4)
		#stroke(255)
		if (self.activated):
			self.rect.setFill("gray")
		
		else:
			self.rect.setFill("black")
			
		
		self.rect.draw(self.window)
		
		self.text.draw(self.window)
		#fill(0)
		#textSize(int(self.size/6))
		#textAlign(CENTER)

		#text(str(i),self.position.x+9, self.position.y+9)
		#text(str(j),self.position.x-9+self.size, self.position.y+9)
		
		#text(str(done), self.position.x+9, self.position.y-9+self.size)
		#text(str(dtwo), self.position.x-9+self.size, self.position.y-9+self.size)
		#if (self.activated){
			#fill(0)
			#textSize(10)
			#textAlign(CENTER)
			#text(self.text, self.position.x+self.size/2, 
			#	self.position.y+self.size/2)