import os
from random import randint
from World import World
from Entity import Entity



monster= Entity([randint(0,5),randint(0,5)], "M" )
player= Entity([0,0],"P")
treasure= Entity([6,6],"T")

level1= World((6,6), player, 3)


counter=0
while True:
	os.system("cls")
	print()
	print("              Developed by Luca Bergognoni & Alessandro Valenti")
	print()
	print()
	level1.campo()
	command=input().lower()
	counter+=1
	if command=="w":
		player.move("N")
	elif command=="s":
		player.move("S")
	elif command=="a":
		player.move("W")
	elif command=="d":
		player.move("E")
	elif command== "b":
		break
	

	



	












	











