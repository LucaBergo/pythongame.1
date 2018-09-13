from random import randint

class Entity:



	

	def __init__(self,coordinates,graphic):
		self.coordinates=coordinates
		self.graphic=graphic
		
		for i in range(2):
			if coordinates[i]<0:
				coordinates[i]=0

	def move(self,direction):
		curX=self.coordinates[0]
		curY=self.coordinates[1]
		world=self.world



		if self.world==None:
			return

		


		if direction=="N" and curY>0 and world.GetEntityAtCoords((curX,curY-1))==None :
			self.coordinates[1]= self.coordinates[1]-1
			
		elif direction== "S" and curY<=world.size[1]-2 and world.GetEntityAtCoords((curX,curY+1))==None:
			self.coordinates[1]= self.coordinates[1]+1
			
		elif direction== "W" and curX>0  and world.GetEntityAtCoords((curX-1,curY))==None:
			self.coordinates[0]= self.coordinates[0]-1
			
		elif direction== "E" and curX<=world.size[0]-2 and world.GetEntityAtCoords((curX+1,curY))==None:
			self.coordinates[0]= self.coordinates[0]+1

		elif direction=="N" and curY>0 and world.GetEntityAtCoords((curX,curY-1))!=None :
			print()
			print()
			print("                     GAME OVER              ")
			print()
			print()
			exit()
		elif direction== "S" and curY<=world.size[1]-2 and world.GetEntityAtCoords((curX,curY+1))!=None:
			print()
			print()
			print("                     GAME OVER              ")
			print()
			print()
			print()
			exit()
			
		elif direction== "W" and curX>0  and world.GetEntityAtCoords((curX-1,curY))!=None:
			print()
			print()
			print("                     GAME OVER              ")
			print()
			print()
			print()
			exit()
			
		elif direction== "E" and curX<=world.size[0]-2 and world.GetEntityAtCoords((curX+1,curY))!=None:
			print()
			print()
			print("                     GAME OVER              ")
			print()
			print()
			print()
			exit()



		
	def movemonster(self,direction):
		world=self.world
		curX=self.coordinates[0]
		curY=self.coordinates[1]



		if self.world==None:
			return


		z=randint(1,4)
		if z==1 and curY>0 and world.GetEntityAtCoords((curX,curY-1))==None :
			self.coordinates[1]= self.coordinates[1]-1
			
		elif z==2 and curY<=world.size[1]-2 and world.GetEntityAtCoords((curX,curY+1))==None:
			self.coordinates[1]= self.coordinates[1]+1
			
		elif z==3 and curX>0  and world.GetEntityAtCoords((curX-1,curY))==None:
			self.coordinates[0]= self.coordinates[0]-1
			
		elif z==4 and curX<=world.size[0]-2 and world.GetEntityAtCoords((curX+1,curY))==None:
			self.coordinates[0]= self.coordinates[0]+1

		

				
			


	



		


		


	
	
