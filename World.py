from Entity import Entity
from random import randint


class World:

	

	def __init__(self,size,player,monsternumber):
		self.size=size
		self.entities=  [ player ]


		for a in range(1):
			while True:
				position= ([6,6])
				if self.GetEntityAtCoords(position)==None:
					self.entities.append(Entity(position,"T"))
					break




		for i in range(monsternumber):
			while True:
				coordinates= (randint(0,size[0]-1),randint(0,size[1]-1))
				if self.GetEntityAtCoords(coordinates)==None:
					self.entities.append(Entity(coordinates,"M"))
					break



		

		





		for e in self.entities:
			e.world=self

	
	def GetEntityAtCoords(self,coordinates):
		for e in self.entities:
			if e.coordinates[0]==coordinates[0] and e.coordinates[1]==coordinates[1]:
				return e






	def campo(self):
		for y in range(self.size[1]):
			for x in range(self.size[0]):
				e=self.GetEntityAtCoords((x,y))
				if e!=None:
					print("["+e.graphic+"]", end="")
				else:
					print("[ ]", end="")
			print()



